# SC 2.5.1 Pointer Gestures

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.5 Input Modalities
- Tier 1 source: https://www.w3.org/TR/WCAG22/#pointer-gestures
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> All functionality that uses multipoint or path-based gestures for operation can be operated with a single pointer without a path-based gesture, unless a multipoint or path-based gesture is essential.
>
> Note: This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

## What it requires, in our words

Anything done with a two-finger pinch, a swipe, or a drawn path must also be doable with simple taps or clicks. Pinch-to-zoom on a map needs plus and minus buttons. A swipe-to-advance carousel needs next and previous buttons. A slider you drag needs to accept a click on the track or have arrow buttons. People using a head pointer, a mouth stick, a single switch, or a mouse with a tremor can tap but cannot swipe or pinch. The exception is a gesture that is the function itself, such as drawing a signature. Browser-level gestures like page zoom are not covered.

## How it fails in code

- A carousel, image gallery, or tab set that advances only on swipe, with no buttons. Definite. F105.
- A map or image viewer that zooms only on pinch, with no zoom controls. Definite. F105.
- A slider that responds only to drag, with no click-on-track, arrow buttons, or text input. Definite under this criterion and 2.5.7.
- A canvas that requires drawing a shape to unlock something. Definite unless the shape itself is essential; manual review.
- Swipe present alongside buttons. Passes; the gesture is an extra.

## How to meet it

- Technique G215, "Providing controls to achieve the same result as path based or multipoint gestures": visible buttons for every gesture.
- Technique G216, "Providing single point activation for a control slider".
- Native HTML `input type="range"` accepts clicks and arrow keys.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.5.7 Dragging Movements (entry in this package). The WCAG 2.2 criterion for drag specifically.
- SC 2.1.1 Keyboard (entry in this package). The keyboard route is usually the same control.
- SC 2.5.2 Pointer Cancellation (entry in this package). Whether the single-pointer action can be undone.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Gestures live in script and are found by reading it or trying the interface by tap alone. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
