# Role: list

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "list role", https://www.w3.org/TR/wai-aria-1.2/#list. ARIA in HTML, W3C Recommendation 11 August 2026, section 3.2 "Avoid specifying redundant roles" and the rows for `ul`, `ol`, `menu`, `li`, and `dl`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.144 (`ul`), 3.5.97 (`ol`), 3.5.91 (`menu`), 3.5.36 (`dl`), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: list role", last modified 12 May 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/list_role
- Related entries: `aria/roles/listitem.md`, `aria/roles/listbox.md`, `aria/roles/menu.md`, `aria/roles/presentation.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="list"` on a `ul`, `ol`, or `menu` is redundant and never a finding; it is also the one redundant role ARIA in HTML gives a reason for (below).

## What it is

A container of list items. WAI-ARIA 1.2: "A section containing listitem elements." It is static content. A list the user picks from is a `listbox` (`aria/roles/listbox.md`).

## The native element

`ul`, `ol`, and `menu` (HTML-AAM 3.5.144, 3.5.97, 3.5.91). ARIA in HTML allows `role="list"` on each but marks it "NOT RECOMMENDED".

The sources disagree about `dl`. HTML-AAM 3.5.36 maps it to the `list` role, with an editorial note that the value may change. ARIA in HTML says `dl` has no corresponding role. ARIA in HTML is tier 1, so do not count on a `dl` being exposed as a list.

## When writing the role is justified

- **A list whose markers were removed with CSS.** ARIA in HTML, section 3.2: "some user agents suppress a list's implicit ARIA semantics if the list markers are removed from the visual presentation of the list items." It goes on to say that in that situation, where the role needs to be exposed, authors can add it. Its example puts `role="list"` on the `ul`. MDN's `listitem` page says to add `role="listitem"` for the same problem; ARIA in HTML is tier 1, so the role goes on the list.
- A legacy page being retrofitted, where `div` elements cannot be replaced (`aria/using-aria.md`, rule 1).

MDN notes the role does not tell ordered from unordered lists; `ol` does.

## What the spec asks of authors

WAI-ARIA 1.2 places no SHOULD or MUST on authors in the role's text. It says: "Lists contain children whose role is listitem." The requirement comes from the characteristics table (below).

Naming: allowed, from the author; not required.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `listitem`.
- Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.

**The whole component.** A `list` owns `listitem` elements (`aria/roles/listitem.md`). On `div` elements both roles must be written. MDN's `listitem` page says a list may hold `group` elements that hold the items; WAI-ARIA 1.2 lists only `listitem` as the owned element, so keep the items directly in the list.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `ul`, `ol`, `menu` (redundant, "NOT RECOMMENDED", with the exception above).
- **Allowed:** `dl`, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `nav`, `section`, `main`, and the other landmark elements; an `li` inside a list; `button`; `a` with `href`; `h1` to `h6`; `fieldset`.

ARIA in HTML also says authors SHOULD NOT use the deprecated `directory` role on a list.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- On a `ul`, `ol`, or `menu`, ARIA in HTML allows `group`, `listbox`, `menu`, `menubar`, `none`, `presentation`, `radiogroup`, `tablist`, `toolbar`, and `tree`. Each replaces the list. The `li` children then stop being list items: ARIA in HTML gives an `li` the `listitem` role only while its parent is exposed as a list, and `generic` otherwise.
- `role="menu"` on the `ul` of a site navigation is the common case: `aria/roles/menu.md`.

## How it fails in code

- A list shown as a list but built from `div` or `br` elements with no roles: `wcag/sc-1.3.1-info-and-relationships.md`, definite per that entry. `ul` or `ol` is the fix; this role with `listitem` is the retrofit.
- `role="list"` whose children are not list items: the list is exposed empty or not at all. `wcag/sc-1.3.1-info-and-relationships.md`, at that entry's confidence for items outside a list.
- A role on a `ul` that replaces the list, with the `li` elements left as they were: `wcag/sc-1.3.1-info-and-relationships.md`, likely; check what the new role needs its children to be.
- `role="list"` on a real list: never a finding.

## How to check

Search for `role="list"`. On a `div`, each child is a `listitem`. On a `ul` or `ol`, it is redundant: fine. Then look at every `ul` and `ol` that carries another role and ask what became of its items. In the browser's accessibility tree, confirm a list with the expected number of items. axe: `aria-required-children` fires on a `role="list"` with no `listitem` (mapped to 1.3.1; observed with axe-core 4.14.0 on 2026-11-23); `list` and `listitem` check the native elements (`knowledge/axe-rules.md`).
