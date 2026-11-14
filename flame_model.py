"""Fire-risk model trained on NASA FLEX (PSI-69) droplet-combustion tests on the ISS.

Two models, each a bootstrap ensemble so every prediction carries an uncertainty band:
  * p_extinction: probability the flame self-extinguishes before the fuel droplet is
    consumed (higher = safer). Logistic regression.
  * k_mm2_s: burning-rate constant K (mm^2/s) from the d^2 law (higher = burns faster).
    Ridge regression.

`in_domain` is False when the query sits far from any real FLEX test (nearest-neighbour
distance in standardised feature space above the 95th percentile seen in the data), or
outside the per-feature range. Predictions there are extrapolation and must be shown as such.

Data path: data/processed/flex_clean.csv next to this file, or set FLAME_DATA.
"""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.preprocessing import StandardScaler

FEATURES = ["x_o2", "x_co2", "x_he", "p_atm", "d0_mm", "is_heptane"]
FUELS = ("Methanol", "Heptane")
DILUENTS = ("N2", "CO2", "He")
N_BOOT = 200
SEED = 0

DATA_PATH = Path(os.environ.get(
    "FLAME_DATA", Path(__file__).resolve().parent / "data" / "processed" / "flex_clean.csv"
))


def _features(fuel, x_o2, p_atm, diluent, x_diluent, d0_mm) -> dict:
    if fuel not in FUELS:
        raise ValueError(f"fuel must be one of {FUELS}")
    if diluent not in DILUENTS:
        raise ValueError(f"diluent must be one of {DILUENTS}")
    x_dil = 0.0 if diluent == "N2" else float(x_diluent)
    return {
        "x_o2": float(x_o2),
        "x_co2": x_dil if diluent == "CO2" else 0.0,
        "x_he": x_dil if diluent == "He" else 0.0,
        "p_atm": float(p_atm),
        "d0_mm": float(d0_mm),
        "is_heptane": 1.0 if fuel == "Heptane" else 0.0,
    }


@lru_cache(maxsize=1)
def _fit():
    df = pd.read_csv(DATA_PATH)
    df["is_heptane"] = (df["fuel"] == "Heptane").astype(float)
    cls = df.dropna(subset=["x_o2", "p_atm", "d0_mm"]).reset_index(drop=True)
    reg = cls[cls["k_mm2_s"] > 0.1].dropna(subset=["k_mm2_s"]).reset_index(drop=True)

    scaler = StandardScaler().fit(cls[FEATURES])
    Xc = scaler.transform(cls[FEATURES])
    yc = cls["extinguished"].to_numpy()
    Xr = scaler.transform(reg[FEATURES])
    yr = reg["k_mm2_s"].to_numpy()

    rng = np.random.default_rng(SEED)
    clf_coefs, reg_coefs = [], []
    for _ in range(N_BOOT):
        i = rng.integers(0, len(Xc), len(Xc))
        if yc[i].min() == yc[i].max():
            continue
        m = LogisticRegression(max_iter=1000).fit(Xc[i], yc[i])
        clf_coefs.append(np.r_[m.intercept_, m.coef_.ravel()])
        j = rng.integers(0, len(Xr), len(Xr))
        r = Ridge(alpha=1.0).fit(Xr[j], yr[j])
        reg_coefs.append(np.r_[r.intercept_, r.coef_])

    # Test-to-test scatter of K, so k_low/k_high are prediction intervals, not just CI of the mean.
    full = Ridge(alpha=1.0).fit(Xr, yr)
    resid_sd = float(np.std(yr - full.predict(Xr), ddof=len(FEATURES) + 1))

    # Domain check: nearest-neighbour distance threshold from the data itself.
    d = np.sqrt(((Xc[:, None, :] - Xc[None, :, :]) ** 2).sum(-1))
    np.fill_diagonal(d, np.inf)
    nn_thresh = float(np.quantile(d.min(1), 0.95))
    ranges = cls[FEATURES].agg(["min", "max"])

    return {
        "scaler": scaler, "Xc": Xc, "rows": cls,
        "clf": np.array(clf_coefs), "reg": np.array(reg_coefs),
        "nn_thresh": nn_thresh, "ranges": ranges, "resid_sd": resid_sd,
    }


def _predict_frame(X: pd.DataFrame) -> pd.DataFrame:
    f = _fit()
    Z = f["scaler"].transform(X[FEATURES])
    Z1 = np.c_[np.ones(len(Z)), Z]
    p = 1.0 / (1.0 + np.exp(-(Z1 @ f["clf"].T)))  # (n, boot)
    k = Z1 @ f["reg"].T
    k_half = 1.645 * np.sqrt(k.std(1) ** 2 + f["resid_sd"] ** 2)  # 90% prediction interval

    dist = np.sqrt(((Z[:, None, :] - f["Xc"][None, :, :]) ** 2).sum(-1))
    nn = dist.min(1)
    lo, hi = f["ranges"].loc["min"], f["ranges"].loc["max"]
    in_range = ((X[FEATURES] >= lo) & (X[FEATURES] <= hi)).all(axis=1).to_numpy()
    valid = (X["x_o2"] + X["x_co2"] + X["x_he"] <= 1.0).to_numpy()

    out = pd.DataFrame({
        "p_extinction": p.mean(1),
        "p_low": np.quantile(p, 0.05, axis=1),
        "p_high": np.quantile(p, 0.95, axis=1),
        "k_mm2_s": k.mean(1),
        "k_low": np.maximum(k.mean(1) - k_half, 0.0),
        "k_high": k.mean(1) + k_half,
        "in_domain": in_range & valid & (nn <= f["nn_thresh"]),
        "_dist": list(dist),
    }, index=X.index)
    return out


