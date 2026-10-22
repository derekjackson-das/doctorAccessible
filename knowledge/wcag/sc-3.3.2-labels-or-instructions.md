# SC 3.3.2 Labels or Instructions

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 3 Understandable / 3.3 Input Assistance
- Tier 1 source: https://www.w3.org/TR/WCAG22/#labels-or-instructions
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Labels or instructions are provided when content requires user input.

## What it requires, in our words

Every place a person has to type, choose, or upload tells them what is wanted. A field has a visible label. A field with a required format, such as a date or a phone number, says so before the person fills it in. Required fields are marked, and the marking is explained. A group of related controls, such as a set of radio buttons, has a question or heading that applies to the group. This criterion is about whether the label or instruction exists and is visible; whether it is programmatically attached is 1.3.1 and 4.1.2, and whether it is descriptive is 2.4.6. A placeholder that disappears when typing starts is not a label.

## How it fails in code

- A field with no visible label at all, where the only cue is a placeholder or the field's position. Definite.
- A set of fields that together make up one value, such as three boxes for a phone number or a date, with a label on the group only visually or on none of them. Definite. F82.
- A field with a required format (date, time, code) and no instruction about the format, where the format is not obvious. Likely; definite once a person agrees the format is not self-evident.
- Required fields marked with an asterisk and no explanation of the asterisk anywhere on the form. Likely.
- A group of radio buttons or checkboxes with no group label. Definite; also 1.3.1 for the missing association.
- A visible label that is not programmatically associated. Not this criterion; the label exists. That is 1.3.1 and 4.1.2.

## How to meet it

- Native HTML first. Technique H44, "Using label elements to associate text labels with form controls". Technique H71, "Providing a description for groups of form controls using fieldset and legend elements".
- Technique G131, "Providing descriptive labels", and Technique G167, "Using an adjacent button to label the purpose of a field", for a search field whose button says "Search".
- Instructions before the field, not after, and not only in the placeholder. Content standards section 7 in `docs/content-standards.md`.
- Advisory: Technique ARIA2, "Identifying a required field with the aria-required property", alongside a visible mark. Technique G13 for controls that cause a change of context.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`) and 1.3.1 Info and Relationships (`wcag/sc-1.3.1-info-and-relationships.md`). Whether the label is attached in the code.
- SC 2.4.6 Headings and Labels (`wcag/sc-2.4.6-headings-and-labels.md`). Whether the label describes the field.
- SC 1.3.5 Identify Input Purpose (`wcag/sc-1.3.5-identify-input-purpose.md`). The machine-readable purpose behind the label.
- SC 3.3.1 Error Identification (entry in this package). What happens when the instruction was not followed.
- SC 3.3.5 Help is Level AAA and not a requirement here.

## Automated coverage (tier 3)

axe-core tags `form-field-multiple-labels` to this criterion, which catches a field with more than one `label`. The `label` rule, tagged to 4.1.2, catches a field with no accessible name, which often coincides with a missing visible label. Whether instructions exist for a format, or an asterisk is explained, is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
