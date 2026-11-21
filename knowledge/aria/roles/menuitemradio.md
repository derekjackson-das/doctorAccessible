# Role: menuitemradio

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "menuitemradio role", https://www.w3.org/TR/wai-aria-1.2/#menuitemradio. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `input type=radio`, `a` with `href`, `button`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Menu and Menubar Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/menubar/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: menuitemradio role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role
- Related entries: `aria/roles/menu.md`, `aria/roles/menuitem.md`, `aria/roles/radio.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A menu item that is one of a set where only one can be chosen, such as a text size. WAI-ARIA 1.2: "A checkable menuitem in a set of elements with the same role, only one of which can be checked at a time."

## The native element

None.

## When writing the role is justified

Only inside a `menu` or `menubar`, in a set.

## What the spec asks of authors

- "Authors SHOULD enforce that only one menuitemradio in a group can be checked at the same time."
- "In order to identify that they are related widgets, authors MUST ensure that menu item radios are owned by an element with role menu or menubar, or by a role group which itself is owned by an element with role menu or menubar."
- "If a menu or menubar contains more than one group of menuitemradio elements, or if the menu contains one group and other, unrelated menu items, authors SHOULD contain each set of related menuitemradio elements in an element using the group role."
- "Authors MAY also delimit the group from other menu items with an element using the separator role, or an element with an equivalent role from the native markup language."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `group`, `menu`, `menubar`.
- Required owned elements: none.
- Required states and properties: `aria-checked` (inherited from its superclass).
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-checked` takes `true` or `false` (no `mixed`). On an `input type=radio` use the native `checked` instead (ARIA in HTML).

**The whole component.** It must be owned by a `menu` or `menubar`, or by a `group` inside one. When a menu holds more than one set, or a set plus other items, each set goes in its own `group` (WAI-ARIA 1.2, below); a `separator` may divide them. Only one in a set is checked.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `input type=radio`, `a` with `href`, `button`, `img` with alt text, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li` inside a real list, headings, `label`, landmark elements, text inputs, `select`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

The menu's keys, plus: Space checks the item and unchecks the others in its set without closing (APG, optional); Enter does the same and closes (MDN).

## What an explicit role takes away

- As for `menuitem`.
- Children are presentational.

## How it fails in code

- No `aria-checked`, or more than one checked in a set: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a missing state; manual review for two checked.
- Two sets in one menu with no `group` around each: breaks a WAI-ARIA SHOULD; advice unless the sets cannot be told apart.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.

## How to check

Inside a menu; each set grouped; one checked per set. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
