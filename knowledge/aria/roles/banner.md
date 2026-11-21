# Role: banner

- Category: landmark.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "banner role", https://www.w3.org/TR/wai-aria-1.2/#banner. ARIA in HTML, W3C Recommendation 11 August 2026, row for `header`, https://www.w3.org/TR/html-aria/#el-header
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.49 and 3.5.50 for `header`, https://www.w3.org/TR/html-aam/#el-header-ancestorbody
- Practice (tier 2): ARIA Authoring Practices Guide, "Landmark Regions", banner section (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- Reference (tier 3): MDN Web Docs, "ARIA: banner role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/banner_role
- Related entries: `html/landmarks.md`, `aria/roles/contentinfo.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.4.1-bypass-blocks.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="banner"` on a page-level `header` is redundant, never a finding.

## What it is

The landmark for the site-wide content at the top of a page: the logo or site name, site search, often the main navigation. WAI-ARIA 1.2: "A landmark that contains mostly site-oriented content, rather than page-specific content."

## The native element

`header`, but only when it is scoped to the `body`. HTML-AAM maps a `header` to `banner` when it is not inside `article`, `aside`, `main`, `nav`, or `section` (or an element with one of their roles). Inside those, it maps to a different role (`sectionheader` in HTML-AAM; `generic` in ARIA in HTML) and is not a landmark. ARIA in HTML allows `role="banner"` on a body-scoped `header` but marks it "NOT RECOMMENDED".

## When writing the role is justified

When a `header` cannot be used, such as on a legacy page being retrofitted (APG, "Landmark Regions"; `aria/using-aria.md`, rule 1). MDN adds: prefer `header`, and add the role by script only if the HTML cannot be changed.

## What the spec asks of authors

- "Within any document or application, the author SHOULD mark no more than one element with the banner role." A nested document or application, such as an `iframe`, may have its own.
- Naming: name from author; not required. APG: when a page has more than one banner, give each a unique label, and do not put the word "banner" in it.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required by WAI-ARIA 1.2; APG asks for a unique one when there is more than one.
- It stands alone: it is not one part of a larger component, so it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** a `header` scoped to the `body` (redundant, "NOT RECOMMENDED").
- **Allowed:** `section`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** a `header` inside `article`, `aside`, `main`, `nav`, or `section`; `footer`, `nav`, `aside`, `article`, `main`, `form`, `search`; `ul`, `ol`, `li`; `h1` to `h6`; `a` with `href`; `button`; form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- `role="banner"` on a `div` or `section` replaces nothing a reader relies on. It is not allowed on a `ul` or a `nav` at all (above); where a browser honors it there anyway, the list or the navigation landmark is lost.
- ARIA in HTML allows only `group`, `none`, or `presentation` on a `header` (plus `banner` where it already is one). `none` or `presentation` on a body-scoped `header` removes the banner landmark.

## How it fails in code

- No banner, navigation, or main landmark, no skip link, and no heading at the start of the main content: `wcag/sc-2.4.1-bypass-blocks.md`, definite per that entry. A missing banner alone is not a failure.
- A `header` inside `main` or an `article` expected to act as the page banner: it is not one. Advice; a failure only if it leaves 2.4.1 unmet.
- Two banners in one document. Advice (axe `landmark-no-duplicate-banner`, best practice).
- A banner nested inside another landmark. Advice (axe `landmark-banner-is-top-level`).

## How to check

Find the page-level `header` or `role="banner"`; confirm it is a direct part of the `body`, not inside a sectioning element. In the browser's accessibility tree, look for one `banner`. axe: `landmark-banner-is-top-level`, `landmark-no-duplicate-banner` (best practice, `knowledge/axe-rules.md`).
