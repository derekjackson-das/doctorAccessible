# Design: Contrast

- Requirement sources (tier 1): `wcag/sc-1.4.3-contrast-minimum.md`, `wcag/sc-1.4.11-non-text-contrast.md`, `wcag/sc-1.4.1-use-of-color.md`.
- Practice sources:
  - W3C, WCAG 2.2 SC 1.4.6 Contrast (Enhanced), Level AAA, W3C Recommendation 12 December 2024. https://www.w3.org/TR/WCAG22/#contrast-enhanced Tier 1, beyond our target.
  - W3C, "Understanding Success Criterion 1.4.6: Contrast (Enhanced)", updated 6 September 2026. https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html Tier 2.
  - WebAIM, "Contrast and Color Accessibility", last updated 9 January 2021. https://webaim.org/articles/contrast/ Tier 3. Over five years old, but its WCAG 2 guidance has not changed.
  - Adrian Roselli, "WCAG3 Contrast as of April 2026", 10 April 2026, updated 13 April 2026. https://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html Tier 3. On APCA, for awareness only.
- Related entries: `testing/forced-colors.md`, `design/focus-indicators.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A design that fails the Requirement is reported under its criterion, once, at the confidence its `wcag/` entry gives. A design that meets the Requirement but misses a Practice point is reported as likely or manual review, never definite, and never as a WCAG failure. Level AAA criteria are practice for this project.

## Requirement (tier 1)

- **Text** must reach the contrast ratios in `wcag/sc-1.4.3-contrast-minimum.md` against its background, with the lower ratio for large text and the exemptions listed there.
- **Non-text:** the parts of a control that identify it and its state, and the parts of graphics needed to understand them, must reach the ratio in `wcag/sc-1.4.11-non-text-contrast.md` against the colors next to them. That includes focus indicators.
- **Color alone** must not carry information (`wcag/sc-1.4.1-use-of-color.md`). That includes links in running text told apart from surrounding text by color alone, which the 1.4.1 entry grades definite.

## Practice (tier 2 and 3, not required)

- **Do not design at the threshold.** Ratios are not rounded up; WebAIM's example is a common gray at 4.47:1, which fails 4.5:1. Our own inference from that: leave a margin, so small color shifts in production do not tip a pass into a fail.
- **Aim for the enhanced ratios where you can.** SC 1.4.6, Level AAA, sets 7:1 for text and 4.5:1 for large text. The Understanding page ties those figures to the loss of contrast sensitivity that comes with reduced visual acuity (W3C, tier 1 beyond target and tier 2).
- **Test the worst spot, not the average.** For text over gradients, translucent colors, or images, WCAG gives no measuring method; WebAIM recommends testing where contrast is lowest.
- **Test every state.** WebAIM notes that each state of a component, such as hover and keyboard focus, needs its own contrast check, and that text colors which change on interaction need checking too.
- **Measure against what is actually adjacent.** Non-text contrast is measured against the neighboring colors, which can differ across a header, a card, and the page body; a color that passes on one may fail on another (WebAIM).
- **Style what the browser leaves weak.** WebAIM pointed out in January 2021 that Chrome's default text-box border was about 2.4:1. That is exempt because the browser draws it, but it is a reason to style field borders deliberately.
- **Underline links in running text.** WebAIM shows color combinations where links without underlines cannot meet the text contrast requirement and still stand apart from surrounding text; an underline removes the problem, and the color-alone requirement with it.
- **APCA is not a requirement.** Roselli records that APCA was pulled from WCAG 3 drafts in 2023 and that the WCAG 3 contrast method is undecided as of April 2026; he warns that dismissing WCAG 2's ratios creates legal risk. Colors below the ratios in `wcag/sc-1.4.3-contrast-minimum.md` fail that criterion whatever another algorithm says. Per principle 4, drafts are awareness only.

## How to check

Measure each text and non-text pairing with a contrast tool that implements the WCAG formula, at the lowest-contrast spot, in every state, against every background the element can sit on. Then view the page in forced colors (`testing/forced-colors.md`) to check that nothing depends on author colors alone.
