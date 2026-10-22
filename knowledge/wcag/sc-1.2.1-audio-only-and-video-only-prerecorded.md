# SC 1.2.1 Audio-only and Video-only (Prerecorded)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.2 Time-based Media
- Tier 1 source: https://www.w3.org/TR/WCAG22/#audio-only-and-video-only-prerecorded
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> For prerecorded audio-only and prerecorded video-only media, the following are true, except when the audio or video is a media alternative for text and is clearly labeled as such:
>
> **Prerecorded Audio-only.** An alternative for time-based media is provided that presents equivalent information for prerecorded audio-only content.
>
> **Prerecorded Video-only.** Either an alternative for time-based media or an audio track is provided that presents equivalent information for prerecorded video-only content.

## What it requires, in our words

A recording that is only sound, such as a podcast or a lecture recording, needs a transcript that carries everything in it: the words, who said them, and meaningful sounds. A recording that is only picture, such as a silent animation or a screen recording with no narration, needs either a text description of what happens or a narrated audio track. "Alternative for time-based media" is the W3C term for a full text version, in order, of everything the media conveys. The exception is media that itself exists as an alternative to text already on the page and is labeled that way.

## How it fails in code

- An `audio` element, or a link to an audio file, with no transcript on the page or linked from beside it. Definite once the content is confirmed to be prerecorded and not an alternative for text.
- A `video` element with no audio track and no text description, when the video conveys information. Definite under the same confirmation.
- A transcript that is a filename, a title, or a one-line summary rather than the equivalent content. Definite. F30.
- A long description that does not match what the media conveys. Manual review; a person must compare. F67.
- Whether the media is a labeled alternative for text already present, which would exempt it. Manual review.

## How to meet it

- Technique G158, "Providing an alternative for time-based media for audio-only content": a transcript, in order, with speaker identification and meaningful non-speech sounds, placed on the page or linked immediately next to the player.
- Technique G159, "Providing an alternative for time-based media for video-only content": a text description of the visual content in sequence.
- Technique G166, "Providing audio that describes the important video content and describing it as such", for video-only media.
- Advisory: Technique H96, "Using the track element to provide audio descriptions".

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.1.1 Non-text Content (entry in this package). Media also needs a descriptive label there; this criterion requires the full alternative.
- SC 1.2.2 Captions (Prerecorded) and 1.2.3 Audio Description or Media Alternative (Prerecorded) (entries in this package). Those cover media with both sound and picture. This one covers media with only one.

## Automated coverage (tier 3)

axe-core tags `audio-caption` to this criterion. In practice axe can flag an `audio` element with no `track` for captions, likely as "incomplete, needs review" rather than a violation, which is a hint, not the requirement; a transcript on the page satisfies this criterion and axe cannot see it. Whether a transcript exists and is equivalent is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
