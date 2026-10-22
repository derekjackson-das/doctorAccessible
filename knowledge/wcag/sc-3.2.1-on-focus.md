# SC 3.2.1 On Focus

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 3 Understandable / 3.2 Predictable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#on-focus
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/on-focus.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> When any user interface component receives focus, it does not initiate a change of context.

## What it requires, in our words

Simply landing on something must not make anything big happen. Tabbing to a link must not follow it; tabbing to a select must not submit the form; focusing a field must not open a new window or jump to another page. A keyboard user tabs through everything to get where they are going, and a screen reader user focuses things just to hear what they are. If focus alone triggers a change of context, the Recommendation's term for a new page, a new window, a moved focus, or content rearranged so the page means something different, they lose their place every time they move. Small changes such as showing a tooltip or highlighting the focused element are fine.

## How it fails in code

- A `focus` or `focusin` handler that navigates, submits a form, opens a window, or moves focus elsewhere. Definite. F55 covers the "move focus away on focus" case.
- A dropdown that opens a full-page overlay or dialog as soon as it is focused rather than activated. Definite once observed.
- A link that follows itself on `focus`. Definite.
- A field that shows inline help text on focus. Not a failure; help text is not a change of context.
- A custom widget that opens a small popup listbox on focus. Likely; the Understanding page treats a non-disruptive popup as acceptable, so a person judges whether it reorients the page.

## How to meet it

- Technique G107, "Using 'activate' rather than 'focus' as a trigger for changes of context": bind the behavior to `click`, Enter, or `change`, never to `focus`.
- Native HTML controls meet this by default.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.2.2 On Input (entry in this package). The same rule for changing a control's value.
- SC 2.1.1 Keyboard and 2.4.7 Focus Visible (`wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.7-focus-visible.md`). Script that blurs on focus fails all three; F55.
- SC 2.4.3 Focus Order (`wcag/sc-2.4.3-focus-order.md`). Focus arriving somewhere unexpected.
- SC 3.2.5 Change on Request is Level AAA and not a requirement here.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Focus handlers are found by reading the script or by tabbing through the page. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
