# Pattern: Drag and drop

- W3C pattern (tier 2): none. The ARIA Authoring Practices Guide publishes no drag-and-drop pattern; its patterns index was checked 2026-10-22. https://www.w3.org/WAI/ARIA/apg/patterns/
- W3C specification (tier 1): "Accessible Rich Internet Applications (WAI-ARIA) 1.2", W3C Recommendation 6 June 2023, sections on `aria-grabbed` and `aria-dropeffect`. https://www.w3.org/TR/wai-aria-1.2/#aria-grabbed Both are marked deprecated since ARIA 1.1, with a note that a replacement is expected in a future version. There is no current ARIA vocabulary for drag and drop.
- W3C tutorial: none.
- Practitioner testing (tier 3): none found. No practitioner on `knowledge/SOURCES.md` was found to have published tested drag-and-drop results when searched 2026-10-22.
- Related entries: `wcag/sc-2.5.7-dragging-movements.md`, `wcag/sc-2.5.1-pointer-gestures.md`, `wcag/sc-2.5.2-pointer-cancellation.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-4.1.3-status-messages.md`, `coga/objective-6-do-not-rely-on-memory.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own.

**Testing gap.** No source on the list reports testing drag and drop with assistive technology, in any year. There is no Authoring Practices pattern to depart from and no ARIA state to expose. Treat any library's claim of accessible drag and drop as unverified until the project tests it with the assistive technology in its spec. Do not fill the gap with sources off the list; proposing one is a pull request to `knowledge/SOURCES.md` under its admission rule.

## The need

Reorder a list, move an item between groups, upload a file, place something on a canvas, set a range. The person wants the thing moved. Dragging is one way to say "move this there"; it is rarely the only way the person would accept. `coga/objective-6-do-not-rely-on-memory.md` applies when a drag requires holding a target in mind across a long move.

## The simpler alternative and its cost

Buttons and menus that make the same move: up and down arrows beside each item, a "move to" menu, a file chooser button, a numeric field for a position. `wcag/sc-2.5.7-dragging-movements.md` requires a single-pointer, non-drag alternative at Level AA in any case, so the alternative has to be built regardless; the question is only whether drag is added on top. What is lost by not building drag: the directness and the visual flourish. What is gained: an interaction that works for keyboard, switch, voice, and tremor, and that can be announced because each step is a discrete action.

## What doing it right requires

Native HTML has a drag-and-drop API for pointer events and a file `input` for uploads; neither supplies a keyboard or assistive-technology path by itself. With the ARIA drag attributes deprecated and no Authoring Practices pattern, a correct build is assembled from parts that do have patterns and entries: buttons with names that say what they move and where (`wcag/sc-4.1.2-name-role-value.md`); a listbox or grid for selection where ordering matters; a live region that announces each move's result (`wcag/sc-4.1.3-status-messages.md`); focus kept on or returned to the moved item (`wcag/sc-2.4.3-focus-order.md`); and Escape or an undo to cancel, which `wcag/sc-2.5.2-pointer-cancellation.md` requires for pointer operations that commit on release. Drag, if kept, is an extra on top of working controls.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 2.5.7 | Dragging Movements | AA | `wcag/sc-2.5.7-dragging-movements.md` | A non-drag single-pointer alternative is required |
| 2.5.1 | Pointer Gestures | A | `wcag/sc-2.5.1-pointer-gestures.md` | Path-based gestures need a simple alternative |
| 2.5.2 | Pointer Cancellation | A | `wcag/sc-2.5.2-pointer-cancellation.md` | Cancelling a drag before release; undo after |
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Every move possible from the keyboard |
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Names and states on handles, targets, and move controls |
| 4.1.3 | Status Messages | AA | `wcag/sc-4.1.3-status-messages.md` | Announcing the result of a move |
| 2.4.3 | Focus Order | A | `wcag/sc-2.4.3-focus-order.md` | Where focus goes after a move |
| 2.5.8 | Target Size (Minimum) | AA | `wcag/sc-2.5.8-target-size-minimum.md` | Handles, targets, and move buttons |
| 1.4.1 | Use of Color | A | `wcag/sc-1.4.1-use-of-color.md` | Drop targets shown by more than color |
| 1.4.11 | Non-text Contrast | AA | `wcag/sc-1.4.11-non-text-contrast.md` | Drop target and handle boundaries |
| 3.3.4 | Error Prevention (Legal, Financial, Data) | AA | `wcag/sc-3.3.4-error-prevention-legal-financial-data.md` | Undo for moves that change stored data |

## Manual tests

- Pointer: start a drag, move off target, release; record whether the move is cancelled. Press Escape mid-drag; record the result.
- Keyboard only: perform every move the drag allows using the alternative controls; record any move that cannot be done.
- Screen reader, each pair in the spec: perform a move with the alternative controls; record what is announced about the result and where focus lands.
- Voice control: say the name of a move control; record whether it activates.
- Touch: record whether the drag alternative is reachable and sized at 24 CSS pixels.
