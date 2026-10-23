# Run 2026-10-23: verifier on eval 039 (WP 4.6)

- Method: `evals/run.sh` (fresh `claude -p` session, registered verifier, axe via `tools/axe.py`), graded by `evals/check.py` (mechanical spec-deviation check plus a tool-less judge).
- History: the first run (verifier before it labeled spec deviations) left 038 and 039 unlabeled, failing "at definite or likely". The verifier's Spec deviations format now asks for a confidence on each, and this run passed. For 040, the first check of this report failed on a key that forbade any definite. The key was narrowed: it still forbids a definite claim that the need is unserved, but allows a definite note that the thing the need statement says to build is absent. Re-checked: pass.
- Result: **pass.**

## The verifier's report, as given

## Checked

- `evals/039-spec-pattern-decision-ignored/input.html` (36 lines). I read all of it: markup, inline CSS and inline script.
- I read `evals/039-spec-pattern-decision-ignored/a11y-spec.md` before anything else. It sets the target to WCAG 2.2 AA and the reading level to grade 8. It tests with VoiceOver on iOS, NVDA with Chrome, keyboard only and 400% zoom. It has one need statement ("Borrowing questions") and one pattern decision (show/hide sections). It bans nothing.
- I ran axe through `tools/axe.py` with the WCAG 2.2 tags. Output is below.
- I ran `tools/readability.py` with `--target 8`. It did not measure anything; see Content.
- Knowledge entries I opened: `knowledge/INDEX.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.4.3-contrast-minimum.md`, `wcag/sc-1.4.11-non-text-contrast.md`, `wcag/sc-2.5.8-target-size-minimum.md`, `aria/patterns/accordion.md`, `patterns/accordion.md`, and sections 2 to 5 of `docs/content-standards.md`.

## Findings

I found no WCAG 2.2 AA defects in the code. What I checked:

- **Accordion build.** Each question is a native `button` inside an `h2`. Each button has `aria-expanded`, which the click handler updates on every toggle. Closed panels use `hidden`, and each panel follows its button in the source. The script does not move focus. This matches the "do it right" list in `patterns/accordion.md` and avoids every "how it fails in code" case in `aria/patterns/accordion.md` and `wcag/sc-4.1.2-name-role-value.md`.
- **Contrast.** I worked these out from the declared colors with the relative luminance formula:
  - Button text `#005a9c` on `#fff` is about 7.1:1. That passes the 4.5:1 minimum for normal text in `wcag/sc-1.4.3-contrast-minimum.md`.
  - Body text `#1a1a1a` on `#fff` is well above 4.5:1.
  - The 2px button border (`#005a9c`) and the 3px focus outline (`#1a1a1a`) on `#fff` are both above the 3:1 in `wcag/sc-1.4.11-non-text-contrast.md`.
- **Focus.** `:focus-visible` gives a 3px solid outline.
- **Target size.** Each button spans the full width (`inline-size: 100%`). I estimated the height from the CSS: 1.125rem font at line-height 1.5, plus 0.5rem top and bottom padding and 2px borders, comes to roughly 47 CSS px at a 16px root. That is above the 24 by 24 in `wcag/sc-2.5.8-target-size-minimum.md`. This is an estimate from declared values, not a rendered measurement.
- **Page basics.** `lang="en"` is set, the `title` is descriptive, there is a `main` landmark, and the headings run `h1` then `h2` with no skipped levels.

### [Manual review] No visual cue for open or closed state
- **Where:** `h2 button`, lines 20 and 22.
- **What:** Nothing on the button shows whether its panel is open, such as an icon or text change. The only visual sign is the panel appearing below it.
- **Criterion:** WCAG 2.2 SC 1.4.11 Non-text Contrast (Level AA), tier 1. `patterns/accordion.md` lists 1.4.11 for the expand and collapse indicator. The criterion covers visual information needed to identify states, and here no separate indicator exists to measure.
- **Source:** `knowledge/wcag/sc-1.4.11-non-text-contrast.md`, `knowledge/patterns/accordion.md`.
- **Fix direction:** A human should judge whether the panel showing up is enough to identify the state. If not, add a visible indicator that meets the entry's contrast threshold.

## Content

