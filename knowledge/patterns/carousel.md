# Pattern: Carousel

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Carousel (Slide Show or Image Rotator) Pattern", accessed 2026-10-22 (the page shows no date). https://www.w3.org/WAI/ARIA/apg/patterns/carousel/ A pattern, not a requirement.
- W3C tutorial (tier 2): WAI Tutorials, "Carousels Tutorial", updated 13 April 2017, first published May 2015. https://www.w3.org/WAI/tutorials/carousels/
- Practitioner sources (tier 3, on `knowledge/SOURCES.md`):
  - Sara Soueidan, "Are 'CSS Carousels' accessible?", 6 May 2025, updated 19 August 2025. https://www.sarasoueidan.com/blog/css-carousels-accessibility/ Tested Chrome's experimental CSS-only carousels with VoiceOver on macOS, the keyboard, and the browser's accessibility tree.
  - Heydon Pickering, "A Content Slider", Inclusive Components, 22 November 2017. https://inclusive-components.design/a-content-slider/ Design and build guidance; it reports no named assistive technology test.
- Related entries: `ux/carousels.md` (whether people want one at all), `wcag/sc-2.2.2-pause-stop-hide.md`, `wcag/sc-4.1.2-name-role-value.md`, `coga/objective-5-help-users-focus.md`; `aria/` once that domain exists.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

**Testing gap.** Only one source on the list reports assistive technology testing, and it covers Chrome's experimental CSS-only carousels, not scripted ones. A search of the other practitioners on the list, including Adrian Roselli, found no carousel test. a11ysupport.io renders its results with script and could not be read for this entry. Nothing on the list tests an auto-rotating carousel, voice control, or magnification. Treat everything in "What doing it right requires" as needing confirmation in the manual tests.

## The need

Several items, often from different teams, competing for the top of a page. Sometimes a gallery of images people want to look through one at a time. `ux/carousels.md` covers how often the first need is organizational rather than a user need.

## The simpler alternative and its cost

- **A static hero and a short list of links.** One featured item, then the others as plain links or cards. It moves nothing, hides nothing, and needs no script. The cost: only one item gets the big image, which is a political cost inside the organization more than a cost to readers.
- **A list that scrolls only when the person scrolls it.** Pickering's "content slider": a labeled list of items in a horizontally scrolling region that never moves on its own, with previous and next buttons added only as an enhancement. The cost: a horizontal scroller needs care of its own (keyboard focus, visible scroll cue), and it still hides most items.

For a gallery people chose to browse, the second option usually serves. For promotional content, the first one does.

## What doing it right requires

From the Authoring Practices and the WAI tutorial, unless noted:
- **No movement the person did not ask for.** If it rotates at all, a stop and start button comes first in the carousel's tab order, and rotation stops while the pointer hovers and when keyboard focus enters; after keyboard focus it does not restart unless asked. Pickering argues that an inclusive carousel moves only when the person moves it, since a pause button helps only after the motion has begun.
- **Native buttons** for previous, next, and rotation, with names that say what they do; the rotation button's name changes between "Stop" and "Start".
- **A labeled region** around the carousel, slides marked up as a list or as groups with names such as "3 of 10" when slides have no unique title.
- **Decide what off-screen slides are.** In a rotating carousel, the Authoring Practices want slides that are not shown truly hidden, warning that slides merely moved off screen confuse screen reader reading. Pickering's scrollable list takes the other approach: every item stays readable, and he says invisible content should never be focusable, removing off-screen links from the tab order as an enhancement. Pick one model and test it; do not leave content that is out of view but still focusable.
- **Focus stays put** when previous or next is pressed, so people can press them repeatedly. A polite live region may announce the new slide when the person changed it; it should be off while the carousel rotates on its own.
- **Do not trust CSS-only carousels yet.** Testing Chrome's experimental version behind a flag in May 2025, Soueidan found it exposed its scroll markers as tabs with no matching panels, with missing or identical names, a selected state that did not match the screen, wrong item counts, and disabled buttons that still took focus. She advised against using it in real products. Chrome's behavior may have changed since; retest before relying on it.
- **Buttons as well as swiping.** Some people cannot swipe, so the previous and next buttons must be there on touch screens too (WAI tutorial).

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 2.2.2 | Pause, Stop, Hide | A | `wcag/sc-2.2.2-pause-stop-hide.md` | Auto-rotation that starts on its own, lasts over five seconds, and sits beside other content |
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Every control, including slide pickers, works from the keyboard |
| 2.4.3 | Focus Order | A | `wcag/sc-2.4.3-focus-order.md` | Focusable content inside hidden slides |
| 2.4.7 | Focus Visible | AA | `wcag/sc-2.4.7-focus-visible.md` | Focus on controls drawn over images |
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Names for buttons and picker controls; picker state exposed |
| 1.1.1 | Non-text Content | A | `wcag/sc-1.1.1-non-text-content.md` | Text alternatives for slide images and icon-only controls |
| 1.4.11 | Non-text Contrast | AA | `wcag/sc-1.4.11-non-text-contrast.md` | Arrows and dots over changing images |
| 2.5.8 | Target Size (Minimum) | AA | `wcag/sc-2.5.8-target-size-minimum.md` | Small dot controls placed close together |
| 2.5.1 | Pointer Gestures | A | `wcag/sc-2.5.1-pointer-gestures.md` | A carousel that advances only by swiping |
| 1.4.3 | Contrast (Minimum) | AA | `wcag/sc-1.4.3-contrast-minimum.md` | Text placed over slide images |

## Manual tests

With the assistive technology named in the project's `a11y-spec.md`:
- Keyboard only: Tab reaches the rotation control before any slide; rotation stops when focus enters and stays stopped; previous and next work repeatedly without focus moving; no hidden slide content takes focus.
- Screen reader: the region's name is announced; each slide's name or position is announced; reading through the carousel never jumps to a slide the person did not choose.
- Voice control: each control can be activated by its visible name or a number overlay.
- Zoom to 200% and 400%, and forced colors: controls stay visible and usable.
- With the operating system's reduced-motion setting on, nothing animates on its own.
