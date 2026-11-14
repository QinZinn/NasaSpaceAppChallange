# Fact check — numbers and claims in submission.md, demo_script.md, pitch_5min.md

✅ = traced to a repo file, `evidence.json` / `insights.json` id or command output · ⚠️ = [CẦN KIỂM TRA], not verified.
Updated 14 Nov 2026 after pulling `main` (evidence.json: 27 items, all `verified: true`; insights.json: in-01…in-06).
**Deadline (Hà Nội judging): 11:00 Sunday 15 Nov 2026.**

## Model numbers — `uv run flame_model.py`, re-run 14 Nov 2026

| Claim | Value | Status |
|---|---|---|
| Tests used: extinction / K | 261 / 256 | ✅ evaluate() |
| Base rate self-extinguished (of the 261) | 0.686 | ✅ |
| ROC-AUC · balanced accuracy · K R² | 0.881 · 0.762 · 0.71 | ✅ |
| CV scheme · bootstrap | GroupKFold(5) by test day · 200 | ✅ |
| In-domain share of default grid | 19 % (0.187 of 754) → "81 % extrapolation" | ✅ risk_grid |
| ISS air, 3 mm: methanol | 72 % (62–81 %), K 0.50 (0.38–0.61) | ✅ predict() |
| ISS air, 3 mm: heptane | 43 % (32–55 %), K 0.53 (0.42–0.65) | ✅ predict() |

Re-run before submitting; if workstream M changes the model, update all files.

## Insights — `insights/insights.json`

| Claim in text | Id | Status |
|---|---|---|
| 0 of 17 FLEX tests self-extinguished at 0.70–0.71 atm, 30–34 % O₂ in N₂ (8 heptane, 9 methanol) | in-02 | ✅ re-counted from `flex_clean.csv`: 17 tests, p 0.703–0.714, O₂ 0.30–0.34, N₂ only |
| Of those 17: 15 ended in Disruption (8 heptane, 7 methanol), 2 methanol burned to completion, 0 extinction | — (my count) | ✅ same recount; not in insights.json, so labelled "our own count" |
| Heptane self-extinction 11/14 (≤ 16 % O₂), 5/17 (20–22 %), 0/3 (23–30 %); methanol 22/22, 9/12, 2/4 | in-01 | ✅ re-counted, identical (p 0.9–1.1 atm, N₂ only) |
| Model self-extinction: heptane 43 % / 41 % / 2 %; methanol 72 % / 70 % / 6 % at 21 %-1.0, 21 %-0.7, 30 %-0.7 | in-05 | ✅ predict(): 0.432 / 0.409 / 0.020 and 0.722 / 0.700 / 0.065 (methanol 30 %-0.7 atm rounds to 6–7 %; the text follows insights.json: 6 %); all in-domain |
| Caveats: liquid droplets only; "not self-extinguished" includes Disruption | in-02 basis, in-01 basis | ✅ quoted in slide 4, §5 and pitch |

## Evidence-backed numbers

| Claim in text | Id | Status |
|---|---|---|
| Apollo 1, 27 Jan 1967, ground test; 100 % O₂; hatch 90 s → 3 s; three crew died of asphyxia (CO and toxic gases); no names used | ev-26 | ✅ |
| Mir, 24 Feb 1997; three-foot flame, several minutes; six crew; blocked one Soyuz route; smoke hours; three foam extinguishers; flame finally extinguished itself; "worst in-orbit fire" is NASA's wording | ev-27 | ✅ wording kept as "after the crew used foam extinguishers, the flame extinguished itself" — no claim that the extinguishers put it out |
| SIBAL 29 cm, 2.1 and 2.6 mm/s at 0 g; 1 g complete; 30 vs 20 cm/s note | ev-01 | ✅ |
| Silicone 0.27 / 0.61 / 1.03 mm; 0 g ≈ 0 | ev-02 | ✅ |
| Thick PMMA ≈ 10 cm, anchored; 1 g complete | ev-06 | ✅ |
| Prior tests ≤ 10 cm; terrestrial standards | ev-12 | ✅ |
| Saffire I–III not covering exploration atmospheres (elevated O₂, lower pressure is the type planned) | ev-14 | ✅ qualitative only; **no NASA numbers for exploration atmospheres are used anywhere** |
| 2 large + 9 smaller samples | ev-19 | ✅ |
| FLEX 186 / 27 / 61 of 274; 157 methanol, 117 heptane; Mar 2009–Dec 2011 | ev-22 | ✅ |
| Median K heptane He 0.65, CO₂ 0.50 | ev-23 | ✅ |
| CO₂ may be less effective in microgravity | ev-16 | ✅ |
| MEC 1 g → 0 g values; 0 g values simulated | ev-05 | ✅ |

## Exploration preset (app)

| Item | Status |
|---|---|
| Preset 34 % O₂, 0.6 atm, N₂ in `app/app.py` (`EXPLORATION`, `source: None`) | ✅ the app labels it "illustrative, needs a cited source" |
| Our text | ✅ describes it only as "high O₂, low pressure" (ev-14) and as illustrative; its values appear nowhere in the submission text or pitch. The screenshot `01_habitat_fire_risk.png` shows the button with 34 % / 0.6 atm → caption it "illustrative, not a NASA figure" (slide 5) |
| Model status of the preset | ✅ `predict('Methanol', 0.34, 0.6)` → `in_domain=False` (extrapolation) |

## Still open ⚠️

| Item | What to do |
|---|---|
| Character limits of the 8 form fields | Unknown; check on the form and trim `submission.md`. |
| Repo public? Which branch to link? App URL? Demo URL? | Fill `submission.md` §3–4. |
| LLM actually used in the demo | Code default `anthropic/claude-sonnet-4.5` via OpenRouter, overridable by `FLAME_LLM_MODEL`; confirm. Does the judges' copy have `OPENROUTER_API_KEY`? |
| How much of the evidence you checked yourself | Fill the `[CẦN KIỂM TRA]` in §6 and pitch Q8. |
| PSI licence wording / PSI URL | Check on the PSI site; add URL to references. |
| Team name as registered | Fill in. |
| Slide 5 screenshot 3 shows no answer | Re-capture with a real answer + citations if the API key works. |

Resolved: pypdf removed from References (no workstream B confirmation; nothing in the repo imports it — it is still listed in `pyproject.toml`, which is not ours to edit). Apollo 1 / Mir filled from ev-26 / ev-27.
