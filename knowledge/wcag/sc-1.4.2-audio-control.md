# SC 1.4.2 Audio Control

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#audio-control
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> If any audio on a web page plays automatically for more than 3 seconds, either a mechanism is available to pause or stop the audio, or a mechanism is available to control audio volume independently from the overall system volume level.
>
> Note: Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether or not it is used to meet other success criteria) must meet this success criterion. See Conformance Requirement 5: Non-Interference.

## What it requires, in our words

Sound that starts on its own and runs longer than three seconds must come with a way to stop it, pause it, or turn its volume down separately from the device volume. A screen reader user hears the page through the same speakers; background music drowns out the speech they need to operate the page, and turning down the system volume silences the screen reader too. The note makes this a non-interference requirement: one autoplaying video anywhere on the page fails the whole page, even if that video is otherwise irrelevant. The simplest way to meet it is not to autoplay sound at all.

## How it fails in code

- An `audio` or `video` element with `autoplay`, not `muted`, longer than three seconds, with no visible controls (`controls` attribute or custom pause button). Definite. F93.
- Background audio started by script on page load with no stop control. Definite. F23.
- An autoplaying element with controls that appear only on hover, so a keyboard user cannot reach them. Likely; definite once confirmed unreachable.
- An autoplaying `video` with `muted` set. Passes this criterion; moving content is SC 2.2.2.

## How to meet it

- Technique G171, "Playing sounds only on user request": no autoplay. Preferred.
- Technique G60, "Playing a sound that turns off automatically within three seconds".
- Technique G170, "Providing a control near the beginning of the web page that turns off sounds that play automatically".
- Native HTML: the `controls` attribute on `audio` and `video` gives a pause control and a volume control for free.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.2.2 Pause, Stop, Hide (`wcag/sc-2.2.2-pause-stop-hide.md`). Moving, blinking, or auto-updating content, including silent video.
- SC 1.2.4 Captions (Live) and 1.2.2 (entries in this package). The content of the sound.

## Automated coverage (tier 3)

axe-core tags `no-autoplay-audio` to this criterion. It flags `audio` and `video` elements that autoplay unmuted for more than three seconds without controls, when it can determine the duration. Script-started audio and custom players are outside its reach. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
