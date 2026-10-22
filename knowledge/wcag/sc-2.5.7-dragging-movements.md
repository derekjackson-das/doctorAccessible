# SC 2.5.7 Dragging Movements

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 2 Operable / 2.5 Input Modalities
- Tier 1 source: https://www.w3.org/TR/WCAG22/#dragging-movements
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- Also in: WCAG 2.2 only. New in 2.2; not in 2.0 or 2.1.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging, unless dragging is essential or the functionality is determined by the user agent and not modified by the author.
>
> Note: This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

## What it requires, in our words

Anything a person does by pressing, moving, and releasing, such as reordering a list, moving a card between columns, drawing a selection box, or setting a slider, must also be doable with plain clicks or taps. Dragging demands holding a button down while moving precisely, which many people with motor disabilities cannot do. The alternative can be anything that works without a drag: up and down buttons, a "move to" menu, a text field for the value. Dragging may stay as a shortcut. Browser-native drags such as scrollbars and text selection are exempt, and so is a function where the drag is the point, such as a drawing tool.

## How it fails in code

- A sortable list, kanban board, or file-upload area where drag is the only way to move or add items. Definite. F108.
- A slider that can only be dragged, with no click-on-track, no arrows, and no text input. Definite; also 2.5.1.
- A map that pans only by drag, with no pan buttons. Definite.
- Drag with keyboard support but no single-pointer alternative. Still a failure; the keyboard path meets 2.1.1, not this.
- A signature pad. Not a failure; essential.

## How to meet it

- Technique G219, "Ensuring that an alternative is available for dragging movements that operate on content": buttons, menus, or inputs that reach the same result.
- Native HTML `input type="range"` accepts clicks on the track.
- The `patterns` entry for drag and drop, when it exists, carries the fuller discussion of when drag is worth building at all.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.5.1 Pointer Gestures (entry in this package). Path-based gestures in general; drag is one.
- SC 2.5.2 Pointer Cancellation (entry in this package). Cancelling a drag before release.
- SC 2.1.1 Keyboard (entry in this package). Keyboard alternative is required separately.
- SC 2.5.8 Target Size (Minimum) (entry in this package). The alternative buttons must be big enough.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Drag handlers are found by reading the script or trying the interface with taps only. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
