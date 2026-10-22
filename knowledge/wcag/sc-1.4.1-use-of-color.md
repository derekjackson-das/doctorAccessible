# SC 1.4.1 Use of Color

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#use-of-color
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.
>
> Note: This success criterion addresses color perception specifically. Other forms of perception are covered in Guideline 1.3 including programmatic access to color and other visual presentation coding.

## What it requires, in our words

Color can carry meaning, but never alone. If required fields are shown in red, add the word "required" or an asterisk with a key. If a chart distinguishes series by color, add labels or patterns. If links are distinguished from body text only by being blue, add an underline or make sure the contrast between link and text colors is itself strong. Roughly one in twelve men cannot tell red from green, and people using monochrome displays or high-contrast modes see no color at all. This is about what sighted people see; whether the same information reaches assistive technology is Guideline 1.3.

## How it fails in code

- Required fields or fields in error marked only by a color change on the label or border. Definite. F81.
- Links inside body text distinguished from surrounding text by color alone, with no underline or other cue, where the link color's contrast with the body text is under 3:1. Definite. F73.
- A chart or graph image whose series are told apart by color only, with no text alternative that supplies the information. Definite. F13.
- Status shown by a colored dot or badge with no text or icon shape. Definite once confirmed the color is the only cue.
- A selected tab or current page shown only by background color. Likely; often there is also a position or weight cue a person must confirm.
- A focus indicator that changes only color. Covered by 2.4.7 and 1.4.11 rather than here.

## How to meet it

- Technique G14, "Ensuring that information conveyed by color differences is also available in text": the word, number, or label alongside the color.
- Technique G205, "Including a text cue for colored form control labels".
- Technique G182, "Ensuring that additional visual cues are available when text color differences are used to convey information", such as underline, bold, or an icon.
- Technique G183, "Using a contrast ratio of at least 3:1 to distinguish inline text links from surrounding text", together with a visible cue on hover and focus.
- Technique G111, "Using color and pattern", for graphics.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.3.3 Sensory Characteristics (entry in this package). Color in instructions.
- SC 1.3.1 Info and Relationships (entry in this package). Whether the information is also in the code.
- SC 1.4.3 Contrast (Minimum) and 1.4.11 Non-text Contrast (entries in this package). How visible the color is, as distinct from whether color is the only cue.
- SC 1.1.1 Non-text Content (entry in this package). Alt text that omits color-coded information fails both; F13.

## Automated coverage (tier 3)

axe-core tags `link-in-text-block` to this criterion. It checks that links inside text blocks differ from the text by more than color, or by sufficient color contrast. It cannot see that a red border means "error" or that a chart uses color alone. Most of this criterion is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
