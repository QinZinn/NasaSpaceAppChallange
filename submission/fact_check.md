# Fact check — numbers and claims in submission.md, demo_script.md, pitch_5min.md

✅ = traced to a repo file, `evidence.json` id or command output · ⚠️ = [CẦN KIỂM TRA], not verified.
Updated 14 Nov 2026 after pulling `main` (evidence.json: 25 items, all `verified: true`; app/ present).

## Model numbers — `uv run flame_model.py`, re-run 14 Nov 2026 (unchanged since the first draft)

| Claim | Value | Status |
|---|---|---|
| Tests used: extinction / K | 261 / 256 | ✅ evaluate() |
| Base rate self-extinguished (of the 261) | 0.686 | ✅ |
| ROC-AUC · balanced accuracy · K R² | 0.881 · 0.762 · 0.71 | ✅ |
| CV scheme | GroupKFold(5) by test day | ✅ |
| Bootstrap resamples | 200 | ✅ `N_BOOT` |
| In-domain share of default grid | 19 % (0.187 of 754) → "81 % extrapolation" | ✅ risk_grid |
| ISS air, 3 mm droplet, methanol | 72 % (62–81 %), K 0.50 (0.38–0.61) | ✅ predict() |
| ISS air, 3 mm droplet, heptane | 43 % (32–55 %), K 0.53 (0.42–0.65) | ✅ predict() |

Re-run before submitting; if workstream M changes the model, update all four files.

## Evidence-backed numbers

| Claim in text | Evidence id | Status |
|---|---|---|
| SIBAL: 29 cm, 2.1 and 2.6 mm/s at 0 g; 1 g burned completely | ev-01 | ✅ |
| One SIBAL sample planned at 30 cm/s, logged 20 cm/s | ev-01 | ✅ |
| Silicone 0.27 / 0.61 / 1.03 mm: 0 g ≈ 0; 1 g complete / 7.6 cm @ 1.2 mm/s / ≈ 0 | ev-02 | ✅ |
| Thick PMMA ≈ 10 cm, flame anchored, 0.01–0.04 mm/s; 1 g complete | ev-06 | ✅ |
| Nomex not ignited by burning PMMA | ev-10 | ✅ |
| Prior tests ≤ 10 cm; reliance on terrestrial standards | ev-12 | ✅ |
| Saffire I–III cover ISS-like air, not exploration atmospheres | ev-14 | ✅ |
| 2 large + 9 smaller samples | ev-19 | ✅ |
| FLEX 186 extinction / 27 completion / 61 disruption of 274; 157 methanol, 117 heptane; Mar 2009–Dec 2011 | ev-22 | ✅ |
| Methanol 37/37 at ≤ 0.15 O₂ vs 13/35 above 0.22 | ev-15 | ✅ |
| Median K heptane: He 0.65, CO₂ 0.50 mm²/s | ev-23 | ✅ |
| MEC 1 g → 0 g: CO₂ 0.16 → 0.19, N₂ 0.26 → 0.38; 0 g values are simulations | ev-05 | ✅ |
| CO₂ may be less effective in microgravity | ev-16 | ✅ |
| PMMA rod burned at 14.8 % O₂ (single run) | ev-04 | ✅ |
| Saffire-I flew on an uncrewed Cygnus after leaving the ISS | ev-11 | ✅ (resolves the earlier "Cygnus" doubt; SAFFIRE-II's carrier is not claimed) |

Resolved since the first draft: "?-g" column = microgravity (confirmed by workstream B); SAFFIRE-II sample 2-6 is SIBAL (ev-01); Submission rules, 8 fields and 5 criteria (confirmed by user from the Hà Nội organisers).

## Still open ⚠️

| Item | What to do |
|---|---|
| Apollo 1 / Mir | No dates or details are used. User offered to paste two NASA pages; until then slide 1, pitch opening and references carry a `[ĐIỀN]` slot. |
| Character limits of the 8 form fields | Unknown; check on the form and trim `submission.md`. |
| Repo public? Which branch to link? App URL? Demo URL? | Fill `submission.md` §3–4. |
| LLM actually used in the demo | Code default is `anthropic/claude-sonnet-4.5` via OpenRouter, overridable by `FLAME_LLM_MODEL`; confirm what the demo runs on. |
| Does the judges' copy have an `OPENROUTER_API_KEY`? | If not, tab 3 is off; say so in §4 and skip it in the demo. |
| How much of the evidence you checked yourself | Fill the `[CẦN KIỂM TRA]` in §6 and pitch Q8. I do not claim a human review that I cannot see. |
| PSI licence wording / PSI URL | Check on the PSI site; add URL to references. |
| pypdf used by workstream B? | Confirm or delete from references. |
| Team name as registered | Fill in. |
| "CLAUDE.md" still says deadline 23:59 | Shared file; change only if you ask. Real Hà Nội deadline: 11:00 Sun 15 Nov. |
