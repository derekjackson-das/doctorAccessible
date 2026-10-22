# SC 1.3.2 Meaningful Sequence

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.3 Adaptable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#meaningful-sequence
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> When the sequence in which content is presented affects its meaning, a correct reading sequence can be programmatically determined.

## What it requires, in our words

When order matters, the order in the code must be an order that makes sense. A screen reader reads the document in source order, and a browser lays out reflowed content in source order, regardless of where CSS has placed things on screen. If a page puts the price after the product name visually but before it in the code, a listener hears them backwards. Not every order matters: a sidebar and a main column can usually be read in either order. The criterion applies when swapping the order would change the meaning.

## How it fails in code

- CSS positioning (floats, grid `order`, flexbox `order`, absolute positioning) that produces a visual order different from the source order, where the order carries meaning. Likely from code; definite once a person confirms the meaning changes. F1.
- A layout table whose cells read in a nonsensical order when linearized. Definite when the linear order is wrong. F49.
- Whitespace used to space out letters within a word, so the word is read letter by letter. Definite. F32.
- Whitespace used to build columns or tables in plain text, so lines interleave when read. Definite. F33, F34.
- A visually hidden "skip to" or instruction placed in source where it is read at the wrong moment. Manual review.

## How to meet it

- Technique G57, "Ordering the content in a meaningful sequence": write the source in the order a reader needs.
- Technique C27, "Making the DOM order match the visual order": when CSS moves things, move the source instead, or keep the move cosmetic.
- Use CSS for spacing (letter-spacing, margins), never spaces or non-breaking spaces inside words.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.3.1 Info and Relationships (entry in this package). Structure, as distinct from order.
- SC 2.4.3 Focus Order (no entry yet). The order in which focus moves, which usually follows source order and has the same cure.
- SC 1.4.10 Reflow (entry in this package). At 320 CSS pixels, source order becomes the visible order; a wrong source order shows up there.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Reading order is judged by comparing the visual layout to the source, or by reading the page linearized, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
