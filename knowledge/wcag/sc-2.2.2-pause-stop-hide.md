# SC 2.2.2 Pause, Stop, Hide

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.2 Enough Time
- Tier 1 source: https://www.w3.org/TR/WCAG22/#pause-stop-hide
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> For moving, blinking, scrolling, or auto-updating information, all of the following are true:
>
> **Moving, blinking, scrolling.** For any moving, blinking or scrolling information that (1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content, there is a mechanism for the user to pause, stop, or hide it unless the movement, blinking, or scrolling is part of an activity where it is essential; and
>
> **Auto-updating.** For any auto-updating information that (1) starts automatically and (2) is presented in parallel with other content, there is a mechanism for the user to pause, stop, or hide it or to control the frequency of the update unless the auto-updating is part of an activity where it is essential.
>
> Note 1: For requirements related to flickering or flashing content, refer to Guideline 2.3.
>
> Note 2: Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether it is used to meet other success criteria or not) must meet this success criterion. See Conformance Requirement 5: Non-Interference.
>
> Note 3: Content that is updated periodically by software or that is streamed to the user agent is not required to preserve or present information that is generated or received between the initiation of the pause and resuming presentation, as this may not be technically possible, and in many situations could be misleading to do so.
>
> Note 4: An animation that occurs as part of a preload phase or similar situation can be considered essential if interaction cannot occur during that phase for all users and if not indicating progress could confuse users or cause them to think that content was frozen or broken.

## What it requires, in our words

Anything that moves, blinks, scrolls, or refreshes itself, starts on its own, runs longer than five seconds, and sits next to other content, needs a pause, stop, or hide control. Carousels that auto-advance, news tickers, animated backgrounds, and live-updating feeds are the usual cases. Motion pulls attention away from the content for people with attention or cognitive disabilities, and a screen magnifier user cannot read text that keeps moving. A loading spinner during a phase when nothing else can be done is allowed. The note makes this a non-interference requirement: one unstoppable animation fails the page.

## How it fails in code

- A carousel or slideshow that auto-advances with no pause button. Definite. F16.
- A `marquee` or `blink` element, or CSS or script that scrolls or blinks text for more than five seconds with no stop. Definite. F16, F112, F50.
- An animated GIF or CSS animation that loops indefinitely beside content and cannot be stopped. Definite once confirmed to exceed five seconds.
- An auto-refreshing feed, score, or stock ticker with no pause and no frequency control. Definite.
- A video with `autoplay muted loop` as a background, with no pause. Definite under this criterion (sound is 1.4.2).
- An animation that respects the user's reduced-motion preference and stops. Passes; the preference is the mechanism. Manual review to confirm.

## How to meet it

- Technique G4, "Allowing the content to be paused and restarted from where it was paused".
- Technique G186, "Using a control in the web page that stops moving, blinking, or auto-updating content".
- Technique G11, "Creating content that blinks for less than 5 seconds", and G152 or SCR22 to stop blinking within five seconds.
- Technique G191, "Providing a link, button, or other mechanism that reloads the page without any blinking content".
- Technique SCR33, "Using script to scroll content, and providing a mechanism to pause it".
- Simplest: do not auto-play motion. Let the user start it.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.3.1 Three Flashes or Below Threshold (entry in this package). Flashing that can cause seizures; Note 1 points there.
- SC 1.4.2 Audio Control (`wcag/sc-1.4.2-audio-control.md`). The sound side of autoplaying media.
- SC 2.2.1 Timing Adjustable (entry in this package). Content that advances on a clock.
- SC 2.3.3 Animation from Interactions is Level AAA and not a requirement here.

## Automated coverage (tier 3)

axe-core tags `blink` and `marquee` to this criterion. Those elements are rare now. CSS animations, auto-advancing carousels, and refreshing feeds are found by watching the page, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
