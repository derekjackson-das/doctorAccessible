# SC 3.3.1 Error Identification

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 3 Understandable / 3.3 Input Assistance
- Tier 1 source: https://www.w3.org/TR/WCAG22/#error-identification
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> If an input error is automatically detected, the item that is in error is identified and the error is described to the user in text.

## What it requires, in our words

When a form catches a mistake, it must say which field and what is wrong, in words. A red border alone fails: a colorblind user cannot see it and a screen reader user cannot hear it. An icon alone fails for the same reason. "There was an error" at the top of the page, with no indication of which field, fails because the user has to hunt. The text can be beside the field, in a summary at the top that names the fields, or both. The criterion does not require the form to detect errors; it requires that detected errors be identified and described in text. How to fix the error is the next criterion.

## How it fails in code

- A field in error marked only by a border color, background color, or icon, with no text. Definite. Also 1.4.1.
- A generic message ("Please correct the errors below") with no indication of which fields. Definite.
- Error text present but not associated with the field, so a screen reader user on the field does not hear it. Likely; the text exists, but the "identified" part depends on association. Use `aria-describedby` or place the text inside the label.
- A field cleared on error with no message. Definite.
- Error text that names the field and says what is wrong. Passes this criterion even if it does not say how to fix it.

## How to meet it

- Technique G83, "Providing text descriptions to identify required fields that were not completed", and Technique G85, "Providing a text description when user input falls outside the required format or values", and G84 for values not in an allowed list.
- Technique ARIA21, "Using aria-invalid to Indicate An Error Field", alongside the text, never instead of it.
- Technique ARIA19, "Using ARIA role=alert or Live Regions to Identify Errors", so client-side errors are announced when they appear. Technique SCR18 and SCR32 for client-side validation that adds text to the page.
- Content: see `docs/content-standards.md` section 7 for how to word the message. Name the field, say what is wrong, say what to do.
- Advisory: Technique G139, "Creating a mechanism that allows users to jump to errors", and G199, "Providing success feedback when data is submitted successfully".

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.3.3 Error Suggestion (entry in this package). Saying how to fix it, Level AA.
- SC 3.3.2 Labels or Instructions (entry in this package). Preventing the error in the first place.
- SC 1.4.1 Use of Color (`wcag/sc-1.4.1-use-of-color.md`). Color as the only error cue fails both; F81.
- SC 4.1.3 Status Messages (`wcag/sc-4.1.3-status-messages.md`). Whether the error message is announced without moving focus; Level AA.
- SC 1.3.1 Info and Relationships (`wcag/sc-1.3.1-info-and-relationships.md`). Associating the message with the field.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Error handling is script and server behavior that axe does not exercise; found by submitting the form with bad input. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
