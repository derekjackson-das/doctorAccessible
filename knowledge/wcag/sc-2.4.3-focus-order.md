# SC 2.4.3 Focus Order

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.4 Navigable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#focus-order
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> If a web page can be navigated sequentially and the navigation sequences affect meaning or operation, focusable components receive focus in an order that preserves meaning and operability.

## What it requires, in our words

When a keyboard user presses Tab, focus should move through the page in an order that makes sense: usually the visual reading order, and always one that keeps related things together. A form whose Tab order jumps from the first field to the submit button and then back to the second field fails. A dialog that opens and leaves focus behind it fails. The default order is source order, so this is usually met by writing the HTML in a sensible sequence and not fighting it with positive `tabindex` values or CSS that moves things around visually. Where focus goes after a dialog closes or content appears matters too.

## How it fails in code

- Positive `tabindex` values (1, 2, 3) that impose an order different from the visual and logical one. Definite. F44.
- A dialog or menu that opens but is not placed next to its trigger in the focus sequence, so Tab from the trigger skips it. Definite once observed. F85.
- CSS that reorders content visually (flex or grid `order`, floats, absolute positioning) so Tab jumps around the screen. Likely from code; definite once observed.
- Focus not moved into a modal when it opens, or not returned to the trigger when it closes. Definite once observed.
- New content inserted into the DOM far from the control that revealed it. Likely.

## How to meet it

- Technique G59, "Placing the interactive elements in an order that follows sequences and relationships within the content": write the source in reading order.
- Technique C27, "Making the DOM order match the visual order".
- Technique H102, "Creating modal dialogs with the HTML dialog element", which manages focus on open.
- Technique SCR26, "Inserting dynamic content into the Document Object Model immediately following its trigger element", and SCR27 for reordering sections.
- Avoid positive `tabindex`. Use `0` to add an element to the natural order and `-1` to make it focusable by script only.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.3.2 Meaningful Sequence (`wcag/sc-1.3.2-meaningful-sequence.md`). Reading order; focus order usually follows it.
- SC 2.4.7 Focus Visible and 2.4.11 Focus Not Obscured (Minimum) (entries in this package). Seeing where focus is.
- SC 2.1.2 No Keyboard Trap (entry in this package). Order is irrelevant if focus cannot leave.
- SC 3.2.1 On Focus (`wcag/sc-3.2.1-on-focus.md`). Focus arriving must not change context.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion in its 4.14 list, though its best-practice rule `tabindex` flags positive values. Order is checked by tabbing through the page, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
