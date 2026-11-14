# Project Demo — 7-slide deck (chosen option)

Rules (confirmed by Hà Nội organisers): **max 7 slides including the cover**, public link, **English only**.
Build in Google Slides / Canva / PowerPoint, export a public link, test it in a private window.
Tags: `[ev-NN]` evidence id · `[in-NN]` FLEX insight (`insights/insights.json`) · `[model]` = `uv run flame_model.py`, 14 Nov 2026.
One message per slide, big numbers, source in small print.

**Deadline for Hà Nội judging: 11:00 Sunday 15 Nov 2026.**

---

## Slide 1 — Cover

- **Title:** Flame in Freefall
- **Subtitle:** Honest, AI-assisted fire-safety insights from NASA microgravity combustion data — for Moon & Mars habitats
- **Hook (two lines, both from NASA pages):**
  - "Apollo 1: a flash fire in a 100 % oxygen cabin." [ev-26]
  - "Mir: a three-foot flame that burned for several minutes." [ev-27]
- Footer: Zinnn · NASA Space Apps Challenge 2026 · Hà Nội · repo link
- No astronaut names. No flame illustration that implies data.

## Slide 2 — Two fires, one knowledge gap

- **Headline:** Fire in a sealed spacecraft is a crew-survival problem
- Left card — **Apollo 1, 27 Jan 1967 (ground test, 1 g)** [ev-26]
  - 100 % O₂ cabin; flash fire too fast for the crew to open the hatch
  - Three astronauts died of asphyxia from carbon monoxide and other toxic gases
  - Hatch took 90 s to open → replaced by a 3 s hatch; combustible materials restricted
- Right card — **Mir, 24 Feb 1997 (in orbit)** [ev-27]
  - Oxygen-generator canister; three-foot flame, several minutes; six crew aboard
  - Blocked the route to one of two Soyuz escape vehicles; smoke took hours to clear
  - Crew used three foam extinguishers; the flame finally **extinguished itself**; no lasting harm
- Bottom strip — **The gap:** before Saffire, microgravity fire tests used samples ≤ 10 cm and design leaned on terrestrial standards [ev-12]; Saffire I–III did not cover exploration atmospheres [ev-14].
- Source line: NASA OSMA "Apollo 1 AS-204"; J. Uri, NASA JSC, "25 Years Ago: Fire Aboard Space Station Mir"; Schoren, Ruff & Urban NTRS 20170001636.

## Slide 3 — SAFFIRE-II: same test, different gravity, different answer

- **Headline:** Gravity changes the result — in both directions
- Table (PSI-99; 5 × 29 cm samples, 20 cm/s flow, ~21.5–22.1 % O₂):

  | Sample | 0 g | 1 g |
  |---|---|---|
  | Silicone 0.27 mm | ≈ 0 cm burned | burned completely |
  | Cotton-fiberglass | **all 29 cm**, 2.1 & 2.6 mm/s | burned completely |
  | Thick PMMA | ≈ 10 cm, flame anchored | burned completely |

- Callout: "It burns on Earth, not in space — and the fabric burns end-to-end in space." [ev-01, ev-02, ev-06]
- Small print: one SIBAL sample was planned at 30 cm/s but logged at 20 cm/s [ev-01]; silicone 1.03 mm did not burn at either gravity [ev-02]; Saffire I–III = 2 large + 9 small samples [ev-19].

## Slide 4 — The result: no droplet flame put itself out in low-pressure, oxygen-rich air (main message)

- **Headline (huge number):** **0 of 17** FLEX tests self-extinguished at 0.7 atm with 30–34 % O₂ [in-02]
- Sub-headline: the direction NASA describes for exploration atmospheres — elevated O₂, lower pressure [ev-14]. (Direction only: NASA gives no numbers there.)
- Two supporting panels:
  - **Oxygen is the strongest lever** [in-01]: self-extinction of heptane 11/14 at ≤ 16 % O₂ → 5/17 at 20–22 % → 0/3 at 23–30 %; methanol 22/22 → 9/12 → 2/4
  - **Pressure alone barely matters; the oxygen that comes with it does** [in-05] (model, 3 mm droplet): heptane 43 % (21 % O₂, 1 atm) → 41 % (21 %, 0.7 atm) → 2 % (30 %, 0.7 atm); methanol 72 % → 70 % → 6 %
- Credibility strip (small): FLEX PSI-69, 274 ISS droplet tests · logistic + ridge, 200 bootstraps · 5-fold CV grouped by test day: ROC-AUC 0.881, balanced acc. 0.762, K R² 0.71 [model]
- **Caveat box on the slide (required):** liquid fuel droplets only · "not self-extinguished" includes tests that ended in Disruption (15 of the 17; 2 burned to completion) · 17 tests, one pressure band, N₂ only.

## Slide 5 — The dashboard (screenshots from `app/screenshots/`)

- **Headline:** See the risk, see where the data stops, ask the data
- Screenshot 1 `01_habitat_fire_risk.png`: heatmap with grey extrapolation veil, ISS star, "Inside the range of NASA FLEX tests".
  - It also shows the "Exploration atmosphere (34 % O₂, 0.6 atm)" button. **Add a caption: "illustrative preset, not a NASA figure"** — the app itself says "illustrative, needs a cited source".
- Screenshot 2 `02_evidence_ranking.png`: evidence cards with verified badge.
- Screenshot 3 `03_ask_the_data.png` shows only the question box and sample questions. For a better slide, run a real question (e.g. "How did fabric burn in microgravity compared with normal gravity?") and capture the answer with its `[ev-…]` citations — only if the key works. Otherwise use it as is and caption "answers must cite ids".
- Caption (ISS air, 3 mm droplet) [model]: methanol 72 % self-extinction (62–81 %); heptane 43 % (32–55 %).

## Slide 6 — Honest limits (this slide is a feature)

- **Headline:** What this does *not* do
- Liquid fuel droplets only — no fabrics, plastics or real habitat fires
- **81 % of the default grid is extrapolation** (19 % inside NASA data) — greyed out, never hidden [model]
- The exploration preset is an illustration: its values have no NASA source
- Microgravity suppressant values (CO₂, N₂, He) are partly simulation [ev-05]
- Every number links to a PSI file, a NASA document, a computed insight or the model's printed output
- Visual: grey-veiled heatmap, enlarged.

## Slide 7 — Impact, AI, data, links

- **Headline:** From open NASA data to habitat design questions
- Impact: lets designers and students see how O₂, pressure and CO₂/He/N₂ move a flame toward or away from extinction [in-01, in-04, in-05]; exploratory support, not certification
- Next: FLEX-2 outcomes · a solid-fuel model from SAFFIRE data · tests at Moon/Mars-relevant atmospheres as NASA data arrives
- **Use of AI:** Claude (Anthropic) via Claude Code → code, evidence extraction, drafting; scikit-learn model; LLM via OpenRouter in "Ask the Data" (answers only from cited evidence)
- **NASA data:** PSI-25, 26, 68, 69, 98, 99, 100
- Links: GitHub repo · app · submission page

---

## Checks before exporting
1. English only; exactly 7 slides; link opens without login in a private window.
2. Numbers match `submission.md`, `fact_check.md`; re-run `uv run flame_model.py`.
3. Mir wording: "the flame finally extinguished itself" **after** the crew used foam extinguishers — never "the extinguishers put it out".
4. No astronaut names; Apollo 1 labelled ground test.
5. Slide 4 caveat box present; exploration preset values never shown as NASA data.
