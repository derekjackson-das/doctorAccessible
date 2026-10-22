# Pattern: Carousel

- Sources:
  - W3C, "Carousel (Slide Show or Image Rotator) Pattern", ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/carousel/. Tier 2. A pattern, not a requirement.
  - W3C WAI, "Carousels Tutorial", https://www.w3.org/WAI/tutorials/carousels/. Tier 2.
  - Adrian Roselli, "Horizontal Scrolling Containers Are Not a Content Strategy", 1 August 2025, updated 3 September 2025, https://adrianroselli.com/2025/08/horizontal-scrolling-containers-are-not-a-content-strategy.html. Tier 3.
  - Sara Soueidan, "Are 'CSS Carousels' accessible?", 6 May 2025, updated 19 August 2025, https://www.sarasoueidan.com/blog/css-carousels-accessibility/. Tier 3.
- Related entries: `ux/carousels.md`, `coga/objective-2-find-what-they-need.md`, `coga/objective-5-help-users-focus.md`, `wcag/sc-2.2.2-pause-stop-hide.md`, `wcag/sc-2.5.1-pointer-gestures.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`, `wcag/sc-2.5.8-target-size-minimum.md`, `wcag/sc-1.1.1-non-text-content.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the carousel is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## The need it usually serves

Several items want the most visible spot on a page and the team does not want to choose. The person on the other side wants to see what is there and pick one. Those two wants pull apart: the carousel shows one item at a time, so it serves the team's problem by hiding most of the content from the person.

## The simpler thing that often serves, and what is lost

A list of the items, or one static featured item followed by a list. `ux/carousels.md` carries the research: people scroll past carousels, frames after the first are seen least, and moving content reads as advertising. What is lost by choosing the list: the large image per item, the one-at-a-time spotlight, and the sense that each team got its turn. What is gained: every item visible at once, in reading order, with nothing to pause and nothing to build.

## What doing it right requires

There is no native HTML carousel. The APG pattern's expectations, in our words: auto-rotation stops the moment anything inside the carousel receives keyboard focus and does not restart until the user asks; if there is a rotation control it is the first thing in the carousel's tab order; previous and next are real buttons that do not move focus, so a person can press them repeatedly; slides are reachable in the page tab sequence without extra scripting. The WAI tutorial adds that users must be able to pause the movement and that the structure must be semantic so assistive technology can make sense of it.

What the APG does not say: whether the carousel should exist. It also does not solve the problem that a hidden slide is still content, so the choice between leaving hidden slides in the accessibility tree and removing them until shown is a design decision with consequences for screen reader users either way.

## What practitioners found when they tested it

- **Roselli, 2025.** Horizontal scrolling containers, which users read as carousels, bring keyboard problems he details separately in his keyboard-only scrolling areas work: a focused item may not scroll fully into view, which risks the focus-not-obscured criterion; mouse-wheel users may not know to hold Shift; the container's height interacts with viewport media queries; and right-to-left or vertical-script localization breaks unless CSS logical properties were used throughout.
- **Soueidan, 2025.** The new CSS-only carousel features were, at the time of writing, experimental and in one browser behind a flag, and she found major accessibility problems: the scroll markers the CSS creates are interactive pseudo-elements rather than links, so how they are exposed to assistive technology was an open question, and the approach bypasses the semantic HTML that screen readers depend on. Her conclusion: not ready for production, and not the developer's job to fix.

## Criteria it touches

Auto-rotation: `wcag/sc-2.2.2-pause-stop-hide.md`, and `wcag/sc-2.2.1-timing-adjustable.md` if it advances on a clock. Swipe: `wcag/sc-2.5.1-pointer-gestures.md`, and `wcag/sc-2.5.7-dragging-movements.md` if implemented as drag. Controls: `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.5.8-target-size-minimum.md`, `wcag/sc-1.4.11-non-text-contrast.md` over images. Slides: `wcag/sc-1.1.1-non-text-content.md`, `wcag/sc-1.4.5-images-of-text.md`, `wcag/sc-1.4.3-contrast-minimum.md` for text over pictures, `wcag/sc-2.4.3-focus-order.md` for hidden slides that stay focusable, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`, `wcag/sc-1.4.10-reflow.md` at 320 CSS pixels. Flashing transitions: `wcag/sc-2.3.1-three-flashes-or-below-threshold.md`.

## Manual tests it demands

- Keyboard: Tab into the carousel; record whether rotation stops, which control gets focus first, and whether hidden slides receive focus. Press next five times; record that focus stays put.
- Screen reader, each pair in the spec: record what is announced on entering the region, on activating next, and whether the slide change is announced at all, and whether that announcement is tolerable.
- Reduced motion on: record whether rotation still starts.
- 400% zoom: record whether one slide fills the screen and whether the controls remain reachable and visible.
- Pointer: record whether every swipe action has a button equivalent and whether controls measure 24 CSS pixels.
- Contrast: measure control and text contrast at the worst spot of every image.

## What consult should say

1. What is the one thing the person must see here? Put it in text near the top.
2. Why more than one item? If the answer is that several teams want the space, that is governance, not a need; offer a list.
3. If a carousel stays: no auto-rotation, visible buttons, and the same items reachable as a list elsewhere.

"Build less" is the usual answer. See `ux/carousels.md` for the questions in full.
