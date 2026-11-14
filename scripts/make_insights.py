"""Compute insights/insights.json from the FLEX table and the model, so every number is reproducible.

Usage (from repo root): uv run scripts/make_insights.py
"""
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import flame_model as fm  # noqa: E402

d = pd.read_csv(ROOT / "data/processed/flex_clean.csv")
n2 = d[d.diluent == "N2"]
atm1 = n2[n2.p_atm.between(0.9, 1.1)]


def frac(df):
    return f"{int(df.extinguished.sum())} of {len(df)}"


def pct(x):
    return f"{100 * x:.0f}%"


out = []

# in-01: oxygen vs self-extinction, N2 atmospheres near 1 atm
bands = [("at or below 16% O2", atm1[atm1.x_o2 <= 0.165]),
         ("at 20-22% O2", atm1[atm1.x_o2.between(0.195, 0.225)]),
         ("at 23-30% O2", atm1[atm1.x_o2.between(0.226, 0.31)])]
parts = []
for fuel in ("Heptane", "Methanol"):
    parts.append(fuel + ": " + "; ".join(f"{frac(b[b.fuel == fuel])} {name}" for name, b in bands))
out.append({
    "id": "in-01",
    "statement": "Oxygen is the strongest lever on whether a droplet flame goes out by itself: "
                 "self-extinction is common in oxygen-poor air and rare once oxygen is enriched.",
    "numbers": "Tests ending in self-extinction, O2/N2 near 1 atm. " + " | ".join(parts),
    "basis": "Counts of FLEX tests (PSI-69) with test end = Extinction; other tests ended in "
             "Disruption or Completion. Observed data, not model output.",
})

# in-02: low pressure + enriched oxygen
lp = n2[(n2.p_atm < 0.8) & (n2.x_o2 > 0.225)]
out.append({
    "id": "in-02",
    "statement": "In the low-pressure, oxygen-enriched conditions closest to proposed exploration "
                 "atmospheres, no FLEX droplet flame put itself out.",
    "numbers": f"{frac(lp)} tests self-extinguished at {lp.p_atm.min():.2f}-{lp.p_atm.max():.2f} atm "
               f"with {pct(lp.x_o2.min())}-{pct(lp.x_o2.max())} O2 in N2 "
               f"({(lp.fuel == 'Heptane').sum()} heptane, {(lp.fuel == 'Methanol').sum()} methanol).",
    "basis": "Counts of FLEX tests (PSI-69). Liquid droplets only; says nothing direct about solids.",
})

# in-03: burning rate vs oxygen (data + model)
k_obs = "; ".join(
    f"{fuel}: " + ", ".join(f"{b[b.fuel == fuel].k_mm2_s.mean():.2f} {name}" for name, b in bands)
    for fuel in ("Heptane", "Methanol"))
k_mod = []
for fuel in ("Heptane", "Methanol"):
    a, b = fm.predict(fuel, 0.21, 1.0), fm.predict(fuel, 0.30, 1.0)
    assert a["in_domain"] and b["in_domain"]
    k_mod.append(f"{fuel} {a['k_mm2_s']:.2f} -> {b['k_mm2_s']:.2f} mm2/s (+{pct(b['k_mm2_s'] / a['k_mm2_s'] - 1)})")
out.append({
    "id": "in-03",
    "statement": "Fuel burns faster as oxygen rises: going from 21% to 30% O2 at 1 atm raises the "
                 "burning-rate constant K by about a third.",
    "numbers": "Model, 3 mm droplet, 21% -> 30% O2 at 1 atm: " + "; ".join(k_mod)
               + ". Mean measured K (mm2/s), O2/N2 near 1 atm: " + k_obs + ".",
    "basis": "Ridge model on FLEX (PSI-69), both points inside the data domain, plus measured means.",
})

# in-04: diluent comparison at similar oxygen
m = d[d.x_o2.between(0.17, 0.21) & d.p_atm.between(0.9, 1.1)]
rows = []
for fuel in ("Heptane", "Methanol"):
    for dil in ("N2", "CO2", "He"):
        s = m[(m.fuel == fuel) & (m.diluent == dil)]
        rows.append(f"{fuel}/{dil}: K {s.k_mm2_s.mean():.2f}, self-extinguished {frac(s)}")
out.append({
    "id": "in-04",
    "statement": "Adding CO2 slows droplet burning and makes self-extinction more likely; adding "
                 "helium does not slow burning.",
    "numbers": "Tests at 17-21% O2 near 1 atm (mean K in mm2/s). " + "; ".join(rows) + ".",
    "basis": "Grouped FLEX tests (PSI-69). Not a controlled comparison: diluent fraction and exact "
             "O2 differ between groups.",
})

# in-05: pressure matters much less than oxygen (model)
rows = []
for fuel in ("Heptane", "Methanol"):
    a, b, c = fm.predict(fuel, 0.21, 1.0), fm.predict(fuel, 0.21, 0.7), fm.predict(fuel, 0.30, 0.7)
    assert a["in_domain"] and b["in_domain"] and c["in_domain"]
    rows.append(f"{fuel}: {pct(a['p_extinction'])} at 21% O2/1.0 atm, {pct(b['p_extinction'])} at "
                f"21%/0.7 atm, {pct(c['p_extinction'])} at 30%/0.7 atm")
out.append({
    "id": "in-05",
    "statement": "Lowering cabin pressure barely changes the chance of self-extinction; the oxygen "
                 "enrichment that usually comes with it removes most of that chance.",
    "numbers": "Model probability of self-extinction, 3 mm droplet in O2/N2. " + "; ".join(rows) + ".",
    "basis": "Logistic model on FLEX (PSI-69), all points inside the data domain. Pressure range "
             "tested in N2 is mostly 0.7 and 1.0 atm.",
})

# in-06: how much fuel is left when the flame goes out
e = d[(d.extinguished == 1) & d.d_ext_mm.notna() & d.d0_mm.notna()]
r = (e.d_ext_mm / e.d0_mm).groupby(e.fuel).median()
cnt = e.groupby("fuel").size()
out.append({
    "id": "in-06",
    "statement": "When a flame self-extinguishes, unburned fuel is left behind, and for heptane "
                 "most of the droplet remains.",
    "numbers": f"Median droplet diameter at visible-flame extinction, as a share of initial diameter: "
               f"heptane {pct(r['Heptane'])} ({cnt['Heptane']} tests), methanol {pct(r['Methanol'])} "
               f"({cnt['Methanol']} tests).",
    "basis": "FLEX tests (PSI-69) ending in Extinction with both diameters recorded. Observed data.",
})

path = ROOT / "insights" / "insights.json"
path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
for i in out:
    print(i["id"], "|", i["statement"], "\n   ", i["numbers"])
