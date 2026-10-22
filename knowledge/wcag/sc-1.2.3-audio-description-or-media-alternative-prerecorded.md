# SC 1.2.3 Audio Description or Media Alternative (Prerecorded)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.2 Time-based Media
- Tier 1 source: https://www.w3.org/TR/WCAG22/#audio-description-or-media-alternative-prerecorded
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> An alternative for time-based media or audio description of the prerecorded video content is provided for synchronized media, except when the media is a media alternative for text and is clearly labeled as such.

## What it requires, in our words

A recorded video needs one of two things for someone who cannot see it: an audio description, meaning narration added in the pauses that says what is happening on screen, or a full text alternative that describes the visuals and transcribes the sound in order. At Level A either one is enough. At Level AA, SC 1.2.5 requires the audio description. If the video is a talking head with nothing visual that matters, a plain transcript can serve as the alternative. The exception is media that is a labeled alternative to text already on the page.

## How it fails in code

- A `video` element with visual content that matters, no described audio track, and no text alternative on the page or linked beside it. Definite once a person confirms the visuals carry information.
- A transcript that covers only the speech when the video also conveys information visually. Likely; the transcript must describe the visuals too.
- Whether the visuals carry information at all, and whether the media is a labeled text alternative. Manual review.

## How to meet it

- Technique G69, "Providing an alternative for time based media": a full text version placed on the page or linked next to the player, with Technique H53 when the `object` element is used.
- Technique G78, "Providing a second, user-selectable, audio track that includes audio descriptions".
- Technique G173, "Providing a version of a movie with audio descriptions".
- Technique G8, "Providing a movie with extended audio descriptions", when pauses are too short.
- Technique G203, "Using a static text alternative to describe a talking head video", when there is no meaningful visual content.
- Advisory: Technique H96, "Using the track element to provide audio descriptions".

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.2.5 Audio Description (Prerecorded) (entry in this package). The Level AA criterion that removes the text-alternative option. Our target is AA, so in practice 1.2.5 governs.
- SC 1.2.2 Captions (Prerecorded) (entry in this package). The companion requirement for people who cannot hear.
- SC 1.2.1 (entry in this package). For video with no sound at all.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Whether a video has audio description or an equivalent text alternative is entirely manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
