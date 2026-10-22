# Eval 003: video with no captions

Input: `input.html`. A page with one prerecorded video of a narrated campus tour.

Intended defect: the `video` element has a soundtrack (the description says a guide narrates) and no `track` element with `kind="captions"`, and nothing on the page indicates open captions. Everything else is clean: language set, title present, one heading, landmarks, the video has `controls`, it does not autoplay, visible focus, zoom not blocked.

## Expected findings

1. **[Definite]** Prerecorded video has no captions.
   - Criterion: WCAG 2.2 SC 1.2.2 Captions (Prerecorded) (Level A), tier 1
   - Source: `knowledge/wcag/sc-1.2.2-captions-prerecorded.md`
   - Where: the `video` element inside `main`
   - Acceptable fix directions: add a `track kind="captions"` pointing at a WebVTT file with the speech and meaningful sounds (technique G87), or provide open captions in the video (technique G93).

## Also acceptable

- A cross-reference to SC 1.2.3 and 1.2.5, marked as a second gap or as manual review, noting that a narrated video also needs audio description or a text alternative. The entries exist in this package. If the verifier reports this as a separate Definite finding, note it: the page description does not say whether the visuals carry information beyond the narration, so Likely or Manual review is the better confidence.
- A manual-review note that the file is not provided, so the presence of sound and the nature of the content cannot be confirmed from code.
- A manual-review note that the video also needs a descriptive label under SC 1.1.1 if the heading and paragraph are judged insufficient.

## Must not

- Report autoplay or audio control; the video does not autoplay.
- Report the fallback text inside the `video` element.
- Report the heading, landmarks, focus style, or language.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report rule `video-caption`, tagged `wcag122`, as **incomplete (needs review)** rather than as a violation, because it cannot tell from code whether the video has an audio track. It reports no violations. A verifier that treats "no violations" as a pass has failed this eval; the defect is found by reading the markup and the page's own description of the content. If axe reports a violation on anything else, the input is not clean and needs fixing.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
