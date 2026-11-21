# Role: tree

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "tree role", https://www.w3.org/TR/wai-aria-1.2/#tree. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `ul`, `ol`, and `menu`, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Tree View Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/treeview/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: tree role", last modified 29 September 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role
- Related entries: `aria/roles/treeitem.md`, `aria/roles/treegrid.md`, `html/landmarks.md` (nested navigation lists)
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A hierarchical list the user can expand and collapse, such as a file browser. WAI-ARIA 1.2: "A widget that allows the user to select one or more items from a hierarchically organized collection."

## The native element

None. Nested lists of links, or `details` and `summary`, often meet the same need with no ARIA (MDN advises considering alternatives).

## When writing the role is justified

For a real tree of selectable items with the full keyboard below. Not for a site's nested navigation, which is better as nested lists of links.

## What the spec asks of authors

- "To be keyboard accessible, authors SHOULD manage focus of descendants for all instances of this role, as described in Managing Focus."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `group → treeitem`, `treeitem`.
- Required states and properties: none.
- Supported states and properties: `aria-errormessage`, `aria-invalid`, `aria-multiselectable`, `aria-required`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-haspopup` as deprecated on this role.
- Naming: name from author; **required**.
- `aria-multiselectable="true"` for multiple selection; `aria-orientation` defaults to `vertical`.

**The whole component.** It must own `treeitem` elements; each parent item owns a `group` holding its children and has `aria-expanded`; end items have no `aria-expanded`. Selection uses `aria-selected` or `aria-checked`, not both. With lazy loading, every item carries `aria-level`, `aria-setsize`, and `aria-posinset` (APG).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `ul`, `ol`, `menu`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `nav` and the other landmark elements, `li`, headings, `button`, form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Tree View Pattern (vertical tree): on focus, the selected node or the first. Right opens a closed node, or moves into an open one; Left closes an open node, or moves to the parent. Down and Up move between visible nodes; Home and End go to the first and last. Enter performs the node's default action. Type-ahead is recommended. `*` expands all siblings (optional). Multi-select: Space toggles, Shift with the arrows extends, Control+A selects all (several optional). Arrow keys, not Tab, move within the tree; MDN warns this is unusual on the web and to consider alternatives first.

## What an explicit role takes away

- On a `ul` or `ol`, the list goes; the `li` elements must take `treeitem` (or `none`, with the item inside), and nested lists `group`.

## How it fails in code

- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- No arrow-key navigation, with items out of the tab order: `wcag/sc-2.1.1-keyboard.md`, definite per that entry.
- Parent items without `aria-expanded`, or with it not updated: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- A `tree` used for site navigation links: advice; nested lists of links are simpler and expected.

## How to check

The tree has a name; arrows move, open, and close; parents expose `aria-expanded`. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
