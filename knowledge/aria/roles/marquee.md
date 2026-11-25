# Role: marquee

- Category: live region.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "marquee role", https://www.w3.org/TR/wai-aria-1.2/#marquee. ARIA in HTML, W3C Recommendation 11 August 2026, row for `section`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): none. The ARIA Authoring Practices Guide has no pattern for this role.
- Reference (tier 3): MDN Web Docs, "ARIA: marquee role", last modified 23 June 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/marquee_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): awareness only. The draft no longer lists a name as required for this role.
- Related entries: `aria/live-regions.md`, `aria/roles/log.md`, `aria/roles/timer.md`
- WCAG: `wcag/sc-2.2.2-pause-stop-hide.md`, `wcag/sc-4.1.3-status-messages.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: when a live region is the right tool, how to make one, how it fails, and the manual tests are in `aria/live-regions.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

The role is not the obsolete `marquee` element, and it moves nothing. Content that scrolls or updates by itself is judged under `wcag/sc-2.2.2-pause-stop-hide.md`, whatever its role.

## What it is

A region of non-essential content that changes often, such as a stock ticker. WAI-ARIA 1.2: "A type of live region where non-essential information changes frequently." The spec gives it "an implicit aria-live value of off", so its changes are not announced by default.

## The native element

None. HTML-AAM maps no element to this role and has no row for the obsolete `marquee` element.

## What the spec asks of authors

No MUST or SHOULD for authors beyond the name.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones. `aria-live` is global, with the implicit value above.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; **required** ("Accessible Name Required: True").

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `section`, and the elements that allow any role, such as `div`.
- **Not allowed:** `article`, `aside`, `ul`, `ol`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On a `section` with an accessible name, the `region` landmark is replaced.

## Where the detail lives

- `aria/live-regions.md` records two practitioner sources advising against `marquee` and `timer`, and treats using either to announce something as advice: their changes are off by default.
- Moving or auto-updating content: `wcag/sc-2.2.2-pause-stop-hide.md`. axe's `marquee` rule is about the element, not this role (`knowledge/axe-rules.md`).
