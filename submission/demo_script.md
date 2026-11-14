# Demo script — Flame in Freefall

**Limit used here: 30-second video OR 7-slide deck (title and intro slides included), public link, no login,
English subtitles if not spoken in English.** This is from the official 2021–2025 guides as found via search;
the 2026 guide could not be fetched → **[CẦN KIỂM TRA]** on spaceappschallenge.org before recording.
Submit ONE demo format. The deck (Option B) is the safer fallback if the 30 s limit turns out to differ.

---

## Option A — 30-second video

Target ≈ 70 words (≈ 2.5 words/s). Record, then trim to ≤ 30.0 s. Burn English subtitles into the video.

| Time | Voice-over | On screen |
|---|---|---|
| 0–5 s | "Apollo 1, 1967. Mir, 1997. Fires in sealed spacecraft." | Two archive-style captions (use NASA public-domain images **[CẦN KIỂM TRA: image credit/licence]**) or plain text cards |
| 5–15 s | "NASA's SAFFIRE-II burned the same materials in microgravity and on Earth. Silicone: fully consumed at 1 g, almost nothing at 0 g. Cotton-fiberglass: all 29 centimetres burned in space." | Table crop of the 0 g vs 1 g result (from PSI-99), silicone row then SIBAL row highlighted |
| 15–25 s | "So Earth tests can mislead in both directions. Our dashboard turns 274 ISS droplet-flame tests into extinction-risk maps with uncertainty, and greys out anything beyond NASA's data." | Screen recording of dashboard: move O₂ slider → risk map changes; grey out-of-domain area visible |
| 25–30 s | "Flame in Freefall: honest fire-safety insight for the Moon and Mars." | Title card + repo link |

Recording checklist
- Screen capture only the real app. No mock-up unless labelled "demo data".
- Show greyed-out extrapolation region on screen — it is the honesty point.
- Do not state accuracy in the video; put numbers in the description (30 s is too short to qualify them).
- Dashboard steps depend on the final app **[CẦN KIỂM TRA with workstream A: slider names, default fuel]**.

---

## Option B — 7-slide deck (including title and intro)

| # | Slide | Content |
|---|---|---|
| 1 | Title + hook | "Flame in Freefall" — Apollo 1 (1967), Mir (1997): fire in sealed spacecraft **[CẦN KIỂM TRA facts, see fact_check.md]** |
| 2 | The gap | Moon/Mars habitats are sealed; our fire intuition and standards come from 1 g |
| 3 | SAFFIRE-II: 0 g ≠ 1 g | Table: silicone ≈ 0 cm at 0 g vs complete at 1 g; SIBAL 29 cm at 0 g; PMMA anchored flame. Source: PSI-99 |
| 4 | Data & model | FLEX PSI-69, 274 ISS tests; logistic + ridge bootstrap ensembles; day-grouped CV: ROC-AUC 0.881, balanced acc 0.762, K R² 0.71 (`evaluate()`) |
| 5 | The dashboard | Screenshots: risk map with uncertainty band; evidence cards |
| 6 | Honest limits | Droplets only; 19 % of default grid in-domain, ~81 % greyed extrapolation; evidence cards ≠ model output |
| 7 | Impact + links | Who uses it, next steps, repo + app links, NASA data list, AI tools disclosure |

Speaker notes (if recording a voice-over for the deck instead of reading): one sentence per slide, taken from the table above.

---

## Live Q&A cheat-sheet (if a judge asks)

- *"Does it predict real habitat fires?"* No. Liquid droplets in FLEX conditions only; solids are cited evidence.
- *"How accurate?"* Cross-validated by test day: ROC-AUC 0.881, balanced accuracy 0.762 for extinction; R² 0.71 for burning rate K. Source: `uv run flame_model.py`.
- *"What is in-domain?"* Within the range/neighbourhood of real FLEX tests; 19 % of our default 754-point grid.
- *"Why SAFFIRE-II?"* It's the one NASA table that directly compares 0 g and 1 g on the same materials.
- *"Which AI?"* Claude Code for coding/drafting; scikit-learn for the model. See submission.md §5.
