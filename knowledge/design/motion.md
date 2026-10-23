# Design: Motion

- Requirement sources (tier 1): `wcag/sc-2.3.1-three-flashes-or-below-threshold.md`, `wcag/sc-2.2.2-pause-stop-hide.md`.
- Practice sources:
  - W3C, WCAG 2.2 SC 2.3.3 Animation from Interactions and SC 2.3.2 Three Flashes, both Level AAA, and the definition of "motion animation", W3C Recommendation 12 December 2024. https://www.w3.org/TR/WCAG22/#animation-from-interactions Tier 1, beyond our target.
  - W3C, "Understanding Success Criterion 2.3.3: Animation from Interactions", updated 16 September 2025. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html Tier 2.
  - W3C, "Technique C39: Using the CSS prefers-reduced-motion query to prevent motion", updated 12 January 2026. https://www.w3.org/WAI/WCAG22/Techniques/css/C39 Tier 2.
  - MDN Web Docs, "prefers-reduced-motion", last modified 10 June 2026. https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion Tier 3.
  - WebAIM, "Seizure and Vestibular Disorders", last updated 21 August 2020. https://webaim.org/articles/seizure/ Tier 3. Over five years old.
  - Scott O'Hara, "Reduced Position Sticky", 27 March 2019. https://www.scottohara.me/note/2019/03/27/reduced-sticky.html Tier 3. Old; a worked example.
- Related entries: `testing/reduced-motion.md`, `patterns/carousel.md`, `coga/objective-5-help-users-focus.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A design that fails the Requirement is reported under its criterion, once, at the confidence its `wcag/` entry gives. A design that meets the Requirement but misses a Practice point is reported as likely or manual review, never definite, and never as a WCAG failure. Level AAA criteria, including SC 2.3.3, are practice for this project. Motion triggered by an interaction that ignores the reduced-motion setting is a practice finding unless it also flashes or starts on its own.

## Requirement (tier 1)

- **No flashing above the threshold** (`wcag/sc-2.3.1-three-flashes-or-below-threshold.md`). This is a safety requirement and applies to the whole page.
- **Motion that starts by itself can be controlled.** Moving, blinking, or scrolling content that starts automatically, lasts over five seconds, and sits beside other content needs a way to pause, stop, or hide it, unless essential; auto-updating content likewise (`wcag/sc-2.2.2-pause-stop-hide.md`).

## Practice (tier 2 and 3, not required)

- **Honor the reduced-motion setting for interaction-triggered motion.** SC 2.3.3, Level AAA, asks that motion animation triggered by interaction can be turned off unless essential. Technique C39 meets it with the `prefers-reduced-motion` media query (W3C).
- **Know what counts as motion.** WCAG's definition of motion animation excludes changes of color, blur, or opacity that leave an element's size, shape, and position unchanged. A fade is not motion animation; a slide, a zoom, or a scale is (W3C, tier 1).
- **Large translations and scaling are the risky kind.** MDN notes that scaling or panning large objects can trigger vestibular disorders; WebAIM names parallax and moving content behind static text among the triggers.
- **Reduce means remove, reduce, or replace.** MDN's example swaps a scaling animation for an opacity fade under the reduced setting, which keeps the feedback without the movement.
- **Avoid parallax, or make it optional.** The Understanding page for 2.3.3 lists avoiding unnecessary animation as one solution, and gives as an example a site whose scroll-triggered decorative motion can be turned off by a site-wide control (W3C). O'Hara turned off a parallax-like sticky header under the reduced-motion query on his own site.
- **No flashing at all, where possible.** SC 2.3.2, Level AAA, drops the threshold allowance and forbids flashing more than three times a second outright.

## How to check

List every animation and sort it as the reduced-motion testing entry does: motion animation, color or opacity only, or motion that starts on its own. Check auto-starting motion against 2.2.2 and any flashing against 2.3.1. Then turn on the reduced-motion setting and check that each interaction-triggered motion animation is suppressed or replaced (`testing/reduced-motion.md`).
