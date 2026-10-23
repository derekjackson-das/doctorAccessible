# Run 2026-10-23: verifier on eval 033

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit fd3d319.
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, SC 4.1.2 Name, Role, Value (Level A), tier 1, definite, on `#rotate` and `setPlaying()`, citing the 4.1.2 entry's visual-state case and `aria/patterns/carousel.md`: present.
- Fix direction: update the name in `setPlaying()`. Acceptable.
- Must not: nothing from the list. 2.2.2 was judged met; previous and next, the region and slide names, and the hidden slides were checked and not reported.

Observation: under Content (house standard, not WCAG), it raised the `h2` "This week" as a thin heading for manual review. The must-not item on headings is about WCAG findings; this is a house-standard manual-review note, so it is recorded here, not counted against the run.

## The report, as given

## Checked
I checked `evals/033-aria-carousel-rotation-label-stale/input.html`, lines 1–87. It holds an auto-rotating "This week" carousel with three slides, a rotation toggle, previous and next buttons, and its inline CSS and script. I read the code in full. axe was not run, because Node.js is not installed on this machine and no browser is available. There is no `a11y-spec.md` at the repo root or in `docs/`, so I checked against WCAG 2.2 AA alone.

Sources opened: `knowledge/INDEX.md`, `.claude/skills/wcag/SKILL.md`, `knowledge/wcag/sc-4.1.2-name-role-value.md`, `knowledge/wcag/sc-2.2.2-pause-stop-hide.md`, `knowledge/patterns/carousel.md`, `knowledge/aria/patterns/carousel.md`, `knowledge/aria/accessible-name.md`, `docs/content-standards.md`.

## Findings
### [Definite] Rotation button keeps the name "Pause slides" after rotation stops
- Where: `#rotate`, line 24 (`aria-label="Pause slides"`), and `setPlaying()`, lines 70–74. It is triggered by the click handler on line 77 and by the `focusin` handler on line 80.
- What: When rotation stops, `setPlaying()` changes the icon from pause bars to a play triangle, but it never updates the button's `aria-label`. The button's name stays "Pause slides" while the button now starts rotation. The visual state changes, but the programmatic state does not. It goes wrong as soon as keyboard focus enters the section, Tab onto the button itself included, because the `focusin` handler on line 80 pauses rotation.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
- Source: `knowledge/wcag/sc-4.1.2-name-role-value.md` ("a custom ... toggle ... that changes state visually without exposing that state ... Definite when the state is user-settable"). `knowledge/aria/patterns/carousel.md` names this exact case as definite under 4.1.2: an icon flips between pause and play while the name stays the same and no state is exposed. The APG pattern (tier 2) gives the rotation control a name for its current action, changed by script.
- Fix direction: In `setPlaying()`, update the button's accessible name along with the icon so it always names the action the next press will take ("Pause slides" or "Start slides").

No other WCAG 2.2 AA defects found by reading:
- SC 2.2.2: there is a working pause mechanism. Rotation also stops on hover and when keyboard focus enters, and does not restart after focus unless asked.
- SC 4.1.2: the previous and next buttons have names, and the SVGs are `aria-hidden`.
- The rotation control comes first in tab order.
- Hidden slides use `hidden`, so their links cannot take focus.
- The section is named by its visible heading, and each slide group is named by its heading.

## Content
- Reading level: not measured. There is no tool here and no spec target. The house default is grade 8 Flesch-Kincaid, per `docs/content-standards.md`. The slide text is short and plain, but a human should confirm.
- Headings: there is one `h1` ("Library news") and the levels go in order (h1 > h2 > h3). "This week" is a thin heading for the section. That is manual review against content-standards section 4.
- Link text: "See all opening hours", "Book a study room" and "Sign up for the workshop" each say where they go on their own. No issue.
- Alt text: there are no images. The icons are decorative and hidden from assistive technology.
- Error messages: none on the page.
- Language: `lang="en"` is declared and no passages are in another language.
- Abbreviation: "2 a.m." is standard and needs no expansion.

## Spec deviations
None to report, because the project has no `a11y-spec.md`.

## Manual checks remaining
- Keyboard only:
  - Tab into the carousel and confirm rotation stops on focus.
  - Activate the rotation button and confirm it starts and stops rotation.
  - Press previous and next several times; record whether focus stays on the button.
  - Confirm no link in a hidden slide takes focus.
- Screen reader, with whatever assistive technology the team tests with:
  - Tab to the rotation button before and after pausing, and after starting again. Record the name exposed in each state.
  - Check the accessibility tree for the button's name after each toggle.
  - Record whether the region name "This week" and each slide's group name are exposed.
  - Record whether a slide change made with next or previous is conveyed. There is no live region.
- Pointer: rotation stops on hover. Clicking the rotation button while hovering does not move focus, because of the `mousedown` `preventDefault`. Confirm rotation pauses and resumes as the icon shows.
- Voice control: the rotation button has no visible text. Record whether the tester can activate it by name in each state, or only with a number overlay.
- Zoom to 200% and 400%, and forced colors: confirm the controls and focus outline stay visible and usable.
- Reduced motion: slides switch instantly with no animation, but rotation still starts on its own with the OS reduced-motion setting on. Record the observed behavior.

## Automated scan
Not run: Node.js is not installed on this machine, so `npx @axe-core/cli` is unavailable, and there is no browser to load the page. Even a clean axe run would not have caught the stale name, because axe checks that a name exists, not that it changes with state.
