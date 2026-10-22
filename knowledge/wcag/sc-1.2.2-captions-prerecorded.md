# SC 1.2.2 Captions (Prerecorded)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.2 Time-based Media
- Tier 1 source: https://www.w3.org/TR/WCAG22/#captions-prerecorded
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Captions are provided for all prerecorded audio content in synchronized media, except when the media is a media alternative for text and is clearly labeled as such.

## What it requires, in our words

A recorded video that has sound needs captions: text of the speech, who is speaking when it matters, and meaningful sounds such as laughter or a door slamming, timed to the video. "Synchronized media" is the W3C term for sound and picture together, or either one paired with interaction. Captions can be closed, meaning the viewer turns them on, or open, meaning burned into the picture. Automatic captions count only if they are accurate; the criterion is about what the viewer gets, not how it was produced. The exception is a video that is itself a labeled alternative to text on the page.

## How it fails in code

- A `video` element with an audio track and no `track kind="captions"` and no open captions in the picture. Definite once the video is confirmed to have speech or meaningful sound and not to be a labeled text alternative. F75.
- Captions present but missing dialogue or important sounds. Manual review; a person must watch with captions on. F8.
- A video that is an alternative for text on the page but is not labeled as such. Likely; the label is what makes the exception apply. F74.
- An embedded third-party player (for example an `iframe`) whose captions cannot be confirmed from the code. Manual review.

## How to meet it

- Technique G87, "Providing closed captions". In HTML, a `track` element with `kind="captions"` inside the `video` element, pointing at a WebVTT file.
- Technique G93, "Providing open (always visible) captions", when the player cannot show closed captions.
- Content: captions follow the house content standards for plain language where they paraphrase, but speech is transcribed as spoken.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.2.4 Captions (Live) (entry in this package). The live counterpart, Level AA.
- SC 1.2.3 and 1.2.5 (entries in this package). Captions serve people who cannot hear; audio description serves people who cannot see. A video usually needs both.
- SC 1.2.1 (entry in this package). For media with sound only or picture only.

## Automated coverage (tier 3)

axe-core tags `video-caption` to this criterion. It reports a `video` element with no captions `track` as "incomplete, needs review", not as a violation, because it cannot tell whether the video has sound; a one-line summary that shows only violations will hide it (observed with axe-core 4.14.0 on eval 003). It cannot detect open captions, cannot judge caption accuracy, and cannot see inside a third-party player. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
