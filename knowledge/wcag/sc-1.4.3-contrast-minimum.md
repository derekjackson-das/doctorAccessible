# SC 1.4.3 Contrast (Minimum)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#contrast-minimum
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for the following:
>
> **Large Text.** Large-scale text and images of large-scale text have a contrast ratio of at least 3:1;
>
> **Incidental.** Text or images of text that are part of an inactive user interface component, that are pure decoration, that are not visible to anyone, or that are part of a picture that contains significant other visual content, have no contrast requirement.
>
> **Logotypes.** Text that is part of a logo or brand name has no contrast requirement.

## What it requires, in our words

Text must stand out from its background by a measured amount. The measure is the contrast ratio defined in the Recommendation, from 1:1 (same color) to 21:1 (black on white). Normal text needs at least 4.5:1. Large text needs at least 3:1; the Recommendation defines large as at least 18 point, or at least 14 point and bold, which works out to roughly 24 CSS pixels, or about 18.7 CSS pixels bold. Placeholder text, link text, and text over images or gradients all count. Disabled controls, pure decoration, and logos are exempt. The thresholds are a floor, not a target; the `design` entries, when they exist, carry the practice above it.

## How it fails in code

- Normal-size text whose computed contrast against its background is below 4.5:1, or large text below 3:1. Definite when both colors are solid and known.
- Text color set without a background color, or the reverse, so the page depends on browser defaults that a user may have changed. Likely. F24.
- Text over a background image, gradient, or video where parts of the background bring the ratio below the threshold. Likely from code; a person must check the worst spot. F83.
- Placeholder text in a light gray that fails the ratio. Definite when measured.
- Text in a disabled control that fails. Not a failure; exempt as inactive.

## How to meet it

- Technique G18, "Ensuring that a contrast ratio of at least 4.5:1 exists between text (and images of text) and background behind the text", and Technique G145 for the 3:1 large-text case. Measure with a tool that implements the Recommendation's formula.
- Technique G148, "Not specifying background color, not specifying text color, and not using technology features that change those defaults": leaving both to the browser.
- Technique G174, "Providing a control with a sufficient contrast ratio that allows users to switch to a presentation that uses sufficient contrast", when the default design cannot change.
- Always set text and background colors together.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.4.11 Non-text Contrast (entry in this package). The 3:1 requirement for controls and graphics, as distinct from text.
- SC 1.4.6 Contrast (Enhanced) is Level AAA and not a requirement here; it raises the ratios to 7:1 and 4.5:1.
- SC 1.4.1 Use of Color (entry in this package). Whether color is the only cue, as distinct from how visible it is.
- SC 1.4.5 Images of Text (entry in this package). Text in images must meet the same ratios and is harder to fix.

## Automated coverage (tier 3)

axe-core tags `color-contrast` to this criterion. It computes the ratio for rendered text against solid backgrounds and catches most plain failures. It reports "needs review" rather than a violation when the background is an image, gradient, or overlapping element it cannot resolve, and those cases are manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
