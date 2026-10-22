# Testing: Reduced motion

- Sources:
  - W3C, "Technique C39: Using the CSS prefers-reduced-motion query to prevent motion", Techniques for WCAG 2.2, accessed 2026-10-22. https://www.w3.org/WAI/WCAG22/Techniques/css/C39 Tier 2. Its test procedure is the basis of step 3.
  - W3C, "Understanding Success Criterion 2.3.3: Animation from Interactions", Understanding WCAG 2.2, accessed 2026-10-22. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html Tier 2.
  - W3C, WCAG 2.2, definition of "motion animation", W3C Recommendation 12 December 2024. https://www.w3.org/TR/WCAG22/#dfn-motion-animation Tier 1.
  - MDN Web Docs, "prefers-reduced-motion", last modified 10 June 2026. https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion Tier 3. Where each operating system keeps the setting.
- Related entries: `wcag/sc-2.2.2-pause-stop-hide.md`, `wcag/sc-2.3.1-three-flashes-or-below-threshold.md`, `coga/objective-5-help-users-focus.md`.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

WCAG 2.2 SC 2.3.3 Animation from Interactions (Level AAA, no entry yet), tier 1, reads in part: "Motion animation triggered by interaction can be disabled, unless the animation is essential". Using the operating system's reduced-motion setting, as in technique C39, is one sufficient way to meet it. It is beyond our AA target, so a failure here alone is manual review, not a WCAG finding.

WCAG defines motion animation narrowly: changes of color, blurring, or opacity that do not change an element's perceived size, shape, or position are not motion animation. A plain fade is outside 2.3.3; at most it is an optional note.

Motion that starts on its own is a different matter. It falls under `wcag/sc-2.2.2-pause-stop-hide.md` at Level A whatever the setting, and flashing falls under `wcag/sc-2.3.1-three-flashes-or-below-threshold.md`. Report those under their criteria.

## Setup

Turn on the operating system's reduced-motion setting, using MDN's list of where it lives:
- Windows 11: Settings, Accessibility, Visual Effects, Animation Effects (off).
- macOS: System Settings, Accessibility, then Display or Motion depending on version, Reduce motion.
- iOS: Settings, Accessibility, Motion.
- Android 9 and later: Settings, Accessibility, Remove animations.

Reload the page after changing the setting. Keep a second browser or device with the setting off, for comparison.

## The steps

1. With the setting off, list every visual change the component makes, and sort each one:
   - motion animation: movement, scaling, parallax, scroll effects;
   - not motion animation under WCAG's definition: fades, color changes, blurs that leave size, shape, and position unchanged;
   - motion that starts on its own: auto-playing animation or video, carousels, loading spinners.
2. Turn the setting on and reload.
3. For each motion animation triggered by an interaction (C39's procedure): trigger it, and note whether it is suppressed, or whether it is essential to the function.
4. For each motion that starts on its own: note whether it still starts, and whether a visible control can pause, stop, or hide it.
5. Note anything that now breaks, such as content that never appears because its entrance animation was removed.

## What passing looks like

- With the setting on, non-essential motion animation from interaction is suppressed (C39; SC 2.3.3, AAA, advisory here). MDN also describes toning motion down rather than removing it; that is a design choice to note, not C39's pass condition.
- Motion that starts on its own and runs over five seconds beside other content can be paused, stopped, or hidden, setting or no setting (`wcag/sc-2.2.2-pause-stop-hide.md`).
- Nothing flashes more than the threshold allows (`wcag/sc-2.3.1-three-flashes-or-below-threshold.md`).
- No content or function is lost when motion is removed.

## What to record

Operating system and version, the setting's exact name, browser, and for each change: what it was, which group from step 1 it falls in, what happened with the setting on, pass, fail, or "essential" with the reason, and the tester.
