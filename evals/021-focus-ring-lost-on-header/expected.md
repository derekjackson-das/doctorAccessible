# Eval 021: focus ring that passes on the page but disappears on the header

Input: `input.html`. A short library-hours page with a dark blue header holding three navigation links, and a white main area.

Intended defect: one site-wide focus style, `outline: 3px solid #005a9c`, is used everywhere. On the white main area it is about 7.1:1 against the page, so a check against the page background passes. The header links sit on `#00478a`, and the outline (offset 2px into the header) is about 1.3:1 against it, so focus on the three header links is effectively invisible. Everything else is clean: language set, title present, one heading, landmarks, a named navigation region, link text, text contrast (white on the header about 9.3:1; body text and links above 7:1), no motion.

## Expected findings

1. **[Definite]** The focus indicator on the header links does not contrast with the color next to it.
   - Criterion: WCAG 2.2 SC 1.4.11 Non-text Contrast (Level AA), tier 1, from `knowledge/wcag/sc-1.4.11-non-text-contrast.md` ("a focus indicator below 3:1 against the adjacent colors", graded definite). SC 2.4.7 Focus Visible (Level AA) may be cross-referenced, or raised as likely; the 2.4.7 entry grades "invisible in practice" definite only once observed, which reading the code does not do. One finding, not two.
   - Design entry: `knowledge/design/focus-indicators.md`, for the requirement and the practice of checking the ring against every background it can sit on.
   - Where: `header a` focus, from the `:focus-visible` rule.
   - Acceptable fix directions: a focus color that contrasts with both backgrounds, a header-specific focus style (for example a white or yellow outline in the header), or a two-color indicator. Any of these, as a direction, not a patch.

## Also acceptable

- Stating the measured ratios (about 7.1:1 on white, about 1.3:1 on the header), computed from the declared colors.
- A practice note, marked as practice and tier 2 or 3, about the focus indicator's size or a two-color ring, or that SC 2.4.13 Focus Appearance is Level AAA and beyond the target.
- Noting that axe has no rule for focus indicators, from the entries.

## Must not

- Report the main-area links' focus ring, which passes.
- Report text contrast, the header link color, landmarks, headings, or language.
- Report the defect twice, once under 1.4.11 and once under 2.4.7.
- Mark a practice-only point (two-color rings, thickness above the minimum, SC 2.4.13) as definite.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

The 1.4.11 and 2.4.7 entries say axe has no rule tagged to either criterion and that its `color-contrast` rule covers text only, so axe is not expected to report this defect; the finding must come from reading. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under 1.4.11 with the right level and tier, and nothing from the Must not list appears.
