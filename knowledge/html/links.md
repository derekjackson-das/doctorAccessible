# HTML: Links

- Tier 1: HTML Living Standard, §4.5.1 The a element, and §4.6 Links, accessed 2026-10-23. https://html.spec.whatwg.org/multipage/text-level-semantics.html , https://html.spec.whatwg.org/multipage/links.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026, rows for `a` with and without `href`. https://www.w3.org/TR/html-aria/
- Tier 2: WAI Tutorials, "Functional Images" (updated 12 April 2017), for image links. https://www.w3.org/WAI/tutorials/images/functional/
- Related: `content/link-text.md` (what links should say), `html/buttons.md`, `wcag/sc-2.4.4-link-purpose-in-context.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how to mark links up; `content/link-text.md` says what they should say. Whether code fails WCAG is decided by the `wcag/` entries named below; report a failure once, under its criterion, at that entry's confidence.

## The native approach

- **`a` with an `href` is a link.** The HTML Standard: with `href`, it represents a hyperlink labeled by its contents; without one, it is only a placeholder, and the `target`, `download`, and similar attributes must be left off.
- **A link goes somewhere; a button does something.** Navigating to a page, a file, or a place in the page is a link. Submitting, opening, toggling, or deleting is a button (`html/buttons.md`).
- **The link's text is its name.** For an image link, the image's `alt` is (`html/images.md`).
- **In-page links** point at an `id` with `href="#id"`.

## What the native approach satisfies by default

A real link is in the tab order, opens with Enter, and exposes the link role and its name, with no script and no ARIA (`wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`).

## Where people go wrong

- A `div` or `span` with a click handler that navigates: not focusable and no role (`wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`; report once).
- `a` with no `href` acting as a control: not a link and not focusable (HTML Standard), so `wcag/sc-2.1.1-keyboard.md` (F42) and `wcag/sc-4.1.2-name-role-value.md`, definite, reported once. `href="#"` used for an action is focusable and named, so it is advice, not a finding.
- Generic text ("click here") with no context (`wcag/sc-2.4.4-link-purpose-in-context.md`, eval 009).
- `aria-expanded` on a link that navigates; Roselli advises against it (`aria/patterns/accordion.md`).

## When ARIA is genuinely needed

- `aria-current="page"` on the link to the current page in a navigation menu.
- `aria-label` or visually hidden text to add context, keeping the visible words in the name (`wcag/sc-2.5.3-label-in-name.md`).
- `role="link"` with `aria-disabled="true"` on an `a` without `href`, the one case ARIA in HTML gives for a disabled link.
