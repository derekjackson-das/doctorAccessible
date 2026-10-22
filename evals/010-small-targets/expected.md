# Eval 010: pagination links too small and too close together

Input: `input.html`. A search results page with a row of numbered page links.

Intended defect: the pagination links are 16 by 16 CSS pixels (plus a 1-pixel border, so 18 by 18 rendered) with no gap between them. They are under 24 by 24, and a 24-pixel circle centered on each one overlaps its neighbors, so the spacing exception does not apply. An earlier draft used 18-pixel links with a 2-pixel gap; axe 4.14 passed that layout, because its spacing check measures against the neighbor's box rather than the neighbor's circle, so the targets were shrunk to make the defect unambiguous to both the scanner and the standard. They are not inline in a sentence, there is no equivalent larger control, and they are author-styled, so no other exception applies. Everything else is clean: language set, title present, one `h1`, landmarks including a labeled `nav`, descriptive result links, `aria-current="page"` on the current page, visible focus, contrast above the thresholds.

## Expected findings

1. **[Definite]** Pagination targets are smaller than 24 by 24 CSS pixels and too close together.
   - Criterion: WCAG 2.2 SC 2.5.8 Target Size (Minimum) (Level AA), tier 1
   - Source: `knowledge/wcag/sc-2.5.8-target-size-minimum.md`
   - Where: the `a` elements inside `nav ul.pager`
   - Acceptable fix directions: set `min-width: 24px; min-height: 24px` on the links (technique C42), or keep them small and increase the gap so 24-pixel circles do not intersect. Larger is better for a pager; the `design` entry for target size, when it exists, will say how much.

One finding covering the pager is correct, not one per link.

## Also acceptable

- A note that the current-page `span` is not a target and is not counted.
- A note that the result links in the main list are exempt as inline text, or simply pass because their line height exceeds 24 pixels.
- A manual-review note to confirm rendered sizes in a browser, since the verifier is computing from CSS.
- A manual-review note under SC 1.4.4 that the pager boxes are sized in pixels while the text is in rem, so text-only zoom may overflow them. Not a second defect; the fix for 2.5.8 with em-based minimums resolves it.

## Must not

- Report the result links or the heading.
- Report SC 2.4.4; each pager link's number, inside a labeled `nav`, identifies its destination.
- Report landmarks, focus style, language, or contrast. The pager text at 0.75rem on white in `#005a9c` is 7.14:1; the current page white on `#005a9c` is the same ratio.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core 4.14 tags `target-size` with `wcag22aa` and `wcag258`, but the `@axe-core/cli` default run did not execute the rule at all on this page: it appeared in no result bucket. Run with `--rules target-size`, or with `--tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`, it reports five violations, one per pager link, with the message that safe clickable space is 18 pixels instead of 24. So the expected default scan is clean, and a verifier that treats a clean default scan as a pass has failed this eval. A verifier that enables the rule and reports the five pager links has done well. If the rule flags the result links in the main list, the input is not clean and needs fixing; their line height is set so the links are over 24 pixels tall.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
