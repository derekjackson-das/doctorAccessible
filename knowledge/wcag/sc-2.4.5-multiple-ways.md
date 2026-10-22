# SC 2.4.5 Multiple Ways

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 2 Operable / 2.4 Navigable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#multiple-ways
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/multiple-ways.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> More than one way is available to locate a web page within a set of web pages except where the web page is the result of, or a step in, a process.

## What it requires, in our words

On a site of several pages, a person should have at least two ways to find a given page: for example navigation menus plus a search box, or a site map plus links between related pages. People differ in how they find things. Someone with a cognitive disability may find a site map easier than a deep menu; a screen reader user may prefer search to scanning navigation. A page that is a step in a process, such as the second page of a checkout, is exempt, because it is reached by doing the step before it. This is a site-level criterion; one page cannot pass or fail it alone.

## How it fails in code

- A site reachable only through one navigation menu, with no search, no site map, and no related-page links. Definite once the site is surveyed.
- A page reachable only by typing its URL or following one link buried in body text. Definite.
- A single page that happens to have only one way in while the site provides two overall. Not a failure of this page; manual review of the site.
- The second step of a form or checkout with no other route. Not a failure; exempt as a step in a process.

## How to meet it

- Any two of: Technique G125, "Providing links to navigate to related web pages"; Technique G64, "Providing a Table of Contents"; Technique G63, "Providing a site map"; Technique G161, "Providing a search function to help users find content"; Technique G126, "Providing a list of links to all other web pages"; Technique G185, "Linking to all of the pages on the site from the home page".
- Most sites meet this with a navigation menu plus a working search.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.4.1 Bypass Blocks (entry in this package). Moving within a page, as distinct from between pages.
- SC 2.4.8 Location is Level AAA and not a requirement here.
- SC 3.2.3 Consistent Navigation (no entry yet). The navigation that is one of the ways should be the same on every page.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. It is a site-level judgment made by surveying the pages, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
