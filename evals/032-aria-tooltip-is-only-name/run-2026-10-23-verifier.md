# Run 2026-10-23: verifier on eval 032 (first run)

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit fd3d319.
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **fail, against the key as written at fd3d319.**

## Graded against `expected.md` (as at fd3d319)

- Finding 1, SC 4.1.2 Name, Role, Value (Level A), tier 1, definite, on `button.icon-btn`, with the AccName reasoning and `aria/patterns/tooltip.md`; reported once, with 1.1.1 explained as not separate: present and correct.
- Must not, "Report the tooltip's behavior under 1.4.13": **broken.** The answer filed a "[Manual review]" item under SC 1.4.13, saying the code "appears to meet all three conditions" and needs to be watched in a browser.
- Everything else on the must-not list was respected.

## What changed after this run

The key's intent was to stop a false 1.4.13 failure. A manual-review note that a criterion appears met and needs a browser check is what principle 7 asks for. At commit 813d4c6 the must-not item was amended to forbid only a 1.4.13 failure (likely or definite) and to allow such a note. The eval was then run again; see `run-2026-10-23-verifier-rerun.md`.

## The report, as given (findings section)

### [Definite] Icon-only download button has no accessible name; its only text is a description
- Where: input.html lines 23–26, `button.icon-btn[aria-describedby="tip-download"]`
- What: the button has no `aria-label`, no `aria-labelledby`, no `title` and no text content. Its SVG is `aria-hidden="true"`. The only text, "Download citation (RIS file)", is connected through `aria-describedby`, which supplies a description, not a name. Working through the AccName order in `aria/accessible-name.md` gives the button no name, and `aria/patterns/tooltip.md` lists this exact pattern as a definite 4.1.2 failure.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), W3C Rec 12 Dec 2024, tier 1
- Source: knowledge/wcag/sc-4.1.2-name-role-value.md; knowledge/aria/accessible-name.md; knowledge/aria/patterns/tooltip.md
- Fix direction: give the button a name of its own that does not depend on the tip being shown. Use visible text, or `aria-labelledby` pointing at the tip text instead of `aria-describedby`, or an `aria-label`.

This is reported once. The icon is hidden from the accessibility tree, so the missing text alternative is the button's missing name and is not a separate SC 1.1.1 finding.

### [Manual review] Tooltip behaviour on hover and focus
- Where: input.html lines 13–14 and 32–42
- What: the code appears to meet all three conditions.
  - Dismissible: Escape hides the tip without moving focus.
  - Hoverable: the tip sits inside `.wrap`, which carries the mouseenter and mouseleave handlers, and its transparent top border closes the gap to the button.
  - Persistent: there is no timer; the tip hides on blur or mouseleave unless the other trigger is still active.
  This has to be watched in a browser. Two points to check: whether the pointer can move onto the tip without it closing, and whether the tip comes back correctly after Escape while hover or focus stays.
- Criterion: WCAG 2.2 SC 1.4.13 Content on Hover or Focus (Level AA), tier 1
- Source: knowledge/wcag/sc-1.4.13-content-on-hover-or-focus.md
- Fix direction: none unless testing shows a failure.

The rest of the report computed contrast (tip about 17:1; icon and border about 7:1), target size (44 CSS px), and focus style as passing; covered content; listed accessibility tree, screen reader, keyboard, mouse, touch, zoom, and speech checks; and said axe was not run.
