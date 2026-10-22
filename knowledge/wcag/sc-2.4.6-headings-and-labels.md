# SC 2.4.6 Headings and Labels

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 2 Operable / 2.4 Navigable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#headings-and-labels
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Headings and labels describe topic or purpose.

## What it requires, in our words

Where there is a heading, it says what the section is about. Where there is a label, it says what the field is for. This criterion does not require headings or labels to exist (that is 1.3.1 and 3.3.2); it requires that the ones present be meaningful. Screen reader users navigate by headings and hear labels when they land on a field; "Section 2", "Overview", "Details", and "Field 1" leave them guessing. Short and specific beats long and vague. The house content standards in `docs/content-standards.md` set the house style for both.

## How it fails in code

- A heading that does not describe its section: "Overview", "Introduction", "More", "Untitled", or a decorative phrase. Definite once a person reads the section and the heading does not fit it. Judgment is involved, so Likely from code alone.
- Several headings with the same text over different content on one page. Definite.
- A form label that does not say what to enter: "Field", "Input", "Enter here", or a label that describes format but not purpose. Definite once confirmed.
- Headings that are descriptive but use the wrong level or skip levels. Not this criterion; that is 1.3.1 and a best practice.
- A heading that is missing where one is needed. Not this criterion; 1.3.1 if the visual design implies one.

## How to meet it

- Technique G130, "Providing descriptive headings", and Technique G131, "Providing descriptive labels".
- Content: write the heading as the answer to "what will I find here?" and the label as the answer to "what goes in this box?" See `docs/content-standards.md`.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.3.1 Info and Relationships (`wcag/sc-1.3.1-info-and-relationships.md`). Whether the heading or label exists in the code.
- SC 3.3.2 Labels or Instructions (`wcag/sc-3.3.2-labels-or-instructions.md`). Whether a label exists at all.
- SC 2.4.2 Page Titled (entry in this package). The same requirement for the page title.
- SC 2.4.10 Section Headings is Level AAA and not a requirement here.
- SC 2.5.3 Label in Name (entry in this package). The visible label must be in the accessible name.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Its `empty-heading` best-practice rule catches a heading with no text, but whether a heading describes its section is a reading judgment. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
