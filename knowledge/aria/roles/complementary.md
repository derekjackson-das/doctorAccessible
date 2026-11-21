# Role: complementary

- Category: landmark.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "complementary role", https://www.w3.org/TR/wai-aria-1.2/#complementary. ARIA in HTML, W3C Recommendation 11 August 2026, row for `aside`, https://www.w3.org/TR/html-aria/#el-aside
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.9 and 3.5.10 for `aside`, https://www.w3.org/TR/html-aam/#el-aside
- Practice (tier 2): ARIA Authoring Practices Guide, "Landmark Regions", complementary section (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- Reference (tier 3): MDN Web Docs, "ARIA: complementary role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/complementary_role
- Related entries: `html/landmarks.md`, `aria/roles/region.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="complementary"` on `aside` is redundant, never a finding.

## What it is

The landmark for content that supports the main content and still makes sense on its own: a sidebar of related articles, a call-out, show times. WAI-ARIA 1.2: "A landmark that is designed to be complementary to the main content at a similar level in the DOM hierarchy, but remaining meaningful when separated from the main content."

## The native element

`aside`. HTML-AAM maps an `aside` scoped to the `body` or `main` to `complementary`. An `aside` inside other sectioning content (`article`, `aside`, `nav`, `section`) is `complementary` only if it has an accessible name (HTML-AAM 3.5.10; MDN). ARIA in HTML allows `role="complementary"` on `aside` but marks it "NOT RECOMMENDED".

## When writing the role is justified

When an `aside` cannot be used, such as a legacy page being retrofitted.

## What the spec asks of authors

- WAI-ARIA 1.2: if the content is completely separable from the main content, "it may be appropriate to use a more general role". APG suggests `region` for content unrelated to the main content.
- Naming: name from author; not required. APG and MDN: give each a unique label when there is more than one, without the word "complementary".
- APG: keep it at the top level, not nested inside another landmark.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required by WAI-ARIA 1.2; APG asks for a unique one when there is more than one, and needed for an `aside` inside sectioning content to be a landmark at all.
- It stands alone: it is not one part of a larger component, so it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `aside` (redundant, "NOT RECOMMENDED").
- **Allowed:** `section`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `article`, `header`, `footer`, `nav`, `main`, `form`, `search`; `ul`, `ol`, `li`; `h1` to `h6`; `a` with `href`; `button`; form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- ARIA in HTML allows `feed`, `none`, `note`, `presentation`, `region`, or `search` on an `aside`. Each replaces `complementary`. `none` or `presentation` removes the landmark entirely.
- `role="complementary"` on a `section` replaces `region`. It is not allowed on a `ul` (above); where a browser honors it anyway, the list is lost.

## How it fails in code

- Missing or misused complementary landmarks are not a WCAG failure on their own. 1.3.1 applies only when the page's structure is conveyed visually and nowhere in the markup; likely or manual review per that entry.
- An unnamed `aside` nested in an `article`, expected to be a landmark: it is not one. Advice.
- Several unnamed `aside` elements. Advice (axe `landmark-unique`). A complementary landmark nested in another: advice (axe `landmark-complementary-is-top-level`, which `knowledge/axe-rules.md` marks deprecated).

## How to check

For each `aside`: where is it scoped, and does it need a name to be a landmark there? In the accessibility tree, does it show as `complementary`? Is the content actually supporting the main content, or would `region` fit better?
