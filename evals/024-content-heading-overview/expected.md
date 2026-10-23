# Eval 024: a heading that says only "Overview"

Input: `text.md`. A transcript eval for the `content` skill: a "Library cards" page with one `h2` over a short section on how to renew a card: two paragraphs and a numbered list of steps.

Intended defect: the `h2` says only "Overview". The section under it is about renewing a library card, online or at a desk, and the heading says none of that. Everything else is clean: the `h1` says what the page is, the levels do not skip, and the section is plain: the point comes first, the steps are a list, sentences are short and active, and no abbreviation is left unexpanded (textstat 0.7.13 `flesch_kincaid_grade` 2.9 over the section text, well under grade 8).

## Expected findings

1. **[Likely]** The heading does not describe its section.
   - Criterion: WCAG 2.2 SC 2.4.6 Headings and Labels (Level AA), tier 1, from `knowledge/wcag/sc-2.4.6-headings-and-labels.md`, which lists "Overview" as a heading that does not describe its section, likely until a person confirms it. The skill is not that person (principle 7), so the answer reports likely and says a human reviewer confirms.
   - Content entry: `knowledge/content/headings.md`, with `docs/content-standards.md` section 4, which names "Overview" as not a heading.
   - Where: `<h2>Overview</h2>`.
   - Acceptable fix directions: a heading that says what the section holds, for example a question ("How do I renew my library card?") or a statement ("Renew your card online or at a library desk"). Offered as a suggestion.

## Also acceptable

- Reporting it once under 2.4.6 and naming the house standard as context.
- A manual-review note that a page with a single section may not need an `h2` at all.

## Must not

- Report the defect twice, once under 2.4.6 and once as a house-standard miss.
- Grade it definite.
- Report the section's reading level or wording, the list, the `h1`, or the heading levels.
- Speak as, or for, a reader with a disability.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Replace the writer's text without offering it as a suggestion.

## Pass condition

Finding 1 is present under SC 2.4.6 (Level AA), tier 1, at likely, reported once, and nothing from the Must not list appears.
