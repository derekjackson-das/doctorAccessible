# Run 2026-10-23: verifier on eval 031 (first run)

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit fd3d319.
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **fail, against the key as written at fd3d319.**

## Graded against `expected.md` (as at fd3d319)

- Finding 1, SC 4.1.2 Name, Role, Value (Level A), tier 1, definite, on `highlight()`, `#dept`, and the options, citing the 4.1.2 entry and `aria/patterns/autocomplete.md`: present and correct.
- Must not, "Report a missing count of results under 4.1.3": **broken.** The answer filed a "[Manual review]" item under SC 4.1.3 for the result count. It said in the same item that 4.1.3 is "not triggered" and "not a failure as written".
- Everything else on the must-not list was respected.

## What changed after this run

The note came from `patterns/autocomplete.md`, whose criteria table lists 4.1.3 for "announcing how many suggestions match". The key's intent was to stop a false 4.1.3 failure, not a note that the criterion does not apply. At commit 813d4c6 the must-not item was amended to forbid only a 4.1.3 failure (likely or definite) and to allow a manual-review note that it is not triggered. The eval was then run again; see `run-2026-10-23-verifier-rerun.md`.

## The report, as given (findings section)

### [Definite] Highlighted option is shown only by styling, not exposed programmatically
- Where: `input.html` lines 53–57 (`highlight()`), and line 23 (`#dept`, which never receives `aria-activedescendant`). Options built at lines 39–46 never receive `aria-selected`.
- What: Arrow keys move the highlight by toggling only the `.active` class. The combobox never sets `aria-activedescendant` to the highlighted option's id, and no option ever gets `aria-selected="true"`. The active option is a state that changes on screen with no programmatic exposure or change notification.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
- Source: knowledge/wcag/sc-4.1.2-name-role-value.md. Pattern detail is in knowledge/aria/patterns/autocomplete.md ("How it fails in code", first bullet), tier 2 APG and tier 1 WAI-ARIA 1.2.
- Fix direction: On every highlight change, set `aria-activedescendant` on the input to the active option's id, and clear it when nothing is highlighted or the popup closes. Mark the highlighted option `aria-selected="true"`.

### [Manual review] No announcement of how many suggestions match
- Where: `render()`, lines 35–51.
- What: The page shows no visible result count, so SC 4.1.3 Status Messages (Level AA) is not triggered: the entry covers visible messages inserted by script. Whether the field and listbox give enough feedback when suggestions appear is a judgment for testing.
- Criterion: WCAG 2.2 SC 4.1.3 Status Messages (Level AA), tier 1. This is not a failure as written.
- Source: knowledge/wcag/sc-4.1.3-status-messages.md, knowledge/patterns/autocomplete.md
- Fix direction: If a visible count is added later, put it in a `role="status"` region that exists before it is filled.

Advice, not a finding (knowledge/patterns/autocomplete.md, knowledge/aria/using-aria.md): there are 16 fixed departments, so a native `select` or an `input` with `datalist` would avoid hand-built ARIA.

The rest of the report checked the label, `aria-expanded`, `aria-controls`, keyboard handling, contrast (white on #005a9c about 7.1:1; #4a4a4a border about 8.9:1; #005a9c outline about 7.1:1), headings, and language and found them sound; listed manual keyboard, screen reader, mobile, zoom, forced-colors, and invalid-value checks; and said axe was not run.
