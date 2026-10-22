# SC 4.1.3 Status Messages

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 4 Robust / 4.1 Compatible
- Tier 1 source: https://www.w3.org/TR/WCAG22/#status-messages
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> In content implemented using markup languages, status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.

## What it requires, in our words

When a page tells the user something has happened without moving them anywhere, such as "5 results found", "Item added to cart", "Saving...", or "Your changes were saved", a screen reader user must hear it too, without having to go looking for it. Sighted users see the message appear. A screen reader reads where focus is, so a message that appears somewhere else is silent unless the code marks it as a status message. In HTML that means a live region: `role="status"` for results and confirmations, `role="alert"` for warnings and errors that need attention now, `role="log"` for a running list, or an `aria-live` attribute. The criterion does not apply when the message does receive focus, such as a dialog, and it does not apply to content that is not a status message. The region should exist in the page before the message is put into it, because assistive technology watches for changes inside a live region it already knows about.

## How it fails in code

- Script that inserts or changes a visible message (a result count, a success note, an error summary, a "loading" indicator) in an element with no live-region role or `aria-live`, and does not move focus to it. Definite. F103.
- A live region created and filled in the same moment, so the first message is often missed. Likely; behavior varies by assistive technology, and a person confirms.
- A toast or snackbar that appears and disappears with no role. Definite when it carries a status.
- A status message that does receive focus, such as a confirmation dialog the user is placed in. Not covered by this criterion; focus management is 2.4.3.
- `role="alert"` used for a routine result count. Not a failure of this criterion, but the wrong level of interruption; `role="status"` is the quieter choice. Manual review on fit.
- `aria-live` on a large region that changes constantly, so the screen reader never stops talking. Not a failure of this criterion; a usability problem a person should raise.

## How to meet it

- Technique ARIA22, "Using role=status to present status messages", for the success or result of an action.
- Technique ARIA19, "Using ARIA role=alert or Live Regions to Identify Errors", for warnings and errors the user needs now.
- Technique ARIA23, "Using role=log to identify sequential information updates", for a chat or activity feed.
- Technique ARIA25, "Using an ARIA live region to convey the status of a progress bar", and Technique ARIA27, "Using ariaNotify to convey the status of a progress bar", for progress.
- Put the live region in the markup on page load, empty, and change its text when the status changes. Native HTML has `output`, which carries `role="status"` by default, and is the native-first choice for a result count.
- Advisory: Technique SCR14, "Using scripts to make nonessential alerts optional".

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.3.1 Error Identification (`wcag/sc-3.3.1-error-identification.md`). The error must exist in text; this criterion is about whether it is announced.
- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). Roles on controls; this criterion is roles on messages.
- SC 2.4.3 Focus Order (`wcag/sc-2.4.3-focus-order.md`). The alternative of moving focus to the message, which has its own rules.
- SC 1.3.1 Info and Relationships (`wcag/sc-1.3.1-info-and-relationships.md`). Whether the message's meaning is in the code at all.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion in the 4.14 rule list. Its `aria-roles` and related rules check that a live-region role used is valid, not that one is present where a status appears. Whether a message is announced is found by triggering it with a screen reader running, or by reading the script that produces it. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
