# Eval 019: test script for a confirmation dialog

Input: `request.md`. A developer describes a native modal dialog for a destructive action and asks for the manual test script. The spec names five modes: NVDA with Firefox, VoiceOver with Safari on macOS, keyboard only, 200% and 400% zoom, reduced motion. Forced colors is not on the list.

Intended outcome: a numbered script, grouped by the spec's modes, built from `knowledge/testing/` and `knowledge/patterns/modal-dialog.md`, that tells a tester what to do and what to check, and never says what a user would experience.

## Expected

1. **Uses the spec's list and only that.** Sections for keyboard only, NVDA with Firefox, VoiceOver with Safari on macOS, zoom, and reduced motion. No section for modes not on the list (forced colors, TalkBack, JAWS), though a one-line note that they are not on the list is fine.
2. **Opens the pattern entry.** Steps drawn from `patterns/modal-dialog.md`'s manual tests: where focus lands on open, that focus cannot reach the page behind, Escape closes, focus returns to the trigger.
3. **Keyboard steps are concrete:** open from the "Delete" button; note focus lands on "Cancel"; Tab and Shift+Tab never reach the page behind; Escape closes and focus returns to that row's "Delete" button; "Delete search" works with Enter and Space; focus is visible on every stop. Each tied to the right entry (`wcag/sc-2.1.1-keyboard.md`, `sc-2.1.2-no-keyboard-trap.md`, `sc-2.4.3-focus-order.md`, `sc-2.4.7-focus-visible.md`).
4. **Screen reader steps, both platforms:** on open, note what is announced (the dialog's role and name, and whether the explanatory sentence is read); check that the virtual cursor (NVDA) or VO navigation cannot leave the dialog; after deleting, note whether "Saved search deleted" is announced without focus moving there (`wcag/sc-4.1.3-status-messages.md`); setup notes from the testing entries (Speech Viewer for NVDA; Safari and Tab settings for VoiceOver).
5. **Zoom:** at 200%, the dialog's text and both buttons can be read and used with nothing lost (`wcag/sc-1.4.4-resize-text.md`); at 400% (or 320 CSS pixels), the same without two-way scrolling (`wcag/sc-1.4.10-reflow.md`).
6. **Reduced motion:** the 300 ms fade is an opacity change, which WCAG's definition of motion animation excludes, so it is outside SC 2.3.3. The script may note the fade with the setting on as an optional observation, but must not treat it as a 2.3.3 check or a WCAG failure. Saying the component has no motion animation to test is also correct.
7. **What to record:** versions of the screen readers and browsers, what was done, what was heard (Speech Viewer text for NVDA), pass or fail, and the tester.
8. **Never speaks as a user.** No "the user will hear", "would experience", or predicted announcements. Checks are phrased as "note what is announced" or "check that".

## Also acceptable

- A note for the developer, outside the script, that the native element lets Tab reach the browser's own controls and that this is not a failure (from `patterns/modal-dialog.md`).
- Proposing to add the script to the spec's "Open manual tests" with an owner.
- Including the warning that a tester new to a screen reader can mistake unfamiliarity for a defect.
- A step for where focus goes after "Delete search" removes the row and its "Delete" button, since the trigger no longer exists.

## Must not

- Write or change code.
- Include a forced colors or TalkBack section as if it were on the spec's list.
- Predict what a screen reader will say, or describe what a user would experience.
- State a criterion number, title, level, or keyboard command not found in the entries without marking it unverified.
- Treat the opacity fade as motion animation under SC 2.3.3, or mark any reduced-motion result as a WCAG AA failure.

## Pass condition

Items 1 to 5, 7, and 8 are present, item 6 is not contradicted, and nothing from the Must not list appears.
