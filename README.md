# Flame in Freefall — NASA Space Apps 2026

AI-powered fire-safety insights from NASA microgravity combustion experiments, for Moon and Mars habitats.
Team: Zinnn (NASA Space Apps Challenge 2026, Hà Nội local event).

## Run

```bash
uv run flame_model.py               # model self-test + cross-validated metrics
uv run streamlit run app/app.py     # dashboard
```

## Data

NASA Physical Sciences Informatics (PSI) experimental tables in `data/raw/`:
FLEX (PSI-69), FLEX-2 (PSI-68), BASS (PSI-26), BASS-II (PSI-25), SAFFIRE I–III (PSI-98/99/100).

## Layout

- `flame_model.py` — extinction-probability and burning-rate models trained on 274 ISS FLEX tests
- `app/` — Streamlit dashboard
- `evidence/` — ranked, cited findings from NASA documents
- `submission/` — Space Apps submission text and pitch

See `CLAUDE.md` for how the parallel workstreams fit together.
