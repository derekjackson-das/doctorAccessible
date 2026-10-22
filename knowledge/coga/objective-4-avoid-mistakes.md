# COGA Objective 4: Help users avoid mistakes and know how to correct them

- Source: W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021
- Tier: 2, informative from W3C. A Working Group Note is guidance, not a conformance requirement. Meeting it is not needed to conform to WCAG 2.2, and missing it is not a WCAG failure.
- Objective: https://www.w3.org/TR/coga-usable/#x4-5-objective-4-help-users-avoid-mistakes-and-know-how-to-correct-them
- User stories: https://www.w3.org/TR/coga-usable/#x3-4-objective-4-help-users-avoid-mistakes-and-know-how-to-correct-them
- User-need map: https://www.w3.org/TR/coga-usable/#a-4-objective-4-help-users-avoid-mistakes-and-know-how-to-correct-them
- Verified against the live source: 2026-10-22 by Caesar Alam with Claude Code, direct fetch of the Note and of the WCAG 2.2 Recommendation for every criterion cited

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. When the same defect also fails a WCAG criterion, report it once, under that criterion and its entry, and name this entry as context. This objective overlaps WCAG more than any other, so check the WCAG criteria first.

## The objective in plain words

Design so mistakes are unlikely, and make them easy to fix when they happen. Ask for as little as possible. Accept the formats people actually type. Keep labels visible and instructions next to the field. Do not let content shift under the pointer. Never time people out without warning or throw away what they entered. Tell people what a task will cost before they start, confirm when something worked, and let them go back without losing their place.

## User needs it serves

- **Assistance and support.** People who find organization, typing, or ordering characters hard need interfaces that prevent errors: few fields, only valid choices, long numbers split into chunks, inputs that accept several formats, units they know, autofill and spelling help, clear labels and step-by-step instructions with examples, enough time without a session ending while they look something up, work saved as they go, knowing in advance what they will need, and understanding the consequences of what they do.
- **Undo.** People who often touch the wrong thing need to check their work, go back one step easily, and know exactly where back will take them, without losing what they did.

## Patterns W3C lists

- [Ensure controls and content do not move unexpectedly](https://www.w3.org/TR/coga-usable/#x4-5-1-ensure-controls-and-content-do-not-move-unexpectedly-pattern): nothing shifts during load or refresh unless the user caused it; show a loading indicator when it must.
- [Let users go back](https://www.w3.org/TR/coga-usable/#x4-5-2-let-users-go-back-pattern): the browser back button works and loses nothing.
- [Notify users of fees and charges at the start of a task](https://www.w3.org/TR/coga-usable/#x4-5-3-notify-users-of-fees-and-charges-at-the-start-of-a-task-pattern): all costs and terms up front, in plain language.
- [Design forms to prevent mistakes](https://www.w3.org/TR/coga-usable/#x4-5-4-design-forms-to-prevent-mistakes-pattern): minimal fields, required fields marked, valid-only choices, autocomplete.
- [Make it easy to undo form errors](https://www.w3.org/TR/coga-usable/#x4-5-5-make-it-easy-to-undo-form-errors-pattern): review before submit, fix without redoing steps, easy cancellation of transactions.
- [Use clear visible labels](https://www.w3.org/TR/coga-usable/#x4-5-6-use-clear-visible-labels-pattern): plain-word labels, visible, next to the control, readable by assistive technology.
- [Use clear step-by-step instructions](https://www.w3.org/TR/coga-usable/#x4-5-7-use-clear-step-by-step-instructions-pattern): before or beside the field, broken into steps, with examples.
- [Accept different input formats](https://www.w3.org/TR/coga-usable/#x4-5-8-accept-different-input-formats-pattern): for phone numbers, dates, currency, addresses, card numbers.
- [Avoid data loss and "timeouts"](https://www.w3.org/TR/coga-usable/#x4-5-9-avoid-data-loss-and-timeouts-pattern): no timeouts where possible, save progress, and warn at the start when a limit is unavoidable.
- [Provide feedback](https://www.w3.org/TR/coga-usable/#x4-5-10-provide-feedback-pattern): say whether each step succeeded.
- [Help the user stay safe](https://www.w3.org/TR/coga-usable/#x4-5-11-help-the-user-stay-safe-pattern): protect personal information and explain risks in plain language.
- [Use familiar metrics and units](https://www.w3.org/TR/coga-usable/#x4-5-12-use-familiar-metrics-and-units-pattern): the units common where the user is.

## WCAG criteria that touch it

Numbers, titles, and levels checked against the WCAG 2.2 Recommendation of 12 December 2024. Level AAA rows are not our target; they show how far WCAG reaches.

| SC | Title | Level | Entry | Overlap |
|---|---|---|---|---|
| 3.3.1 | Error Identification | A | no entry yet | A detected error is identified and described in text |
| 3.3.2 | Labels or Instructions | A | no entry yet | Labels or instructions when input is required |
| 3.3.3 | Error Suggestion | AA | no entry yet | Known corrections are suggested |
| 3.3.4 | Error Prevention (Legal, Financial, Data) | AA | no entry yet | Reversible, checked, or confirmed submissions, for legal, financial, data, and test cases only |
| 3.3.7 | Redundant Entry | A | no entry yet | Information already given in the same process is filled in or selectable |
| 1.3.5 | Identify Input Purpose | AA | `wcag/sc-1.3.5-identify-input-purpose.md` | `autocomplete` on fields about the user, so tools can fill them |
| 2.2.1 | Timing Adjustable | A | `wcag/sc-2.2.1-timing-adjustable.md` | Time limits can be turned off, adjusted, or extended |
| 3.2.2 | On Input | A | no entry yet | Changing a setting does not change context without warning |
| 2.5.2 | Pointer Cancellation | A | `wcag/sc-2.5.2-pointer-cancellation.md` | A pointer action can be aborted or undone, reducing accidental activation |
| 4.1.3 | Status Messages | AA | no entry yet | Success and status messages reach assistive technology without focus |
| 2.2.6 | Timeouts | AAA | no entry yet | Warning of inactivity that loses data, unless data is kept 20 hours |
| 3.3.6 | Error Prevention (All) | AAA | no entry yet | The 3.3.4 protections for every submission |

## Where WCAG stops

WCAG covers what happens once an error is detected, and prevention only for legal, financial, data, and test submissions. It does not require minimal fields, accepting varied input formats, splitting long numbers, familiar units, stating fees at the start, saving work as the user goes, warning about data loss on timeout (AAA), a working back button, or a review step for an ordinary form. A form can reject "617 555 0100" because it wanted "6175550100", say so in text, and conform.

## How it is used

- **Verify** reports WCAG failures first, under their criteria. Then, under this entry: a phone field that rejects spaces or dashes (likely); a checkout that shows fees only at the last step (likely); a form that clears entered data on a validation error (likely); layout shift that moves a button as the page loads (manual review).
- **Consult** asks what the user must have ready before a task starts, and whether a timeout is truly needed.
- **html-patterns** forms entries, when they exist, link here for the reasons behind input tolerance.
