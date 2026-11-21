# Role: menubar

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "menubar role", https://www.w3.org/TR/wai-aria-1.2/#menubar. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `ul`, `ol`, `menu`, and `nav`, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Menu and Menubar Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/menubar/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: menubar role", last modified 27 August 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menubar_role
- Related entries: `aria/roles/menu.md`, `aria/roles/menuitem.md`, `aria/roles/toolbar.md`, `aria/roles/navigation.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A menu that stays on screen, usually across the top, like an application's menu bar. WAI-ARIA 1.2: "A presentation of menu that usually remains visible and is usually presented horizontally."

## The native element

None.

## When writing the role is justified

For an application-style menu bar of commands. Same caution as `menu` for site navigation; WAI-ARIA 1.2 says its interaction SHOULD match a desktop menu bar.

## What the spec asks of authors

- "Authors SHOULD ensure that menubar interaction is similar to the typical menu bar interaction in a desktop graphical user interface."
- "To be keyboard accessible, authors SHOULD manage focus of descendants for all instances of this role, as described in Managing Focus."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `group → menuitem`, `group → menuitemradio`, `group → menuitemcheckbox`, `menuitem`, `menuitemcheckbox`, `menuitemradio`.
- Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- `aria-orientation` defaults to `horizontal`.

**The whole component.** It owns `menuitem` elements (or the checkbox and radio item roles, or `group` and `separator`); items that open submenus have `aria-haspopup` and `aria-expanded` and own a `menu`. It takes one tab stop, with the first item at `tabindex="0"` (APG).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `ul`, `ol`, `menu`, `nav` (which then loses its navigation landmark), and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li`, headings, `button`, `a`, landmark elements other than `nav`, form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Menu and Menubar Pattern. When a menu opens, focus goes to its first item; Tab does not move into a menu, so script must. Down and Up move between items, optionally wrapping; Home and End go to the first and last. Enter activates an item and closes the menu, or opens a submenu and focuses its first item; Space may do the same (optional) and toggles a `menuitemcheckbox` without closing. Right opens a submenu; Left closes it and returns to the parent item. Escape closes the menu and returns focus to the button or item that opened it. A typed character may move to the next item that starts with it (optional). Tab and Shift+Tab leave the menu and close it. Focus is managed with roving `tabindex` or `aria-activedescendant` on the menu. In a horizontal menubar, Right and Left move between top-level items and Down opens a submenu; in a vertical one the arrows swap.

## What an explicit role takes away

- On a `ul`, `ol`, or `nav`, as for `menu`.

## How it fails in code

- A menubar with no arrow keys between items: `wcag/sc-4.1.2-name-role-value.md`, likely; `wcag/sc-2.1.1-keyboard.md` if items cannot be reached at all.
- Items that both navigate and open a submenu: APG says to avoid it. Advice.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.

## How to check

One tab stop into the bar; arrows move between items; Down opens submenus; Escape closes them. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
