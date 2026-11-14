# Project Demo — 7-slide deck (chosen option)

Rules (confirmed by Hà Nội organisers): **max 7 slides including the cover**, public link, **English only**.
Build in Google Slides / Canva / PowerPoint and export a public link; test it in a private window.
Tag in brackets = source: `[ev-NN]` evidence id, `[model]` = `uv run flame_model.py` output (14 Nov 2026).
Keep text light: one message per slide, numbers big, source in small print at the bottom of each slide.

---

## Slide 1 — Cover

- **Title:** Flame in Freefall
- **Subtitle:** Honest, AI-assisted fire-safety insights from NASA microgravity combustion data — for Moon & Mars habitats
- **Hook line:** "Apollo 1. Mir. Two spacecraft fires."
  **[ĐIỀN]** one sentence from the NASA pages on Apollo 1 and Mir once the user pastes them. Until then keep only the hook line above: no dates, no causes, no casualty numbers.
- Footer: Zinnn · NASA Space Apps Challenge 2026 · Hà Nội · repo link
- Visual: dark background, a rounded teardrop flame (in 0 g a flame is spherical, on Earth it is a teardrop — only draw this if you label it "illustration").

## Slide 2 — The gap: we test fire at 1 g, we will live at 0 g and 1/6 g

- **Headline:** Spacecraft fire safety still leans on Earth standards
- Bullets:
  - Before Saffire, microgravity fire tests used samples ≤ 10 cm; design relied on terrestrial fire standards — "an inherent risk" that grows as missions travel farther from Earth [ev-12]
  - Saffire-I to -III covered roughly ISS-like air, **not** the elevated-O₂, lower-pressure atmospheres planned for exploration habitats [ev-14]
  - Evidence base is small: 2 large + 9 smaller samples [ev-19]
- Source line: Schoren, Ruff & Urban, NTRS 20170001636

## Slide 3 — SAFFIRE-II: same test, different gravity, different answer

- **Headline:** Gravity changes the result — in both directions
- Table (PSI-99, 5 × 29 cm samples, 20 cm/s flow, ~21.5–22.1 % O₂):

  | Sample | 0 g | 1 g |
  |---|---|---|
  | Silicone 0.27 mm | ≈ 0 cm burned | burned completely |
  | Cotton-fiberglass | **all 29 cm**, 2.1 & 2.6 mm/s | burned completely |
  | Thick PMMA | ≈ 10 cm, flame anchored | burned completely |

- Callout: "It burns on Earth, not in space — and the fabric burns end-to-end in space." [ev-01, ev-02, ev-06]
- Small print: one SIBAL sample was planned at 30 cm/s but logged at 20 cm/s [ev-01]. Silicone 1.03 mm did not burn at either gravity [ev-02].

## Slide 4 — Data and model

- **Headline:** 274 real ISS flames → an uncertainty-aware risk model
- Left: NASA FLEX (PSI-69), 274 droplet tests (methanol 157, heptane 117), 2009–2011: 186 extinguished, 27 burned out, 61 disrupted [ev-22]
- Middle: logistic + ridge regression, 200-bootstrap ensembles, 90 % intervals
- Right (big numbers, from 5-fold CV grouped by test day [model]):
  - **0.881** ROC-AUC (self-extinction)
  - **0.762** balanced accuracy
  - **0.71** R² (burning-rate constant K)
- Small print: 261 tests with complete inputs for extinction, 256 for K; liquid droplets only.

## Slide 5 — The dashboard (3 screenshots from the real app)

- **Headline:** See the risk, see where the data stops, ask the data
- Screenshot 1: *Habitat Fire Risk* heatmap with grey extrapolation veil and ISS star marker
- Screenshot 2: *Evidence Ranking* cards (ev-02 visible, "✔ verified")
- Screenshot 3: *Ask the Data* answer with `[ev-…]` citations
- Caption example (ISS air, 3 mm droplet) [model]: methanol 72 % self-extinction (62–81 %), heptane 43 % (32–55 %)
- Label screenshots with their real conditions; never mock-ups. If "Ask the Data" is off for lack of a key, omit screenshot 3 and say so.

## Slide 6 — Honest limits (this slide is a feature)

- **Headline:** What this does *not* do
- Bullets:
  - Liquid fuel droplets only — no fabrics, plastics or real habitat fires
  - **81 % of the default grid is extrapolation** (19 % inside NASA data) — greyed out, never hidden [model]
  - Suppressant results for microgravity are partly simulation [ev-05]
  - Every number links to a PSI file, a NASA document or the model's printed output
- Visual: the grey-veiled heatmap, enlarged.

## Slide 7 — Impact, AI, data, links

- **Headline:** From open NASA data to habitat design questions
- Impact: lets designers/students explore how O₂, pressure and CO₂/He/N₂ move a flame toward or away from extinction [ev-15, ev-16, ev-23]; exploratory support, not certification
- Next: FLEX-2 outcomes, a solid-fuel model from SAFFIRE data, Moon/Mars-like atmospheres as data arrives
- **Use of AI:** Claude (Anthropic) via Claude Code → code, evidence extraction, drafting; scikit-learn model; LLM via OpenRouter in "Ask the Data" (answers only from cited evidence)
- **NASA data:** PSI-25, 26, 68, 69, 98, 99, 100
- Links: GitHub repo · app · submission page (QR optional)

---

## Checks before exporting
1. English only, no Vietnamese text left on slides.
2. Exactly 7 slides; link opens without login in a private window.
3. Numbers on slides match `submission.md` and `fact_check.md`; re-run `uv run flame_model.py` and compare.
4. Screenshots come from the current `main` build of the app.
5. Slide 1: add Apollo 1 / Mir details only from the NASA pages the user pastes.
