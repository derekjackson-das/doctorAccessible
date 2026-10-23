# HTML: Buttons

- Tier 1: HTML Living Standard, §4.10.6 The button element, accessed 2026-10-23. https://html.spec.whatwg.org/multipage/form-elements.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026, row for `button` (implicit `button`; may take `checkbox`, `switch`, `tab`, and other listed roles, not `heading`). https://www.w3.org/TR/html-aria/
- Tier 2: WAI Tutorials, "Labeling Controls" (updated 13 May 2024), on labeling buttons. https://www.w3.org/WAI/tutorials/forms/labels/
- Tier 2: W3C, "Using ARIA", Discontinued Draft 24 February 2026, rule 3 (`aria/using-aria.md`).
- Related: `html/links.md`, `aria/using-aria.md`, `aria/accessible-name.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.5.8-target-size-minimum.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how to build it. Whether code fails WCAG is decided by the `wcag/` entries named below; report a failure once, under its criterion, at that entry's confidence. A `div` with a click handler is a finding only through the criteria it breaks, usually 2.1.1 and 4.1.2, reported once.

## The native approach

- **`button` for anything that does something on the page:** submits, opens, closes, toggles, deletes.
- **Set `type`.** Inside a form, a `button` with no `type` submits it (the HTML Standard's Auto state makes it a submit button there). Use `type="button"` for anything that is not a submit.
- **The label is the content** (WAI tutorial), so it can hold markup such as a language change. An icon-only button needs a name: visually hidden text or `aria-label` (`aria/accessible-name.md`).
- **State with ARIA on the native element,** such as `aria-pressed` for a toggle or `aria-expanded` for a disclosure (ARIA in HTML).

## What the native approach satisfies by default

A `button` is in the tab order, activates on Enter and Space, and exposes the button role and its name, with no ARIA and no key handling (`wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`).

## Where people go wrong

- A `div` or `span` with only a click handler: not focusable, no role, no name exposed as a button (`wcag/sc-2.1.1-keyboard.md`, F42 and F54; `wcag/sc-4.1.2-name-role-value.md`; report once). Eval 036.
- `role="button"` and `tabindex="0"` on a `span`, but no Enter or Space handling: focusable, not operable (`wcag/sc-2.1.1-keyboard.md`, eval 006). Using ARIA rule 3: a role is a promise of keyboard behavior.
- A link (`a href="#"`) used as a button.
- A `button` inside a form with no `type`, which submits the form by surprise.
- An icon-only button with no name (`wcag/sc-4.1.2-name-role-value.md`, eval 032).

## When ARIA is genuinely needed

- `aria-pressed` (toggle), `aria-expanded` (disclosure, `aria/patterns/accordion.md`), `aria-haspopup`.
- `aria-label` for an icon-only button with no visible text.
- `role="button"` only when the element cannot be a `button`, and then with `tabindex="0"`, Enter and Space handling, and a name (`aria/using-aria.md`).
