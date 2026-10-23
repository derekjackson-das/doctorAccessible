# Eval 026: alt text that starts "Image of"

Input: `text.md`. A transcript eval for the `content` skill: a "The reading room" section with a photo of the room and one short paragraph.

Intended defect: the photo's `alt` starts "Image of". The rest of it, "rows of wooden desks under tall windows", serves the image's purpose and does not repeat the heading or the paragraph, so it meets SC 1.1.1. The opening words are redundant, because screen readers already announce an image. Everything else is clean: the heading describes the section, and the paragraph is plain (textstat 0.7.13 `flesch_kincaid_grade` 3.4).

## Expected findings

1. **[Likely]** The alt text starts "Image of", which screen readers already announce.
   - Standard: `docs/content-standards.md` section 6. A house-standard finding, not a WCAG failure.
   - Content entry: `knowledge/content/alt-text.md`. The "image of" point rests on WebAIM, tier 3; the W3C alt decision tree, tier 2, supports only the reading that a brief description meets the image's purpose.
   - WCAG: the answer says SC 1.1.1 Non-text Content (Level A) is met, since a text alternative that serves the purpose is present, citing `knowledge/wcag/sc-1.1.1-non-text-content.md`.
   - Where: `img[src="reading-room.jpg"]`.
   - Acceptable fix directions: drop "Image of", for example "Rows of wooden desks under tall windows". Offered as a suggestion.

## Also acceptable

- A manual-review note that only the author knows what the photo is for on this page, so the description could be shorter or longer.
- A manual-review question on whether the photo is decorative and could take an empty `alt`, as long as the answer does not call the current `alt` a failure.

## Must not

- Report the alt text as a WCAG failure, or as definite.
- Report it twice, under WCAG and under the house standard.
- Report the heading, the reading level, or the paragraph.
- Speak as, or for, a reader with a disability.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Replace the writer's text without offering it as a suggestion.

## Pass condition

Finding 1 is present as likely under the house standard, with 1.1.1 explained as met, and nothing from the Must not list appears.
