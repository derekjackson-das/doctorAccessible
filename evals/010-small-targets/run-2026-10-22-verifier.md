# Verifier run, 2026-10-22, eval 010

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), given the file path, the index, the content standards, and the axe command, and told not to open `expected.md`, `RESULTS.md`, or any run file.

Result against `expected.md`: **pass**. One Definite finding, SC 2.5.8 Target Size (Minimum) (Level AA), tier 1, sourced to the entry with the matching pattern quoted, at the five pager links, with C42 as the fix direction. The agent noticed that `target-size` was absent from the default axe output, re-ran with `--rules target-size`, got five violations, and said in so many words that the "0 violations" headline is not evidence that target size passes. That is the behavior the answer key hoped for. It also raised a manual-review note under SC 1.4.4 about pixel-fixed boxes with rem text; the key was amended after the run to allow that note, since it is not a second defect and the fix for 2.5.8 resolves it. Nothing from the must-not list. No file modified.

Note on the input: an earlier draft used 18-pixel links with a 2-pixel gap. axe passed that layout even with the rule forced, because its spacing check measures against the neighbor's box rather than the neighbor's circle. The targets were shrunk to 16 pixels with no gap before this run so the defect is unambiguous to both the scanner and the standard. The result links also gained a line-height so they clear 24 pixels and stay out of the finding.

## Report as returned (findings and scan)

### [Definite] Pager links are undersized and touching
- Where: `.pager a` rule, lines 12 to 16; the five links at lines 34, 35, 37, 38, 39. `.pager { gap: 0 }` at line 11.
- What: each pagination link is `width: 16px; height: 16px` with a 1px border (18 by 18 CSS pixels rendered), in a flex row with no gap, so each target is under 24 by 24 and a 24-pixel circle centered on any one intersects its neighbors; none of the exceptions applies.
- Criterion: WCAG 2.2 SC 2.5.8 Target Size (Minimum) (Level AA), tier 1. New in 2.2.
- Source: knowledge/wcag/sc-2.5.8-target-size-minimum.md. Confirmed by axe `target-size`: "Target has insufficient size (18px by 18px, should be at least 24px by 24px)" on all five links.
- Fix direction: give each link a minimum 24 by 24 CSS pixel box (Technique C42), or add enough gap that the 24-pixel circles do not overlap. The current-page `span` is not a target.

### [Manual review] Pixel-fixed pager boxes under text-only enlargement
- Criterion: WCAG 2.2 SC 1.4.4 Resize Text (Level AA), tier 1. Source: knowledge/wcag/sc-1.4.4-resize-text.md.
- What: the box and line-height are fixed in pixels while the text is in rem, so at 200 percent text-only zoom the digits exceed the box; whether they overlap neighbors is a rendering question. Fix: size the boxes in em; fixing 2.5.8 with em-based minimums resolves both.

Everything else read as conforming: `lang`, title matches `h1`, landmarks including a labelled `nav`, `aria-current` on a non-interactive `span`, focus outline, viewport allows zoom, contrast 7.14:1 and 17.4:1.

Content: reading level grade 9.7 on a tiny sample pushed up by the subject words; manual review. Headings pass. Pager digits pass 2.4.4 via the labelled `nav` and list items; against content standard 5 a bare digit is a judgment call; manual review.

Manual checks remaining: pointer and touch aiming at the pager; text-only zoom at 200 percent; keyboard order and focus; screen reader `nav` label, `aria-current`, and digit names; text spacing overrides on the pager boxes.

Automated scan: axe-core 4.14.0. Default run: 0 violations, 26 passed; `target-size` absent from every bucket. Second run with `--rules target-size`: 1 violation, 5 nodes, tagged `wcag22aa`, `wcag258`; the three result links passed. Note for the project: the CLI's default rule set does not run `target-size`; it has to be requested explicitly.