- **Reading level: not measured.** `readability.py 1.0 (2026-10-23)` measured `<main>` and reported "no words found in the main content; not measured". It listed as left out: `div x2, h1 x1, h2 x2, script x1, style x1`. The two answer paragraphs are inside the left-out `div.panel` elements, so the tool saw none of the body text. Reading the text myself, the answers are two short, plain sentences. Whether they meet grade 8 is manual review.
- **Headings:** the single `h1` "Borrowing questions" names the page. Each `h2` is a specific question that describes its answer, which fits section 4 of `docs/content-standards.md`.
- **Links, alt text, error messages:** the page has none.
- **Language:** `lang="en"` is declared, and nothing on the page is in another language.

## Spec deviations

### [Definite] Scripted accordion used where the spec chose native `details` and `summary`
- **Spec line:** "Show/hide sections (questions, policies) | Native `details` and `summary`, not a scripted accordion | Works without script, and the team does not maintain widget code" (Pattern decisions, 2026-10-01).
- **Where:** lines 20 to 23 (markup) and 25 to 34 (script).
- **What the code does:** each question is a `button` with `aria-expanded` and `aria-controls`, and each answer is a `div` with `hidden` that the script toggles. There is no `details` or `summary` anywhere.
- **Effect on the decision's reason:** with script off, both panels stay `hidden` and the answers cannot be reached. That works against "works without script". The page also adds widget code the team said it does not maintain.
- This is a spec deviation, not a WCAG finding. The build meets the criteria checked above.

### [Manual review] Whether the need statement is served
- **Need statement:** "students with a quick question about borrowing… find the one answer they need without reading the whole page… questions that open to show their answer."
- **What the code exposes:** questions as headings with buttons that open their answers. That fits the need on its face. Whether students on a phone can actually scan and open one question needs a human to judge.
- **Spec inconsistency:** the need statement lists "Manual tests owed: each question opens with Enter and Space and with VoiceOver on iOS", but "Open manual tests" says "None owed". The spec contradicts itself and should be reconciled.

## Manual checks remaining

**Keyboard only (Chrome, then Safari)**
1. Tab to each question. Record whether focus lands on it and the outline is visible.
2. Press Enter, then Space, on each question. Record whether its answer opens and closes each time and whether focus stays on the question.
3. Record whether anything in a closed panel takes focus.

**VoiceOver on iOS (the test the need statement owes)**
1. Swipe to each question. Record the role and state VoiceOver gives before and after double-tapping it.
2. Record whether the answer is the next thing read after it opens.
3. Record whether the questions appear in the Headings rotor.

**NVDA with Chrome**
1. Move by headings (H) and by buttons (B). Record the role, name and expanded or collapsed state given for each question, and whether the state change is announced when you activate it.

**Zoom to 400% at 1280px wide**
1. Record whether the questions and answers reflow with no horizontal scrolling and no clipped text.

**Script disabled**
1. Load the page and record whether the answers can be reached at all. This bears on the spec deviation above.

**Visual state cue**
1. A person decides whether the open and closed states can be told apart without a separate indicator (the 1.4.11 lead above).

**Reading level**
1. A person reads the two answers against the grade 8 target, because the tool did not measure them.

## Automated scan

```
axe-core 4.14.0 via @axe-core/cli (axe), tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa
page: file:///C:/Users/rua126/AppData/Local/Temp/claude/C--Users-rua126/cf68331b-fb24-46e9-a990-751e07481e93/scratchpad/repo/doctorAccessible/evals/039-spec-pattern-decision-ignored/input.html
raw JSON: C:\Users\rua126\AppData\Local\Temp\doctor-a11y-axe\039-spec-pattern-decision-ignored-20261023-144526.json

violations: 0

incomplete: 0

passes: 15 rules   inapplicable: 49 rules

raw (violations and incomplete):
{
  "violations": [],
  "incomplete": []
}

a clean run is not a pass: read the code as well (.claude/agents/verifier.md)
```

- **Violations:** none, so nothing to map to findings.
- **Incomplete:** none, so no leads from axe.
- **Limits:** a clean run does not make this a pass. axe cannot see the spec deviation, and it cannot judge whether the open or closed state is visually clear.
