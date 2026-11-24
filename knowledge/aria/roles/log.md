# Role: log

- Category: live region.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "log role", https://www.w3.org/TR/wai-aria-1.2/#log. ARIA in HTML, W3C Recommendation 11 August 2026, row for `section`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): none. The ARIA Authoring Practices Guide has no pattern for this role.
- Reference (tier 3): MDN Web Docs, "ARIA: log role", last modified 23 June 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/log_role
- Related entries: `aria/live-regions.md`, `aria/roles/status.md`, `aria/roles/marquee.md`
- WCAG: `wcag/sc-4.1.3-status-messages.md`, `wcag/sc-1.3.2-meaningful-sequence.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: when a live region is the right tool, how to make one, how it fails, and the manual tests are in `aria/live-regions.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A live region whose entries arrive in order, newest last: a chat, an activity history, an error log. WAI-ARIA 1.2: "A type of live region where new information is added in meaningful order and old information may disappear." The spec gives it "an implicit aria-live value of polite". It states no implicit `aria-atomic`, so only the new entry is announced by default.

## The native element

None.

## What the spec asks of authors

No MUST or SHOULD for authors. The definition says new information is added "only to the end of the log, not at arbitrary points."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones. `aria-live` is global, with the implicit value above.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author.

**Sources differ on the name.** WAI-ARIA 1.2 has no "Accessible Name Required" row for `log`. MDN says a log is required to have a name. The Recommendation stands: a name is allowed, not required. Naming a log is sound advice where a page has more than one; its absence is not a finding.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `section`, and the elements that allow any role, such as `div`.
- **Not allowed:** `ul`, `ol`, `article`, `aside`. To announce items added to a list and keep the list, `aria-live` on the `ul` keeps its role (`aria/live-regions.md`).

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On a `section` with an accessible name, the `region` landmark is replaced. On a `div` holding a list, nothing: the list inside keeps its role.

## Where the detail lives

- When a log fits (ARIA23), how to make a live region, and how it fails: `aria/live-regions.md`.
- axe has no rule for whether a log is announced. The manual tests are in `aria/live-regions.md`.
