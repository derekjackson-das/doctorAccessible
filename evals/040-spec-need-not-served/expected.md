# Eval 040: a page that does not serve its need statement

Input: `input.html`, with the project's `a11y-spec.md` beside it. A Widener Library page with news, visiting notes, and a weekly hours table.

Intended defect, a spec deviation, not a WCAG failure: the need statement says the page shows "today's opening and closing time, as text, as the first thing in the main content", instead of "a weekly timetable as the only way to find today". The page puts a weekly table last, after news and visiting notes, and nothing says which day is today.

Everything else is clean, on purpose, so the only thing to find is the deviation: the table has a caption and row and column headers; headings describe their sections and are in order; contrast is about 7.1:1 or better; language, title, one `h1`, `main`.

## Expected findings

1. **[Manual review]** The page does not appear to serve the opening-hours need statement: today's hours are not first, and appear only in a weekly table at the end.
   - Spec deviation: Need statements, "Opening hours", "today's opening and closing time, as text, as the first thing in the main content".
   - Spec check: the report's Spec deviations section must mention: need statement / today / opening hours
   - Reported under the report's Spec deviations heading, quoting the spec line, and not as a WCAG finding (`.claude/agents/verifier.md`, "Spec deviations").
   - Manual review, or likely: the verifier reports what the code exposes against what the spec says and hands the judgment to a person (`.claude/agents/verifier.md`, Rules). Definite is not expected.

## Also acceptable

- Naming the manual test the spec owes (VoiceOver on a phone reading today's hours first).
- Suggesting today's hours as text above the news, as a direction.
- Manual-review notes that a criterion appears met and needs a browser check.
- A note that axe has nothing to say about a spec deviation.

## Must not

- Report the deviation as a WCAG failure, or in the WCAG findings.
- Grade the deviation definite.
- Report the table, headings, or order of sections as a WCAG failure (1.3.1, 1.3.2, 2.4.6); they are correct.
- Report any WCAG failure (likely or definite); the page is built to pass WCAG 2.2 AA.
- Speak as, or for, a reader with a disability.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe checks WCAG rules, not the project's spec, so it is not expected to report the deviation. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 appears in the Spec deviations section, at manual review or likely, quoting or naming the need statement, and nothing from the Must not list appears.
