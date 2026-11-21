# Role: menuitemcheckbox

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "menuitemcheckbox role", https://www.w3.org/TR/wai-aria-1.2/#menuitemcheckbox. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `input type=checkbox`, `a` with `href`, `button`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Menu and Menubar Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/menubar/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: menuitemcheckbox role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role
- Related entries: `aria/roles/menu.md`, `aria/roles/menuitem.md`, `aria/roles/checkbox.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A menu item that is checked or unchecked, such as "Show ruler". WAI-ARIA 1.2: "A menuitem with a checkable state whose possible values are true, false, or mixed."

## The native element

None.

## When writing the role is justified

Only inside a `menu` or `menubar`.

## What the spec asks of authors

- "In order to identify that they are related widgets, authors MUST ensure that menu item checkboxes are owned by an element with role menu or menubar."
- "Authors MAY separate menu items into sets by use of a separator or an element with an equivalent role from the native markup language."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `group`, `menu`, `menubar`.
- Required owned elements: none.
- Required states and properties: `aria-checked`.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-checked` takes `true`, `false`, or `mixed`. On an `input type=checkbox` use the native `checked` instead (ARIA in HTML).

**The whole component.** It must be owned by a `menu` or `menubar`, optionally through a `group`, and expose `aria-checked`. See `aria/roles/menu.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `input type=checkbox`, `a` with `href`, `button`, `img` with alt text, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li` inside a real list, headings, `label`, landmark elements, text inputs, `select`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

The menu's keys, plus: Space toggles the item without closing the menu (APG, optional); Enter toggles and closes (MDN).

## What an explicit role takes away

- As for `menuitem`.
- Children are presentational.

## How it fails in code

- No `aria-checked`, or not updated: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- Outside a `menu` or `menubar`: invalid; `wcag/sc-4.1.2-name-role-value.md`, likely.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.

## How to check

Inside a menu; `aria-checked` present and changing. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
