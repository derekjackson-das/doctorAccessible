# Role: switch

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "switch role", https://www.w3.org/TR/wai-aria-1.2/#switch. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `button`, `input type=checkbox`, `a` with `href`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Switch Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/switch/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: switch role", last modified 12 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/switch_role
- Related entries: `aria/roles/checkbox.md`, `aria/roles/button.md` (toggle buttons), `html/buttons.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

An on/off control. Functionally a checkbox whose states read as on and off. WAI-ARIA 1.2: "A type of checkbox that represents on/off values, as opposed to checked/unchecked values."

## The native element

None. The closest are `input type=checkbox` and a toggle `button` with `aria-pressed`. APG says switch, checkbox, and toggle button are often interchangeable; choose by what the visual and the wording suggest.

## When writing the role is justified

When the control is visibly an on/off switch. It can go on a `button` or on an `input type=checkbox`; on a checkbox, use the native `checked` state, not `aria-checked` (APG).

## What the spec asks of authors

- WAI-ARIA 1.2 places no author requirement on this role beyond its characteristics, below.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: `aria-checked`.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-haspopup` as deprecated on this role.
- Naming: name from contents or author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-checked` takes `true` (on) or `false` (off). `mixed` is not supported and is treated as `false` (MDN).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `button`, `input type=checkbox`, `a` with `href`, `img` with alt text, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `input type=radio`, text inputs, `select`, `li`, headings, `label`, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Switch Pattern: Space toggles it; Enter may too (optional). The label must not change with the state ("Lights" stays "Lights"), or the state is said twice.

## What an explicit role takes away

- On a `button`, the button role goes and `aria-pressed` no longer applies; use `aria-checked`.
- On `input type=checkbox`, the checkbox role becomes switch; the native `checked` state still drives it.
- Children are presentational.

## How it fails in code

- The role on a `div` or `span` with no `tabindex`, so the control cannot be reached by keyboard: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F42). Report once, as that entry says, not again under 4.1.2.
- The role and `tabindex="0"` but no key handler, so the control can be focused but not operated: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F54).
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- No `aria-checked`, or not updated: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- A label that flips between "On" and "Off" as well as the state: manual review under `wcag/sc-4.1.2-name-role-value.md`.

## How to check

Each `role="switch"`: focusable, Space toggles, `aria-checked` changes, the label stays the same. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
