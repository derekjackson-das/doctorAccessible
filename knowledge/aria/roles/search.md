# Role: search

- Category: landmark.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "search role", https://www.w3.org/TR/wai-aria-1.2/#search. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `search` and `form`, https://www.w3.org/TR/html-aria/#el-search
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.113, https://www.w3.org/TR/html-aam/#el-search
- Practice (tier 2): ARIA Authoring Practices Guide, "Landmark Regions", search section (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- Reference (tier 3): MDN Web Docs, "ARIA: search role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role
- Related entries: `html/forms.md`, `aria/roles/form.md`, `aria/live-regions.md` (search results), `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.4.1-bypass-blocks.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="search"` on `search` is redundant, never a finding.

## What it is

The landmark around a site or page search: the field, its button, and any options. WAI-ARIA 1.2: "A landmark region that contains a collection of items and objects that, as a whole, combine to create a search facility."

## The native element

`search` (HTML-AAM 3.5.113). ARIA in HTML allows `role="search"` on it but marks it "NOT RECOMMENDED". The `search` element is newer than the role; where support for it is in doubt, `<form role="search">` is the established way, and ARIA in HTML allows `search` on a `form`.

## When writing the role is justified

On the `form` that holds the search, when a `search` element is not used (MDN). Not on the input: the landmark is the container, and an `input type="search"` alone does not make one (MDN).

## What the spec asks of authors

- WAI-ARIA 1.2 places no naming or count requirement on search. Name from author.
- From the form role: "If the purpose of a form is to submit search criteria, authors SHOULD use the search role instead of the generic form role."
- APG and MDN: give each a unique label when there is more than one (such as site search and a search within results), without the word "search" in the label.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required by WAI-ARIA 1.2; APG asks for a unique one when there is more than one.
- It stands alone: it is not one part of a larger component, so it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `search` (redundant, "NOT RECOMMENDED").
- **Allowed:** `form`, `aside`, `section`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `input type=search` and other form fields (ARIA in HTML allows no role on `input type=search` but `searchbox`); `nav`, `header`, `footer`, `article`, `main`; `ul`, `ol`, `li`; `h1` to `h6`; `a` with `href`; `button`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- ARIA in HTML allows `form`, `group`, `none`, `presentation`, or `region` on a `search` element. Each replaces `search`.
- `role="search"` on a `form` replaces `form`, which is what is wanted for a search form. On an `input`, it is not allowed at all: ARIA in HTML allows no role on `input type=search` other than `searchbox`. Where a browser honors it, the field stops being exposed as a field: likely 4.1.2 (`wcag/sc-4.1.2-name-role-value.md`).

## How it fails in code

- `role="search"` on the input itself: the field is no longer a text field to assistive technology. 4.1.2, likely per that entry.
- A search form with no search landmark: advice, not a failure.
- Two unnamed search landmarks: advice (axe `landmark-unique`).

## How to check

Is the site search inside one `search` element or `role="search"` container, with the field, label, and button all inside it? Is the role on the container, not the input? In the accessibility tree, the field is still a `searchbox` or `textbox`.
