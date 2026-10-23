# Run 2026-10-23: verifier on eval 034 (first run)

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit c35330d.
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **pass** against the key, with a real page problem found.

## Graded against `expected.md` (as at c35330d)

- Finding 1, SC 4.1.2 (Level A), tier 1, definite, on `render()` and the grid cells, citing the 4.1.2 entry and `aria/patterns/date-picker.md`: present.
- Must not: nothing from the list. The dialog's being non-modal and the missing APG keys were correctly treated as advice.

Page problem: the run raised, as manual review under SC 1.4.11, that the inset focus outline (#1a1a1a) on the chosen day sits against its #005a9c fill at a computed 2.44:1, with white on its outer side. It did not call it a failure, so the key was not broken, but the page was not as clean as the key claimed. The review agent raised the same point. At 019516f the page gained a white inner ring on the chosen day when focused, and the month heading is now rewritten only when the month changes. The eval was run again; see `run-2026-10-23-verifier-rerun.md`.

## The report, as given (findings section)

### [Definite] Selected day shown only by styling, with no `aria-selected`
- Where: `input.html` line 79 (`render()`: `cell.classList.add('chosen')`), with the styling on line 22 (`td.chosen`).
- What: When the dialog reopens, the day already chosen is marked with a class that only changes how it looks (fill, bold, underline). No cell ever gets `aria-selected="true"`, so the selected state is not exposed in code.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
- Source: knowledge/wcag/sc-4.1.2-name-role-value.md; knowledge/aria/patterns/date-picker.md, "How it fails in code", first bullet, names this exact case as definite.
- Fix direction: In `render()`, set `aria-selected="true"` on the chosen day's cell and on that cell only, alongside the visual class.

### [Manual review] Focus ring on the selected day against its blue fill
- Where: line 23 (`td:focus-visible { outline: 3px solid #1a1a1a; outline-offset: -3px; }`) together with line 22 (`td.chosen { background: #005a9c; }`).
- What: The ring is drawn inside the cell. On the selected day it sits against the `#005a9c` fill at a computed 2.44:1, which is below the 3:1 non-text threshold in the entry. Against the white around the cell it computes to 17.4:1. Whether one contrasting edge is enough depends on how the ring renders, so a person needs to look at it.
- Criterion: WCAG 2.2 SC 1.4.11 Non-text Contrast (Level AA), tier 1
- Source: knowledge/wcag/sc-1.4.11-non-text-contrast.md; knowledge/design/focus-indicators.md
- Fix direction: Confirm visually. If it does not hold up, use a ring that contrasts with both the blue fill and white, for example a two-color ring.

The rest of the report computed the text and border contrast as passing, listed the controls and keys checked, covered content, listed screen reader, keyboard, visual, typed-date, voice, and zoom checks, and said axe was not run.
