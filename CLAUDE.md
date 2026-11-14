# Flame in Freefall — NASA Space Apps 2026 (Hà Nội)

Challenge: *Flame in Freefall: AI-Powered Fire Safety Insights from Microgravity Combustion Data*.
Build an interactive, AI-powered dashboard that summarizes, ranks and interprets NASA microgravity
combustion results to deliver fire-safety insights for Moon and Mars missions.
**Submission closes 15 Nov 2026, 23:59 (Asia/Ho_Chi_Minh).** Working and honest beats pretty.

Solo participant; several Claude sessions work on this repo **in parallel**. Read all of this first.

## Who owns what — edit ONLY your own paths

| Workstream | Owns | Does not touch |
|---|---|---|
| **M — Model** | `flame_model.py`, `scripts/`, `data/processed/flex_clean.csv`, `insights/` | everything else |
| **A — Dashboard** | `app/` (mocks go in `app/mocks/`) | model, evidence, submission |
| **B — Evidence** | `evidence/`, `data/processed/bass2_structured.csv` | model, app, submission |
| **C — Submission & pitch** | `submission/` | code and data |

Shared files (`CLAUDE.md`, `README.md`, `pyproject.toml`, `data/raw/`): change only if the user asks.
Need a new dependency or an API change? Write it in your final message to the user instead of
editing someone else's file.

## Git rules (sessions may share one working tree)

- Stage only your own paths: `git add app/` — **never** `git add -A` / `git add .` / `git commit -a`.
- Before pushing: `git pull --rebase origin main`, then `git push origin main`.
- Small, frequent commits. Never force-push, never rewrite history, never delete others' files.
- If a rebase conflicts in a path you do not own, stop and tell the user.

## Environment

The user uses **uv**, never bare python/pip/venv. Run things from the repo root:
- Model self-test: `uv run flame_model.py`
- Re-clean FLEX: `uv run scripts/clean_flex.py`
- Dashboard: `uv run streamlit run app/app.py`
- One-off extra package: `uv run --with <pkg> ...` (ask the user before adding to pyproject).

## Data (`data/raw/`, from NASA PSI, CC0)

| File | Rows | State | Use |
|---|---|---|---|
| `PSI-69_FLEX.csv` | 274 | clean, has outcomes; **cp1252 encoding** | the only ML-grade table |
| `PSI-25_BASS-II.csv` | 129 | flow settings are free text ("5 3 2 ext") | evidence on solid-material limits |
| `PSI-26_BASS.csv` | 122 | test list + material only | catalogue of materials tested |
| `PSI-68_FLEX-2.csv` | 8 | design matrix only, no outcomes | describes coverage |
| `PSI-98/99/100_SAFFIRE-*.csv` | 2/9/2 | tiny; SAFFIRE-II compares 0 g vs 1 g | strongest evidence for the pitch |

FLEX header fixes (already applied in `flex_clean.csv`): column "CO" is **CO2**; "Burning rate; mm"
is the burning-rate constant **K in mm²/s**.

## API contract

### `flame_model.py` (workstream M)
```python
predict(fuel, x_o2, p_atm, diluent="N2", x_diluent=0.0, d0_mm=3.0) -> dict
# keys: p_extinction, p_low, p_high, k_mm2_s, k_low, k_high, in_domain, nearest_tests, source
risk_grid(fuel, diluent="N2", x_diluent=0.0, d0_mm=3.0) -> DataFrame
# columns: x_o2, p_atm, p_extinction, p_low, p_high, k_mm2_s, k_low, k_high, in_domain
evaluate() -> dict   # day-grouped CV metrics; use these numbers in the pitch, nothing else
```
- `fuel` ∈ {"Methanol","Heptane"}; `diluent` ∈ {"N2","CO2","He"}; fractions are mole fractions, N2 fills the rest.
- `p_extinction` = probability the flame **self-extinguishes** before the droplet is consumed → **higher is safer**.
- `k_mm2_s` = burning-rate constant → higher burns faster. `k_low/k_high` = 90% prediction interval.
- `in_domain=False` = extrapolation beyond NASA data (~80% of the default grid). UI must grey it out.
- The model covers **liquid fuel droplets only** (FLEX). Solids (fabric, plastic) are evidence cards, not model output.

### `evidence/evidence.json` (workstream B)
A JSON list; each item:
```json
{"id": "ev-01", "source": "PSI-99", "investigation": "SAFFIRE-II",
 "claim": "...", "condition": "20 cm/s concurrent flow, ~22% O2",
 "gravity": "0g vs 1g", "numbers": "2.1-2.6 mm/s",
 "topic": "solid_flame_spread|extinction|suppressant|oxygen_limit|smoke",
 "importance": 1, "citation": "document title, page X", "verified": true}
```
`importance` 1–5 = relevance to fire safety in Moon/Mars habitats. Never invent: an unverifiable
number stays empty with `"verified": false`.

## Honesty rules (all workstreams)

- Every number shown or pitched must trace to a PSI file, a cited document, or `evaluate()`.
- Label extrapolation and synthetic/demo content as such.
- Do not claim the model predicts solid-material fires or real habitat fires.
