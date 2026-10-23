# Run 2026-10-23: verifier on eval 028

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit 3e395e0.
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, SC 2.4.3 Focus Order (Level A), tier 1, at likely, on `openDialog()`, citing the 2.4.3 entry, `aria/patterns/modal-dialog.md`, and the WAI-ARIA 1.2 "should": present.
- Fix direction: focus Cancel, the least destructive control, or use `showModal()`. Acceptable.
- Must not: nothing from the list. Role, name, description, `aria-modal`, keyboard trap, focus return, contrast, and headings were checked and not reported.
- Also acceptable, used: manual keyboard and screen reader tests of where focus lands; a note that axe has no rule for 2.4.3.

## The report, as given

## Checked
`evals/028-aria-dialog-focus-not-moved/input.html` (59 lines: HTML, inline CSS, inline script). I read the whole file myself. axe was not run (see Automated scan). The repo has no `a11y-spec.md`, neither at the root nor in `docs/`, so I checked against WCAG 2.2 AA alone, plus the house defaults in `docs/content-standards.md`.

Entries opened: `knowledge/INDEX.md`, `.claude/skills/wcag/SKILL.md`, `wcag/sc-2.4.3-focus-order.md`, `aria/patterns/modal-dialog.md`, `patterns/modal-dialog.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-1.4.3-contrast-minimum.md`, `wcag/sc-1.4.11-non-text-contrast.md`, `wcag/sc-2.5.8-target-size-minimum.md`.

## Findings

### [Likely] Focus is not moved into the modal dialog when it opens
- Where: input.html lines 40-43, `openDialog()`. It is the handler for `#delete-trigger` (line 51), which opens the dialog at lines 24-33.
- What: `openDialog()` un-hides the `role="dialog" aria-modal="true"` container and makes `#page` inert, but it never calls `focus()` on anything inside the dialog. Focus is left on the trigger, which is now inside an inert subtree, or it is lost to the document.
- Criterion: WCAG 2.2 SC 2.4.3 Focus Order (Level A), W3C Rec 12 Dec 2024, tier 1.
- Source: knowledge/wcag/sc-2.4.3-focus-order.md ("Focus not moved into a modal when it opens ... Definite once observed"); knowledge/aria/patterns/modal-dialog.md (a dialog with `aria-modal="true"` whose script never moves focus in on open is "likely from code, definite once observed"). Supporting, tier 1: the WAI-ARIA 1.2 `dialog` role says authors should focus an element in a modal dialog when it is displayed. Supporting, tier 2: the APG says that for an action that is hard to undo, focus goes to the least destructive control.
- Fix direction: On open, move focus into the dialog. For this irreversible delete, the entries point to the least destructive control (Cancel). Alternatively, use a native `<dialog>` opened with `showModal()`.

No other defects found. Checks that passed in the code:
- **Contrast.** I computed the ratios from the declared hex colors, using the relative-luminance formula. Body text #1a1a1a on #fff is about 17.4:1. Button text, button border and focus outline #005a9c on #fff are about 7.1:1. Both are above the 4.5:1 (SC 1.4.3) and 3:1 (SC 1.4.11) thresholds in the entries.
- **Target size.** I estimated button size from the CSS, assuming the browser default 16px font: 1.5 line-height plus 0.5rem padding plus a 2px border gives roughly 44px tall. That is above the 24 by 24 CSS px floor in the SC 2.5.8 entry. Confirm the rendered size.
- **Keyboard trap.** Escape closes the dialog (lines 54-56) and both buttons close it, so SC 2.1.2 is met.
- **Name and description.** The dialog takes its name from `aria-labelledby` pointing at the visible h2. Its `aria-describedby` points at a single short paragraph, which the APG allows.
- **Focus on close.** Focus returns to the trigger (line 48).
- **Page behind.** It is made inert while the dialog is open.

## Content
- Reading level: not measured. There is no spec target. The house default is Flesch-Kincaid grade 8 or below, and no measuring tool was used in this run. The text is three short sentences plus button labels. A human should read it.
- Headings: the h1 "Shared files" and the h2 "Delete this file?" both describe their content, and no levels are skipped.
- Button labels: "Delete Budget-2026.xlsx", "Cancel" and "Delete" say what they do.
- Links, images, alt text, error messages: none present.
- Language: `lang="en"` is declared.

## Spec deviations
No `a11y-spec.md` exists at the repo root or in `docs/`. Nothing to compare against.

## Manual checks remaining
- **Keyboard only.** Activate "Delete Budget-2026.xlsx". Record where focus lands, and whether a focus indicator is visible. Then press Tab once and record which element receives focus.
- **Keyboard only.** Tab and Shift+Tab through the open dialog. Record whether focus ever reaches `#page` content. Reaching the browser's own controls is acceptable per `patterns/modal-dialog.md`.
- **Keyboard only.** Press Escape, then repeat using Cancel and using Delete. Record where focus goes each time; the code sends it to the trigger.
- **Screen reader** (no spec names one; the INDEX lists NVDA on Windows and VoiceOver on macOS and iOS):
  - Open the dialog and record what is announced, and whether the role, name and description are conveyed.
  - Try to reach the page behind with the virtual cursor, and on iOS by swiping, and record the result. The entry notes that VoiceOver on iOS 15 could leave `aria-modal` dialogs.
- **Voice control.** Activate "Cancel" and "Delete" by their visible names.
- **Zoom.** At 400% and at a narrow window width, confirm all dialog content and both buttons can be reached.

## Automated scan
Not run. axe cannot run on this machine because Node.js is not installed, so `npx @axe-core/cli` is unavailable. No browser was available either. The planned command was `npx --yes @axe-core/cli --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`. axe has no rule tagged to SC 2.4.3, so the main finding would need a manual check even if axe ran.
