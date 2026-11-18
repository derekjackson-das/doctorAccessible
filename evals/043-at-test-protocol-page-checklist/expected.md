# Eval 043: manual testing checklist for a whole page

Input: `request.md`. A developer pastes a small page and asks for a manual testing checklist with expected outcomes. The page has three parts: a "More actions" menu button on each list row, a native rename dialog opened with `showModal()`, and a "Report deleted" notice with Undo that hides after 5 seconds. There is no spec. The code holds several likely problems on purpose, so the eval can tell whether they land in the Watch for section and stay out of the checklist items. This eval tests the checklist shape, not one defect.

Intended outcome: a checklist in the shape of `templates/at-test-checklist.md`, built from `knowledge/testing/` and `knowledge/patterns/modal-dialog.md`, with a pass condition and an entry on every item, followed by a separate Watch for section that points each likely problem at the item that confirms it.

## Expected

1. **No spec, said plainly.** The answer says there is no `a11y-spec.md`, proposes a list of modes marked as a proposal or "to confirm", and suggests the `planning` skill or a spec. The list fits a macOS developer: at least keyboard only and VoiceOver with Safari.
2. **Checklist shape.** Items are tick boxes (`- [ ]`). Each item says what to do and gives an "Expected" pass condition with a `wcag/` entry, or is marked manual review. Items are grouped by mode, then by part of the page.
3. **Keyboard items are concrete for this page:**
   - open "More actions"; Escape closes the menu and focus returns to the "More actions" button that opened it (`wcag/sc-2.4.3-focus-order.md`);
   - Tab out of the open menu, and the menu does not stay open over other content (or a no-trap check, `wcag/sc-2.1.2-no-keyboard-trap.md`);
   - the rename dialog: where focus lands on open, Tab and Shift+Tab never reach the page behind, Escape and Cancel close it, focus returns to the trigger (`patterns/modal-dialog.md`);
   - after Delete removes the row, focus lands somewhere sensible, not lost to the top of the page;
   - Undo can be reached by keyboard before the notice hides, or the 5-second limit can be changed (`wcag/sc-2.2.1-timing-adjustable.md`);
   - Enter and Space on each control by name: More actions, Rename, Delete, Cancel, Save, Undo (`wcag/sc-2.1.1-keyboard.md`).
4. **Screen reader items:** setup from `knowledge/testing/screen-reader-apple.md` (Safari, Tab setting); the "More actions" button's name and role, and whether its name says which report it acts on; the dialog's role and name on open; "Report deleted" announced while focus stays put (`wcag/sc-4.1.3-status-messages.md`); the warning that a tester's unfamiliarity can look like a defect.
5. **Zoom items** at 200% and 400%, tied to `wcag/sc-1.4.4-resize-text.md` and `wcag/sc-1.4.10-reflow.md`, including the menu and dialog at 400%.
6. **A Watch for section, separate from the items,** that names at least three of these, each with a place in the code and the checklist item that confirms it:
   - Escape hides the menu without returning focus to the "More actions" button;
   - the notice is not a live region, so "Report deleted" may not be announced;
   - Delete removes the row that held focus and does not move focus;
   - Undo hides after 5 seconds and focus is not moved to it;
   - every "More actions" button has the same name, with no report name;
   - `aria-haspopup="menu"` with plain buttons and no menu role or arrow keys;
   - the dialog's heading is not tied to it as its name.
7. **Items stay neutral.** No checklist item says it will fail. Predictions belong only in the Watch for section, which says these are leads, not results.
8. **Gaps:** no pattern entry for a menu button or for the notice; the proposed list is unconfirmed.
9. **Never speaks as a user.** No "the user will hear", "would experience", or predicted announcements in the items.
10. **The save step.** The answer offers the checklist as a file and asks where it should live, or offers a place outside the repo. It does not claim to have written it into a repo.

## Also acceptable

- A reduced motion section that says there is no motion to test, or leaving it out with one line saying why.
- A forced colors section marked as manual review, with Edge emulation named as a first pass on macOS.
- Proposing an `a11y-spec.md` and adding the checklist to its "Open manual tests".
- A "What to record" section.

## Must not

- Write or change code, or offer fixed code.
- State a criterion number, title, level, or keyboard command not found in the entries without marking it unverified.
- Present the proposed modes as the project's confirmed list.
- Put an expected failure in a checklist item, such as "Expected: focus is lost" or "this will fail".
- Predict what a screen reader will say.

## Pass condition

Items 1 to 7 and 9 are present, items 8 and 10 are not contradicted, and nothing from the Must not list appears.
