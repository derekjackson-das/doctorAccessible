# SC 1.2.4 Captions (Live)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.2 Time-based Media
- Tier 1 source: https://www.w3.org/TR/WCAG22/#captions-live
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/captions-live.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Captions are provided for all live audio content in synchronized media.

## What it requires, in our words

A live stream with sound, such as a webcast lecture or a streamed event, needs captions as it happens. For live events this usually means a human captioner or a captioning service feeding text into the stream; automatic captions count if they are accurate enough to carry the content. The criterion is about the stream the audience receives, so the code question is whether the player exposes a caption track or the captions are open in the picture. There is no "alternative for text" exception here.

## How it fails in code

- A live `video` or embedded live player with no captions visible or available. Definite once a person confirms the stream is live and has speech.
- Captions provided on a separate page or window the viewer has to find. Likely; the captions should be part of the synchronized media.
- Caption accuracy and lag. Manual review during the event.

## How to meet it

- Technique G9, "Creating captions for live synchronized media", combined with either Technique G93, "Providing open (always visible) captions", or Technique G87, "Providing closed captions". The Understanding page lists each pair as sufficient together.
- Operationally: book captioning for live events as part of planning. This is a procurement and scheduling decision more than a code one. The `at-test-protocol` skill, when it exists, should include a live-caption check for projects that stream.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.2.2 Captions (Prerecorded) (entry in this package). Once a live stream is published as a recording, 1.2.2 applies to the recording.
- SC 1.4.2 Audio Control (entry in this package). If the stream autoplays, a pause control is required.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Entirely manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
