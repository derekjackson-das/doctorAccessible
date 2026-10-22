# SC 2.4.1 Bypass Blocks

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.4 Navigable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#bypass-blocks
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> A mechanism is available to bypass blocks of content that are repeated on multiple web pages.

## What it requires, in our words

A keyboard or screen reader user arriving on a page should not have to work through the same header, navigation, and sidebar on every page before reaching what they came for. The page needs a way to skip past repeated blocks: a "skip to main content" link at the top, or landmarks and headings that assistive technology can jump between. A sighted mouse user does this by looking; everyone else needs the mechanism. Landmarks such as `main` and `nav` count because screen readers can jump straight to them, and the Understanding page accepts them as sufficient. A visible skip link helps sighted keyboard users too, and is the conservative choice.

## How it fails in code

- A page with a repeated header and navigation, no skip link, no landmark elements or roles, and no heading at the start of the main content. Definite.
- A skip link whose target does not exist, or points at an element that cannot receive focus so the jump does nothing. Definite once observed.
- A skip link that is hidden with `display: none` so it can never be focused. Definite. A link that is visually hidden until focused is fine.
- Landmarks present but no skip link. Passes; a person may still want to recommend one.

## How to meet it

- Technique G1, "Adding a link at the top of each page that goes directly to the main content area": the first focusable thing on the page, visible at least on focus, pointing at `main` with a `tabindex="-1"` or at the first heading.
- Technique ARIA11, "Using ARIA landmarks to identify regions of a page", or native elements that carry those roles: `header`, `nav`, `main`, `aside`, `footer`. Technique H101 in the 1.3.1 entry covers the same.
- Technique H69, "Providing heading elements at the beginning of each section of content".
- Technique G124, "Adding links at the top of the page to each area of the content", for complex pages.
- Technique H64, "Using the title attribute of the iframe element", so embedded frames can be skipped.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.3.1 Info and Relationships (`wcag/sc-1.3.1-info-and-relationships.md`). Landmarks and headings serve both.
- SC 2.4.3 Focus Order (entry in this package). The skip link must be early in the focus order to help.
- SC 2.4.5 Multiple Ways (entry in this package). Finding pages, as distinct from skipping within one.

## Automated coverage (tier 3)

axe-core tags `bypass` to this criterion. It passes a page that has a skip link, landmarks, or headings, and fails one that has none. It cannot tell whether a skip link works or whether the landmarks are placed sensibly. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