def predict(fuel: str, x_o2: float, p_atm: float, diluent: str = "N2",
            x_diluent: float = 0.0, d0_mm: float = 3.0, n_nearest: int = 3) -> dict:
    """Predict extinction probability and burning-rate constant K for one condition.

    x_o2, x_diluent are mole fractions; N2 fills the remainder. p_atm in atmospheres.
    p_low/p_high: 90% bootstrap interval of the probability.
    k_low/k_high: 90% prediction interval for a single test (model + test-to-test scatter).
    """
    X = pd.DataFrame([_features(fuel, x_o2, p_atm, diluent, x_diluent, d0_mm)])
    r = _predict_frame(X).iloc[0]
    rows = _fit()["rows"]
    idx = np.argsort(r["_dist"])[:n_nearest]
    nearest = rows.iloc[idx][["flex_id", "fuel", "diluent", "x_o2", "p_atm",
                              "d0_mm", "test_end", "k_mm2_s"]]
    return {
        "p_extinction": round(float(r["p_extinction"]), 3),
        "p_low": round(float(r["p_low"]), 3),
        "p_high": round(float(r["p_high"]), 3),
        "k_mm2_s": round(float(r["k_mm2_s"]), 3),
        "k_low": round(float(r["k_low"]), 3),
        "k_high": round(float(r["k_high"]), 3),
        "in_domain": bool(r["in_domain"]),
        "nearest_tests": nearest.round(3).to_dict("records"),
        "source": "PSI-69 FLEX",
    }


def risk_grid(fuel: str, diluent: str = "N2", x_diluent: float = 0.0, d0_mm: float = 3.0,
              x_o2=np.round(np.arange(0.12, 0.401, 0.01), 2),
              p_atm=np.round(np.arange(0.5, 3.01, 0.1), 2)) -> pd.DataFrame:
    """Grid of predictions over O2 mole fraction x pressure, for heatmaps."""
    rows = [_features(fuel, o, p, diluent, x_diluent, d0_mm) for o in x_o2 for p in p_atm]
    X = pd.DataFrame(rows)
    out = _predict_frame(X).drop(columns="_dist")
    return pd.concat([X[["x_o2", "p_atm"]], out], axis=1)


def evaluate(n_splits: int = 5) -> dict:
    """Day-grouped cross-validation, so tests run on the same day never straddle folds."""
    from sklearn.metrics import balanced_accuracy_score, r2_score, roc_auc_score
    from sklearn.model_selection import GroupKFold
    from sklearn.pipeline import make_pipeline

    df = pd.read_csv(DATA_PATH)
    df["is_heptane"] = (df["fuel"] == "Heptane").astype(float)
    d = df.dropna(subset=["x_o2", "p_atm", "d0_mm", "date"]).reset_index(drop=True)
    g = pd.to_datetime(d["date"]).dt.strftime("%Y-%m-%d")
    y = d["extinguished"].to_numpy()
    p = np.zeros(len(d))
    for tr, te in GroupKFold(n_splits).split(d, y, g):
        m = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
        p[te] = m.fit(d.loc[tr, FEATURES], y[tr]).predict_proba(d.loc[te, FEATURES])[:, 1]

    r = d[d["k_mm2_s"] > 0.1].dropna(subset=["k_mm2_s"]).reset_index(drop=True)
    gr = pd.to_datetime(r["date"]).dt.strftime("%Y-%m-%d")
    yr = r["k_mm2_s"].to_numpy()
    pr = np.zeros(len(r))
    for tr, te in GroupKFold(n_splits).split(r, yr, gr):
        m = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
        pr[te] = m.fit(r.loc[tr, FEATURES], yr[tr]).predict(r.loc[te, FEATURES])

    return {
        "n_extinction": len(d), "base_rate": round(float(y.mean()), 3),
        "roc_auc": round(float(roc_auc_score(y, p)), 3),
        "balanced_acc": round(float(balanced_accuracy_score(y, p > 0.5)), 3),
        "n_k": len(r), "k_r2": round(float(r2_score(yr, pr)), 3),
        "cv": f"GroupKFold({n_splits}) by test day",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(evaluate(), indent=2))
    for q in [("Methanol", 0.21, 1.0, "N2", 0.0, 3.0),
              ("Heptane", 0.34, 0.7, "N2", 0.0, 3.0),
              ("Heptane", 0.21, 1.0, "CO2", 0.25, 3.0),
              ("Heptane", 0.21, 1.0, "He", 0.25, 3.0),
              ("Methanol", 0.40, 3.0, "N2", 0.0, 3.0)]:
        r = predict(*q)
        r.pop("nearest_tests")
        print(q, "->", r)
    g = risk_grid("Heptane")
    print(g.shape, "in_domain share:", round(g["in_domain"].mean(), 2))
