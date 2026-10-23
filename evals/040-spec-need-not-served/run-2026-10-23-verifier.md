# Run 2026-10-23: verifier on eval 040 (WP 4.6)

- Method: `evals/run.sh` (fresh `claude -p` session, registered verifier, axe via `tools/axe.py`), graded by `evals/check.py` (mechanical spec-deviation check plus a tool-less judge).
- History: the first run (verifier before it labeled spec deviations) left 038 and 039 unlabeled, failing "at definite or likely". The verifier's Spec deviations format now asks for a confidence on each, and this run passed. For 040, the first check of this report failed on a key that forbade any definite. The key was narrowed: it still forbids a definite claim that the need is unserved, but allows a definite note that the thing the need statement says to build is absent. Re-checked: pass.
- Result: **pass.**

## The verifier's report, as given

## Checked

- **Files:** `C:\Users\rua126\AppData\Local\Temp\claude\C--Users-rua126\cf68331b-fb24-46e9-a990-751e07481e93\scratchpad\repo\doctorAccessible\evals\040-spec-need-not-served\input.html` (40 lines, static HTML with inline CSS and no script) and the spec beside it, `...\evals\040-spec-need-not-served\a11y-spec.md`. I read the spec first.
- **Method:** I read the code in full, ran `tools/axe.py` (axe-core 4.14.0) and ran `tools/readability.py` with target 8, which the spec sets.
- **Knowledge entries opened:** `knowledge/INDEX.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-1.3.2-meaningful-sequence.md`, `wcag/sc-2.4.6-headings-and-labels.md`, `content/organization.md`, `content/reading-level.md`, and `docs/content-standards.md`.

## Findings

No WCAG 2.2 AA findings.

What the code exposes, judged against the entries I opened:
- **Headings (SC 1.3.1, `knowledge/wcag/sc-1.3.1-info-and-relationships.md`):** headings are real `h1`/`h2` elements. There is one `h1` and no skipped levels.
- **Hours table (SC 1.3.1, same entry):** it is a real data table. It has a `caption`, column headers marked `th scope="col"` and row headers marked `th scope="row"`. None of the table failures that entry lists are present.
- **Reading order (SC 1.3.2, `knowledge/wcag/sc-1.3.2-meaningful-sequence.md`):** the source order matches the visual order. No CSS moves anything. The hours come last on the page, but that is a choice about content order, not a gap between source and presentation, so it is not a 1.3.2 failure. It is reported below under Spec deviations and Content.
- **Headings and labels (SC 2.4.6, `knowledge/wcag/sc-2.4.6-headings-and-labels.md`):** "News", "Visiting" and "Opening hours" each describe their section. None is a generic heading of the kind that entry lists.
- **Page basics:** `lang="en"`, the page title and the viewport meta tag are all present, and axe passed all three.
- **Unused styles:** the CSS styles `button` and `a`, but the page has neither, so nothing here can receive focus. I did not compute contrast; axe `color-contrast` passed.

## Content

- **Reading level:** measured with `tools/readability.py` version line "readability.py 1.0 (2026-10-23)", over `<main>`.
  - Left out: one `h1`, three `h2`, one `style`.
  - Counts: 92 words, 30 sentences, 119 syllables (estimated by rule).
  - Flesch-Kincaid Grade Level: 0.9 against the spec target of grade 8, so at or below.
  - The tool warns that a text under 100 words gives a score that means little.
  - The count of 30 sentences in 92 words suggests the table cells were counted as separate sentences, which would push the score down. Treat 0.9 as a weak signal, not a pass.
  - Read by hand, the prose is short and plain.
- **Organization** (`docs/content-standards.md` section 3, `knowledge/content/organization.md`): **[Likely]**. The standard says the page puts key information at the top and follows the reader's order. On this page the hours come after News and Visiting. This is the same defect as the first spec deviation below, so it is not counted twice.
- **Headings:** they describe their sections and follow the rules in section 4 of the content standards.
- **Link text, alt text, error messages:** none on the page, so these do not apply.
- **Language:** `lang="en"` is declared. The page has no passages in another language and no abbreviations ("a.m." and "p.m." are standard time forms).

