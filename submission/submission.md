# Space Apps 2026 — Project Submission Text (EN)

> Status: DRAFT, 14 Nov 2026. Items marked **[CẦN KIỂM TRA]** are not yet verified against a source.
> Form field names and character limits are **[CẦN KIỂM TRA]** — the 2026 Project Submission Guide
> could not be fetched (HTTP 503 / TLS error from this environment). Paste into the form and
> trim to whatever limit it shows. Replace `<…>` placeholders before submitting.

---

## 1. Title

**Flame in Freefall: An Honest AI Fire-Safety Explorer for Moon & Mars Habitats**

Short alternative (if the title limit is tight): **Flame in Freefall**

## 2. Summary (short form)

Fire behaves differently in microgravity — NASA's SAFFIRE-II burned a silicone sheet completely at 1 g
but almost not at all at 0 g, while a cotton-fiberglass fabric burned its full length in space.
Flame in Freefall turns NASA's FLEX droplet-combustion tests into an interactive dashboard that
maps extinction risk and burning rate with uncertainty bands, labels every extrapolation, and
pairs it with ranked evidence from SAFFIRE and BASS experiments.

(≈ 60 words. If a ~30-word limit applies **[CẦN KIỂM TRA]**, use:)

> NASA experiments show fire behaves differently at 0 g than at 1 g. We turn NASA's FLEX
> combustion data into an interactive, uncertainty-aware fire-risk dashboard for Moon and Mars habitats.

## 3. Description (long form)

### The problem
On 27 January 1967 a cabin fire killed the three Apollo 1 astronauts during a ground test in a
pure-oxygen atmosphere **[CẦN KIỂM TRA: date, crew count, atmosphere — source: NASA Apollo 204 Review Board report]**.
In February 1997 a fire from an oxygen-generating canister broke out aboard the Mir space
station **[CẦN KIỂM TRA: date and details — source: NASA/ESA accounts]**. Both are sealed
environments where a fire cannot be walked away from. Future Moon and Mars habitats will be
sealed too, possibly with different pressure and oxygen levels than Earth — but our intuition
and most of our fire-safety test standards come from 1 g.

### What NASA's data says: gravity changes the answer — in both directions
NASA's SAFFIRE experiments burned materials in the Cygnus cargo vehicle in orbit. In SAFFIRE-II
(PSI-99), samples were exposed to 20 cm/s concurrent flow at roughly 21.5–22.1 % O₂, and the table
compares burn results in microgravity with 1 g:

| Test | Material | 0 g (microgravity) | 1 g |
|---|---|---|---|
| 2-1 | Silicone, 0.27 mm | burn length ≈ 0 | burned completely |
| 2-2 | Silicone, 0.61 mm | burn length ≈ 0 | 7.6 cm, 1.2 mm/s |
| 2-5 | Cotton-fiberglass (SIBAL) | 29 cm (whole sample), 2.1 mm/s | burned completely |
| 2-6 | SIBAL (material cell blank in CSV) | 29 cm (whole sample), 2.6 mm/s | burned completely |
| 2-8 | PMMA | ≈ 10 cm of visible damage, flame anchored at base | burned completely |

Source: `data/raw/PSI-99_SAFFIRE-II.csv`. **[CẦN KIỂM TRA]**: (a) the CSV column header for the
microgravity columns is garbled ("?-g"); we read it as µ-g because the other columns are "1-g";
(b) the 1 g runs use the same flow and ignition settings as the flight runs; (c) row 2-6's material
is read as SIBAL from the neighbouring row. A thin silicone sheet that burns fully on Earth
barely burns in space, while a fabric burns end-to-end in space: **testing only at 1 g can
mislead in either direction.** That is why microgravity data matters for habitat fire safety.

### What we built
An interactive dashboard (Streamlit **[CẦN KIỂM TRA with workstream A]**) with two parts:

1. **Risk explorer (model output).** Choose fuel (methanol or heptane), O₂ fraction, pressure,
   diluent (N₂, CO₂ or He) and droplet size. The model returns:
   - `p_extinction` — probability that the flame self-extinguishes before the droplet is consumed (higher = safer);
   - `k` — burning-rate constant in mm²/s (higher = burns faster);
   - a 90 % interval on both, and the nearest real NASA tests behind the prediction.
