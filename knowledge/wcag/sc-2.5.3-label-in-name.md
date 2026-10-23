# SC 2.5.3 Label in Name

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.5 Input Modalities
- Tier 1 source: https://www.w3.org/TR/WCAG22/#label-in-name
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON
- Updated 2026-10-23 by Caesar Alam with Claude Code: added the `aria-labelledby` case under "How it fails in code" (WP 3.8).

## Normative text (tier 1, quoted)

> For user interface components with labels that include text or images of text, the name contains the text that is presented visually.
>
> Note: A best practice is to have the text of the label at the start of the name.

## What it requires, in our words

The name a control exposes to assistive technology must include the words a sighted person sees on it. A speech recognition user says "click Search" because that is what the button says; if the button's `aria-label` is "Submit query", the command fails. The accessible name can say more than the visible label, but it must contain it, ideally at the start. This goes wrong when `aria-label` or `aria-labelledby` overrides the visible text with something different, or when an icon button has a visible word beside it that the name does not include.

## How it fails in code

- A control with visible text and an `aria-label` that does not contain that text: visible "Search", name "Submit". Definite. F96.
- A control whose `aria-labelledby` points only at other text, such as a format hint, so the visible label is left out of the name: the `aria-labelledby` replaces the `label` (`aria/accessible-name.md`). Definite. F96.
- A link whose visible text is "Read more" and whose `aria-label` is "Article about printing", omitting "Read more". Definite. F96. The fix for 2.4.4 that breaks 2.5.3 is a common pattern; include both: "Read more about printing".
- A control with visible label text but no accessible name at all. Definite; shared with 1.3.1 and 4.1.2. F111.
- Visible text that is an image of text, with an alt that differs. Definite.
- A name that contains the visible text plus more, at the end: "Printing, read more". Passes; the note prefers label first.

## How to meet it

- Technique G208, "Including the text of the visible label as part of the accessible name".
- Technique G211, "Matching the accessible name to the visible label": the simplest is no `aria-label` at all, so the visible text is the name.
- Advisory: Technique G162 on label placement.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). Whether a name exists; this says what it must contain.
- SC 2.4.4 Link Purpose (In Context) (entry in this package). Making link text descriptive without replacing the visible words.
- SC 1.3.1 Info and Relationships (`wcag/sc-1.3.1-info-and-relationships.md`). An unassociated label.
- SC 2.4.6 Headings and Labels (entry in this package). Whether the visible label is itself descriptive.

## Automated coverage (tier 3)

axe-core tags `label-content-name-mismatch` to this criterion. It compares visible text to the accessible name for elements named by their content and flags a mismatch. It is marked experimental in some versions; check whether it ran. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
