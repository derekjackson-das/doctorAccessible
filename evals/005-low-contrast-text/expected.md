# Eval 005: body text below the contrast minimum

Input: `input.html`. A short page about office hours with two paragraphs.

Intended defect: the second paragraph is normal-size text in `#999999` on `#ffffff`, a contrast ratio of about 2.85:1, below the 4.5:1 minimum for text that is not large. Everything else is clean: language set, title present, one heading, landmarks, the first paragraph is `#1a1a1a` on white, visible focus, zoom not blocked.

## Expected findings

1. **[Definite]** Text contrast below the minimum.
   - Criterion: WCAG 2.2 SC 1.4.3 Contrast (Minimum) (Level AA), tier 1
   - Source: `knowledge/wcag/sc-1.4.3-contrast-minimum.md`
   - Where: the paragraph with class `note` inside `main`
   - Acceptable fix directions: darken the text color until the ratio against white is at least 4.5:1 (technique G18). `#767676` is the lightest neutral gray that passes on white. Or do not de-emphasize the note with color at all.

## Also acceptable

- Stating the measured ratio, since the entry gives the thresholds and the colors are solid and known. This is a computation from the source, not a number from memory.
- A content note that the second paragraph is the one with the time-sensitive warning, so making it fainter works against the reader. Manual review.

## Must not

- Report the first paragraph or the heading; both are far above 4.5:1.
- Report the focus outline color; `#005a9c` on white is above 3:1 and in any case is SC 1.4.11, not this criterion.
- Report the heading, landmarks, or language.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report one violation, rule `color-contrast`, tagged `wcag143`, on the `.note` paragraph. If axe reports more, the input is not clean and needs fixing.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
