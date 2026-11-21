# Role: main

- Category: landmark.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "main role", https://www.w3.org/TR/wai-aria-1.2/#main. ARIA in HTML, W3C Recommendation 11 August 2026, row for `main`, https://www.w3.org/TR/html-aria/#el-main
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.87, https://www.w3.org/TR/html-aam/#el-main
- Practice (tier 2): ARIA Authoring Practices Guide, "Landmark Regions", main section (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- Reference (tier 3): MDN Web Docs, "ARIA: main role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/main_role
- Related entries: `html/landmarks.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-2.4.1-bypass-blocks.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="main"` on `main` is redundant, never a finding.

## What it is

The landmark for the page's main content. WAI-ARIA 1.2: "A landmark containing the main content of a document." The spec describes it as a non-obtrusive alternative to a "skip to main content" link, because assistive technology can jump straight to it.

## The native element

`main`, always (HTML-AAM). ARIA in HTML allows no role on `main` other than `main`, which it marks "NOT RECOMMENDED".

## When writing the role is justified

When a `main` element cannot be used, such as a legacy page being retrofitted. Rare.

## What the spec asks of authors

- "Within any document or application, the author SHOULD mark no more than one element with the main role." A nested document or application may have its own. The HTML Standard also allows only one `main` that is not `hidden` (`html/landmarks.md`).
- Naming: name from author; not required. MDN suggests naming it in a single-page app, with `aria-labelledby` to the visible heading.
- MDN: when script swaps in a second `main`, hide the inactive one with `hidden` so assistive technology does not find two.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- It stands alone: it is not one part of a larger component, so it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `main` (redundant, "NOT RECOMMENDED"). `main` allows no other role.
- **Allowed:** `article`, `section`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `header`, `footer`, `nav`, `aside`, `form`, `search`; `ul`, `ol`, `li`; `h1` to `h6`; `a` with `href`; `button`; form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- `role="main"` on another element replaces its role; on a `div` there is nothing to lose.
- No other role is allowed on `main`, so there is nothing to take away from it except by breaking ARIA in HTML.

## How it fails in code

- No `main` landmark, no skip link, and no heading at the start of the main content, on a page with repeated blocks: `wcag/sc-2.4.1-bypass-blocks.md`, definite per that entry. A `main` alone usually meets the landmark part.
- Two visible `main` landmarks. Advice (HTML conformance; axe `landmark-no-duplicate-main`). A failure only if it confuses where the main content is in a way that breaks 2.4.1.
- `main` nested inside another landmark. Advice (axe `landmark-main-is-top-level`).
- Main content partly outside `main`. Advice; APG asks for all content to sit in some landmark.

## How to check

One `main` in the accessibility tree, at the top level, holding all the page-specific content. axe: `landmark-one-main`, `landmark-no-duplicate-main`, `landmark-main-is-top-level` (best practice).
