# Design: Text spacing

- Requirement sources (tier 1): `wcag/sc-1.4.12-text-spacing.md`.
- Practice sources:
  - W3C, "Understanding Success Criterion 1.4.12: Text Spacing", updated 1 October 2025. https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html Tier 2.
  - W3C, WCAG 2.2 SC 1.4.8 Visual Presentation, Level AAA, W3C Recommendation 12 December 2024. https://www.w3.org/TR/WCAG22/#visual-presentation Tier 1, beyond our target.
  - W3C, "Understanding Success Criterion 1.4.8: Visual Presentation", updated 6 September 2026. https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html Tier 2.
  - WebAIM, "Text/Typographical Layout", last updated 22 October 2020. https://webaim.org/techniques/textlayout/ Tier 3. Over five years old.
- Related entries: `testing/zoom.md`, `coga/objective-3-clear-content.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A design that fails the Requirement is reported under its criterion, once, at the confidence its `wcag/` entry gives. A design that meets the Requirement but misses a Practice point is reported as likely or manual review, never definite, and never as a WCAG failure. Level AAA criteria are practice for this project. No practitioner on the sources list has a dedicated article on text spacing; the practice here rests on W3C material and WebAIM.

## Requirement (tier 1)

When a reader overrides line height, paragraph spacing, letter spacing, and word spacing to the values in `wcag/sc-1.4.12-text-spacing.md`, nothing is lost: no text is clipped, overlapped, or cut off. Content does not have to use those values by default; it has to survive them.

- Text clipped by a container that cannot grow fails; the entry grades it definite (failure F104).
- Text truncated under the spacing override fails unless there is a way to reveal it, such as on focus or on a linked page (W3C Understanding 1.4.12, tier 2, explaining the criterion).

## Practice (tier 2 and 3, not required)

- **Let text containers grow.** Size containers in `em` (technique C28) and avoid fixed heights, so spaced-out text pushes the box larger instead of being clipped (W3C Understanding 1.4.12).
- **Leave room beyond the test values.** The Understanding page notes that users may choose spacing beyond the criterion's values, and that what happens then is not a failure of the content (W3C). Our own inference: a layout that only just survives the test values leaves those readers nothing to spare.
- **Readable blocks of text.** SC 1.4.8, Level AAA, asks for a way to get lines of no more than 80 characters, unjustified text, and more generous line and paragraph spacing. WebAIM (2020) puts a comfortable line length at roughly 50 to 120 characters and says fully justified text impairs readability.

## How to check

Apply the four spacing values with a user stylesheet or bookmarklet, as the Understanding page describes, and look for text that is cut off, overlaps, or disappears, especially in buttons, navigation, cards, and anything with a fixed height. Repeat at 200% zoom (`testing/zoom.md`).
