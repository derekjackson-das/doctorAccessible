# Pattern: Date picker

- Sources:
  - W3C, "Date Picker Dialog Example", ARIA Authoring Practices Guide, under the Dialog (Modal) pattern, https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/. Tier 2. An example of a pattern, not a requirement.
  - Adrian Roselli, "Maybe You Don't Need a Date Picker", 5 July 2019, updated 18 March 2026, https://adrianroselli.com/2019/07/maybe-you-dont-need-a-date-picker.html. Tier 3.
- Related entries: `coga/objective-6-do-not-rely-on-memory.md`, `coga/objective-4-avoid-mistakes.md`, `wcag/sc-3.3.2-labels-or-instructions.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-3.3.3-error-suggestion.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the picker is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## The need it usually serves

The person has to give a date. For a date they know, a birthday or an appointment they already hold, they want to type it and move on. For a date they are choosing, such as a booking, a calendar helps them see which days are available. Those are two needs, and most date pickers serve the second while being imposed on the first.

## The simpler thing that often serves, and what is lost

A text field with the expected format stated before it, or three small fields for day, month, and year, with server-side validation either way. Roselli (2019, kept current to 2026) reports from about twenty years of user testing that date fields which are anything other than plain text for well-known dates frustrate people enough that he has watched participants quit a test more than once; people do not want to stop and learn a new control or discover which keys work. What is lost by choosing text: the visual calendar for choosing among available days. What is gained: typing, pasting, autofill, no new interface to learn, and nothing to test across assistive technologies. `coga/objective-6-do-not-rely-on-memory.md` and `coga/objective-4-avoid-mistakes.md` both point the same way: let people enter what they know in the form they know it, and tell them the format.

## What doing it right requires

Native first, with a caveat: `input type="date"` gives a browser-built calendar, but Roselli reports that it is a known problem for voice-control users across browsers and cites an independent audit he relies on that found the native control not accessible; so native does not settle this one. His position is that a plain text field is the native control that works.

If a calendar is needed for choosing among available dates, the APG's date picker is an example built on the modal dialog pattern: a button opens a dialog holding a grid of days with previous and next month controls, arrow keys move by day and week, and the dialog's focus and Escape behavior follow the dialog pattern. Roselli (2024 update) notes that the APG example relies on an attribute without browser support and kept it in with a hope of future support; treat the example as a sketch to test, not a reference to copy.

Whatever is built, the date field must still be validated on the server, because scripts fail and controls are bypassed, and the format must be stated in text before the field (`wcag/sc-3.3.2-labels-or-instructions.md`).

## What practitioners found when they tested it

- **Roselli, 2019, updated through 2026.** Auditing a widely used third-party picker, he found: previous and next month buttons with no accessible name, announced only as "button" (a 4.1.2 failure); month and year selects with no label (1.3.1 and 3.3.2); a list of supported keyboard shortcuts that the control never told the user about; the month and year controls unreachable by keyboard at all, since arrows did not reach them and Tab left the control; the selected date conveyed only visually (1.4.1 and 4.1.2); and weekdays not conveyed per day because the grid was not a table with header cells. His user-testing observation across two decades is the stronger finding: people want to type a known date.

## Criteria it touches

Format instruction and label: `wcag/sc-3.3.2-labels-or-instructions.md`, `wcag/sc-2.4.6-headings-and-labels.md`. Autocomplete token for a birthday: `wcag/sc-1.3.5-identify-input-purpose.md`. Names and states on every control in a calendar: `wcag/sc-4.1.2-name-role-value.md`. Grid structure with weekday headers: `wcag/sc-1.3.1-info-and-relationships.md`. Keyboard reach of every control: `wcag/sc-2.1.1-keyboard.md`, and the dialog's trap behavior: `wcag/sc-2.1.2-no-keyboard-trap.md`. Selected and today's date by more than color: `wcag/sc-1.4.1-use-of-color.md`. Day targets: `wcag/sc-2.5.8-target-size-minimum.md`. Errors on a bad date: `wcag/sc-3.3.1-error-identification.md`, `wcag/sc-3.3.3-error-suggestion.md`. Not re-asking a date already given: `wcag/sc-3.3.7-redundant-entry.md`. A calendar that opens on focus: `wcag/sc-3.2.1-on-focus.md`.

## Manual tests it demands

- Type a date in the stated format, in a different common format, and a nonsense value; record what happens each time and what the error says.
- Keyboard only: open the calendar; record whether every control (previous, next, month, year, every day) can be reached and operated, and whether Escape closes it with focus returned.
- Screen reader, each pair in the spec: record what is announced on each control, whether the selected day is announced as selected, and whether the weekday is announced with the day.
- Voice control: say the day number; record whether it selects.
- Mobile: record which control the platform shows and whether typing is still possible.

## What consult should say

1. Does the person already know the date? Then a text field with the format stated, and nothing else.
2. Are they choosing among available days? Then a calendar may help; build it so the text field still works without it.
3. If a picker stays: name every control, make the grid a real table, reach everything by keyboard, test with voice control, and validate on the server regardless.
