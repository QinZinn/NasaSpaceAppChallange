# Fact check — every number/claim in submission.md and demo_script.md

Status key: ✅ traced to a repo file or command output · ⚠️ [CẦN KIỂM TRA] not yet verified against a primary source.

## Model numbers — from `uv run flame_model.py` (run 14 Nov 2026)

| Claim | Value | Status |
|---|---|---|
| Extinction tests | 261 | ✅ evaluate().n_extinction |
| Base rate self-extinguished | 0.686 | ✅ |
| ROC-AUC | 0.881 | ✅ |
| Balanced accuracy | 0.762 | ✅ |
| K tests | 256 | ✅ |
| K R² | 0.71 | ✅ |
| CV scheme | GroupKFold(5) by test day | ✅ |
| FLEX rows / fuels / dates | 274; Methanol 157, Heptane 117; 2009-03-05 to 2011-12-08 | ✅ flex_clean.csv |
| In-domain share of default grid | 0.19 of 754 → "~81 % extrapolation" | ✅ self-test output (754, 9) |
| Bootstrap resamples | 200 | ✅ `N_BOOT` in flame_model.py |

**Re-run `uv run flame_model.py` just before submitting**: if workstream M changes the model, update every table here.

## SAFFIRE-II numbers — from `data/raw/PSI-99_SAFFIRE-II.csv`

| Claim | Status |
|---|---|
| 20 cm/s concurrent flow, ~21.5–22.1 % O₂ | ✅ CSV |
| Silicone 0.27 mm: 0 g burn length ~0, 1 g "Complete" | ✅ CSV; ⚠️ "?-g" header read as µ-g |
| Silicone 0.61 mm: 0 g ~0; 1 g 7.6 cm @ 1.2 mm/s | ✅ CSV |
| SIBAL 2-5: 29 cm, 2.1 mm/s (0 g); 1 g complete | ✅ CSV |
| 2-6 is SIBAL, 29 cm, 2.6 mm/s | ⚠️ material cell empty in CSV (inferred from row above) |
| PMMA 2-8: ~10 cm damage, flame anchored (Note 3/4); 1 g complete | ✅ CSV |
| 1 g runs share the same flow/ignition settings as flight runs | ⚠️ not stated in CSV — check NASA SAFFIRE-II report |
| "Cygnus cargo vehicle" as the host | ⚠️ from general knowledge, not in repo — confirm with NASA SAFFIRE page |
| Thickness typos ("037 mm") | ⚠️ avoided in text; rows 2-4 to 2-6 not quoted by thickness |

## Historical claims — NOT in the repo, from general knowledge

| Claim | Status |
|---|---|
| Apollo 1 fire 27 Jan 1967, three astronauts died | ⚠️ verify: NASA Apollo 204 Review Board report |
| Pure/near-pure O₂ cabin atmosphere | ⚠️ same source |
| Mir fire Feb 1997 from an oxygen-generating canister | ⚠️ verify: NASA/ESA incident accounts |

Per CLAUDE.md honesty rules these need a cited document. Ask workstream B to add them to `evidence/evidence.json`
(or give me the citations), then flip to ✅. If they cannot be verified before the deadline, drop the dates
and keep only "Apollo 1 and Mir" as widely-known examples.

## Process / rules claims

| Claim | Status |
|---|---|
| 30 s video or 7 slides, public link, no login, English subtitles | ⚠️ from 2021–2025 guides via search snippets; 2026 guide unreadable |
| Judging criteria Impact, Creativity, Validity, Relevance, Presentation | ⚠️ from 2025 guide per search; confirm 2026 |
| Submission closes 15 Nov 2026 23:59 local | ✅ CLAUDE.md; official page says same (secondhand) |
| Project Submission Guide / Judging Guide 2026 contents | ⚠️ could not be fetched (HTTP 503; curl TLS error) |
