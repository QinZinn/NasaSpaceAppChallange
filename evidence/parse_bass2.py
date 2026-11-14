"""Parse the BASS-II as-run test matrix (PSI-25) into a structured table.

Usage (from repo root): uv run evidence/parse_bass2.py
  optional args: <bass2_csv> <out_csv>

Nothing is invented: every derived column comes from a raw column of the same row, and the raw
free-text fields are kept next to the parsed ones. Column meanings follow the NASA
"BASS-II data FAQ" (fan display = fan voltage x10 or control-box pot setting; air display =
duct flow speed in cm/s with ~1 min response; OR = CO over range, > 1000 ppm).
"""
import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data/raw/PSI-25_BASS-II.csv"
out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "data/processed/bass2_structured.csv"

raw = pd.read_csv(src, dtype=str, encoding="utf-8-sig", keep_default_na=False)
raw.columns = [re.sub(r"\s+", " ", c).strip() for c in raw.columns]
raw = raw.apply(lambda s: s.str.strip())

# Ignition end / flow geometry per PI. "FAQ" = stated in the BASS-II data FAQ (as run);
# "SRD plan" = only the pre-flight science requirements say so (planned, not confirmed as run).
GEOMETRY = {
    "Olson": ("concurrent", "FAQ"),            # rods ignited at the upstream end, stagnation flame
    "Fernandez-Pello": ("opposed", "FAQ"),     # rods ignited at the downstream end
    "Miller": ("opposed", "SRD plan"),
    "T'ien": ("concurrent", "SRD plan"),       # plan: mostly concurrent SIBAL, a few opposed
}

# Rows where the air-display cell does not hold a plain list of cm/s values (fan voltages and
# air speeds are swapped or mixed). Values below are read off the same row by hand.
AIR_OVERRIDES = {
    "O5b": [5],            # "49   5 cm/s": 49 is the fan display
    "O13a": [5, 2, 0],     # "49 44 42 41 41 40.5 (5 2 0)": fan first, air in brackets
    "O13b": [7, 4],        # "7   4? (49 ?)"
    "O6": [5],             # air cell says "see fan"; fan cell starts at 5 cm/s, then pot settings
    "O7": [5], "O8a": [5], "O8b": [5], "O9": [5],   # air cell empty; same pattern in fan cell
}

INCH = {"1/4": 0.25, "3/8": 0.375, "1/2": 0.5, "0.5": 0.5}


def num(x):
    """Sensor reading -> float, or None for 'none' / over-range / blank."""
    try:
        return float(x)
    except ValueError:
        return None


def material(pi: str, text: str) -> dict:
    t = text.lower()
    d = dict(material=None, geometry=None, thickness_mm=None, width_cm=None,
             rod_diameter_in=None, rod_diameter_mm=None, color=None, burn_sides=None)
    if "rod" in t:
        d.update(material="PMMA", geometry="rod")
        m = re.search(r"(1/4|3/8|1/2|0\.5)", t)
        d["rod_diameter_in"] = INCH[m.group(1)]
        d["rod_diameter_mm"] = round(INCH[m.group(1)] * 25.4, 2)
        d["color"] = "black" if "bla" in t else "clear"
    elif "sibal" in t:
        d.update(material="SIBAL (75/25 cotton/fiberglass)", geometry="fabric sheet")
    elif "nomex" in t:
        d.update(material="Nomex III", geometry="fabric sheet")
    elif "candle" in t:
        d.update(material="Japan wax", geometry="candle")
    elif "spherical" in t:
        d.update(material="PMMA", geometry="spherical section")
    else:  # Bhattacharjee films and Miller slabs: all PMMA per the FAQ
        d.update(material="PMMA", geometry="film" if pi == "Bhattacharjee" else "slab")
        m = re.search(r"(\d+)\s*micron", t)
        if m:
            d["thickness_mm"] = int(m.group(1)) / 1000
        else:
            m = re.search(r"([\d.]+)\s*mm", t)
            d["thickness_mm"] = float(m.group(1)) if m else None
        if pi == "Miller":
            d["burn_sides"] = 1 if "1 sided" in t else 2 if "2 sided" in t else None
    if d["geometry"] in ("film", "slab", "fabric sheet"):
        m = re.search(r"([\d.]+)\s*cm", t)
        d["width_cm"] = float(m.group(1)) if m else None
    if d["geometry"] == "spherical section":
        d["width_cm"] = 4.0  # "4 cm spherical section"
    return d


