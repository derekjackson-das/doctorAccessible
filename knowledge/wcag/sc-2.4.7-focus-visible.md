# SC 2.4.7 Focus Visible

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 2 Operable / 2.4 Navigable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#focus-visible
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible.

## What it requires, in our words

A keyboard user needs to see which element has focus, the way a mouse user sees the pointer. Browsers draw a focus ring by default. The failure is almost always an author removing it, with `outline: none` or `outline: 0`, because a designer did not like the look, and not replacing it with anything. The criterion asks only that some visible indicator exist in at least one mode; how strongly it contrasts is 1.4.11, and whether it is covered by other content is 2.4.11. Leaving the browser default alone passes. Styling a clearer indicator with `:focus-visible` is better still.

## How it fails in code

- `outline: none` or `outline: 0` on focusable elements, or on `*`, with no replacement style for the focused state. Definite. F78.
- A replacement focus style that is invisible in practice, such as a one-pixel change in a color that matches the background. Definite once observed; F78.
- Script that blurs an element as soon as it receives focus. Definite. F55.
- Focus styles set only on `:hover` and not `:focus` or `:focus-visible`. Definite.
- `outline: none` on `:focus` with a visible style on `:focus-visible`. Passes; the indicator shows for keyboard users.

## How to meet it

- Technique G149, "Using user interface components that are highlighted by the user agent when they receive focus": leave the default alone.
- Technique C45, "Using CSS :focus-visible to provide keyboard focus indication", and Technique C15, "Using CSS to change the presentation of a user interface component when it receives focus".
- Technique G195, "Using an author-supplied, visible focus indicator", and Technique C40, "Creating a two-color focus indicator to ensure sufficient contrast with all components".
- Technique G165, "Using the default focus indicator for the platform so that high visibility default focus indicators will carry over".

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.4.11 Non-text Contrast (`wcag/sc-1.4.11-non-text-contrast.md`). The indicator must contrast at 3:1 with adjacent colors.
- SC 2.4.11 Focus Not Obscured (Minimum) (entry in this package). The focused element must not be fully hidden by other content.
- SC 2.4.12 Focus Not Obscured (Enhanced) and 2.4.13 Focus Appearance are Level AAA and not requirements here.
- SC 2.1.1 Keyboard (entry in this package). An element must be reachable before its focus can be visible.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Whether focus is visible is observed by tabbing through the page, which is manual; a grep for `outline: none` or `outline: 0` in the CSS is a useful first pass. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
