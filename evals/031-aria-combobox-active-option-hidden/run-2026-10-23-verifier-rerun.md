# Run 2026-10-23: verifier on eval 031 (re-run after the key amendment)

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit 813d4c6. The knowledge is unchanged from the first run; only this eval's `expected.md` changed.
- Method: a fresh general-purpose agent, same instructions as the first run (`run-2026-10-23-verifier.md`). A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **pass** against the amended key.

## Graded against `expected.md` (as at 813d4c6)

- Finding 1, SC 4.1.2 (Level A), tier 1, definite, on `highlight()`, the input, and the options, citing the 4.1.2 entry and `aria/patterns/autocomplete.md`: present.
- The result count was raised only under "Manual checks remaining", as a judgment for a human, not as a finding. 1.3.5 was explained as not applying.
- Must not: nothing from the list.

Observations: this run did not compute contrast and left it as a manual check, where the first run computed it. It also cited the 2.5.2 entry for pointer cancellation without opening it, and marked that point unverified, as the rules require.

## The report, as given (findings section)

### [Definite] The highlighted option is shown only by styling
- Where: input.html lines 53-57 (`highlight()`), with the input at line 23 and the options created at lines 39-46.
- What: Up and Down Arrow change which option is active only by toggling the `.active` class. The combobox never gets `aria-activedescendant`, and no option gets `aria-selected`, so the active option is a state that changes on screen but is never exposed to assistive technology.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), W3C Rec 12 Dec 2024, tier 1. The pattern entry names this exact case as a definite 4.1.2 failure. Its source for the roles and attributes is WAI-ARIA 1.2 (tier 1), with the APG Combobox Pattern as tier 2.
- Source: knowledge/wcag/sc-4.1.2-name-role-value.md; knowledge/aria/patterns/autocomplete.md
- Fix direction: On each arrow key, point `aria-activedescendant` on the input at the highlighted option's id and set `aria-selected="true"` on that option. Clear both when the list is re-rendered, closed or chosen from, or when nothing is highlighted.

No other defects found from the code. Things checked and found present:
- The visible `label` is tied to the input with `for`/`id`.
- `role="combobox"` has `aria-controls`, and `aria-expanded` is updated whenever the list opens or closes.
- The listbox is named.
- Down Arrow, Up Arrow, Enter and Escape are handled, and DOM focus stays in the field.
- The `:focus-visible` outline is declared.
- The highlight does not rely on color alone: it also adds bold text and an outline.

SC 1.3.5 does not apply, because the field asks for a department, not the user's own details.

Advice, not a finding (per `knowledge/patterns/autocomplete.md`): this is a fixed list of 16 departments, so a native `select` or an `input` with `datalist` may meet the need with less to test.

The rest of the report covered content (a manual-review note on no-match feedback), listed keyboard, screen reader, mobile, match-count (4.1.3, for a human to judge), pointer, zoom, contrast, and forced-colors checks, and said axe was not run.
