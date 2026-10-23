# Run 2026-10-23: verifier on eval 029

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit 3e395e0.
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, SC 2.1.1 Keyboard (Level A), tier 1, definite, on `#tab-online` and `#tab-hybrid` and the click-only script, citing the 2.1.1 entry's roving-tabindex case and `aria/patterns/tabs.md`: present.
- Fix direction: arrow-key handling on the tablist. Acceptable.
- Must not: nothing from the list. Roles and states, the selected-tab cue (weight and underline, not color alone), contrast, focus, and headings were checked and not reported.
- Also acceptable, used: the virtual cursor caveat from the tabs entry, with the testing gap named.

Observation: under Content, the answer worked out a grade level by hand (about 4.8 from a syllable count) and labelled it as a hand count and "a signal, not a pass". The content skill calls an on-the-spot formula an estimate to be marked unverified; this was close to that but did not use the word. Not a must-not item for this eval.

## The report, as given

## Checked
`evals/029-aria-tabs-no-arrow-keys/input.html` (50 lines: one page with a three-tab ARIA tab widget, inline CSS and inline script). I read all of it. axe was not run because Node.js is not installed on this machine and no browser is available. There is no `a11y-spec.md` in the repo root or in `docs/`, so the page is checked against WCAG 2.2 AA alone. Sources opened: `knowledge/INDEX.md`, `.claude/skills/wcag/SKILL.md`, `knowledge/aria/patterns/tabs.md`, `knowledge/patterns/tabs.md`, `knowledge/wcag/sc-2.1.1-keyboard.md`, `sc-1.4.1-use-of-color.md`, `sc-1.4.3-contrast-minimum.md`, `sc-1.4.11-non-text-contrast.md`, `sc-2.5.8-target-size-minimum.md`, and `docs/content-standards.md`.

## Findings
### [Definite] Inactive tabs cannot be reached by keyboard
- Where: input.html lines 21–22 (`#tab-online`, `#tab-hybrid`, `tabindex="-1"`), and the script at lines 36–47
- What: The inactive tabs are taken out of the tab order with `tabindex="-1"` (a roving tabindex), and the script adds only a `click` listener with no arrow-key handler, so there is no keyboard route to "Online" or "Hybrid" or to their panels.
- Criterion: WCAG 2.2 SC 2.1.1 Keyboard (Level A), tier 1, W3C Rec 12 Dec 2024
- Source: knowledge/wcag/sc-2.1.1-keyboard.md ("inactive tabs in a roving tabindex with no arrow-key handler", definite); knowledge/aria/patterns/tabs.md, "How it fails in code" (tier 2 pattern, APG)
- Fix direction: Add a keydown handler on the tablist so Left and Right Arrow move focus between tabs, wrapping at the ends (Home and End optional), in line with the roving tabindex already in place.

No other defects found from code. These were checked and pass:
- Roles and states: `tablist` with `aria-label`, `tab` on native `button`s, `aria-selected` and `tabindex` updated by script, panels named by `aria-labelledby` and hidden with `hidden`.
- Selected-tab cue: weight and underline, not color alone (sc-1.4.1).
- Tab text contrast: computed from the declared colors, #005a9c on #fff and #fff on #005a9c are both about 7.14:1, against the 4.5:1 in sc-1.4.3.
- Focus outline: computed, #1a1a1a against the white page is about 17.4:1, against the 3:1 in sc-1.4.11.
- Target size: estimated from the CSS, the tabs are about 40px tall at the default font size, against the 24 by 24 CSS px in sc-2.5.8.

## Content
- Reading level: no spec, so the house default applies (grade 8 or below, Flesch-Kincaid). No reading-level tool was run. A hand count of the three panel sentences (31 words, 43 syllables) gives about grade 4.8, computed by hand. The sample is too small to mean much; it is a signal, not a pass.
- Headings: one `h1`, "Course formats", which matches the page title and says what the page is.
- Links, alt text, error messages: none on the page.
- Language: `lang="en"` is declared.
- Manual review: whether the panel text answers what a prospective student needs to know about each format.

## Spec deviations
No `a11y-spec.md` found (repo root, then `docs/`). Nothing to compare against.

## Manual checks remaining
- Keyboard only, after the fix: Tab lands on the selected tab; Left and Right Arrow move between tabs and wrap; Enter or Space (or focus, if automatic activation is chosen) shows the matching panel; Tab moves into the panel; Shift+Tab returns to the selected tab. Record any tab or panel that cannot be reached.
- Screen reader, with the team's chosen AT (no spec names it): record the role, name, position and selected state exposed for each tab, and the name of each panel. Also press Tab from reading mode into the tab list and record which tab gets focus. The source notes that a virtual cursor can reach the inactive tabs, so a screen reader test alone can hide the keyboard defect. The newest listed AT test of tabs is from 2018 to 2019.
- Mobile screen readers: tabs can be found and activated by swiping; record whether the selected state is exposed.
- Voice control: each tab can be activated by its visible name.
- Zoom to 400%: the tab list wraps without hiding tabs, and the selected cue and focus outline stay visible. Also look at the focus outline on the selected tab where it meets the tablist's blue bottom border.
- Forced colors: record whether the selected tab can still be told apart and whether the focus outline stays visible.

## Automated scan
Not run. axe cannot run here because Node.js is not installed and no browser is available. Note: the 2.1.1 entry says axe does not detect missing key handlers of this kind, so a clean scan would not have cleared this defect.
