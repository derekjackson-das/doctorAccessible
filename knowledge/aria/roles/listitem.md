# Role: listitem

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "listitem role", https://www.w3.org/TR/wai-aria-1.2/#listitem. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `li` and `dt`, https://www.w3.org/TR/html-aria/#el-li
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.85, https://www.w3.org/TR/html-aam/#el-li
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: listitem role", last modified 27 August 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listitem_role
- Related entries: `aria/roles/list.md`, `aria/roles/presentation.md`, `aria/roles/option.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="listitem"` on an `li` inside a list is redundant and never a finding.

## What it is

One item in a list. WAI-ARIA 1.2: "A single item in a list or directory."

## The native element

An `li` whose parent is exposed as a list: `ul`, `ol`, or `menu`. HTML-AAM 3.5.85 maps it to `listitem`, with `aria-setsize` and `aria-posinset` worked out from the list. Its comment adds that an `li` outside such a list, or in a list no longer exposed as one, is exposed as `generic`.

## When writing the role is justified

Only with `role="list"` on the parent, on a page where `ul`, `ol`, and `li` cannot be used (`aria/roles/list.md`). For a list whose markers were removed with CSS, the role goes on the list, not the items.

## What the spec asks of authors

- "Authors MUST ensure elements whose role is listitem are contained in, or owned by, an element whose role is list."
- Naming: allowed, from the author; not required.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `list` (or `directory`, which WAI-ARIA 1.2 deprecates).
- Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-level`, `aria-posinset`, `aria-setsize`. The last two are for lists whose items are not all in the page.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.

**The whole component.** It must sit in, or be owned by, a `list` (`aria/roles/list.md`). A `listitem` with no list around it is not valid.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `li` inside a list (redundant, "NOT RECOMMENDED"). While its parent is exposed as a list, an `li` allows no other role.
- **Allowed:** `dt`, an `li` whose parent no longer exposes a list role, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `dd`; `a` with `href`; `button`; `h1` to `h6`; `tr`, `td`, and `th` inside a table.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- Another role on an `li` inside a real list, such as `role="option"` or `role="tab"`, is not allowed while the parent is a list. Change the parent's role first; the `li` elements are then free to take the roles the parent requires.
- `role="presentation"` on the parent list removes the items' roles too (`aria/roles/presentation.md`).

## How it fails in code

- A `listitem` with no `list` parent: breaks the WAI-ARIA MUST, and the item is not part of any list. `wcag/sc-1.3.1-info-and-relationships.md`, definite per that entry for list items outside a list.
- A `ul` or `ol` given another role, with `li` children left alone: see `aria/roles/list.md`.

## How to check

Every `role="listitem"` has a parent with `role="list"`, or is owned by one through `aria-owns`. In the browser's accessibility tree, confirm each item sits under a list. axe: `aria-required-parent` fires on a `listitem` outside a list (mapped to 1.3.1; observed with axe-core 4.14.0 on 2026-11-23); `listitem` checks `li` elements (`knowledge/axe-rules.md`).
