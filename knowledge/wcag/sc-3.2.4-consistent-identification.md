# SC 3.2.4 Consistent Identification

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 3 Understandable / 3.2 Predictable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#consistent-identification
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Components that have the same functionality within a set of web pages are identified consistently.

## What it requires, in our words

A thing that does the same job on every page is called the same thing on every page. The search button is "Search" everywhere, not "Search" here and "Find" there. The icon for downloading a PDF has the same alt text wherever it appears. The link to the help page is "Help" throughout, not sometimes "Support". Screen reader users navigate by names, and people with cognitive disabilities rely on recognizing the same word. Different things may of course have different names; the criterion is about same function, same name. Two components with the same label that do different things is a related problem, covered by whether each label is descriptive.

## How it fails in code

- The same function labeled differently on different pages: a search field labeled "Search" on one and "Find" on another, or a download icon whose alt text varies by page. Definite once two pages are compared. F31.
- The same icon used for different functions across the site. Likely; also raises 2.4.6.
- A label that varies only because the context genuinely differs ("Search this site" versus "Search the catalog" for two different searches). Not a failure; different function.

## How to meet it

- Technique G197, "Using labels, names, and text alternatives consistently for content that has the same functionality": one shared component, one shared string.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.2.3 Consistent Navigation (entry in this package). Same order, as distinct from same name.
- SC 2.4.6 Headings and Labels (`wcag/sc-2.4.6-headings-and-labels.md`). Whether the label describes the function at all.
- SC 1.1.1 Non-text Content (`wcag/sc-1.1.1-non-text-content.md`). Alt text for repeated icons.
- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). Whether the component has a name.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Consistency is judged by comparing pages, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
