# Run 2026-10-23: verifier on eval 030

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit 3e395e0.
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, SC 4.1.2 Name, Role, Value (Level A), tier 1, definite, on both header buttons and the click handler, citing the 4.1.2 entry and `aria/patterns/accordion.md`: present.
- Fix direction: set `aria-expanded` in the same handler. Acceptable.
- Must not: nothing from the list. Keyboard, headings, `aria-controls`, the chevron, contrast, focus, and language were checked and not reported.
- Also acceptable, used: a manual screen reader test of the state, with the entry's testing gap named; a note that axe cannot judge it.

## The report, as given

## Checked
`evals/030-aria-accordion-state-not-updated/input.html` (40 lines: HTML, inline CSS, inline script). I read all of it by hand. axe was not run (see Automated scan). The repo has no `a11y-spec.md` at the root or in `docs/`, so this check is against WCAG 2.2 AA alone. Knowledge entries opened: `knowledge/INDEX.md`, `.claude/skills/wcag/SKILL.md`, `knowledge/wcag/sc-4.1.2-name-role-value.md`, `knowledge/aria/patterns/accordion.md`, `knowledge/patterns/accordion.md`, `knowledge/wcag/sc-1.4.3-contrast-minimum.md`, `knowledge/wcag/sc-1.4.11-non-text-contrast.md`, and `docs/content-standards.md`.

## Findings
### [Definite] Accordion buttons never update `aria-expanded`
- Where: input.html lines 20 and 24 (`h2 button[aria-expanded="false"]`), and the click handler on lines 31–37
- What: The script toggles the panel's `hidden` attribute and the `open` class, which rotates the chevron. It never changes `aria-expanded`, so the exposed state stays "false" after a panel opens, and the visible state and the programmatic state disagree.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
- Source: knowledge/wcag/sc-4.1.2-name-role-value.md; knowledge/aria/patterns/accordion.md ("aria-expanded written in the markup but never updated by the script ... definite")
- Fix direction: In the same handler that toggles `hidden`, set `aria-expanded` on the button to match the panel's new state on every toggle.

No other defects found. Everything else checked out:
- Native `button` elements sit inside `h2` headings.
- Panels follow their buttons in the source and are hidden with `hidden`.
- Focus does not move when a panel opens.
- `:focus-visible` gives a visible outline.
- Contrast, computed from the declared colors with the WCAG relative-luminance formula: `#005a9c` on `#fff` is about 7.1:1. That clears the 4.5:1 text threshold in sc-1.4.3 and the 3:1 threshold in sc-1.4.11, for the button text, the border and the currentColor chevron. The `#1a1a1a` focus outline on `#fff` is far above 3:1.

## Content
- Reading level: not measured. There is no readability tool in this run, so the grade-8 house default in `docs/content-standards.md` was not checked. The body text is two short sentences, but that is not a measurement.
- Headings: one `h1`, which matches `<title>`, and two `h2` questions that each describe their panel. No skipped levels. This meets section 4 of the content standards.
- Link text, alt text, error messages: none on the page.
- Language: `lang="en"` is declared on `html`.

## Spec deviations
No `a11y-spec.md` found at the repo root or in `docs/`. There are no spec deviations to report, and the check is against WCAG 2.2 AA alone.

## Manual checks remaining
- Keyboard only: Tab reaches each header button, and Enter and Space each toggle its panel. Focus stays on the button after toggling, and nothing inside a closed panel takes focus. Record any key that fails.
- Screen reader (no spec, so no pairing is named; use the team's standard pairings, for example NVDA with Firefox or Chrome, and VoiceOver with Safari on macOS and iOS):
  - Move to each header by heading navigation and by control navigation, then activate it.
  - Record the role and the expanded or collapsed state reported before and after activation, and whether the panel content is reachable next in reading order.
  - The ARIA button pattern has a testing gap: per `knowledge/aria/patterns/accordion.md`, no listed source tested it within three years.
- Voice control: activate each header by its visible text. Record whether it responds.
- Zoom to 400% and narrow widths: headers and panels reflow, and the chevron stays visible. Record any clipping or horizontal scroll.
- Forced colors (Windows Contrast Themes): the button border, the chevron and the focus outline stay visible. Record which ones disappear.

## Automated scan
Not run: Node.js is not installed on this machine, so `npx @axe-core/cli` is not available, and there is no browser to load the page. axe could not judge the defect above in any case: the 4.1.2 entry notes that axe cannot tell whether a custom widget's state updates when the user acts.
