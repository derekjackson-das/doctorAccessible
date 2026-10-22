# Eval 011 verifier run, 2026-10-22

Blind run. The verifier was a general-purpose agent given `.claude/agents/verifier.md` (commit f93f693) as its instructions, told not to open `expected.md`, `RESULTS.md`, any other file under `evals/`, or git history. Report as returned, scratch paths shortened.

## Checked
- File: `evals/011-silent-save-message/input.html` (39 lines: an email preferences form with three checkboxes in a fieldset, a "Save preferences" button, and an empty `<p id="save-msg">` that a click handler fills).
- Method: I read the whole file, and I ran axe-core.
- Project spec: there is no `a11y-spec.md` at the repo root or in `docs/`, so the page was checked against WCAG 2.2 AA and `docs/content-standards.md` only.
- Knowledge entries opened: `knowledge/INDEX.md`, `wcag/sc-4.1.3-status-messages.md`, `wcag/sc-1.4.3-contrast-minimum.md`, `wcag/sc-2.5.8-target-size-minimum.md` and `wcag/sc-1.4.11-non-text-contrast.md`.

## Findings

### [Definite] Save confirmation is written into an element with no status role or live region
- Where: input.html line 30 (`<p id="save-msg" class="saved"></p>`), filled by the script at lines 34–36.
- What: Clicking "Save preferences" puts "Your preferences are saved." into a plain `<p>`. The `<p>` has no `role="status"`, `role="alert"`, `role="log"` or `aria-live`, and focus stays on the button. So assistive technology cannot programmatically determine this success message without the message receiving focus. The entry lists this pattern as failure F103.
- Criterion: WCAG 2.2 SC 4.1.3 Status Messages (Level AA), tier 1
- Source: knowledge/wcag/sc-4.1.3-status-messages.md
- Fix direction: Keep the container in the page from load, but give it `role="status"` (or make it an `<output>` element), and then change only its text when the user saves (techniques ARIA22 + G199).

No other defects found.

Checked and passing, with values I computed from the declared CSS:
- Text contrast against the `#fff` background: body text `#1a1a1a` is about 17.4:1, and the saved message `#1b5e20` is about 7.87:1. The 1.4.3 entry's threshold for normal text is 4.5:1.
- Focus outline: `#005a9c` against `#fff` is about 7.14:1. The 1.4.11 entry's threshold is 3:1.
- Focus is visible: there is an author `:focus-visible` outline.
- Checkboxes are 20px (1.25rem), but each sits inside a block label with 0.5rem padding. axe's `target-size` rule passed.

## Content
- Reading level: not measured. The page has under 20 words of body text, which is too little for a Flesch-Kincaid score to mean anything. By inspection the words are short and common.
- Headings: there is one `h1`, "Email preferences", which matches the `<title>` and says what the page is. That is consistent with the headings standard in content-standards.md (section 4).
- Labels: each checkbox has a visible label that wraps it. The legend "Send me" groups them and reads as a sentence with each label ("Send me Monthly newsletter"). This is judged acceptable, but marked manual review.
- Success message: "Your preferences are saved." is plain and clear. There are no error messages, links or images on the page.
- Language: `lang="en"` is declared.

## Spec deviations
None to report. The project has no `a11y-spec.md`.

## Manual checks remaining
- With a screen reader (for example NVDA + Firefox, JAWS + Chrome, VoiceOver + Safari on macOS and iOS): move to "Save preferences", activate it, and leave focus on the button. Record whether the confirmation text is conveyed without moving focus. Repeat after the fix. Also record whether a message is conveyed again when Save is pressed a second time with the same text, since the text does not change on a repeat click.
- Keyboard only: check the tab order (three checkboxes, then the button), that Space toggles each checkbox, that Enter or Space activates Save, and that the focus outline is visible on every control.
- Visually: check how the browser-default checkboxes render against white in the browsers you test. They are exempt from 1.4.11 because the author did not style their appearance, but confirm that author CSS for width and height did not change that.
- Zoom to 200% and test a 320px-wide viewport: confirm nothing is clipped and the message stays near the button.
- Product decision: should the message clear or update when checkboxes change after a save? This is a judgment call, not a WCAG failure.

## Automated scan
- axe-core 4.14.0 (via @axe-core/cli), in headless Chrome for Testing 156.0.8078.47.
- Command: `npx --yes @axe-core/cli "file://.../evals/011-silent-save-message/input.html" --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa --chrome-path <Chrome for Testing 156.0.8078.47> --chromedriver-path <matching chromedriver> --save axe.json --dir <scratch>`
- Results:
  - Violations: 0
  - Incomplete: 0
  - Passes: 11 (aria-hidden-body, button-name, color-contrast, document-title, form-field-multiple-labels, html-has-lang, html-lang-valid, label, meta-viewport, nested-interactive, target-size)
  - Inapplicable: 53
- This clean run says nothing about the 4.1.3 defect. The knowledge entry notes that axe-core 4.14.0 has no rule tagged for 4.1.3, and axe does not watch a message appear after a user action. The finding comes from reading the code.
- Isolation: I did not open `expected.md`, `RESULTS.md` or any other `evals/` file, I did not read git history, and I made no edits to the repository.

## Compared with `expected.md`

Pass. Finding 1 present with the right criterion, level, tier, source, and location. Nothing from the must-not list: no focus-move fix, no 4.1.2 finding, no reports on the clean parts, thresholds stated only from opened entries and marked as computed, manual checks written as test steps.
