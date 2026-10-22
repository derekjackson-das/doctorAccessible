# SC 3.3.4 Error Prevention (Legal, Financial, Data)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 3 Understandable / 3.3 Input Assistance
- Tier 1 source: https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> For web pages that cause legal commitments or financial transactions for the user to occur, that modify or delete user-controllable data in data storage systems, or that submit user test responses, at least one of the following is true:
>
> **Reversible.** Submissions are reversible.
>
> **Checked.** Data entered by the user is checked for input errors and the user is provided an opportunity to correct them.
>
> **Confirmed.** A mechanism is available for reviewing, confirming, and correcting information before finalizing the submission.

## What it requires, in our words

When a submission has consequences, such as buying something, signing up for something binding, deleting or changing stored records, or handing in a test, the page must give the user one of three protections: a way to undo it afterward, a check for mistakes with a chance to fix them before it goes through, or a review step that shows everything and asks for confirmation. Everyone makes slips; people with motor or cognitive disabilities make more, and a slip on a course registration or a payment is expensive. A review page before "Place order" is the usual pattern. A "Delete" button that acts immediately with no undo and no confirmation is the usual failure.

## How it fails in code

- A delete or cancel action that executes on one click, with no confirmation and no way to recover. Definite once the data is confirmed to be user-controllable.
- A purchase, registration, or legal agreement submitted directly from the entry form, with no review step, no validation, and no cancellation window. Definite.
- A test or exam submitted without a chance to review answers. Definite.
- A confirmation that is a browser `confirm()` dialog. Passes this criterion, though a custom dialog is better for other reasons.
- A form that validates fields and lets the user correct them before submission. Passes by "Checked".
- A stated period during which the user can cancel the order. Passes by "Reversible". G164.

## How to meet it

- Technique G98, "Providing the ability for the user to review and correct answers before submitting": a review page or summary with an edit path.
- Technique G168, "Requesting confirmation to continue with selected action", for deletions.
- Technique G99, "Providing the ability to recover deleted information", such as a trash or undo.
- Technique G164, "Providing a stated time within which an online request (or transaction) may be amended or canceled by the user after making the request".
- Technique G155, "Providing a checkbox in addition to a submit button", for legal agreements.
- Advisory: SCR18 for client-side validation, G199 for success feedback.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.3.1 and 3.3.3 (entries in this package). Identifying and fixing errors, which is the "Checked" route.
- SC 2.5.2 Pointer Cancellation (`wcag/sc-2.5.2-pointer-cancellation.md`). Undoing an accidental press at the pointer level.
- SC 2.2.1 Timing Adjustable (`wcag/sc-2.2.1-timing-adjustable.md`). A review step must not time out unreasonably.
- SC 3.3.6 Error Prevention (All) is Level AAA and extends this to every form; not a requirement here.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Whether a consequential action is reversible, checked, or confirmed is judged by walking the flow, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
