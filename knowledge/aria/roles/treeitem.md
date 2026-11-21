# Role: treeitem

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "treeitem role", https://www.w3.org/TR/wai-aria-1.2/#treeitem. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `a` with `href`, `button`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Tree View Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/treeview/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: treeitem role", last modified 29 September 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role
- Related entries: `aria/roles/tree.md`, `aria/roles/treegrid.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

One item in a tree. WAI-ARIA 1.2: "An option item of a tree."

## The native element

None.

## When writing the role is justified

Only inside a `tree`, or a `group` inside one.

## What the spec asks of authors

- "Authors MUST ensure elements with role treeitem are contained in, or owned by, an element with the role group or tree."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `group`, `tree`.
- Required owned elements: none.
- Required states and properties: `aria-selected` (inherited from its superclass).
- Supported states and properties: `aria-expanded`, `aria-haspopup`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**.
- **A conflict between sources.** WAI-ARIA 1.2 lists `aria-selected` as required on `treeitem` (inherited from `option`). APG and MDN say items that cannot be selected must have neither `aria-selected` nor `aria-checked`. Principle 13 says take the stricter reading: in a tree where items can be selected, set `aria-selected` (`true` or `false`) on every item; in a tree where nothing is selectable, there is no selection to expose, so name the conflict and leave it off, as APG does. Manual review, never a finding on its own.
- Parent items: `aria-expanded`; end items: none.

**The whole component.** It must be contained in or owned by a `tree`, or a `group` within one. A parent item owns a `group` of its children. See `aria/roles/tree.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `a` with `href`, `button`, `img` with alt text, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li` inside a real list, headings, landmark elements, form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

The tree's keys (`aria/roles/tree.md`).

## What an explicit role takes away

- On an `a` with `href`, the link role goes: the item is announced as a tree item, not a link.

## How it fails in code

- A `treeitem` with no `tree` around it: invalid; `wcag/sc-4.1.2-name-role-value.md`, likely.
- `aria-expanded` on an end item, so it is announced as collapsed: `wcag/sc-4.1.2-name-role-value.md`, likely.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.

## How to check

Every `treeitem` is inside a `tree`; parents expose `aria-expanded`. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
