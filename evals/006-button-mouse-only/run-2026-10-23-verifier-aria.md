# Run 2026-10-23: verifier on eval 006, after the ARIA foundation entries

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit f1d257c (adds `knowledge/aria/` and a row in the wcag skill map).
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- Why: a regression run. This page uses `role="button"`, so the new `aria/` entries could change the answer.
- axe: not run (Node.js not installed).
- Result: **pass.** One definite finding under SC 2.1.1 (Level A), with `aria/using-aria.md` rule 3 named as the cause; 4.1.2 explained as met; nothing from the must-not list.

## The report, as given

## Checked
`evals/006-button-mouse-only/input.html` (38 lines: inline CSS, markup, and inline script). I read all of it. axe was not run because Node.js and npx are not installed on this machine. There is no `a11y-spec.md` at the repo root or in `docs/`, so the page is checked against WCAG 2.2 AA alone.

Knowledge used: `knowledge/INDEX.md`, `.claude/skills/wcag/SKILL.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.4.3-contrast-minimum.md`, `wcag/sc-1.4.11-non-text-contrast.md`, `wcag/sc-2.4.7-focus-visible.md`, `wcag/sc-2.5.8-target-size-minimum.md`, `aria/using-aria.md`, `aria/aria-in-html.md`, `testing/keyboard-only.md`, and `docs/content-standards.md`.

## Findings
### [Definite] Custom button can be focused but not activated from the keyboard
- Where: `input.html` line 21, `span.toggle[role="button"][tabindex="0"]`, and the script on lines 27–36
- What: The toggle is a `span` with `role="button"` and `tabindex="0"`, but it has only an `onclick` handler and no key handler. A keyboard user can tab to it, but pressing Enter or Space does not open or close the syllabus.
- Criterion: WCAG 2.2 SC 2.1.1 Keyboard (Level A), W3C Rec 12 Dec 2024, tier 1. The entry lists this exact pattern as definite (failure F54). Cause: `aria/using-aria.md` rule 3, which says a role is a promise of keyboard behavior; for `role="button"` that means Enter and Space (tier 2, historical W3C guidance). This defect is reported once, here.
- Source: knowledge/wcag/sc-2.1.1-keyboard.md
- Fix direction: Use a native `button` element, which already responds to Enter and Space (technique H91). If a custom element must stay, handle `keydown` for both keys alongside `click` (technique G90).

### [Likely] None.
### [Manual review] None beyond the checks listed below.

Checked and passing on reading:
- **SC 4.1.2 Name, Role, Value (Level A).** The toggle has role `button`, gets its name from its text, and the script updates `aria-expanded` on each click.
- **SC 2.4.7 Focus Visible (Level AA).** `:focus-visible` draws a 3px solid outline in #005a9c.
- **SC 1.4.3 Contrast (Minimum) (Level AA)**, threshold 4.5:1 for normal text. These ratios are my own calculations from the declared colors:
  - #005a9c text on #fff: about 7.1:1
  - #005a9c text on the #e8f1f8 hover background: about 6.2:1
  - #1a1a1a body text on #fff: about 17.4:1
- **SC 1.4.11 Non-text Contrast (Level AA)**, threshold 3:1. The #005a9c border and focus outline against #fff come to about 7.1:1, calculated the same way.
- **SC 2.5.8 Target Size (Minimum) (Level AA)**, threshold 24 by 24 CSS pixels. My estimate from the CSS (0.5rem / 1rem padding, a 2px border, default font size) is well above that. Confirm it on the rendered page.

## Content
- **Reading level:** not measured. No readability tool is available here, and the page has only two short body paragraphs.
- **Headings:** one `h1`, "Course details", which matches the `<title>`. One `h2`, "Syllabus". No levels are skipped and both headings describe their section (content standards section 4).
- **Control label:** "Show syllabus" / "Hide syllabus" says what the control does.
- **Language:** `lang="en"` is declared.
- **Links, images, error messages:** the page has none.

## Spec deviations
None can be assessed, because the project has no `a11y-spec.md`.

## Manual checks remaining
- **Keyboard only** (`testing/keyboard-only.md`):
  - Tab to the toggle and confirm the focus outline is visible.
  - Press Enter, then Space. Record whether the syllabus panel opens and closes, and whether the text changes between "Show syllabus" and "Hide syllabus".
  - Record where focus is after each key press, and confirm Tab and Shift+Tab leave the control.
- **Screen reader** (`testing/screen-reader-windows.md`, and `testing/screen-reader-apple.md` if relevant):
  - Move to the toggle. Record the role, name, and expanded or collapsed state that are reported.
  - Activate it with the screen reader's own commands. Record whether the state change is reported and whether the "Syllabus" heading can then be reached.
  - Repeat after closing it.
- **Rendered checks:**
  - Measure the toggle's rendered size.
  - Confirm the hover background and focus outline in forced colors mode (`testing/forced-colors.md`).
  - Check zoom at 200% and 400% (`testing/zoom.md`).

## Automated scan
Not run. axe (`@axe-core/cli`) needs Node.js and npx, and neither is installed on this machine. Even when run, axe does not detect this kind of failure, a custom control with no key handler; `sc-2.1.1-keyboard.md` says so under automated coverage.