def air_flow(test: str, text: str) -> dict:
    """Air-display cell -> sequence of duct flow speeds (cm/s) in the order they were set."""
    if test in AIR_OVERRIDES:
        seq, conf = AIR_OVERRIDES[test], "manual"
    else:
        t = re.sub(r"\([^)]*\)|\([^)]*$", " ", text)   # bracketed values are fan/pot settings
        if t.rstrip().endswith("pot"):                  # "3  0.5 pot   0.4 pot": pot settings
            t = re.sub(r"[\d.]+\s+pot\b", " ", t)
        else:                                           # "5   pots 0.4 0.36 ...": all that follows
            t = re.split(r"\bpots?\b", t)[0]
        t = t.replace(">", " ")
        seq = [float(x) for x in re.findall(r"(?<![\d.<])\d+\.?\d*(?!\d)", t)]
        clean = re.fullmatch(r"[\d.\s~]*", t) is not None
        conf = "none" if not seq else "high" if clean else "medium"
    return dict(
        air_flow_seq_cm_s=";".join(f"{v:g}" for v in seq) or None,
        air_flow_first_cm_s=seq[0] if seq else None,
        air_flow_min_cm_s=min(seq) if seq else None,
        air_flow_max_cm_s=max(seq) if seq else None,
        air_flow_parse=conf,
    )


def doy(date: pd.Timestamp):
    return None if pd.isna(date) else int(date.day_of_year)


rows = []
for _, r in raw.iterrows():
    pi, test = r["PI"], r["Test #"]
    notes = f'{r["Fan display"]} | {r["Air display"]}'.lower()
    date = pd.to_datetime(r["Date"], format="%m/%d/%Y", errors="coerce")
    o2i, o2f = num(r["Calibrated initial O2 % by vol"]), num(r["Calibrated final O2 % by vol"])
    coi, cof = num(r["Initial CO (ppm)"]), num(r["Final CO (ppm)"])
    co2i, co2f = num(r["Initial CO2 % by vol"]), num(r["Final CO2 % by vol"])
    cof_raw = r["Final CO (ppm)"].lower()

    flags = []
    # A flame cannot move cabin O2 by tens of percent in one burn; such entries are log errors.
    if o2f is not None and o2i is not None and not (o2i - 5 <= o2f <= o2i + 0.5):
        flags.append("o2_final_implausible_dropped")
        o2f = None
    if date is not pd.NaT and str(doy(date)) != r["GMT"]:
        flags.append("date_gmt_day_mismatch")
    if date is not pd.NaT and date.year not in (2014, 2016):
        flags.append("date_year_suspect")
    if r["Fan display"] == "80122":
        flags.append("fan_display_run_together")

    geom, basis = GEOMETRY.get(pi, (None, None))
    row = dict(
        pi=pi, test_id=test, date=None if pd.isna(date) else date.date().isoformat(),
        gmt_day=num(r["GMT"]), sample_id=r["Sample #"],
        **material(pi, r["Fuel Sample Material"]),
        flow_geometry=geom, flow_geometry_basis=basis,
        flow_restrictor=num(r["Flow restrictor"]),
        **air_flow(test, r["Air display"]),
        flow_below_1_cm_s_noted=bool(re.search(r"<\s*1|\blow|(?<![\d.])0(?![\d.])", r["Air display"].lower())),
        extinction_noted=bool(re.search(r"\bext|extinguished|\d\.?\d*ext|\bout\b(?! at fan)", notes)),
        blowoff_noted="blowoff" in notes,
        ignition_failure_noted=bool(re.search(r"no ign|would not stay lit", notes)),
        o2_initial_pct=o2i, o2_final_pct=o2f,
        o2_drop_pct=None if None in (o2i, o2f) else round(o2i - o2f, 2),
        co2_initial_pct=co2i, co2_final_pct=co2f,
        co2_rise_pct=None if None in (co2i, co2f) else round(co2f - co2i, 2),
        co_initial_ppm=coi, co_final_ppm=cof,
        co_rise_ppm=None if None in (coi, cof) else round(cof - coi, 1),
        co_final_over_range=cof_raw in ("or", "over"),   # FAQ: OR = over range (> 1000 ppm)
        co_final_lower_bound_ppm=1000 if cof_raw in ("or", "over") else
        num(cof_raw[1:]) if cof_raw.startswith(">") else None,
        radiometer_gain_raw=r["Radiometer gain (1000 250 50 10)"],
        total_frames=num(r["Total Frames Shot"]),
        quality_flags=";".join(flags) or None,
        material_raw=r["Fuel Sample Material"], fan_display_raw=r["Fan display"],
        air_display_raw=r["Air display"], date_raw=r["Date"],
        o2_final_raw=r["Calibrated final O2 % by vol"], co_final_raw=r["Final CO (ppm)"],
        source="PSI-25 BASS-II",
    )
    rows.append(row)

df = pd.DataFrame(rows)
out.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out, index=False)

if __name__ == "__main__":
    print(f"rows={len(df)} -> {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    print(df.groupby(["pi", "geometry"]).size().to_string())
    print("air_flow_parse:", df["air_flow_parse"].value_counts().to_dict())
    print("flags:", df["quality_flags"].value_counts().to_dict())
    print("extinction/blowoff/ign-failure noted:",
          int(df.extinction_noted.sum()), int(df.blowoff_noted.sum()), int(df.ignition_failure_noted.sum()))
