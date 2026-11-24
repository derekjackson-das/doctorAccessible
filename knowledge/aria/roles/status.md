# Role: status

- Category: live region.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "status role", https://www.w3.org/TR/wai-aria-1.2/#status. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `output` and `section`, https://www.w3.org/TR/html-aria/#el-output
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.100 (`output`), https://www.w3.org/TR/html-aam/#el-output
- Practice (tier 2): none. The ARIA Authoring Practices Guide has no pattern for this role.
- Reference (tier 3): MDN Web Docs, "ARIA: status role", last modified 23 June 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/status_role
- Related entries: `aria/live-regions.md`, `aria/roles/alert.md`, `aria/roles/timer.md`
- WCAG: `wcag/sc-4.1.3-status-messages.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: when a live region is the right tool, how to make one, how it fails, and the manual tests are in `aria/live-regions.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="status"` on an `output` is redundant and never a finding.

## What it is

A live region for advisory news: saved, sent, 3 results. WAI-ARIA 1.2: "A type of live region whose content is advisory information for the user but is not important enough to justify an alert, often but not necessarily presented as a status bar." The spec gives it "an implicit aria-live value of polite and an implicit aria-atomic value of true".

## The native element

`output` (HTML-AAM 3.5.100). ARIA in HTML allows any role on it and marks `status` "NOT RECOMMENDED". Support for `output` as a live region was uneven in the tests `aria/live-regions.md` records; one of those sources adds `role="status"` to the `output` as a workaround, which is redundant by ARIA in HTML and not a finding.

## What the spec asks of authors

- "Authors SHOULD ensure an element with role status does not receive focus as a result of change in status."
- "If another part of the page controls what appears in the status, authors SHOULD make the relationship explicit with the aria-controls attribute."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones. `aria-live` and `aria-atomic` are global, with the implicit values above.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author. WAI-ARIA 1.2 has no "Accessible Name Required" row for this role; MDN says a name is not required.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `output` (redundant, "NOT RECOMMENDED").
- **Allowed:** `section`, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `article`, `aside`, `form`, `ul`, `h1` to `h6`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

Another role on an `output` replaces `status`, and with it the implicit live region. On a `section` with an accessible name, `status` replaces the `region` landmark.

## Where the detail lives

- When a status message needs a live region, how to make one, and how it fails: `aria/live-regions.md` and `wcag/sc-4.1.3-status-messages.md`.
- axe has no rule for whether a status is announced. The manual tests are in `aria/live-regions.md`.
