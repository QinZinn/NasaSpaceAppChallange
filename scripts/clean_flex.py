"""Clean PSI-69 FLEX experimental table and run baseline models.

Usage (from repo root): uv run scripts/clean_flex.py
  optional args: <flex_csv> <out_csv>
"""
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import balanced_accuracy_score, r2_score, roc_auc_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = __import__("pathlib").Path(__file__).resolve().parent.parent
src = sys.argv[1] if len(sys.argv) > 1 else ROOT / "data/raw/PSI-69_FLEX.csv"
out = sys.argv[2] if len(sys.argv) > 2 else ROOT / "data/processed/flex_clean.csv"
raw = pd.read_csv(src, encoding="cp1252", dtype=str)
raw.columns = [c.strip() for c in raw.columns]

cols = {
    "FLEX Test #": "test_no",
    "FLEX Identifier": "flex_id",
    "Test Date": "date",
    "Fuel": "fuel",
    "Ambient pressure; mmHg": "p_mmhg",
    "O initial ambient composition; mole fraction": "x_o2",
    "N initial ambient composition; mole fraction": "x_n2",
    # Header is mangled ("CO"); FLEX used CO2 as a suppressant diluent.
    "CO initial ambient composition; mole fraction": "x_co2",
    "He initial ambient composition; mole fraction": "x_he",
    "Droplet initial diameter; mm": "d0_mm",
    "Visible flame extinction diameter; mm": "d_ext_mm",
    # Header says "mm"; physically this is the burning-rate constant K (mm^2/s).
    "Burning rate; mm": "k_mm2_s",
    "Burn time; s": "burn_time_s",
    "Test end": "test_end",
}
df = raw.rename(columns=cols)[list(cols.values())].copy()

num = ["p_mmhg", "x_o2", "x_n2", "x_co2", "x_he", "d0_mm", "d_ext_mm", "k_mm2_s", "burn_time_s"]
for c in num:
    s = df[c].astype(str).str.replace("~", "", regex=False).str.strip()
    df[c] = pd.to_numeric(s, errors="coerce")  # '�'/blank -> NaN

df.loc[df["p_mmhg"] <= 0, "p_mmhg"] = np.nan  # one row logs 0 mmHg
df["date"] = pd.to_datetime(df["date"], format="mixed", errors="coerce")
df["p_atm"] = df["p_mmhg"] / 760.0
df["p_o2_atm"] = df["x_o2"] * df["p_atm"]  # oxygen partial pressure
df["extinguished"] = (df["test_end"].str.strip() == "Extinction").astype(int)
df["diluent"] = np.select(
    [df["x_he"] > 0, df["x_co2"] > 0], ["He", "CO2"], default="N2"
)
df["source"] = "PSI-69 FLEX"
df.to_csv(out, index=False)

print(f"rows={len(df)}")
print(df["test_end"].value_counts().to_string())
print(df.groupby(["fuel", "diluent"]).size().to_string())
print(df[num + ["p_o2_atm"]].describe().T[["count", "min", "max"]].round(3).to_string())

# Baselines with day-grouped CV (tests on the same day share hardware state).
feat = ["x_o2", "x_co2", "x_he", "p_atm", "d0_mm", "is_heptane"]
d = df.dropna(subset=["x_o2", "p_atm", "d0_mm", "date"]).copy()
d["is_heptane"] = (d["fuel"] == "Heptane").astype(int)
groups = d["date"].dt.strftime("%Y-%m-%d")
gkf = GroupKFold(n_splits=5)

y = d["extinguished"].values
pred = np.zeros(len(d))
for tr, te in gkf.split(d, y, groups):
    m = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    m.fit(d.iloc[tr][feat], y[tr])
    pred[te] = m.predict_proba(d.iloc[te][feat])[:, 1]
print(f"\nExtinction classifier (n={len(d)}, base rate={y.mean():.2f}): "
      f"ROC-AUC={roc_auc_score(y, pred):.3f}, "
      f"balanced acc={balanced_accuracy_score(y, pred > 0.5):.3f}")

r = d.dropna(subset=["k_mm2_s"])
r = r[r["k_mm2_s"] > 0.1]
yr = r["k_mm2_s"].values
pr = np.zeros(len(r))
for tr, te in gkf.split(r, yr, r["date"].dt.strftime("%Y-%m-%d")):
    m = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
    m.fit(r.iloc[tr][feat], yr[tr])
    pr[te] = m.predict(r.iloc[te][feat])
print(f"Burning-rate K regression (n={len(r)}): CV R2={r2_score(yr, pr):.3f}")

m = make_pipeline(StandardScaler(), Ridge(alpha=1.0)).fit(r[feat], yr)
print("Ridge std. coefficients:",
      dict(zip(feat, m[-1].coef_.round(3))))
