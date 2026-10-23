# Pattern: Date picker

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Date Picker Dialog Example", an example under the Dialog (Modal) pattern, accessed 2026-10-22 (the page shows no date). https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/ An example, not a requirement.
- W3C tutorial: none.
- Practitioner testing (tier 3, on `knowledge/SOURCES.md`):
  - Adrian Roselli, "Maybe You Don't Need a Date Picker", 5 July 2019, updated 18 March 2026. https://adrianroselli.com/2019/07/maybe-you-dont-need-a-date-picker.html Reports about twenty years of user testing with date fields, an audit of a widely used third-party picker against WCAG, and notes on the native control and on the Authoring Practices example.
- Related entries: `ux/...` (no entry yet for this pattern), `aria/patterns/date-picker.md` (the roles, states, naming, and keyboard), `patterns/modal-dialog.md`, `wcag/sc-3.3.2-labels-or-instructions.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `coga/objective-6-do-not-rely-on-memory.md`, `coga/objective-4-avoid-mistakes.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

**Testing gap.** One source on the list reports testing. Roselli's screen reader and keyboard findings are from an audit of one third-party picker; his voice-control finding on the native `input type="date"` rests on an independent report he cites, which is not on our list. No listed source reports testing the Authoring Practices example itself with assistive technology.

## The need

The person has to give a date. For a date they know, a birthday or an appointment they already hold, they want to type it and move on. For a date they are choosing, such as a booking, a calendar helps them see which days are available. Those are two needs, and most date pickers serve the second while being imposed on the first. `coga/objective-6-do-not-rely-on-memory.md` and `coga/objective-4-avoid-mistakes.md` point the same way: let people enter what they know in the form they know it, and tell them the format.

## The simpler alternative and its cost

A text field with the expected format stated before it, or three small fields for day, month, and year, with server-side validation either way. Roselli reports from about twenty years of user testing that date fields which are anything other than plain text for well-known dates frustrate people enough that he has watched participants quit a test more than once; people do not want to stop and learn a new control or discover which keys work. What is lost: the visual calendar for choosing among available days. What is gained: typing, pasting, autofill, no new interface to learn, and nothing to test across assistive technologies.

## What doing it right requires

Native first, with a caveat: `input type="date"` gives a browser-built calendar, but Roselli reports it as a known problem for voice-control users across browsers, resting on an independent audit he cites. His position is that a plain text field is the native control that works. Whatever is built, the field is validated on the server, because scripts fail and controls are bypassed, and the format is stated in text before the field (`wcag/sc-3.3.2-labels-or-instructions.md`).

If a calendar is needed for choosing among available dates, the Authoring Practices example builds one on the modal dialog pattern (see `patterns/modal-dialog.md`): a button opens a dialog holding a grid of days with previous and next month controls; arrow keys move by day and week; focus and Escape follow the dialog pattern. Roselli (2024 update) notes the example relies on an attribute without browser support and kept it in with a hope of future support; treat the example as a sketch to test, not a reference to copy.

His audit of a widely used third-party picker found: previous and next month buttons with no accessible name, announced only as "button"; month and year selects with no label; a list of supported keyboard shortcuts the control never told the user about; the month and year controls unreachable by keyboard at all, since arrows did not reach them and Tab left the control; the selected date conveyed only visually; and weekdays not conveyed per day because the grid was not a table with header cells. Each of those is a row in the table below.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 3.3.2 | Labels or Instructions | A | `wcag/sc-3.3.2-labels-or-instructions.md` | The format stated before the field; labels on month and year controls |
| 2.4.6 | Headings and Labels | AA | `wcag/sc-2.4.6-headings-and-labels.md` | The field's label says which date |
| 1.3.5 | Identify Input Purpose | AA | `wcag/sc-1.3.5-identify-input-purpose.md` | Autocomplete token for a birthday |
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Names on every calendar control; selected state exposed |
| 1.3.1 | Info and Relationships | A | `wcag/sc-1.3.1-info-and-relationships.md` | The grid as a table with weekday headers |
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Every control reachable and operable |
| 2.1.2 | No Keyboard Trap | A | `wcag/sc-2.1.2-no-keyboard-trap.md` | Leaving the calendar dialog |
| 1.4.1 | Use of Color | A | `wcag/sc-1.4.1-use-of-color.md` | Selected and today's date by more than color |
| 2.5.8 | Target Size (Minimum) | AA | `wcag/sc-2.5.8-target-size-minimum.md` | Day cells as targets |
| 3.3.1 | Error Identification | A | `wcag/sc-3.3.1-error-identification.md` | A bad date named in text |
| 3.3.3 | Error Suggestion | AA | `wcag/sc-3.3.3-error-suggestion.md` | Saying what a valid date looks like |
| 3.3.7 | Redundant Entry | A | `wcag/sc-3.3.7-redundant-entry.md` | Not re-asking a date already given |
| 3.2.1 | On Focus | A | `wcag/sc-3.2.1-on-focus.md` | A calendar that opens on focus |

## Manual tests

- Type a date in the stated format, in a different common format, and a nonsense value; record what happens each time and what the error says.
- Keyboard only: open the calendar; record whether every control (previous, next, month, year, every day) can be reached and operated, and whether Escape closes it with focus returned.
- Screen reader, each pair in the spec: record what is announced on each control, whether the selected day is announced as selected, and whether the weekday is announced with the day.
- Voice control: say the day number; record whether it selects. This is the gap Roselli flags for the native control.
- Mobile: record which control the platform shows and whether typing is still possible.
