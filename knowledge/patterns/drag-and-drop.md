# Pattern: Drag and drop

- Sources:
  - W3C, ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/. Tier 2. The guide publishes no drag-and-drop pattern; checked 2026-10-22.
  - W3C, "Accessible Rich Internet Applications (WAI-ARIA) 1.2", sections on `aria-grabbed` and `aria-dropeffect`, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/#aria-grabbed. Tier 1. Both attributes are marked deprecated since ARIA 1.1, with a note that a replacement is expected in a future version.
  - No practitioner on `knowledge/SOURCES.md` was found to have published tested drag-and-drop results when searched 2026-10-22. This entry rests on the WCAG entries and the ARIA status above, and says so.
- Related entries: `coga/objective-6-do-not-rely-on-memory.md`, `wcag/sc-2.5.7-dragging-movements.md`, `wcag/sc-2.5.1-pointer-gestures.md`, `wcag/sc-2.5.2-pointer-cancellation.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-4.1.3-status-messages.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the interaction is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer. This entry has no tested practitioner source yet; when one is admitted to the sources list, add it here.

## The need it usually serves

Reorder a list, move an item between groups, upload a file, place something on a canvas, set a range. The person wants the thing moved. Dragging is one way to say "move this there"; it is rarely the only way the person would accept.

## The simpler thing that often serves, and what is lost

Buttons and menus that do the same move: up and down arrows beside each item, a "move to" menu, a file chooser button, a numeric field for a position. The 2.5.7 entry requires a single-pointer, non-drag alternative at Level AA in any case, so the alternative has to be built regardless; the question is only whether drag is added on top. What is lost by not building drag: the directness and the visual flourish. What is gained: an interaction that works for keyboard, switch, voice, and tremor, and that can be announced because each step is a discrete action. `coga/objective-6-do-not-rely-on-memory.md` applies when a drag requires holding a target in mind across a long move.

## What doing it right requires

Native HTML has a drag-and-drop API for pointer events and a file `input` for uploads; neither supplies a keyboard or assistive-technology path by itself. The ARIA attributes that once described drag state are deprecated, so there is no ARIA vocabulary to reach for, and the APG publishes no pattern. That leaves a design built from parts that do have patterns: buttons with names that say what they move and where; a listbox or grid for selection where ordering matters; a live region that announces each move's result (`wcag/sc-4.1.3-status-messages.md`); and Escape or an undo to cancel, which the 2.5.2 entry requires for pointer operations that commit on release.

Honest statement of the gap: there is no settled, tested reference for keyboard-accessible drag and drop on the sources list. Treat any library's claim of accessibility as unverified until the project tests it with the assistive technology in its spec.

## What practitioners found when they tested it

No entry yet. No tested results from a practitioner on `knowledge/SOURCES.md` were found. Proposing a source is a pull request to the sources list under its admission rule.

## Criteria it touches

The alternative to dragging: `wcag/sc-2.5.7-dragging-movements.md`, `wcag/sc-2.5.1-pointer-gestures.md`. Cancelling a drag before release: `wcag/sc-2.5.2-pointer-cancellation.md`. Keyboard operation of the whole thing: `wcag/sc-2.1.1-keyboard.md`. Names, roles, and states on handles and targets: `wcag/sc-4.1.2-name-role-value.md`. Announcing the result of a move: `wcag/sc-4.1.3-status-messages.md`. Focus after a move: `wcag/sc-2.4.3-focus-order.md`. Handle and target size: `wcag/sc-2.5.8-target-size-minimum.md`. Drop targets shown by more than color: `wcag/sc-1.4.1-use-of-color.md`, `wcag/sc-1.4.11-non-text-contrast.md`. Undo for consequential moves: `wcag/sc-3.3.4-error-prevention-legal-financial-data.md`.

## Manual tests it demands

- Pointer: start a drag, move off target, release; record whether the move is cancelled. Press Escape mid-drag; record the result.
- Keyboard only: perform every move the drag allows using the alternative controls; record any move that cannot be done.
- Screen reader, each pair in the spec: perform a move with the alternative controls; record what is announced about the result and where focus lands.
- Voice control: say the name of a move control; record whether it activates.
- Touch: record whether the drag alternative is reachable and sized at 24 CSS pixels.

## What consult should say

1. What is the move, in words? "Move item 3 above item 2." Build the control that says that.
2. Who, in the spec, cannot drag? Keyboard, switch, voice, and tremor users are usually in it.
3. If drag stays: it is an extra on top of working buttons, it cancels on Escape and on release off-target, every move is announced, and the project tests it with its own AT list because no tested reference exists.
