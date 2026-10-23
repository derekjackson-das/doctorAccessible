# Eval 034: date picker whose chosen day is shown only by styling

Input: `input.html`. A study-room booking form with a date field and a "Choose date" button that opens a calendar.

Intended defect: the calendar is a `table` with `role="grid"`, named by its month heading, with full day names in `abbr` on the headers and a roving tabindex on the days. When the dialog is reopened, the chosen day is marked with a CSS class (fill, bold, underline). It never gets `aria-selected="true"`, so its selected state is not exposed.

Everything else is clean:
- The field has a label and its format, the format linked by `aria-describedby`, and typing a date works.
- The "Choose date" button's name changes to "Change date, " plus the date after a choice.
- The calendar is a non-modal `dialog` with a name.
- Previous and next month buttons have names; their icons are hidden SVGs.
- Arrow keys move between days and across months; Enter or Space picks a day.
- Escape and Cancel close the calendar and return focus to the button.
- Focus is visible on every day, including the chosen one, where a white inner ring sits between the dark focus outline and the blue fill; contrast is about 7.1:1 or better; cells are 2.75rem square.
- The month heading changes, and so is announced, only when the month does.
- Language, title, one `h1`, `main`.

## Expected findings

1. **[Definite]** The chosen day's selected state is not exposed: no `aria-selected` on it.
   - Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1, from `knowledge/wcag/sc-4.1.2-name-role-value.md` (a custom control that "changes state visually without exposing that state (... `aria-selected` ...)", definite when user-settable).
   - ARIA entry: `knowledge/aria/patterns/date-picker.md`, which lists this case.
   - Where: `render()`, where the `chosen` class is added; the grid's `td` cells.
   - Why definite, though the date is also in the field and in the button's name: the gridcell itself has a selected state that the user sets and that is shown visually, and the 4.1.2 entry grades that case definite.
   - Acceptable fix directions: set `aria-selected="true"` on the chosen day's cell (and on no other), as the APG example does. As a direction, not a patch.

## Also acceptable

- A note, marked advice, that a plain text field with the stated format may be enough (`patterns/date-picker.md`).
- A note, marked advice, that the APG example also offers keyboard help, Home and End, and Page Up and Page Down; these are not required.
- Manual-review notes that a criterion appears met and needs a browser check.
- A note that axe is not expected to catch this.

## Must not

- Report the calendar's other ARIA (grid, name, headers, roving tabindex), the button names, or keyboard support as failures.
- Report the dialog as a failure for not being modal, or for not trapping focus; it is non-modal.
- Report contrast, target size, focus style, headings, landmarks, or language as failures.
- Report the defect twice, under 4.1.2 and again under 1.3.1 or 1.4.1.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe sees valid grid markup. It does not know which cell is chosen, so it is not expected to report this defect. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 4.1.2 (Level A), tier 1, and nothing from the Must not list appears.
