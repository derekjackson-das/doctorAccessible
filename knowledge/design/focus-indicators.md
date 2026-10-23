# Design: Focus indicators

- Requirement sources (tier 1): `wcag/sc-2.4.7-focus-visible.md`, `wcag/sc-1.4.11-non-text-contrast.md`, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`.
- Practice sources:
  - W3C, WCAG 2.2 SC 2.4.13 Focus Appearance and SC 2.4.12 Focus Not Obscured (Enhanced), both Level AAA, W3C Recommendation 12 December 2024. https://www.w3.org/TR/WCAG22/#focus-appearance Tier 1, beyond our target.
  - W3C, "Understanding Success Criterion 2.4.13: Focus Appearance", updated 6 September 2026. https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html Tier 2.
  - Sara Soueidan, "A guide to designing accessible, WCAG-conformant focus indicators", 13 August 2021, updated 27 August 2023. https://www.sarasoueidan.com/blog/focus-indicators/ Tier 3.
  - Hidde de Vries, "Indicating focus to improve accessibility", 6 June 2019, updated 5 May 2023. https://hidde.blog/indicating-focus-to-improve-accessibility/ Tier 3.
- Related entries: `testing/keyboard-only.md`, `testing/forced-colors.md`, `design/contrast.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A design that fails the Requirement is reported under its criterion, once, at the confidence its `wcag/` entry gives. A design that meets the Requirement but misses a Practice point is reported as likely or manual review, never definite, and never as a WCAG failure. Level AAA criteria are practice for this project.

## Requirement (tier 1)

- **A focus indicator is visible** whenever keyboard focus is used (`wcag/sc-2.4.7-focus-visible.md`). Removing the outline with nothing in its place, or a replacement that is invisible in practice, fails.
- **The indicator contrasts with what is next to it** at the non-text ratio (`wcag/sc-1.4.11-non-text-contrast.md`). An indicator below that ratio against the adjacent colors fails, even if it passes against some other background on the page.
- **The focused element is not entirely hidden** by author content such as sticky headers or banners (`wcag/sc-2.4.11-focus-not-obscured-minimum.md`). This criterion is new in WCAG 2.2; a project held only to WCAG 2.1 is not bound by it.

## Practice (tier 2 and 3, not required)

- **Size and change, the AAA way.** SC 2.4.13, Level AAA, asks for an indicator at least as large as a 2 CSS pixel thick perimeter of the component, with a 3:1 change between focused and unfocused states. A solid 2px outline is the simplest way to meet it; dashed outlines lose area in their gaps and need to be thicker (W3C; Soueidan).
- **Test against every background the ring can sit on.** A single site-wide focus color often passes on the page body and disappears on a colored header, a dark card, or a button of the same color (Soueidan; de Vries). De Vries notes that sites with light and dark areas commonly use a dark ring on light areas and a light ring on dark areas.
- **Use a two-color indicator where backgrounds vary.** The Understanding page points to technique C40, a two-color focus indicator, so one ring contrasts with any background (W3C).
- **Do not trust browser defaults to be enough.** Soueidan found, in 2021 to 2023, that default focus rings varied by browser and could clash with a site's colors, sometimes to the point of being hard or impossible to see. Browser defaults may have changed since; check them.
- **Keep an outline even when using box-shadow.** Box-shadow does not survive high contrast modes; set a transparent solid outline alongside it (de Vries).
- **Never remove outlines globally.** Style the keyboard case with `:focus-visible`, now supported across evergreen browsers (de Vries, 2023 update).
- **Show the whole focused element.** SC 2.4.12, Level AAA, asks that no part of it is hidden by author content.

## How to check

Tab through every region of the page, including headers, footers, cards, and dark sections. Measure the ring against the color directly next to it in each region, not only against the page body. Repeat in forced colors (`testing/forced-colors.md`). The keyboard procedure is `testing/keyboard-only.md`. Automated tools do not cover this (see the 2.4.7 and 1.4.11 entries).
