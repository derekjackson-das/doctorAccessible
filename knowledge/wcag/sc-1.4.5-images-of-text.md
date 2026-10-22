# SC 1.4.5 Images of Text

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#images-of-text
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> If the technologies being used can achieve the visual presentation, text is used to convey information rather than images of text except for the following:
>
> **Customizable.** The image of text can be visually customized to the user's requirements;
>
> **Essential.** A particular presentation of text is essential to the information being conveyed.
>
> Note: Logotypes (text that is part of a logo or brand name) are considered essential.

## What it requires, in our words

Words should be real text, not a picture of words. Real text can be enlarged, recolored, respaced, read aloud, and translated. A picture of words can do none of that, and it blurs when zoomed. If CSS can produce the look, use CSS. The exceptions are a logo, where the exact rendering is the point, and cases where the user can change the image's presentation to suit them. A headline rendered as a PNG because the designer wanted a particular typeface is the classic failure; web fonts have removed the reason for it.

## How it fails in code

- An `img` whose content is text (a heading, a quote, a banner with a slogan) where CSS could render the same words. Definite once a person confirms the image is text and the look is achievable.
- A screenshot of a table or document used in place of the table or document. Definite.
- A logo as an image. Not a failure; essential by the note.
- An image of text with alt text present. Still a failure of this criterion if CSS could have done it; the alt satisfies 1.1.1 only.

## How to meet it

- Technique C22, "Using CSS to control visual presentation of text": fonts, color, spacing, shadows, and transforms in CSS over real text.
- Technique C30, "Using CSS to replace text with images of text and providing user interface controls to switch", when an image is wanted but the user must be able to get text.
- Technique G140, "Separating information and structure from presentation to enable different presentations".

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.1.1 Non-text Content (entry in this package). The image still needs alt text; meeting 1.1.1 does not meet this.
- SC 1.4.3 Contrast (Minimum) (entry in this package). Images of text must meet the ratio and cannot be fixed by the user.
- SC 1.4.4 Resize Text (entry in this package). Images of text are exempt there and blur when zoomed.
- SC 1.4.9 Images of Text (No Exception) is Level AAA and not a requirement here.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Telling that an image contains text requires looking at it, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
