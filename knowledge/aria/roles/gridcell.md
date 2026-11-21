# Role: gridcell

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "gridcell role", https://www.w3.org/TR/wai-aria-1.2/#gridcell. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `td`, `th`, `button`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows for `td` and `th` in a grid or treegrid (3.5.130, 3.5.135), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Grid (Interactive Tabular Data and Layout Containers) Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/grid/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: gridcell role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/gridcell_role
- Related entries: `aria/roles/grid.md`, `aria/roles/treegrid.md`, `html/tables.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A cell in a grid or treegrid that is not a header. WAI-ARIA 1.2: "A cell in a grid or treegrid."

## The native element

A `td` inside a `table` with the `grid` or `treegrid` role (HTML-AAM).

## When writing the role is justified

Only inside a `row` in a `grid` or `treegrid`. MDN notes assistive technology support for the grid cell roles is poor, and recommends native table markup where possible.

## What the spec asks of authors

- "If an author intends a gridcell to have a row header, column header, or both, and if the relevant headers cannot be determined from the DOM structure, authors SHOULD explicitly indicate which header cells are relevant to the gridcell by applying aria-describedby on the gridcell and referencing elements with role rowheader or columnheader."
- "In a treegrid, authors MAY define a gridcell as expandable by using the aria-expanded attribute."
- "Authors MUST ensure elements with role gridcell are contained in, or owned by, an element with the role row."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `row`.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: `aria-disabled`, `aria-errormessage`, `aria-expanded`, `aria-haspopup`, `aria-invalid`, `aria-readonly`, `aria-required`, `aria-selected`.
- Prohibited states and properties: none.
- Naming: name from contents or author; not required.
- `aria-selected` when cells can be selected; `aria-readonly` per cell; `aria-colindex` and `aria-rowindex` when not every column or row is in the page.
- If its headers cannot be worked out from the structure, WAI-ARIA 1.2 asks for `aria-describedby` pointing at them (below).

**The whole component.** It must be contained in or owned by a `row` (WAI-ARIA 1.2 MUST), inside a `grid` or `treegrid`. See `aria/roles/grid.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `td` in a grid or treegrid (redundant).
- **Allowed:** `td` and `th` in a grid or treegrid, `button`, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `td` or `th` in a plain `table` (they take `cell` and the header roles), `li`, headings, landmark elements, form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

The grid's keys (`aria/roles/grid.md`).

## What an explicit role takes away

- On a `button`, the button role goes; the cell is now the focus target and its action must be scripted.

## How it fails in code

- A `gridcell` outside a `row`: invalid; `wcag/sc-4.1.2-name-role-value.md`, likely.
- Cells whose headers cannot be determined: `wcag/sc-1.3.1-info-and-relationships.md`, at that entry's confidence.

## How to check

Every `gridcell` is in a `row` in a `grid` or `treegrid`. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
