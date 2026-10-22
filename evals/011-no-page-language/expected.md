# Eval 011: page with no language declared

Input: `input.html`. A short notice about parking permits.

Intended defect: the `html` element has no `lang` attribute. A screen reader cannot tell what language the page is in and falls back to its own default voice. Everything else is clean: title present and matching the `h1`, landmarks, descriptive link text, visible focus, contrast above the thresholds, zoom not blocked.

## Expected findings

1. **[Definite]** Page language not declared.
   - Criterion: WCAG 2.2 SC 3.1.1 Language of Page (Level A), tier 1
   - Source: `knowledge/wcag/sc-3.1.1-language-of-page.md`
   - Where: the `html` element
   - Acceptable fix directions: add `lang="en"` to the `html` element (technique H57).

## Also acceptable

- A note that the content is in English, so `en` is the right value, marked as a judgment from reading.
- A content note that "a.m." or similar abbreviations are absent and the text meets the reading-level default.

## Must not

- Report SC 3.1.2 Language of Parts; there are no passages in another language.
- Report the heading, link text, landmarks, focus style, or contrast.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report one violation, rule `html-has-lang`, tagged `wcag311`. If axe reports more, the input is not clean and needs fixing.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
