# Space Apps 2026 — Project Submission (Hà Nội) — English, one section per form field

> Updated 14 Nov 2026 after `git pull origin main`.
> **Deadline for Hà Nội judging: Sunday 15 Nov 2026, 11:00 local time.**
> Rules confirmed by the Hà Nội organisers (sepa.org.vn): everything in English; demo = max 7 slides
> including cover OR a video of max 30 s, public link; 8 required fields (below); 5 criteria
> (Impact, Creativity, Validity, Relevance, Presentation), each scored 1–10.
>
> `[ev-NN]` = id in `evidence/evidence.json` (all 25 items are `verified: true`).
> `[model]` = output of `uv run flame_model.py` / `flame_model.predict()` run on 14 Nov 2026.
> **[CẦN KIỂM TRA]** = still not verified. Character limits per field were not given → check the form and trim.
> Delete this header block before pasting.

---

## 1. Project Name

**Flame in Freefall**

(Fuller form if the field allows: *Flame in Freefall — an honest, AI-assisted fire-safety explorer for Moon & Mars habitats*)

## 2. High-Level Summary

Fire does not behave in space as it does on Earth: in NASA's SAFFIRE-II experiment a thin silicone sheet burned completely at 1 g but almost not at all in microgravity, while a cotton-fiberglass fabric burned its full 29 cm in space [ev-01, ev-02]. Flame in Freefall turns 274 NASA FLEX droplet-combustion tests into an interactive risk map with uncertainty bands that greys out everything beyond NASA's data, ranks 25 cited findings from SAFFIRE, BASS-II and FLEX, and lets you question both with an LLM that must cite its sources.

## 3. Project Demo

Link to the **7-slide deck** (public, no login): `<DEMO URL>` **[CẦN KIỂM TRA: fill after export; open it in a private window to check]**

Slide-by-slide content: `submission/demo_script.md`. English only.

## 4. Final Project

- Source code: https://github.com/QinZinn/NasaSpaceAppChallange **[CẦN KIỂM TRA: repository must be public; the work is currently on branch `claude/quirky-bell-n317xp` and `main` — confirm which one the form should point to]**
- Run it: `uv run streamlit run app/app.py`
- Hosted app: `<APP URL>` or write "run locally with the command above" **[CẦN KIỂM TRA]**
- Tab 3 ("Ask the Data") needs an `OPENROUTER_API_KEY`; without a key the tab shows "off" and tabs 1–2 still work. If the judges' copy has no key, say so here.

## 5. Project Details

### The problem
Apollo 1 and Mir were both spacecraft fires. **[CẦN KIỂM TRA / ĐIỀN: no dates or other details are used until the NASA pages are provided; add one sentence from those pages here.]**
Future Moon and Mars habitats will be sealed environments too, yet NASA states that before the Saffire experiments microgravity fire tests were limited to samples of 10 cm or less, so spacecraft fire-safety design has relied on terrestrial fire standards — an inherent risk that grows as missions go farther from Earth [ev-12].

### What NASA's data shows: gravity changes the answer in both directions
SAFFIRE-II (PSI-99) burned 5 cm × 29 cm samples in 20 cm/s air flow at about 21.5–22.1 % O₂ and recorded results at 0 g (microgravity) and 1 g. The column PSI-99 labels "?-g" is the microgravity column (confirmed by the evidence workstream).

| Sample | 0 g (microgravity) | 1 g | Evidence |
|---|---|---|---|
| Silicone 0.27 mm | burn length ≈ 0 | burned completely | [ev-02] |
| Silicone 0.61 mm | ≈ 0 | 7.6 cm at 1.2 mm/s | [ev-02] |
| Silicone 1.03 mm | ≈ 0 | ≈ 0 (did not burn either) | [ev-02] |
| Cotton-fiberglass (SIBAL), samples 2-5 and 2-6 | whole 29 cm burned, 2.1 and 2.6 mm/s | burned completely, accelerating | [ev-01] |
| Thick PMMA (2-8, 2-9) | ≈ 10 cm of 29 cm damaged, flame anchored at base, 0.01–0.04 mm/s regression | burned completely, accelerating | [ev-06] |
| Nomex attached to burning PMMA (2-7) | PMMA consumed, Nomex not ignited | Nomex ≈ 0 | [ev-10] |

So a material that burns on Earth may not burn in space (silicone, thick PMMA), and a fabric burns end-to-end in space. Testing at 1 g alone can mislead in either direction. Caveats from the evidence: the SIBAL runs were logged at 20 cm/s in PSI-99, whereas the pre-flight plan listed 30 cm/s for one of them [ev-01]; the whole Saffire I–III evidence base is two large and nine smaller samples [ev-19]; Saffire-I to -III covered roughly ISS-like air, not the elevated-oxygen, lower-pressure atmospheres planned for exploration vehicles [ev-14].

