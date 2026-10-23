# ARIA pattern: Carousel

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Carousel (Slide Show or Image Rotator) Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/carousel/ A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- Normative (tier 1): WAI-ARIA 1.2, `region` and `group` roles, `aria-roledescription`, and `aria-live`, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/. ARIA in HTML, W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/: a `section` is a `region` once it has an accessible name; a `div` may take any role, such as `group`.
- Practitioner testing (tier 3): Soueidan (2025) and Pickering (2017) are in `patterns/carousel.md`, with their findings. This entry adds:
  - Adrian Roselli, "Avoid aria-roledescription", 30 April 2020, updated 19 April 2022. https://adrianroselli.com/2020/04/avoid-aria-roledescription.html Tested `aria-roledescription` on controls and a region with NVDA 2019.3.1 and Firefox 76, JAWS 2018 with Chrome 81 and Internet Explorer 11, VoiceOver on macOS 10.15.2 and iPadOS 13.4, and TalkBack on Android 10 with Chrome 81 and Firefox 68; the 2022 update rechecked three JAWS bugs in JAWS 2021 and found two still present.
- Related entries: `patterns/carousel.md` (whether to use one, the simpler alternatives, the criteria, the manual tests), `ux/carousels.md`, `aria/using-aria.md`, `aria/patterns/tabs.md` (tabbed carousels), `aria/accessible-name.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.2.2-pause-stop-hide.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/carousel.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. Using or leaving out `aria-roledescription` is never a finding on its own.

**Testing gap.** Roselli's `aria-roledescription` tests are from 2020, with a JAWS recheck in 2022, both outside three years. The one recent carousel test on the list, Soueidan's 2025 test of Chrome's CSS-only carousels, is not of the ARIA pattern. Test with the spec's assistive technology.

## Native first

There is no carousel element. The plainer options, a static feature with links or a list the person scrolls, are in `patterns/carousel.md`. Native `button` elements for every control (APG).

## Roles, states, and properties

From the APG's basic carousel, in our words:

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| The carousel container | `region` or `group` | `aria-labelledby` to a visible heading, or `aria-label` | Author | `region` makes it a landmark; choose by the page's landmarks |
| The container | | `aria-roledescription="carousel"` | Author | Contested; see below |
| Rotation control | `button` | a name that says what it will do, "Stop slide rotation" or "Start slide rotation", changed by script | Script | The APG changes the name instead of using `aria-pressed`; it comes first in the carousel's tab order |
| Previous and next | `button` | names that say what they do | Author | Activating them does not move focus |
| Each slide | `group` | `aria-roledescription="slide"`; a name from its heading, or "3 of 10" | Author | Hidden slides truly hidden |
| Wrapper of the slides | | `aria-live="off"` while rotating, `"polite"` when not; `aria-atomic="false"` | Script | Optional; announces a slide the person chose, never automatic rotation |

A tabbed carousel uses `tablist`, `tab`, and `tabpanel` for the slide pickers instead; see `aria/patterns/tabs.md`.

## Naming

The carousel and each slide take their names from visible headings through `aria-labelledby`, or `aria-label` (`aria/accessible-name.md`). With `aria-roledescription` set, the APG leaves "carousel" and "slide" out of the names, since the role description says it. The rotation control's name is its current action and must change when the action does.

## Keyboard

From the APG pattern, in our words: Tab and Shift+Tab move through the controls with no special scripting; rotation stops as soon as keyboard focus lands anywhere inside the carousel and does not restart unless the person asks; pressing previous, next, or the rotation control leaves focus where it is.

## Sources differ: `aria-roledescription`

The APG sets `aria-roledescription` on the carousel and its slides. Roselli argues against the attribute in general. It is not translated, so a Portuguese JAWS user hears the English words. JAWS announced the role description and the real role together. TalkBack ignored it entirely. Two JAWS bugs were still present in JAWS 2021: the roles of elements inside a group with a role description were not announced, and buttons inside such a container were not announced as buttons in the virtual cursor. Those are exactly the carousel's controls. VoiceOver on iPadOS 13.4 did not recognize it on a region at all (2020). He does note that the ARIA 1.1 specification itself gives a carousel slide as a reasonable use.

Following principle 13, the stricter reading: leave it off unless the spec's assistive technology has been tested with it. If it is used, put it only on the container and the slides, never on the controls, and in the page's language.

## How it fails in code

- A rotation button whose icon flips between pause and play while its name stays the same and no state is exposed: a custom toggle that changes state visually without exposing it, `wcag/sc-4.1.2-name-role-value.md`, definite.
- Icon-only previous and next buttons with no name: 4.1.2, definite.
- Automatic rotation with no working way to stop it: `wcag/sc-2.2.2-pause-stop-hide.md`, at that entry's confidence.
- `aria-live="polite"` left on while the carousel rotates by itself: advice against, from the APG; a finding only through the criterion its effect breaks.
- Slides moved off screen with their links still focusable: see `patterns/carousel.md`; report under the criterion its effect breaks.