## Spec deviations

### [Definite] The thing the need statement says to build is missing, and the thing it rules out is the only way in
- **Spec, "Opening hours (2026-10-01)":** "**We will build:** today's opening and closing time, as text, as the first thing in the main content." and "**Instead of:** a weekly timetable as the only way to find today."
- **Code:** no text anywhere states today's opening and closing time. The only hours on the page are the seven-day table at `input.html` lines 25 to 37. Nothing marks the current day: no text, no class, no script.
- **Position:** the first thing in `<main>` after the `h1` is the News section (lines 19 to 21), then Visiting (lines 22 to 23). The hours are the last section (lines 24 to 37).
- **Result:** the page builds exactly what the "Instead of" line rules out, and puts it last rather than first.
- **Fix direction:** add today's hours as text at the top of the main content, as the need statement says, and keep the table as a secondary view if it is wanted.

### [Manual review] Whether the opening-hours need is served
- **Spec:** "**For:** staff and students on a phone, deciding whether to walk over now." and "**Trying to:** 'Is Widener open right now, and until when?'"
- **Code:** to answer that question, a reader has to know today's day, find the hours section at the bottom of the page and find that day's row in the table.
- **Judgment:** whether that serves the person in the need statement is for a human to decide. I cannot judge it from code.
- **Test the spec says is owed:** "on a phone with VoiceOver, today's hours are the first thing read in the main content." The code as written puts News first, so record whether that test passes or fails.
- **Housekeeping:** the spec's "Open manual tests" section says "None owed", but the need statement lists this test. The spec contradicts itself here, and someone should reconcile the two.

## Manual checks remaining

The spec names VoiceOver on iOS, NVDA with Chrome, keyboard only, and 400% zoom.

1. **VoiceOver on iOS (the spec's owed test):** on a phone, open the page and read the main content from the start. Record what is read first after the page heading, and whether today's hours can be found without going through the whole week.
2. **NVDA with Chrome:** use the table navigation commands on the hours table. Record whether the caption, the column headers and the row headers (day names) are announced with each cell.
3. **NVDA with Chrome:** move through the page by headings. Record whether the four headings give a usable outline and how many steps it takes to reach "Opening hours".
4. **400% zoom on desktop:** check that the text and the table fit the width without horizontal scrolling of the page and without content being cut off. Record whether the table itself needs to scroll.
5. **Keyboard only:** confirm that nothing on the page receives focus (there are no interactive elements), and that the page can be read with browser scrolling alone. Record anything unexpected.

## Automated scan

```
axe-core 4.14.0 via @axe-core/cli (axe), tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa
page: file:///C:/Users/rua126/AppData/Local/Temp/claude/C--Users-rua126/cf68331b-fb24-46e9-a990-751e07481e93/scratchpad/repo/doctorAccessible/evals/040-spec-need-not-served/input.html
raw JSON: C:\Users\rua126\AppData\Local\Temp\doctor-a11y-axe\040-spec-need-not-served-20261023-144518.json

violations: 0

incomplete: 0

passes: 8 rules   inapplicable: 56 rules

raw (violations and incomplete):
{
  "violations": [],
  "incomplete": []
}
```

- **Violations:** none.
- **Incomplete:** none.
- **Passes (8):** `aria-hidden-body`, `color-contrast`, `document-title`, `html-has-lang`, `html-lang-valid`, `meta-viewport`, `td-headers-attr`, `th-has-data-cells`.
- **Inapplicable:** 56 rules.
- **What the clean run means:** it agrees with my reading that there is no WCAG 2.2 AA failure. axe cannot see the spec deviation, which is about what content is on the page and where it sits.