### What we built
A Streamlit dashboard with three tabs:

1. **Habitat Fire Risk** — choose fuel (methanol or heptane droplet), O₂ fraction, pressure, diluent gas (N₂, CO₂ or He) and droplet size. A heatmap shows the probability that the flame **self-extinguishes** before the droplet is consumed (higher = safer) or the burning-rate constant K in mm²/s (higher = burns faster). Real FLEX tests are plotted on top; every cell outside NASA's tested range is greyed out and labelled "extrapolation". Each answer carries a 90 % interval and the nearest real NASA tests.
2. **Evidence Ranking** — 25 findings from NASA data files and documents, ranked 1–5 by relevance to Moon/Mars habitat fire safety, filterable by topic, with the claim, test conditions, numbers, citation and a verified flag. Solid-material results live here; they are *evidence, not model output*.
3. **Ask the Data** — an LLM answers questions using **only** the 25 evidence items and the model's outputs, and must end each factual sentence with the id it used (e.g. `[ev-02]`); the app checks that the ids exist and labels the answer as an AI summary.

Example (ISS cabin air, 21 % O₂, 1 atm, N₂ balance, 3 mm droplet) [model]:
methanol → 72 % self-extinction (90 % interval 62–81 %), K = 0.50 mm²/s (0.38–0.61);
heptane → 43 % self-extinction (32–55 %), K = 0.53 mm²/s (0.42–0.65).
FLEX's raw tests agree in direction: all 37 methanol tests at ≤ 15 % O₂ ended in extinction, against 13 of 35 above 22 % O₂ [ev-15]. Overall 186 of 274 FLEX tests ended in extinction, 27 burned to completion and 61 ended in disruption [ev-22].

### The model and how well it does
Trained on FLEX (PSI-69), 274 droplet-combustion tests on the ISS, March 2009–December 2011 [ev-22]. Two bootstrap ensembles (200 resamples): logistic regression for self-extinction and ridge regression for K. Evaluated by 5-fold cross-validation **grouped by test day**, so tests run on the same day never sit in both training and test folds [model]:

| Metric | Value |
|---|---|
| Extinction model: tests with complete inputs | 261 (68.6 % self-extinguished) |
| Extinction ROC-AUC | 0.881 |
| Extinction balanced accuracy | 0.762 |
| K model: tests | 256 |
| K R² | 0.71 |

These are cross-validated figures for liquid droplets under FLEX conditions. They are not accuracy claims for habitat fires.

### Honest limits
- The model covers **liquid fuel droplets only** (methanol, heptane). Fabrics and plastics appear only as cited evidence.
- Only **19 %** of the default risk grid (754 points) lies inside the range NASA tested [model]; the other ~81 % is extrapolation and is greyed out, not hidden.
- The suppressant evidence is partly simulation: the microgravity values for minimum extinguishing concentration (CO₂ 0.16 → 0.19, N₂ 0.26 → 0.38 mole fraction, 1 g → 0 g) are simulations; the 1 g values are tests [ev-05].
- Evidence cards carry the original caveats (single runs, uncalibrated sensors, raw comparisons without controls) [ev-04, ev-25].
- If the evidence file ever fails to load, the app falls back to mock placeholders and shows a red "DEMO / MOCK DATA" banner.

### Impact and relevance
Atmosphere designers, students and mission-safety enthusiasts can see how oxygen, pressure and diluent gas move a droplet flame toward or away from extinction, and where NASA's data stops. CO₂ is the suppressant used on the US side of the ISS and may work less well in microgravity than expected [ev-16]; FLEX droplets in helium burned faster than in CO₂ (median K, heptane: 0.65 vs 0.50 mm²/s) [ev-23]. This is exploratory decision support, **not** a certification or safety tool. Next steps: add FLEX-2 outcomes when published, fold SAFFIRE material data into a solid-fuel model, and test Moon/Mars-like pressure–oxygen combinations as NASA data arrives.

## 6. Use of AI

**Generative AI used to build the project (disclosed):**
- **Claude (Anthropic), through Claude Code**, was used to write the code (data cleaning, model, dashboard), to extract and draft the 25 evidence items from the NASA files and documents, and to draft this submission and the pitch. Several Claude sessions worked in parallel on separate parts (model, dashboard, evidence, submission). **[CẦN KIỂM TRA: add how much you reviewed by hand — e.g. which evidence items and numbers you personally checked against the source files.]**
- Safeguards: every evidence item carries a file/page citation and a `verified` flag so it can be re-checked; every number in this text is tied to an evidence id or to the model's printed output.

