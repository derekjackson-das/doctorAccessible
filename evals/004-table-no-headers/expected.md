# Eval 004: data table with no header cells

Input: `input.html`. A price list laid out as a table with four columns and five data rows.

Intended defect: the first row looks like a header row (bold, shaded) and the first column looks like row headers, but every cell is a `td`. There is no `th`, no `scope`, no `headers` attribute. A screen reader reading a price cell cannot tell which size or which color it belongs to. Everything else is clean: language set, title present, one heading, landmarks, a `caption`, text and border colors above the contrast thresholds, visible focus, zoom not blocked.

## Expected findings

1. **[Definite]** Data table has no header cells.
   - Criterion: WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), tier 1
   - Source: `knowledge/wcag/sc-1.3.1-info-and-relationships.md`
   - Where: the `table` inside `main`; the first row and the first cell of each row
   - Acceptable fix directions: mark the first row's cells as `th scope="col"` and the first cell of each data row as `th scope="row"` (techniques H51 and H63). The entry lists F91 as the matching failure.

## Also acceptable

- A note that the bold styling on the first row is presentation standing in for structure, which is the F2 pattern, folded into the same finding rather than reported twice.
- A manual-review note that the caption and heading say similar things and a human may want to differentiate them.

## Must not

- Report the `caption`; it is present and correct.
- Report the heading, landmarks, focus style, language, or contrast. The border color `#767676` on white is above 3:1 and the text colors are above 4.5:1.
- Report a layout-table failure; this is a data table that lacks headers, not a layout table with headers.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is not expected to report a violation. The rule that would catch this, `td-has-header`, is tagged experimental and is off by default. A clean axe result with the defect still present is the point of this eval: it tests whether the verifier finds the defect by reading. If the verifier reports "axe found nothing, so the page passes," that is a failure of the verifier.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
