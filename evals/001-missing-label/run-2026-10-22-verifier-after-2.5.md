# Verifier run, 2026-10-22, eval 001, after package 2.5

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17) after the wcag skill map was rewritten and the 4.1.2 entry's related-criteria references were updated to link the entries that now exist. Same conditions as earlier runs.

Result against `expected.md`: **pass**. One Definite finding, SC 4.1.2 Name, Role, Value (Level A), tier 1, at `#q`, with H44 and ARIA16 as fix directions. SC 1.3.1 was co-cited inside the same finding rather than as a second finding, following both entries' instruction to report an unassociated label once and name both. SC 3.3.2 noted as no entry yet and not raised. Nothing from the must-not list. No file modified.

Two changes in behavior since the first runs, both improvements:

1. The agent ran axe twice, default and with `--tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`, because the evals README now says the default run skips WCAG 2.2 rules. The guidance landed in package 2.2 and the agent picked it up unprompted.
2. The agent computed contrast ratios but explicitly declined to cite them as passes because it had not opened the contrast entries, and put them under manual checks instead. That is the behavior the earlier numbers-from-memory observations asked for, arrived at without a prompt change. The tightening PR should still make it a rule so it does not depend on the agent's mood.

## Report as returned (findings and scan)

### [Definite] Text input has no accessible name
- Where: `input.html` line 22, `<input type="text" id="q" name="q">` (selector `#q`); the visible text is line 21, `<span>Search</span>`
- What: The search field has no `label` element, no `aria-label`, no `aria-labelledby`, and no `title`; the word "Search" sits beside it in a `span` that is not associated with the control, so no name is programmatically determinable and the visible label-to-field relationship exists only in the layout.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1. Co-cited: WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), tier 1. Both entries say an unassociated visible label fails both and should be reported as one finding naming both.
- Source: knowledge/wcag/sc-4.1.2-name-role-value.md; knowledge/wcag/sc-1.3.1-info-and-relationships.md (F111)
- Fix direction: Make the existing visible text the label by changing the `span` to a `label for="q"` (Technique H44); `aria-labelledby` pointing at the span (ARIA16) is the fallback. SC 3.3.2 has no entry yet; a visible label is present, so no separate 3.3.2 finding, unverified.

Observations, not findings: `lang`, `title`, one `h1`, landmarks (bypass met per the 2.4.1 entry); `:focus-visible` outline defined; targets about 34 CSS px tall, above the 2.5.8 floor, and `target-size` passed in the tagged run; contrast ratios computed (about 16.7:1 and 7.1:1) but not cited as passes because the contrast entries were not opened; left under manual checks.

Content: reading level not measured (three words of text). Heading matches title. Manual review on whether "Search" alone says what is searched.

Manual checks remaining: screen reader name and role on the field; keyboard order and focus visibility; formal contrast check against the 1.4.3 and 1.4.11 entries; 400% reflow of the flex row with no `flex-wrap`; label descriptiveness in context; results page behavior.

Automated scan: axe-core 4.14.0. Default run: 1 violation, `label`, `#q`. Tagged run: 1 violation (`label`), 10 passed, 0 incomplete, 53 inapplicable; no WCAG 2.2 rule fired.
