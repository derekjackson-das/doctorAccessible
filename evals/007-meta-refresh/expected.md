# Eval 007: timed redirect with a meta refresh

Input: `input.html`. A confirmation page between two steps of a registration process.

Intended defect: a `meta http-equiv="refresh"` with a 20-second delay redirects the page to the next step. A person reading slowly, using a screen reader, or zoomed in may be moved on before they have finished, with no warning and no way to turn the timer off or extend it. Everything else is clean: language set, title present, one `h1`, landmarks, a descriptive link to the same destination, visible focus, contrast above the thresholds.

## Expected findings

1. **[Definite]** Page redirects on a timer with no way to turn it off, adjust, or extend.
   - Criterion: WCAG 2.2 SC 2.2.1 Timing Adjustable (Level A), tier 1
   - Source: `knowledge/wcag/sc-2.2.1-timing-adjustable.md`
   - Where: the `meta http-equiv="refresh"` element in `head`
   - Acceptable fix directions: remove the meta refresh and rely on the existing "Continue" link; or, if an automatic advance is wanted, give the user a way to turn it off or extend it with at least 20 seconds' warning (techniques G198, SCR16 with SCR1). The entry names F40 and F41 as the matching failures.

## Also acceptable

- A cross-reference to SC 3.2.5 Change on Request, marked as Level AAA and not a requirement, or marked "no entry yet".
- A note that the page is a step in a process and still fails, because 2.2.1 has no process exemption (that exemption belongs to 2.4.5).

## Must not

- Report the "Continue" link; its text says where it goes.
- Report the heading, landmarks, focus style, language, or contrast.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report one violation, rule `meta-refresh`, tagged `wcag221`. If axe reports more, the input is not clean and needs fixing.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
