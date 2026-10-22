# SC 2.3.1 Three Flashes or Below Threshold

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.3 Seizures and Physical Reactions
- Tier 1 source: https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Web pages do not contain anything that flashes more than three times in any one second period, or the flash is below the general flash and red flash thresholds.
>
> Note: Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether it is used to meet other success criteria or not) must meet this success criterion. See Conformance Requirement 5: Non-Interference.

## What it requires, in our words

Nothing on the page may flash more than three times in a second, unless the flashing area is small enough and the contrast change low enough to fall under the thresholds the Recommendation defines. Flashing above those limits can trigger seizures in people with photosensitive epilepsy. This is a safety requirement, not a convenience, and the note makes it non-interference: one flashing element fails the page. The thresholds are defined in terms of the area of the visual field and the change in luminance, with a stricter rule for saturated red. In practice, a large element that alternates between light and dark more than three times a second fails.

## How it fails in code

- A CSS animation, script, GIF, or video that alternates a large area between contrasting colors at more than three cycles per second. Definite when the rate and area are evident from the code; otherwise Likely until measured.
- A strobing effect in embedded video. Manual review; needs a flash analysis tool on the video.
- A small blinking cursor or a tiny status dot. Passes; below the area threshold. G176.
- Flashing that runs for under a second, four or more times. Still a failure; the criterion is per one-second period.

## How to meet it

- Technique G19, "Ensuring that no component of the content flashes more than three times in any 1-second period". The simplest route: do not flash.
- Technique G176, "Keeping the flashing area small enough" to be under the general flash threshold.
- Technique G15, "Using a tool to ensure that content does not violate the general flash threshold or red flash threshold", for video and complex animation.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.2.2 Pause, Stop, Hide (entry in this package). Blinking that lasts over five seconds also needs a stop control; a fast flash fails both.
- SC 2.3.2 Three Flashes is Level AAA and removes the threshold exception; not a requirement here.
- SC 2.3.3 Animation from Interactions is Level AAA and not a requirement here.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Flash rate and area are measured by watching the content or running a flash analysis tool over a recording, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
