# SC 3.2.3 Consistent Navigation

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 3 Understandable / 3.2 Predictable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#consistent-navigation
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Navigational mechanisms that are repeated on multiple web pages within a set of web pages occur in the same relative order each time they are repeated, unless a change is initiated by the user.

## What it requires, in our words

The menu, the search box, the skip link, the footer links: whatever repeats from page to page stays in the same order from page to page. People who use a screen reader or a magnifier learn where things are and go there by habit; people with cognitive disabilities depend on that habit. Items may be added or removed on some pages, but the ones that remain keep their relative order. A user choosing to rearrange things, such as sorting a menu, is allowed. This is a site-level criterion checked across pages, not a page-level one.

## How it fails in code

- The main navigation links appear in one order on some pages and a different order on others. Definite once two pages are compared. F66.
- The search box sits before the navigation on one page and after it on another. Definite once compared.
- A page template that places the skip link somewhere different from the rest of the site. Definite once compared.
- A section omits some navigation items but keeps the remaining ones in the same relative order. Passes.

## How to meet it

- Technique G61, "Presenting repeated components in the same relative order each time they appear": one shared template or component for the repeated blocks.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.2.4 Consistent Identification (entry in this package). Same name for the same thing, as distinct from same order.
- SC 3.2.6 Consistent Help (entry in this package). The same requirement, narrowed to help mechanisms, at Level A.
- SC 2.4.1 Bypass Blocks and 2.4.5 Multiple Ways (`wcag/sc-2.4.1-bypass-blocks.md`, `wcag/sc-2.4.5-multiple-ways.md`). The repeated navigation this criterion keeps in order.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Consistency is judged by comparing pages, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
