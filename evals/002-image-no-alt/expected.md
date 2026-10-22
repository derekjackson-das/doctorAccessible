# Eval 002: image with no alt attribute

Input: `input.html`. A short page about visiting a library, with one image of the building.

Intended defect: the `img` element has no `alt` attribute at all. Everything else is clean: language set, title present, one heading, landmarks, body text, one link with descriptive text, visible focus, zoom not blocked.

## Expected findings

1. **[Definite]** Image has no text alternative.
   - Criterion: WCAG 2.2 SC 1.1.1 Non-text Content (Level A), tier 1
   - Source: `knowledge/wcag/sc-1.1.1-non-text-content.md`
   - Where: the `img` inside `main`
   - Acceptable fix directions: add an `alt` attribute that says the purpose (for example the building's name and what the reader is meant to take from it), or, if the image is judged decorative, `alt=""` so assistive technology skips it. The entry points at techniques H37 and H67.

## Also acceptable

- A manual-review note that whether the image is informative or decorative is a judgment for a person, and that the alt text, once written, should be checked against the content standards.
- A cross-reference to SC 4.1.2 marked as not applicable here because the image is not a control.

## Must not

- Report the link text, the heading, landmarks, focus style, language, or contrast.
- Report the `data:` URI or the inline SVG as a defect.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report one violation, rule `image-alt`, tagged `wcag111`. If axe reports more, the input is not clean and needs fixing.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
