# Role: heading

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "heading role" and "Fallback values for missing required attributes", https://www.w3.org/TR/wai-aria-1.2/#heading. ARIA in HTML, W3C Recommendation 11 August 2026, row for `h1 to h6`, https://www.w3.org/TR/html-aria/#el-h1-h6
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.47, https://www.w3.org/TR/html-aam/#el-h1-h6
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: heading role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/heading_role
- Related entries: `html/headings.md`, `aria/using-aria.md`, `aria/aria-in-html.md`, `aria/patterns/accordion.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.4.6-headings-and-labels.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="heading"` on an `h1` to `h6` is redundant and never a finding.

## What it is

A heading for a section of the page, with its level given by `aria-level`. WAI-ARIA 1.2: "A heading for a section of the page."

## The native element

`h1` to `h6`. HTML-AAM 3.5.47 maps them to `heading` with `aria-level` set to the number in the tag name. ARIA in HTML allows `role="heading"` on them but marks it "NOT RECOMMENDED".

## When writing the role is justified

When a heading element cannot be used: text inside a component the team does not control, or a legacy page being retrofitted (`aria/using-aria.md`, rule 1; APG, "Structural Roles"). MDN's advice is not to use the role at all where `h1` to `h6` are available.

## What the spec asks of authors

- "To ensure elements with a role of heading are organized into a logical outline, authors MUST use the aria-level attribute to indicate the proper nesting level."
- Naming: required ("Accessible Name Required: True"), from the content or the author. The text inside is the name; an empty heading has none.
- MDN: a name from `aria-label` or `aria-labelledby` replaces the heading's own text in what is exposed, and levels above 6 give uneven results, so keep to 1 through 6 to match HTML.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none.
- Required states and properties: `aria-level`.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**.
- If `aria-level` is missing, WAI-ARIA 1.2 tells browsers to treat it as 2 ("Fallback values for missing required attributes": `heading`, `aria-level`, 2). The heading is still exposed, at a level the author did not choose.
- It stands alone: it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `h1` to `h6` (redundant, "NOT RECOMMENDED").
- **Allowed:** the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `button`; `a` with `href`; an `li` inside a list; `td` and `th` inside a table; `legend`; `caption`; the `summary` of a `details`; a `label` tied to a control; `section`, `header`, and the other landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- On a `div`, `span`, or `p`, nothing of value is lost.
- The other direction matters more. ARIA in HTML allows only `none`, `presentation`, and `tab` on `h1` to `h6`. Any of them replaces the heading. `role="button"` on a heading is not allowed, and where a browser honors it the heading is gone: put a `button` inside the heading instead (`html/headings.md`, `aria/patterns/accordion.md`).

## How it fails in code

- Text styled to look like a heading with neither a heading element nor this role: `wcag/sc-1.3.1-info-and-relationships.md`, definite per that entry (F2). The role with `aria-level` is one fix; the element is the better one.
- `role="heading"` with no `aria-level`: breaks the WAI-ARIA MUST. Browsers fall back to level 2, so the structure is wrong whenever the heading was meant at another level. `wcag/sc-1.3.1-info-and-relationships.md`, likely: the entry does not list this case, and a person has to say which level was meant. axe reports it under `aria-required-attr`, which axe maps to 4.1.2; a heading is not a user interface component, so report it once, under 1.3.1.
- `aria-level` values that contradict the visual hierarchy, such as every heading at level 1: `wcag/sc-1.3.1-info-and-relationships.md`, likely. A skipped level alone is advice (`html/headings.md`).
- An empty `role="heading"`: breaks the naming requirement; advice (`html/headings.md`; axe `empty-heading`, best practice).
- Heading text that does not describe its section: `wcag/sc-2.4.6-headings-and-labels.md`, at that entry's confidence.

## How to check

Search for `role="heading"`. Each has `aria-level`, the level fits the outline of the page, and the element is one the role is allowed on. In the browser's accessibility tree, confirm the heading and its level. axe: `aria-required-attr` fires on a `role="heading"` with no `aria-level` (observed with axe-core 4.14.0 on 2026-11-23); `empty-heading`, `heading-order`, and `page-has-heading-one` are best practice (`knowledge/axe-rules.md`).
