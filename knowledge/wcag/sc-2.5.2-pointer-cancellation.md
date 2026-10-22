# SC 2.5.2 Pointer Cancellation

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.5 Input Modalities
- Tier 1 source: https://www.w3.org/TR/WCAG22/#pointer-cancellation
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> For functionality that can be operated using a single pointer, at least one of the following is true:
>
> **No Down-Event.** The down-event of the pointer is not used to execute any part of the function;
>
> **Abort or Undo.** Completion of the function is on the up-event, and a mechanism is available to abort the function before completion or to undo the function after completion;
>
> **Up Reversal.** The up-event reverses any outcome of the preceding down-event;
>
> **Essential.** Completing the function on the down-event is essential.
>
> Note 1: Functions that emulate a keyboard or numeric keypad key press are considered essential.
>
> Note 2: This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

## What it requires, in our words

Actions should happen when the finger or mouse button comes up, not when it goes down, so that a person who presses the wrong thing can slide off before releasing and nothing happens. Native buttons and links already work this way. The failure is script that fires on `mousedown`, `touchstart`, or `pointerdown`. If something must fire on the down event, there has to be a way to abort or undo it. An on-screen keyboard key is allowed to fire on press because that is how physical keys behave.

## How it fails in code

- A control whose action runs on `mousedown`, `pointerdown`, or `touchstart` with no abort or undo. Definite. F101.
- A drag-and-drop that commits on the down event with no way to cancel. Definite. G210 is the fix.
- A long-press that triggers irreversibly. Definite.
- An on-screen piano or keyboard that sounds on press. Passes; essential by Note 1.
- Native `button` and `a` elements with `click` handlers. Pass; click fires on up.

## How to meet it

- Technique G212, "Using native controls to ensure functionality is triggered on the up-event": a `button` with a `click` handler, not a `div` with `mousedown`.
- Technique G210, "Ensuring that drag-and-drop actions can be cancelled": releasing outside a target, or pressing Escape, aborts the drop.
- If a down-event action is unavoidable, provide an undo.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.5.1 Pointer Gestures and 2.5.7 Dragging Movements (entries in this package). The other single-pointer requirements.
- SC 3.3.4 Error Prevention (Legal, Financial, Data) (no entry yet). Reversibility of consequential actions.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Which event fires an action is found by reading the script. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
