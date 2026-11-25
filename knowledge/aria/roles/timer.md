# Role: timer

- Category: live region.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "timer role", https://www.w3.org/TR/wai-aria-1.2/#timer. ARIA in HTML, W3C Recommendation 11 August 2026, section 4 (no row names this role), https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): none. The ARIA Authoring Practices Guide has no pattern for this role.
- Reference (tier 3): MDN Web Docs, "ARIA: timer role", last modified 23 June 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/timer_role
- Related entries: `aria/live-regions.md`, `aria/roles/status.md`, `aria/roles/marquee.md`
- WCAG: `wcag/sc-2.2.1-timing-adjustable.md`, `wcag/sc-4.1.3-status-messages.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: when a live region is the right tool, how to make one, how it fails, and the manual tests are in `aria/live-regions.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

The role labels a counter; it does nothing about a time limit. A limit on the user's time is judged under `wcag/sc-2.2.1-timing-adjustable.md`, whatever shows the countdown.

## What it is

A counter of time elapsed or remaining. WAI-ARIA 1.2: "A type of live region containing a numerical counter which indicates an amount of elapsed time from a start point, or the time remaining until an end point." It is a subclass of `status`, but the spec gives it "an implicit aria-live value of off", so its changes are not announced by default.

## The native element

None.

## What the spec asks of authors

- "authors SHOULD update the text contents at fixed intervals, except when the timer is paused or reaches an end-point."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones. `aria-live` is global, with the implicit value above.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author. WAI-ARIA 1.2 has no "Accessible Name Required" row for this role; MDN says a name is not required.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** only the elements that allow any role, such as `div`, `span`, `p`, and `time`. No row names `timer`.
- **Not allowed:** `section`, `article`, `aside`, `ul`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

Nothing native on a `div` or `span`. On an `output`, `timer` replaces `status`, and the region goes from polite to off.

## Where the detail lives

- `aria/live-regions.md` records two practitioner sources advising against `marquee` and `timer`, and treats using either to announce something as advice. To announce a point in a countdown, such as time nearly up, use a `status` or `alert` region as that entry describes.
- Time limits: `wcag/sc-2.2.1-timing-adjustable.md`.