2. **Evidence cards (not model output).** Ranked, cited findings from SAFFIRE-I/II/III and BASS/BASS-II
   covering solid materials, oxygen limits, suppression and smoke, each with a `verified` flag
   **[CẦN KIỂM TRA: count and content once `evidence/evidence.json` is filled by workstream B]**.

### The model — and how well it does
Trained on 274 ISS FLEX droplet-combustion tests (PSI-69, 2009–2011). Two bootstrap-ensemble
models (200 resamples): logistic regression for extinction, ridge regression for K. Evaluated with
5-fold cross-validation **grouped by test day**, so tests run on the same day never appear in both
training and test sets (output of `uv run flame_model.py`, run 14 Nov 2026):

| Metric | Value |
|---|---|
| Extinction: tests used | 261 (68.6 % self-extinguished — base rate) |
| Extinction ROC-AUC | 0.881 |
| Extinction balanced accuracy | 0.762 |
| Burning rate K: tests used | 256 |
| Burning rate K, R² | 0.71 |

These are cross-validated figures on liquid droplets in FLEX conditions. They are **not** accuracy
claims for habitat fires.

### Honesty about limits
- The model covers **liquid fuel droplets only** (methanol, heptane). Fabrics and plastics appear only as evidence cards.
- Only **19 %** of the default risk grid (754 points) lies inside the region NASA actually tested.
  The other ~81 % is extrapolation; the dashboard greys it out and labels it.
- FLEX has 274 tests, so intervals are wide in sparse regions. No claim is made about real habitat fires.
- Any demo or synthetic content in the app is labelled as such.

### Impact and relevance
The dashboard lets a non-specialist see how oxygen level, pressure and diluent gas move a flame
toward or away from extinction — the kind of trade-off space-habitat atmosphere designers face —
while making clear where NASA data stops and guessing starts. Future work: add FLEX-2 outcomes
when published, fold SAFFIRE material data into a solid-fuel model, and test lunar/Mars
pressure-oxygen combinations as new data arrives.

## 4. NASA data used

All from NASA Physical Sciences Informatics (PSI), public domain (CC0 per repo notes
**[CẦN KIỂM TRA: licence wording on PSI site]**):

| PSI ID | Investigation | Used for |
|---|---|---|
| PSI-69 | FLEX (Flame Extinguishment Experiment) — 274 tests | Training data for the model (the only ML-grade table) |
| PSI-68 | FLEX-2 — 8 tests, design matrix, no outcomes | Describing coverage only |
| PSI-99 | SAFFIRE-II | 0 g vs 1 g evidence (key story) |
| PSI-98 / PSI-100 | SAFFIRE-I / SAFFIRE-III | Evidence cards (tiny tables) |
| PSI-25 / PSI-26 | BASS-II / BASS | Evidence on solid-material limits; materials catalogue |

Plus NASA documents cited in `evidence/evidence.json` **[CẦN KIỂM TRA: list from workstream B]**.

## 5. AI and software tools used

- **Claude (Anthropic) via Claude Code** — generative AI used to write and refactor code, clean
  the FLEX table, and draft documentation and this submission text. All numbers were re-derived from
  the NASA files or from `uv run flame_model.py`, and checked by the team member.
- **scikit-learn** (logistic and ridge regression, bootstrap ensembles), **pandas**, **NumPy** — the model itself;
  it is classical ML, not a language model.
- **Streamlit** and **Plotly** — dashboard.
- Does the app call an LLM at runtime? **[CẦN KIỂM TRA with workstream A]** — if yes, state model and purpose here; if no, say so.

## 6. Links (fill before submitting)

- Source code: `<GitHub URL>` **[CẦN KIỂM TRA: repo must be public]**
- Live app: `<URL or "run locally: uv run streamlit run app/app.py">`
- Project demo (video/slides): `<public link, no login>`

## 7. Team

Solo participant: Zinnn — NASA Space Apps Challenge 2026, Hà Nội **[CẦN KIỂM TRA: team name as registered]**
Challenge: *Flame in Freefall: AI-Powered Fire Safety Insights from Microgravity Combustion Data*.
