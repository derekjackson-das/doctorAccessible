# Verifier run, 2026-10-22, eval 003

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), same conditions as the other runs.

Result against `expected.md`: **pass**. One Definite finding, SC 1.2.2 Captions (Prerecorded) (Level A), tier 1, sourced to the entry, at `main > video`, with G87 as the fix direction and a note that confidence rests on the page's own description since the media file is absent. Audio description raised as Likely under SC 1.2.5, reported once with 1.2.3 named, exactly the confidence the key asks for. The video's programmatic name raised as manual review under 1.1.1. Nothing from the must-not list reported as a finding; autoplay was noted as inapplicable and the fallback text as a best-practice gap with no criterion cited. No file modified.

Observation, acted on in this PR: the agent found that axe-core 4.14.0 files `video-caption` under "incomplete, needs review" rather than violations, so the plain CLI summary reads "0 violations". The 1.2.2 entry and the eval's answer key were corrected to say so.

## Report as returned (findings and scan)

### [Definite] Video has no captions
- Where: `input.html` lines 19 to 21, selector `main > video`
- What: The `video` element carries an `src` and `controls` but no `track kind="captions"` child, and nothing on the page indicates open captions; the page's own description ("walk through the main quad with a student guide") indicates prerecorded synchronized media with speech, and the video is not labeled as an alternative for text, so the exception does not apply.
- Criterion: WCAG 2.2 SC 1.2.2 Captions (Prerecorded) (Level A), tier 1
- Source: knowledge/wcag/sc-1.2.2-captions-prerecorded.md (failure pattern F75; technique G87)
- Fix direction: Add a `track kind="captions" srclang="en" label="English"` pointing at an accurate WebVTT file; or supply a version with open captions.
- Note on confidence: the entry conditions Definite on the video having speech or meaningful sound. The media file is absent, so that rests on the page's description. If the file is silent, this moves to SC 1.2.1 instead, which would still be unmet.

### [Likely] Video has no audio description and no media alternative
- Where: `main > video` and the surrounding `main`
- What: No second audio track, no described version, no `track kind="descriptions"`, and no transcript on the page; a walking tour is likely to show things the guide does not say aloud.
- Criterion: WCAG 2.2 SC 1.2.5 Audio Description (Prerecorded) (Level AA), tier 1. SC 1.2.3 is also unmet; the 1.2.3 entry says at an AA target 1.2.5 governs, so reported once.
- Source: knowledge/wcag/sc-1.2.5-audio-description-prerecorded.md; knowledge/wcag/sc-1.2.3-audio-description-or-media-alternative-prerecorded.md
- Fix direction: G78 or G173; if the narration already covers everything shown, a human confirms and documents that.
- Why Likely: both entries make this Definite only once a person confirms the visuals matter.

### [Manual review] Video has no programmatic accessible name
- Where: `main > video`
- What: No `aria-label`, `aria-labelledby`, or `title`; the heading and paragraph identify the media on the page, which plausibly satisfies SC 1.1.1's time-based media clause, but the identification is adjacent rather than attached.
- Criterion: WCAG 2.2 SC 1.1.1 Non-text Content (Level A), tier 1
- Source: knowledge/wcag/sc-1.1.1-non-text-content.md
- Fix direction: If testing shows the player is announced without its subject, point `aria-labelledby` at the `h1` or use a `figcaption`.

Not findings: contrast passes; `lang`, `title`, landmarks, heading order, zoom all fine; no autoplay; fallback text offers no link to the file, a best practice gap with no criterion cited.

Manual checks remaining: play the file to confirm speech; watch with sound off to judge audio description; check captions for completeness once they exist; keyboard-operate the native player; screen reader identification of the player; 400% reflow of the control bar.

Automated scan: axe-core 4.14.0. Violations 0. Incomplete 1: `video-caption`, "Check that captions are available for the element". Passes 17. The plain CLI summary reads "0 violations found"; anyone relying on it would miss the page's main defect.
