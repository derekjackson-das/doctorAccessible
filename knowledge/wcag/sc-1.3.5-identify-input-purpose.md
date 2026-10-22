# SC 1.3.5 Identify Input Purpose

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.3 Adaptable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#identify-input-purpose
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> The purpose of each input field collecting information about the user can be programmatically determined when:
>
> - The input field serves a purpose identified in the Input Purposes for user interface components section; and
> - The content is implemented using technologies with support for identifying the expected meaning for form input data.

## What it requires, in our words

Form fields that ask for the user's own details, such as their name, email, phone, street address, or birthday, must say so in the code using a standard vocabulary, so that browsers and assistive tools can fill them in automatically or show a familiar icon beside them. In HTML the mechanism is the `autocomplete` attribute with the token for that purpose, for example `autocomplete="email"`. The W3C publishes the list of purposes in the Recommendation's "Input Purposes for user interface components" section. Fields that ask about something other than the user, such as a search box or a product quantity, are not covered. This helps people with memory or motor difficulties most, because typing their own address every time is a real barrier.

## How it fails in code

- A field for one of the listed purposes (name, email, tel, street-address, postal-code, bday, and the rest) with no `autocomplete` attribute. Definite once the field is confirmed to collect information about the user.
- An `autocomplete` value that is not a valid token or does not match what the field collects, such as `autocomplete="name"` on an email field, or `autocomplete="off"` on a covered field. Definite. F107.
- A field whose purpose is ambiguous from the label, such as "Contact" that might be phone or email. Manual review.

## How to meet it

- Technique H98, "Using HTML autocomplete attributes": add the matching token to each covered field. Section-and-contact modifiers such as `shipping` or `billing` are allowed in front of the token.
- Check the token against the list in https://www.w3.org/TR/WCAG22/#input-purposes rather than from memory.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). The field also needs a name; this criterion adds a machine-readable purpose.
- SC 3.3.7 Redundant Entry (`wcag/sc-3.3.7-redundant-entry.md`). The WCAG 2.2 criterion that asks not to make users re-enter information in one process. Autocomplete is one way to help with that.
- SC 3.3.2 Labels or Instructions (`wcag/sc-3.3.2-labels-or-instructions.md`). The visible label; this criterion is about the code behind it.

## Automated coverage (tier 3)

axe-core tags `autocomplete-valid` to this criterion. It checks that an `autocomplete` value that is present is a valid token for the field type. It does not flag a covered field that has no `autocomplete` at all, because axe cannot know the field's purpose from the label. That gap is the common failure and remains manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
