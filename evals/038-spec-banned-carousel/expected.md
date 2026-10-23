# Eval 038: a carousel the spec bans

Input: `input.html`, with the project's `a11y-spec.md` beside it. A home page with a three-story news slider.

Intended defect, a spec deviation, not a WCAG failure: the spec's Banned patterns section bans "Carousels and slideshows, rotating or not", and its need statement and pattern decision call for a list. The page shows the news as a slider with previous and next buttons.

Everything else is clean, on purpose, so the only thing to find is the deviation: the slider does not rotate; its buttons are native and named; the region and each story are named; hidden stories use `hidden`; focus is visible; contrast is about 7.1:1 or better; language, title, headings in order, `main`.

## Expected findings

1. **[Definite]** The page uses a carousel, which the spec bans.
   - Spec deviation: Banned patterns, "Carousels and slideshows, rotating or not."
   - Spec check: the report's Spec deviations section must mention: carousel / slideshow / slider
   - Reported under the report's Spec deviations heading, quoting the spec line, and not as a WCAG finding (`.claude/agents/verifier.md`, "Spec deviations").
   - Definite or likely: whether a carousel is on the page is read from the code; the ban is quoted from the spec.

## Also acceptable

- Citing the need statement or the pattern decision as well, inside the same deviation.
- Suggesting the list the spec calls for, as a direction.
- Manual-review notes that a criterion appears met and needs a browser check.
- A note that axe has nothing to say about a spec deviation.

## Must not

- Report the deviation as a WCAG failure, or in the WCAG findings.
- Report the carousel's buttons, names, or hidden slides as WCAG failures; they are correct.
- Report any WCAG failure (likely or definite); the page is built to pass WCAG 2.2 AA.
- Speak as, or for, a reader with a disability.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe checks WCAG rules, not the project's spec, so it is not expected to report the deviation. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 appears in the Spec deviations section, at definite or likely, quoting or naming the ban, and nothing from the Must not list appears.
