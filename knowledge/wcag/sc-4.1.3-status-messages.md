# SC 4.1.3 Status Messages

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 4 Robust / 4.1 Compatible
- Tier 1 source: https://www.w3.org/TR/WCAG22/#status-messages
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
- Also in: WCAG 2.1 (https://www.w3.org/TR/WCAG21/#status-messages), Level AA, same text. Not in WCAG 2.0; it was added in 2.1.
- Verified against the live source: 2026-10-22 by Claude Code for Jennifer Dee, by direct fetch of the WCAG 2.2 and 2.1 Recommendations and the Understanding page

## Normative text (tier 1, quoted)

> In content implemented using markup languages, status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.

The criterion depends on the defined term "status message", which WCAG 2.2 defines as:

> change in content that is not a change of context, and that provides information to the user on the success or results of an action, on the waiting state of an application, on the progress of a process, or on the existence of errors

## What it requires, in our words

When the page shows a short update without moving focus, such as "Saved", "3 results", "Uploading, 40%", or "Email address is required", the update must carry a role or property that lets assistive technology pick it up on its own. A message that only appears visually is invisible to someone who can't see it, because their focus is somewhere else. The criterion covers only messages that don't move focus and don't change the context. If the page moves focus to the message, or loads a new page, this criterion does not apply. The Understanding page also says the criterion does not ask authors to add new messages. It applies only when a message is already shown.

## How it fails in code

- Script writes a success or result message into an element with no `role="status"`, `role="alert"`, `role="log"`, or `aria-live`, and focus stays where it was. Definite. This is failure F103 on the Understanding page.
- A live region is created at the same moment its text is inserted, or is added to the page already holding the message. The test procedure for technique ARIA22 checks that the container has its role before the message occurs (tier 2, https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22). Likely; confirm with assistive technology testing.
- A search filter or results count updates ("12 results") with no live region. Definite when the count is shown as feedback on the user's action.
- A form error appears inline after submit, focus does not move, and the error has no live region or alert role. Definite under this criterion. The error text itself also falls under SC 3.3.1 (no entry yet).
- `role="alert"` or `aria-live="assertive"` on routine, non-urgent updates. The Understanding page lists this as a failure still being written up, with no technique ID yet. Report as likely, as a best-practice concern rather than a confirmed failure, until a numbered failure exists.
- A message that moves focus to itself, or a page reload that shows the message. Not a 4.1.3 failure. Check focus handling under SC 2.4.3 (`wcag/sc-2.4.3-focus-order.md`) instead.

## How to meet it

- Native HTML first. ARIA in HTML maps the `output` element to the `status` role and says not to add `role="status"` to it again (tier 1, ARIA in HTML, W3C Rec 11 Aug 2026, https://www.w3.org/TR/html-aria/). Use `output` when the message is the result of a calculation or user action; otherwise a container with `role="status"`.
- Put the container in the page from the start, with its role, and change only its text. This is what the ARIA22 test procedure checks.
- Results, success, and application state: technique ARIA22, "Using role=status to present status messages", combined with G199, "Providing success feedback when data is submitted successfully".
- Errors and warnings: technique ARIA19, "Using ARIA role=alert or Live Regions to Identify Errors", combined with any of G83, G84, G85, G177, or G194. The Understanding page notes that `alert` is needed only when the context does not change.
- Progress of a process: ARIA23, "Using role=log to identify sequential information updates"; ARIA25, "Using an ARIA live region to convey the status of a progress bar"; ARIA22 combined with G193, "Providing help by an assistant in the web page"; or ARIA27, "Using ariaNotify to convey the status of a progress bar".
- Keep the message short, and do not move focus to it.

All techniques are tier 2, from https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html, which lists them as sufficient, by situation.

## Related criteria

- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). Where state changes on a control belong, as distinct from messages about results.
- SC 2.4.3 Focus Order (`wcag/sc-2.4.3-focus-order.md`). When a page moves focus to the message instead.
- SC 1.3.1 Info and Relationships (`wcag/sc-1.3.1-info-and-relationships.md`). Structure of the message itself.
- SC 3.3.1 Error Identification (no entry yet). Whether an error is identified and described in text at all.
- WAI-ARIA 1.2, tier 1, https://www.w3.org/TR/wai-aria-1.2/, for the `status`, `alert`, and `log` roles and the `aria-live` property.

## Automated coverage (tier 3)

axe-core 4.14.0 (checked in the package source, 2026-10-22) has no rule tagged for this criterion. axe cannot tell whether visible text is a status message, and it cannot watch a message appear after a user action. A clean axe run says nothing about 4.1.3. Find these defects by reading the script that inserts messages, then confirm with assistive technology testing.
