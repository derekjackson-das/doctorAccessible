# ARIA pattern: Tooltip

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Tooltip Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/ A pattern, not a requirement. The page says it is a work in progress without task force consensus, and it has no example.
- Normative (tier 1): WAI-ARIA 1.2, `tooltip` role and `aria-describedby`, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/#tooltip
- Practitioner sources (tier 3): Higley (2019), Pickering (2017), and de Vries and O'Hara (2023, 2024) are cited in `patterns/tooltip.md`, with their findings. None tests a tooltip itself with assistive technology. This entry adds none.
- Related entries: `patterns/tooltip.md` (whether to use one, toggletips, the criteria, the manual tests), `aria/accessible-name.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.4.13-content-on-hover-or-focus.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/tooltip.md` decide whether code fails WCAG; report a failure once, under its criterion. The APG pattern has no consensus, so departing from it is never a finding on its own. Whether `role="tooltip"` is present is advice; what matters is that the control is named and the tip is connected.

**Testing gap.** No listed source reports testing a tooltip with assistive technology (`patterns/tooltip.md` gives the detail). Treat everything here as needing the manual tests.

## Native first

Visible text, so nothing depends on a tooltip, or a toggletip; see `patterns/tooltip.md`. The `title` attribute is not a substitute (Higley; Pickering, in that entry).

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| The trigger, an interactive element such as a `button` | its own | an accessible name of its own; `aria-describedby` pointing at the tip | Author | Focus stays on the trigger while the tip shows (APG) |
| The tip | `tooltip` | | Author | Never focusable, and holds no links or buttons; use a non-modal dialog for that (APG) |

## Naming

The tooltip is a description, not a name. An icon-only button still needs a name: visible text, `aria-label`, or `aria-labelledby` (`aria/accessible-name.md`). If the tip's text is also the button's name, point `aria-labelledby` at it instead of `aria-describedby`, so the name does not depend on the tip ever being shown; `patterns/tooltip.md` records Higley allowing this. Pointing `aria-describedby` at the only text, with no name, leaves an unnamed button.

## Keyboard

From the APG pattern, in our words: the tip shows when the trigger gets focus or the pointer rests on it; Escape dismisses it; it closes on blur, or when the pointer leaves both the trigger and the tip. `wcag/sc-1.4.13-content-on-hover-or-focus.md` sets what is required.

## What testing found

Nothing on the list tests the ARIA of a tooltip. `patterns/tooltip.md` records Higley's 2019 observation that `role="tooltip"` did not change announcements, and the 2024 test of `popover` by de Vries and O'Hara.

## How it fails in code

- An icon-only button whose only text is in the tip, linked by `aria-describedby`: the button has no accessible name, `wcag/sc-4.1.2-name-role-value.md`, definite.
- A tip that shows on hover but not on focus: `wcag/sc-1.4.13-content-on-hover-or-focus.md` and 2.1.1, at those entries' confidence.
- Links or buttons inside the tip: advice against, from the APG; a finding only through the criterion its effect breaks.
- `role="tooltip"` missing while `aria-describedby` connects the tip: not a finding.
