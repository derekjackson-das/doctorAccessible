# Role: menuitem

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "menuitem role", https://www.w3.org/TR/wai-aria-1.2/#menuitem. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `a` with `href`, `button`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Menu and Menubar Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/menubar/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: menuitem role", last modified 12 May 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitem_role
- Related entries: `aria/roles/menu.md`, `aria/roles/menubar.md`, `aria/roles/menuitemcheckbox.md`, `aria/roles/menuitemradio.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

One command in a menu or menubar. WAI-ARIA 1.2: "An option in a set of choices contained by a menu or menubar."

## The native element

None.

## When writing the role is justified

Only inside a `menu` or `menubar`. Outside one it is invalid.

## What the spec asks of authors

- "Authors MAY disable a menu item with the aria-disabled attribute."
- "If the menu item has its aria-haspopup attribute set to true, it indicates that the menu item may be used to launch a sub-level menu, and authors SHOULD display a new sub-level menu when the menu item is activated."
- "In order to identify that they are related widgets, authors MUST ensure that menu items are owned by an element with role menu or menubar."
- "Authors MAY separate menu items into sets by use of a separator or an element with an equivalent role from the native markup language."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `group`, `menu`, `menubar`.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: `aria-disabled`, `aria-expanded`, `aria-haspopup`, `aria-posinset`, `aria-setsize`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**.
- A disabled item uses `aria-disabled="true"` and stays focusable (APG; MDN).
- An item that opens a submenu has `aria-haspopup` (`menu` or `true`) and `aria-expanded`.

**The whole component.** It must be owned by a `menu` or `menubar`, optionally through a `group`. On its own, or inside a plain list, it is not a menu item. See `aria/roles/menu.md` for the whole component.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `a` with `href`, `button`, `img` with alt text, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li` inside a real list, headings, `label`, landmark elements, text inputs, `select`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

The menu's keys (`aria/roles/menu.md`): arrows move between items, Enter activates, Escape closes. An item that opens a dialog conventionally ends its label with an ellipsis (APG; MDN).

## What an explicit role takes away

- On an `a` with `href`, the link role goes: the item is announced as a menu item, not a link.
- On a `button`, the button role goes.

## How it fails in code

- A `menuitem` with no `menu` or `menubar` owning it: invalid; `wcag/sc-4.1.2-name-role-value.md`, likely.
- Disabled items removed from focus inside a menu: APG keeps them focusable so they can be found. Advice.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.

## How to check

Every `menuitem` is inside a `menu` or `menubar` in the accessibility tree. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
