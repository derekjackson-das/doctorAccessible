# HTML: Landmarks

- Tier 1: HTML Living Standard, §4.3 Sections (`header`, `footer`, `nav`, `aside`, `section`) and §4.4.14 The main element, accessed 2026-10-23. https://html.spec.whatwg.org/multipage/sections.html , https://html.spec.whatwg.org/multipage/grouping-content.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026, rows for those elements (a `section` is a `region` only once it has an accessible name). https://www.w3.org/TR/html-aria/
- Tier 2: WAI Tutorials, "Page Regions" (updated 24 March 2026), Page Structure Tutorial (updated 8 April 2026). https://www.w3.org/WAI/tutorials/page-structure/regions/
- Related: `html/headings.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.4.1-bypass-blocks.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how to build it. Whether code fails WCAG is decided by the `wcag/` entries named below; report a failure once, under its criterion, at that entry's confidence. A page with no landmarks is not by itself a failure; see the 2.4.1 and 1.3.1 entries for when it becomes one.

## The native approach

From the WAI tutorial, in our words:

- **`header`** for the site-wide region at the top (logo, search, navigation).
- **`nav`** for each navigation menu. A page can have several; give each a name with `aria-label` or `aria-labelledby` so they can be told apart.
- **`main`** for the main content. The HTML Standard allows only one `main` that is not `hidden` in a document.
- **`aside`** for content that supports the main content but stands on its own.
- **`footer`** for the site-wide region at the bottom.
- **`section` with a name** when a part of the page deserves to be a landmark; without a name it is not one (ARIA in HTML).

## What the native approach satisfies by default

Screen reader users can list and jump between regions with no ARIA. Landmarks are one of the ways to bypass repeated blocks (`wcag/sc-2.4.1-bypass-blocks.md`), and they expose the page's structure (`wcag/sc-1.3.1-info-and-relationships.md`).

## Where people go wrong

- Everything in `div`s, so there is nothing to jump to.
- Two `nav` elements with no names, so they cannot be told apart (the WAI tutorial says to label each). Advice, not a finding.
- More than one visible `main`, which the HTML Standard does not allow. Advice, not a finding.
- Redundant roles such as `<main role="main">`, which ARIA in HTML says not to add (`aria/aria-in-html.md`). Not a finding.

## When ARIA is genuinely needed

- `aria-label` or `aria-labelledby` to name a `nav`, `aside`, or `section`.
- Landmark roles on `div`s only when the HTML elements cannot be used, such as a legacy page being retrofitted (WAI tutorial; `aria/using-aria.md`, rule 1).
