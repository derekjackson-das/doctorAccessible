# Role: menu

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "menu role", https://www.w3.org/TR/wai-aria-1.2/#menu. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `ul`, `ol`, `menu`, `nav`, and `select` rendered as a drop-down, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `menu` (3.5.91), which maps the HTML `menu` element to `list`, not to this role, https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Menu and Menubar Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/menubar/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: menu role", last modified 8 October 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role
- Related entries: `aria/roles/menubar.md`, `aria/roles/menuitem.md`, `aria/roles/button.md` (menu buttons), `aria/roles/navigation.md`, `html/links.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.3-focus-order.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A list of commands or choices, like an application's menu, that the user moves through with the arrow keys. WAI-ARIA 1.2: "A type of widget that offers a list of choices to the user."

## The native element

None. The HTML `menu` element is a list, not this role (HTML-AAM 3.5.91). For a set of page or site links, the native answer is `nav` with a list of links (MDN).

## When writing the role is justified

For an application-style menu of actions, opened by a menu button or from a menubar, with the full keyboard model below. Not for site navigation: MDN says to use `nav` or a list of links. APG does publish a navigation menubar example, so this is MDN's guidance, not APG's; take the stricter reading (principle 13): a menu promises keys most link lists do not have.

## What the spec asks of authors

- "To be keyboard accessible, authors SHOULD manage focus of descendants for all instances of this role, as described in Managing Focus."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `group → menuitem`, `group → menuitemradio`, `group → menuitemcheckbox`, `menuitem`, `menuitemcheckbox`, `menuitemradio`.
- Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- `aria-orientation` defaults to `vertical`.
- A menu opened by a button: the button has `aria-haspopup` (`menu` or `true`) and `aria-expanded`, and may have `aria-controls` (APG, Menu Button Pattern).

**The whole component.** A menu must own `menuitem`, `menuitemcheckbox`, or `menuitemradio` elements, directly or inside a `group`, with `separator` allowed between them; it needs the keyboard below; and it is opened by a menu button or a parent `menuitem`. A `role="menu"` around plain links with no menu items and no arrow keys is a broken menu.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `ul`, `ol`, `menu`, `nav` (which then loses its navigation landmark), `select` rendered as a drop-down, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li`, headings, `button`, `a`, `main`, `header`, `footer`, `aside`, `form`, form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Menu and Menubar Pattern. When a menu opens, focus goes to its first item; Tab does not move into a menu, so script must. Down and Up move between items, optionally wrapping; Home and End go to the first and last. Enter activates an item and closes the menu, or opens a submenu and focuses its first item; Space may do the same (optional) and toggles a `menuitemcheckbox` without closing. Right opens a submenu; Left closes it and returns to the parent item. Escape closes the menu and returns focus to the button or item that opened it. A typed character may move to the next item that starts with it (optional). Tab and Shift+Tab leave the menu and close it. Focus is managed with roving `tabindex` or `aria-activedescendant` on the menu.

## What an explicit role takes away

- On a `ul` or `ol`, the list goes, and the `li` elements must take `menuitem` (or `none` with items inside).
- On a `nav`, the navigation landmark goes (`aria/roles/navigation.md`).
- Its items stop being links to assistive technology even when they are `a` elements with `role="menuitem"`; the browser's link behaviors (open in new tab) may still work, but are no longer announced.

## How it fails in code

- `role="menu"` on site navigation without the menu keyboard: the role promises arrow keys and menu behavior the links do not have. `wcag/sc-4.1.2-name-role-value.md`, likely.
- The role and `tabindex="0"` but no key handler, so the menu can be focused but not operated: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F54).
- A menu whose items are not `menuitem` roles, or that owns links and buttons directly: `wcag/sc-4.1.2-name-role-value.md`, likely.
- Focus not moved into the menu when it opens, or not returned to the button when it closes: `wcag/sc-2.4.3-focus-order.md`, at that entry's confidence.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.

## How to check

For each `role="menu"`: is it an application menu or site navigation? Does it own menu items? Do the arrow keys, Escape, Enter, and Tab behave as above? In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
