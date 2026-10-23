# SC 2.1.1 Keyboard

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.1 Keyboard Accessible
- Tier 1 source: https://www.w3.org/TR/WCAG22/#keyboard
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes, except where the underlying function requires input that depends on the path of the user's movement and not just the endpoints.
>
> Note 1: This exception relates to the underlying function, not the input technique. For example, if using handwriting to enter text, the input technique (handwriting) requires path-dependent input but the underlying function (text input) does not.
>
> Note 2: This does not forbid and should not discourage providing mouse input or other input methods in addition to keyboard operation.

## What it requires, in our words

Everything a person can do with a mouse, they must be able to do with a keyboard: reach it, operate it, and leave it, without having to press keys at a particular speed. Many people cannot use a pointing device at all, and screen readers, switch devices, and voice control all drive the page through the keyboard interface. The only exception is a function whose meaning is the path itself, such as freehand drawing. Native HTML controls are keyboard operable by default. The failures come from custom controls built on `div` and `span` with mouse-only event handlers.

## How it fails in code

- A clickable element that only has a mouse event handler (`click`, `mousedown`, `mouseover`) and is not a native interactive element, so Enter and Space do nothing. Definite. F54.
- A custom control with `role="button"` and `tabindex="0"` but no key handler, so it can be focused but not activated. Definite. F54.
- A `div` or `span` acting as a link or button with no `tabindex`, so it cannot be reached at all. Definite, and also a 4.1.2 defect; see that entry for how to report once. F42.
- Controls taken out of the tab order with `tabindex="-1"` and given no other keyboard route, such as inactive tabs in a roving tabindex with no arrow-key handler (`aria/patterns/tabs.md`). Definite.
- Script that moves focus away from an element as soon as it receives it. Definite. F55.
- A hover-only menu whose items appear on `mouseover` and have no focus equivalent. Definite.
- Drag-and-drop as the only way to reorder or move items. Definite under this criterion; also 2.5.7.
- A server-side image map, where the click coordinates are the function. Definite.
- A freehand signature or drawing canvas with no keyboard alternative. Not a failure; path-dependent by exception. Manual review to confirm.

## How to meet it

- Native HTML first. Technique H91, "Using HTML form controls and links": a `button` is focusable and fires on Enter and Space without any script.
- Technique G202, "Ensuring keyboard control for all functionality".
- Technique G90, "Providing keyboard-triggered event handlers": when a custom control is unavoidable, handle `keydown` for Enter and Space alongside `click`, and give it `tabindex="0"`.
- Advisory: Technique SCR29, "Adding keyboard-accessible actions to static HTML elements".

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.1.2 No Keyboard Trap (entry in this package). Getting out, as distinct from getting in.
- SC 2.4.3 Focus Order and 2.4.7 Focus Visible (entries in this package). Where focus goes and whether you can see it.
- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). A clickable `div` fails both; report once and name both.
- SC 2.5.7 Dragging Movements (entry in this package). Drag as the only method.
- SC 2.1.3 Keyboard (No Exception) is Level AAA and not a requirement here.

## Automated coverage (tier 3)

axe-core tags `scrollable-region-focusable`, `frame-focusable-content`, and `server-side-image-map` to this criterion. It does not detect a clickable `div` with no key handler, which is the common failure; that is found by reading the script or by tabbing through the page. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
