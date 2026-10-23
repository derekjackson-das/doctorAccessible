# Design: Target size

- Requirement sources (tier 1): `wcag/sc-2.5.8-target-size-minimum.md`.
- Practice sources:
  - W3C, WCAG 2.2 SC 2.5.5 Target Size (Enhanced), Level AAA, W3C Recommendation 12 December 2024. https://www.w3.org/TR/WCAG22/#target-size-enhanced Tier 1, beyond our target.
  - W3C, "Understanding Success Criterion 2.5.5: Target Size (Enhanced)", updated 6 September 2026. https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html Tier 2.
  - Adrian Roselli, "Target Size and 2.5.5", 8 June 2019, updated 24 July 2024. https://adrianroselli.com/2019/06/target-size-and-2-5-5.html Tier 3.
  - Adrian Roselli, "2.5.8: Adversarial Conformance", 29 December 2023, updated 31 August 2026. https://adrianroselli.com/2023/12/2-5-8-adversarial-conformance.html Tier 3.
- Related entries: `patterns/carousel.md`, `patterns/modal-dialog.md`, `testing/zoom.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A design that fails the Requirement is reported under its criterion, once, at the confidence its `wcag/` entry gives. A design that meets the Requirement but misses a Practice point is reported as likely or manual review, never definite, and never as a WCAG failure. Level AAA criteria are practice for this project.

## Requirement (tier 1)

Pointer targets meet the minimum size in `wcag/sc-2.5.8-target-size-minimum.md` (new in WCAG 2.2; a project held only to WCAG 2.1 is not bound by it), or one of its exceptions applies: enough spacing around an undersized target, an equivalent control that meets the size, a target inline in text, a size set by the browser, or an essential presentation.

## Practice (tier 2 and 3, not required)

- **Aim for 44 by 44 CSS pixels.** SC 2.5.5, Level AAA, sets that size. Roselli advises it as a working minimum for interactive controls even on projects that only target AA, leaving links inside paragraphs out of it.
- **Go larger for risky or frequent actions.** The Understanding page recommends targets above the minimum when a control is used often, when its result cannot easily be undone, when it sits near the edge of the screen, or when it is part of a sequence (W3C).
- **The exceptions can be gamed.** Roselli shows a tiny close button that technically passes through the spacing exception and is still very hard to hit; meeting the letter of the minimum is not the same as being usable.
- **Check sizes on real devices.** The same CSS pixel size is physically different across screens; Roselli suggests a 44-pixel reference box viewed on the devices in question.

## How to check

Measure each target's clickable box in the browser's developer tools, not the visible icon alone. For undersized targets, check the spacing exception exactly as the 2.5.8 entry describes. Try each small control with a finger on a phone and with a mouse at high zoom (`testing/zoom.md`).
