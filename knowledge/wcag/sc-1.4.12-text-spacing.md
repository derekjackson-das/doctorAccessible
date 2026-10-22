# SC 1.4.12 Text Spacing

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#text-spacing
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> In content implemented using markup languages that support the following text style properties, no loss of content or functionality occurs by setting all of the following and by changing no other style property:
>
> - Line height (line spacing) to at least 1.5 times the font size;
> - Spacing following paragraphs to at least 2 times the font size;
> - Letter spacing (tracking) to at least 0.12 times the font size;
> - Word spacing to at least 0.16 times the font size.
>
> Exception: Human languages and scripts that do not make use of one or more of these text style properties in written text can conform using only the properties that exist for that combination of language and script.
>
> Note 1: Content is not required to use these text spacing values. The requirement is to ensure that when a user overrides the authored text spacing, content or functionality is not lost.
>
> Note 2: Writing systems for some languages use different text spacing settings, such as paragraph start indent. Authors are encouraged to follow locally available guidance for improving readability and legibility of text in their writing system.

## What it requires, in our words

Some people with dyslexia or low vision read far better with more space between lines, letters, and words, and they apply those settings with a browser extension or a user stylesheet. The page does not have to use those spacings itself. It has to survive them: when a user applies all four values at once, no text is cut off, no words overlap, and nothing becomes unreachable. The failures are almost always fixed-height boxes, `overflow: hidden` on text containers, and spacing set in the `style` attribute, which a user stylesheet cannot override without `!important`.

## How it fails in code

- Text clipped, truncated, or overlapping other text after the four spacing values are applied. Definite once observed. F104.
- Text containers with fixed heights in pixels and `overflow: hidden`. Likely from code; confirm by applying the spacing.
- Line height, letter spacing, or word spacing set in an element's `style` attribute. Likely; it resists user overrides.
- Buttons or navigation items whose text wraps out of the control when spaced. Definite once observed.

## How to meet it

- Technique C36, "Allowing for text spacing override": containers that grow with their content, no fixed heights on text, `overflow` left visible or auto.
- Technique C35, "Allowing for text spacing without wrapping", for single-line controls that must not wrap.
- Advisory: Technique C21, "Specifying line spacing in CSS", Technique C28 for em-sized containers, Technique C8 for letter spacing.
- Test: apply the four values with a bookmarklet or user stylesheet and read the whole page.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.4.4 Resize Text and 1.4.10 Reflow (entries in this package). The other two "change the text, nothing breaks" requirements. Test all three in one pass.
- SC 1.4.8 Visual Presentation is Level AAA and not a requirement here; it sets spacing values the author must provide.

## Automated coverage (tier 3)

axe-core tags `avoid-inline-spacing` to this criterion. It flags spacing properties set in `style` attributes with `!important`, which block user overrides. Whether content survives the override is a rendering test and remains manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
