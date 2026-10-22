# AT test protocol run, 2026-10-22, eval 019

Method: a general-purpose agent read `.claude/skills/at-test-protocol/SKILL.md` at commit de80924 and followed it, then answered `request.md`. `expected.md`, run files, and `RESULTS.md` were off limits, and it wrote no files. This is a prompt test of the skill text, not a fresh-session load, the same method as the consult and planning runs.

Result against `expected.md`: **pass**.

- **Modes:** sections for exactly the spec's five: NVDA with Firefox, VoiceOver with Safari on macOS, keyboard only, zoom, reduced motion. No forced colors section.
- **Pattern entry:** steps taken from `patterns/modal-dialog.md`. Tab reaching the browser's own controls is accepted for a native dialog, and the page behind must never be reached.
- **Keyboard:** concrete steps:
  - open with Enter and with Space;
  - focus lands on Cancel;
  - Tab and Shift+Tab stops are written down;
  - Escape and Cancel return focus to the trigger;
  - focus is visible and not obscured.

  Each step is tied to its entry.
- **Screen readers:** setup from the testing entries (Speech Viewer, Safari's Tab setting). The steps check the dialog's role and name on open, whether the explanatory sentence can be read, that the virtual cursor cannot reach the page behind, and that the status message is announced while focus stays put.
- **Zoom:** 200% and 400% split correctly: 1.4.4 at 200%, 1.4.10 at 400%.
- **Reduced motion:** the fade sorted as opacity only, outside SC 2.3.3, with C39's check applied only to anything that is motion.
- **Recording:** fields per mode, including versions, Speech Viewer text, and whether the tester is a daily user.
- **Principle 7:** "note what is announced" throughout; no predicted announcements in the script.

Also covered, from the "also acceptable" list: focus after "Delete search" removes its own trigger, as a script step and a developer note. Developer notes were kept outside the script.

Nothing from the Must not list.
