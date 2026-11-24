# Role: alert

- Category: live region.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "alert role", https://www.w3.org/TR/wai-aria-1.2/#alert. ARIA in HTML, W3C Recommendation 11 August 2026, row for `section`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Alert Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/alert/. A pattern, not a requirement. Read in full from a downloaded copy.
- Reference (tier 3): MDN Web Docs, "ARIA: alert role", last modified 28 September 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/alert_role
- Related entries: `aria/live-regions.md`, `aria/roles/status.md`, `aria/roles/alertdialog.md`, `content/error-messages.md`
- WCAG: `wcag/sc-4.1.3-status-messages.md`, `wcag/sc-2.2.1-timing-adjustable.md`, `wcag/sc-3.3.1-error-identification.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: when a live region is the right tool, how to make one, how it fails, and the manual tests are in `aria/live-regions.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A live region for news that cannot wait. WAI-ARIA 1.2: "A type of live region with important, and usually time-sensitive, information." The spec gives it "an implicit aria-live value of assertive, and an implicit aria-atomic value of true".

## The native element

None.

## When to choose it

Only when the interruption is needed: a submission error, a session about to end. Routine news is a `status`. A message that holds a control, or that the user must answer, is an `alertdialog`. The reasoning, and the pending failure technique for assertive misuse, are in `aria/live-regions.md`.

## What the spec asks of authors

- "Since alerts are not required to receive focus, authors SHOULD NOT require users to close an alert."
- "If an author desires focus to move to a message when it is conveyed, the author SHOULD use alertdialog instead of alert."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones. `aria-live` and `aria-atomic` are global, with the implicit values above.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author. WAI-ARIA 1.2 has no "Accessible Name Required" row for this role.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `section`, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `article`, `aside`, `dialog`, `form`, `ul`, `h1` to `h6`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On a `section` with an accessible name, the `region` landmark is replaced. MDN keeps the role to text content, with no links or buttons inside; what testers recorded for controls inside a live region is in `aria/live-regions.md`.

## Where the detail lives

- Everything about making it work, and how it fails: `aria/live-regions.md`. Two points from the APG pattern that entry does not repeat: an alert must not move keyboard focus, and alerts that disappear on their own are to be avoided.
- axe has no rule for whether an alert is announced. The manual tests are in `aria/live-regions.md`.
