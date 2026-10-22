# SC 2.4.2 Page Titled

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.4 Navigable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#page-titled
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Web pages have titles that describe topic or purpose.

## What it requires, in our words

Every page has a `title` element, and the title says what the page is. The title is the first thing a screen reader announces, the label on the browser tab, the text in bookmarks and history, and what a person with many tabs open uses to find their way back. A title that is the site name alone, or "Untitled", or the same on every page, fails the purpose. The convention of page name first, then site name, puts the distinguishing part where it is read first. On a single-page application, the title should change when the view changes.

## How it fails in code

- No `title` element, or an empty one. Definite.
- A title that does not identify the page's content: "Home", "Page", the site name alone on an inner page, or a filename. Definite. F25.
- The same title on every page of a site. Definite once confirmed across pages.
- A title that is accurate but puts the site name first and the page name last. Passes; worth a content note.
- A single-page application whose title never changes as views change. Likely; definite once observed.

## How to meet it

- Technique H25, "Providing a title using the title element", together with Technique G88, "Providing descriptive titles for web pages".
- Content: see `docs/content-standards.md`. The page title and the `h1` should agree.
- Advisory: Technique G127, "Identifying a web page's relationship to a larger collection of web pages", such as "Printing prices, Library Services".

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.4.6 Headings and Labels (entry in this package). The `h1` should describe the page the way the title does.
- SC 3.2.3 Consistent Navigation (`wcag/sc-3.2.3-consistent-navigation.md`). Titles following one pattern across a site help orientation.

## Automated coverage (tier 3)

axe-core tags `document-title` to this criterion. It flags a missing or empty title. It cannot judge whether the title describes the page. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
