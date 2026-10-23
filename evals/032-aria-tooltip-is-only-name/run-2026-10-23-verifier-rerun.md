# Run 2026-10-23: verifier on eval 032 (re-run after the key amendment)

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit 813d4c6. The knowledge is unchanged from the first run; only this eval's `expected.md` changed.
- Method: a fresh general-purpose agent, same instructions as the first run (`run-2026-10-23-verifier.md`). A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed; no browser).
- Result: **pass** against the amended key.

## Graded against `expected.md` (as at 813d4c6)

- Finding 1, SC 4.1.2 (Level A), tier 1, definite, on `button.icon-btn`, citing the 4.1.2 entry, `aria/patterns/tooltip.md`, and `aria/accessible-name.md`; reported once, with 1.1.1 explained as not separate: present.
- 1.4.13 listed under "checked and passing from code", with observation left to the manual checks.
- Must not: nothing from the list.

Observation, and a gap in the key: under Content, the run raised "RIS" as an abbreviation never expanded, a house-standard miss (`docs/content-standards.md` section 8), as manual review and explicitly not a WCAG failure. That is correct. The key called the page clean and did not consider it. The next revision of the page should expand it ("Download citation (RIS file, for reference managers)" or similar) or the key should list the note as acceptable.

## The report, as given (findings section)

### [Definite] Icon-only download button has no accessible name
- Where: input.html line 23, `button.icon-btn[aria-describedby="tip-download"]`
- What: The button's only content is an SVG with `aria-hidden="true"`. It has no `aria-label`, no `aria-labelledby`, no `title` and no text. The text "Download citation (RIS file)" reaches it only through `aria-describedby`, which gives a description, not a name, so the button exposes a role and no name.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
- Source: knowledge/wcag/sc-4.1.2-name-role-value.md (an icon-only button with no accessible name is listed as definite); knowledge/aria/patterns/tooltip.md ("An icon-only button whose only text is in the tip, linked by `aria-describedby`: the button has no accessible name ... definite"); knowledge/aria/accessible-name.md (description and name are computed separately)
- Fix direction: Give the button a name of its own, either by pointing `aria-labelledby` at the tip instead of `aria-describedby` or with visible text or `aria-label`, so the name does not depend on the tip at all.

I report this once, under 4.1.2. The "Controls, Input" clause of SC 1.1.1 (knowledge/wcag/sc-1.1.1-non-text-content.md) points to 4.1.2 for control names, so I did not add a second finding.

Checked and passing from code:
- SC 1.4.13 Content on Hover or Focus (AA), knowledge/wcag/sc-1.4.13-content-on-hover-or-focus.md. The tip shows on both focus and hover. Escape hides it without moving focus. The tip sits inside `.wrap` with no gap, because a transparent top border bridges the space, so the pointer can move onto it. It closes only on blur or when the pointer leaves, never on a timer. This still needs observing (see manual checks).
- SC 1.4.3 Contrast (Minimum) (AA), knowledge/wcag/sc-1.4.3-contrast-minimum.md. Tip text #fff on #1a1a1a: I computed about 17.4:1 from the declared colors, against a 4.5:1 threshold.
- SC 1.4.11 Non-text Contrast (AA), knowledge/wcag/sc-1.4.11-non-text-contrast.md. Button border and icon #005a9c on #fff: about 7.1:1 (computed). Focus outline #1a1a1a on #fff: about 17.4:1 (computed). The threshold is 3:1.
- SC 2.5.8 Target Size (Minimum) (AA), knowledge/wcag/sc-2.5.8-target-size-minimum.md. The button is 2.75rem square, which I computed as 44 by 44 CSS px at the default 16px root size. The threshold is 24 by 24.
- The SVG is hidden from assistive technology (`aria-hidden`, `focusable="false"`), which is correct for an icon inside a named control once the name is supplied.

Content (excerpt): "Language: `lang="en"` is declared. [Manual review] "RIS" is not spelled out anywhere. `docs/content-standards.md` section 8 says abbreviations are expanded on first use. That is a house standard, not a WCAG AA failure; a person should decide whether this audience needs it expanded."

The rest of the report listed accessibility tree, screen reader, speech, keyboard, mouse, touch, zoom, and activation checks, and said axe was not run.
