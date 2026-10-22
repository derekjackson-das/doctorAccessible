# SC 1.2.5 Audio Description (Prerecorded)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.2 Time-based Media
- Tier 1 source: https://www.w3.org/TR/WCAG22/#audio-description-prerecorded
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Audio description is provided for all prerecorded video content in synchronized media.

## What it requires, in our words

A recorded video with sound needs audio description: narration, fitted into the gaps in the dialogue, that says what is happening on screen that a listener would otherwise miss. This is the Level AA counterpart of SC 1.2.3 and removes the option of a text alternative instead. If the video has no visual information beyond what the soundtrack already conveys, such as a person speaking to camera, the Understanding page accepts that no description is needed, because there is nothing to describe. When the pauses are too short to fit the description, the video can be paused for extended description.

## How it fails in code

- A `video` with visual content that carries information and no described audio track or described version. Definite once a person confirms the visuals matter.
- A described track that skips available pauses and leaves visual information undescribed. Manual review. F113.
- A talking-head video with no description. Not a failure if nothing visual carries information; manual review to confirm.

## How to meet it

- Technique G78, "Providing a second, user-selectable, audio track that includes audio descriptions".
- Technique G173, "Providing a version of a movie with audio descriptions", when a single track must carry it.
- Technique G8, "Providing a movie with extended audio descriptions".
- Technique G203, "Using a static text alternative to describe a talking head video", for video where the description would be empty.
- Advisory: Technique H96, "Using the track element to provide audio descriptions". Browser support for description tracks is uneven; confirm with the project's player.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.2.3 (entry in this package). Level A allows a text alternative instead; this criterion does not.
- SC 1.2.2 Captions (Prerecorded) (entry in this package). The companion requirement for sound.
- SC 1.1.1 Non-text Content (entry in this package). The video also needs a descriptive label.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Entirely manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
