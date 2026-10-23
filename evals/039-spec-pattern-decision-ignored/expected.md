# Eval 039: a scripted accordion where the spec chose details and summary

Input: `input.html`, with the project's `a11y-spec.md` beside it. A borrowing-questions page with two questions that open and close.

Intended defect, a spec deviation, not a WCAG failure: the spec's Pattern decisions table says show/hide sections use "Native `details` and `summary`, not a scripted accordion". The page builds a scripted accordion: buttons in headings with `aria-expanded`.

Everything else is clean, on purpose, so the only thing to find is the deviation: the accordion itself is correct: native buttons in headings, `aria-expanded` updated on every toggle, panels hidden with `hidden`, visible focus, contrast about 7.1:1 or better, language, title, one `h1`, `main`.

## Expected findings

1. **[Definite]** The page uses a scripted accordion where the spec decided on native `details` and `summary`.
   - Spec deviation: Pattern decisions, 2026-10-01, "Native `details` and `summary`, not a scripted accordion".
   - Spec check: the report's Spec deviations section must mention: details / summary / accordion / pattern decision
   - Reported under the report's Spec deviations heading, quoting the spec line, and not as a WCAG finding (`.claude/agents/verifier.md`, "Spec deviations").
   - Definite or likely: the decision is quoted; what the page builds is read from the code.

## Also acceptable

- Noting that the accordion is otherwise built correctly.
- Suggesting `details` and `summary`, as a direction.
- Manual-review notes that a criterion appears met and needs a browser check.
- A note that axe has nothing to say about a spec deviation.

## Must not

- Report the deviation as a WCAG failure, or in the WCAG findings.
- Report `aria-expanded`, the buttons, or the headings as WCAG failures; they are correct.
- Report any WCAG failure (likely or definite); the page is built to pass WCAG 2.2 AA.
- Speak as, or for, a reader with a disability.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe checks WCAG rules, not the project's spec, so it is not expected to report the deviation. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 appears in the Spec deviations section, at definite or likely, quoting or naming the pattern decision, and nothing from the Must not list appears.
