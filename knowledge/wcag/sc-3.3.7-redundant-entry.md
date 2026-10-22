# SC 3.3.7 Redundant Entry

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 3 Understandable / 3.3 Input Assistance
- Tier 1 source: https://www.w3.org/TR/WCAG22/#redundant-entry
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html
- Also in: WCAG 2.2 only. New in 2.2; not in 2.0 or 2.1.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Information previously entered by or provided to the user that is required to be entered again in the same process is either:
>
> - auto-populated, or
> - available for the user to select.
>
> Except when:
>
> - re-entering the information is essential,
> - the information is required to ensure the security of the content, or
> - previously entered information is no longer valid.

## What it requires, in our words

Within one process, such as a checkout, an application, or a multi-step registration, a person should not have to type the same thing twice. If the shipping address was entered on step two, step four offers "same as shipping" or fills it in. If the email was given on the first page, the confirmation page does not ask for it again blank. Re-typing is slow and error-prone for everyone and a real barrier for people with motor or memory difficulties. Exceptions: when re-entry is the point (a "type your password twice" check, or a signature), when security needs it, or when the earlier value has stopped being valid. The criterion applies within a process, not across separate visits.

## How it fails in code

- A multi-step form that asks for the same information on two steps with no auto-fill and no selectable copy. Definite once the steps are confirmed to be one process.
- A billing address form with no "same as shipping" option when shipping was already entered. Definite.
- A "confirm your email" field. Passes by the essential exception, as the Understanding page treats confirmation fields.
- A password re-entered for a security-sensitive step. Passes by the security exception.
- The same information asked for in a separate process on a later visit. Not covered; different process.

## How to meet it

- Technique G221, "Provide data from a previous step in a process": carry the value forward, pre-fill the field, or offer a checkbox or select that copies it.
- The `autocomplete` attributes from SC 1.3.5 help the browser do some of this, but do not by themselves meet the criterion, which is about the process carrying its own data.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.3.5 Identify Input Purpose (`wcag/sc-1.3.5-identify-input-purpose.md`). Browser autofill for the user's own details.
- SC 3.3.8 Accessible Authentication (Minimum) (entry in this package). The other WCAG 2.2 criterion aimed at memory burden.
- SC 2.2.1 Timing Adjustable (`wcag/sc-2.2.1-timing-adjustable.md`). A process that times out and discards entered data forces redundant entry.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Redundant entry is found by walking the process, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
