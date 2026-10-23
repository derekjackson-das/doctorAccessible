# ARIA pattern: Date picker

- W3C examples (tier 2): ARIA Authoring Practices Guide, "Date Picker Dialog Example" (under the Dialog (Modal) pattern) and "Date Picker Combobox Example" (under the Combobox pattern), no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/ and https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-datepicker/ Examples, not patterns, and not requirements. The calendar inside uses the "Grid Pattern", https://www.w3.org/WAI/ARIA/apg/patterns/grid/
- Normative (tier 1): WAI-ARIA 1.2, `dialog` and `grid` roles and `aria-selected`, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/. ARIA in HTML, W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/ : a `table` may take `role="grid"`, and its `tr`, `th`, and `td` then map to row, column header, and cell.
- Practitioner testing (tier 3): Roselli's "Maybe You Don't Need a Date Picker" (2019, updated 2026) and its audit of a third-party picker are in `patterns/date-picker.md`. This entry adds none.
- Related entries: `patterns/date-picker.md` (whether to build one, the native and plain-text options, the criteria, the manual tests), `aria/patterns/modal-dialog.md`, `aria/accessible-name.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-3.3.2-labels-or-instructions.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/date-picker.md` decide whether code fails WCAG; report a failure once, under its criterion. The APG examples are examples, so departing from them is never a finding on its own. A custom calendar where a text field would do is advice (`aria/using-aria.md`).

**Testing gap.** No listed source tests either APG date picker example with assistive technology (`patterns/date-picker.md`). Roselli's audit, the only test on the list, is of a different, third-party picker. Test with the spec's assistive technology.

## Native first

A plain text field with the format stated before it, or `input type="date"`, with the caveats in `patterns/date-picker.md`. The calendar is an addition for choosing among dates, never the only way to enter one.

## Roles, states, and properties

From the APG dialog example, in our words:

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| Date field | native `input type="text"` | `aria-describedby` pointing at the visible format, such as "(mm/dd/yyyy)" | Author | Typing a date always works |
| "Choose Date" button | `button` | name changes to "Change Date, " plus the chosen date | Script | So the chosen date is announced when focus returns |
| Calendar container | `dialog` | `aria-modal="true"`; `aria-label` | Author | Follows `aria/patterns/modal-dialog.md` |
| Month and year heading | | `aria-live="polite"` | Author | Announces the new month when it changes |
| Calendar | `table` with `role="grid"` | `aria-labelledby` pointing at the month heading | Author | Rows, headers, and cells come from the table |
| Day column headers | `th` | `abbr` with the full day name, when the visible text is "Su", "Mo" | Author | The full name is read in the grid |
| Each day | `td` | `tabindex="0"` on one day, `"-1"` on the rest | Script | A roving tabindex, as in `aria/patterns/tabs.md` |
| The selected day | `td` | `aria-selected="true"`, on that day only | Script | The date in the field |
| Keyboard help | | `aria-live="polite"` | Author | Announced when focus enters the grid |

## Naming

The field is named by its `label` and described by its format. The "Choose Date" button carries the chosen date in its name. The grid is named by the visible month and year (`aria/accessible-name.md`).

## Keyboard

From the APG dialog example, in our words: the button opens the dialog with focus on the selected day, or today if none. Arrow keys move by day and week. Home and End go to the start and end of the week. Page Up and Page Down change the month, and with Shift the year. Enter or Space picks a day and closes the dialog. Escape closes it without picking. Focus returns to the button. The month buttons, the grid, and OK and Cancel are each one stop in the dialog's tab sequence.

## What testing found

Nothing on the list tests the ARIA of either APG example. The third-party audit in `patterns/date-picker.md` found the same failures this table guards against: unnamed month buttons, unlabeled selects, the selected date conveyed only visually, and weekdays not conveyed because the grid had no header cells.

## How it fails in code

- The selected day shown only by styling, with no `aria-selected`: a state that changes visually without being exposed, `wcag/sc-4.1.2-name-role-value.md`, definite.
- Icon-only previous and next month buttons with no name: 4.1.2, definite.
- Day cells that cannot be reached by keyboard, through a roving tabindex with no arrow keys: `wcag/sc-2.1.1-keyboard.md`, definite.
- A calendar built from `div`s with no table or grid structure, so weekdays are not tied to days: `wcag/sc-1.3.1-info-and-relationships.md`, at that entry's confidence.
- The format not stated in text before the field: `wcag/sc-3.3.2-labels-or-instructions.md`, at that entry's confidence.
