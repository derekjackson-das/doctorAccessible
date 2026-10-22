# SC 2.4.11 Focus Not Obscured (Minimum)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 2 Operable / 2.4 Navigable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
- Also in: WCAG 2.2 only. New in 2.2; not in 2.0 or 2.1.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> When a user interface component receives keyboard focus, the component is not entirely hidden due to author-created content.
>
> Note 1: Where content in a configurable interface can be repositioned by the user, then only the initial positions of user-movable content are considered for testing and conformance of this success criterion.
>
> Note 2: Content opened by the user may obscure the component receiving focus. If the user can reveal the focused component without advancing the keyboard focus, the component with focus is not considered visually hidden due to author-created content.

## What it requires, in our words

A visible focus indicator does no good if something is sitting on top of it. Sticky headers, fixed footers, cookie banners, and chat widgets can completely cover the element that has focus, so a keyboard user tabs into a link under the footer and sees nothing change. At this level the focused element must not be entirely hidden; partly covered is allowed (the Level AAA version requires fully visible). Content the user opened themselves, such as a dropdown, may cover things as long as the user can close it without moving focus.

## How it fails in code

- A `position: fixed` or `sticky` header or footer that fully covers a focused element when the page is scrolled to it by keyboard. Definite once observed. F110.
- A cookie banner or notification bar fixed at the bottom that covers the last focusable elements. Definite once observed.
- A focused element scrolled under a sticky header because the browser's scroll-into-view ignores the header's height. Definite once observed; fixable with `scroll-padding`.
- A focused element partly covered by a sticky bar. Not a failure at this level; a person may note it against the AAA criterion.
- A dropdown the user opened that covers a control below it. Not a failure if the user can close it without moving focus.

## How to meet it

- Technique C43, "Using CSS scroll-padding to un-obscure content": set `scroll-padding-top` and `scroll-padding-bottom` on the scroll container to the height of the fixed bars.
- Keep fixed and sticky elements small, or make them non-fixed at small viewports (Technique C34 in the 1.4.10 entry).
- Test by tabbing through the page with the window short enough that sticky elements matter.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.4.7 Focus Visible (entry in this package). An indicator exists; this says it must not be covered.
- SC 2.4.12 Focus Not Obscured (Enhanced) is Level AAA and requires no part be hidden; not a requirement here.
- SC 1.4.10 Reflow (`wcag/sc-1.4.10-reflow.md`). Sticky elements take up more of the viewport at high zoom.
- SC 1.4.13 Content on Hover or Focus (`wcag/sc-1.4.13-content-on-hover-or-focus.md`). Popups that appear on focus and may cover things.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Obscured focus is observed by tabbing with sticky elements present, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