**AI inside the running product:**
- **Machine-learning model (not generative):** scikit-learn logistic regression and ridge regression, bootstrap ensembles trained on NASA FLEX data.
- **"Ask the Data" tab:** an LLM called through **OpenRouter** at run time. Default model id in the code is `anthropic/claude-sonnet-4.5` (`FLAME_LLM_MODEL` can override it) **[CẦN KIỂM TRA: model actually used in the demo]**. It runs at temperature 0, receives only the evidence list and the model's outputs, is instructed to cite ids, to say when a result is extrapolation, and not to present droplet results as solid-material or real-habitat fires. The app checks the cited ids and prints "Generated by <model>; an AI summary, check the cited sources." LLM answers can still be wrong; the evidence tab is the source of truth.

## 7. NASA Data

All NASA Physical Sciences Informatics (PSI) tables in `data/raw/` (public domain, CC0 per repo notes **[CẦN KIỂM TRA: licence wording on the PSI site]**):

| PSI ID | Investigation | How it is used |
|---|---|---|
| PSI-69 | FLEX — 274 droplet tests | Training data for the model (the only ML-grade table); evidence [ev-15, ev-22, ev-23] |
| PSI-68 | FLEX-2 — 8 tests, design matrix only | Describes coverage; no outcomes, not used for training |
| PSI-99 | SAFFIRE-II | 0 g vs 1 g evidence [ev-01, ev-02, ev-06, ev-10] |
| PSI-98 | SAFFIRE-I | Evidence [ev-11] |
| PSI-100 | SAFFIRE-III | Catalogue only (2 samples) |
| PSI-25 | BASS-II — 129 runs | Evidence on oxygen limits, extinction, smoke [ev-03, ev-04, ev-07, ev-08, ev-09, ev-17, ev-18, ev-21]; parsed to `data/processed/bass2_structured.csv` |
| PSI-26 | BASS — 122 tests | Materials catalogue only |

Cleaned FLEX table: `data/processed/flex_clean.csv` (column "CO" in the raw header is CO₂; "Burning rate; mm" is K in mm²/s).

## 8. References

**Software**
- Streamlit 1.67.0 — https://streamlit.io
- Plotly (Python) 7.1.0 — https://plotly.com/python/
- scikit-learn 1.9.1 — https://scikit-learn.org
- pandas 3.1.1 — https://pandas.pydata.org
- NumPy — https://numpy.org (version per `uv.lock`)
- pypdf — https://pypdf.readthedocs.io **[CẦN KIỂM TRA: confirm workstream B used it to read the PDFs]**
- OpenRouter API — https://openrouter.ai (access to the LLM used in "Ask the Data")

**NASA data and documents (as cited in `evidence/evidence.json`)**
- NASA Physical Sciences Informatics: PSI-25 BASS-II, PSI-26 BASS, PSI-68 FLEX-2, PSI-69 FLEX, PSI-98 SAFFIRE-I, PSI-99 SAFFIRE-II, PSI-100 SAFFIRE-III **[CẦN KIỂM TRA: add PSI URL]**
- Schoren, Ruff & Urban, "The Spacecraft Fire Experiment (Saffire) — Objectives, Development and Status", NASA Technical Reports Server 20170001636 — https://ntrs.nasa.gov/citations/20170001636 [ev-11, ev-12, ev-13, ev-14, ev-19]
- FLEX Test Plan (FLEX_Test_Plan.pdf), extracted from the FLEX Research Requirements Document, Williams et al., 4 Nov 2005 [ev-05, ev-16, ev-24]
- BASS-II Science Requirements (SRD_BASS-II.pdf) [ev-20, ev-25]
- BASS-II data FAQ [ev-03, ev-04, ev-07, ev-09, ev-18, ev-21, ev-25]
- SAFFIRE-II data description (SAFFIRE-II_DoD.docx) [ev-13]
- Cited second-hand through the FLEX Test Plan, not read directly: Takahashi et al., 2004; Katta et al., 2004 [ev-05]; Honda & Ronney, 1998 [ev-16]
- Apollo 1 and Mir: **[CẦN KIỂM TRA / ĐIỀN: add the two NASA page URLs/titles once provided; nothing is cited until then]**

---
Team: Zinnn — NASA Space Apps Challenge 2026, Hà Nội **[CẦN KIỂM TRA: team name as registered]**.
Challenge: *Flame in Freefall: AI-Powered Fire Safety Insights from Microgravity Combustion Data*.
