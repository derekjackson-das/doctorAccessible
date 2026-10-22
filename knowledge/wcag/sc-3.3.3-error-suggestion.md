# SC 3.3.3 Error Suggestion

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 3 Understandable / 3.3 Input Assistance
- Tier 1 source: https://www.w3.org/TR/WCAG22/#error-suggestion
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> If an input error is automatically detected and suggestions for correction are known, then the suggestions are provided to the user, unless it would jeopardize the security or purpose of the content.

## What it requires, in our words

When the form knows what would fix the error, it says so. "Invalid date" fails; "Enter the date as month, day, year, for example 03/14/2026" passes. "Not a valid option" fails; "Choose one of: Cambridge, Allston, Longwood" passes. If the form cannot know the fix, it is not required to invent one. And where saying the fix would defeat the purpose, such as telling a user which of username or password was wrong on a login form, the exception applies. The content standards' rule for error messages is the same: name the field, say what is wrong, say what to do.

## How it fails in code

- An error message that says a value is wrong without saying what a right value looks like, when the format is known: "Invalid input", "Error", "Please check this field". Definite once the field's format is confirmed to be known.
- A field restricted to a list of values, with an error that does not name or point to the allowed values. Definite.
- A required field left empty, with a message that does not say the field is required. Definite.
- A login error that says only "Sign-in failed". Passes by the security exception.
- An error on free text where no correction can be suggested. Passes; nothing is known.

## How to meet it

- Technique G85, "Providing a text description when user input falls outside the required format or values", and Technique G84 for values not in an allowed list.
- Technique G177, "Providing suggested correction text": the example value, the allowed list, or the nearest match.
- Technique ARIA18, "Using aria-alertdialog to Identify Errors", when a dialog is the right container.
- Content: `docs/content-standards.md` section 7.
- Advisory: G139 to jump to errors, G199 for success feedback, SCR18 and SCR32 for client-side validation text.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.3.1 Error Identification (entry in this package). Saying which field and what is wrong, Level A. This adds the fix.
- SC 3.3.2 Labels or Instructions (entry in this package). Giving the format before the error happens.
- SC 3.3.4 Error Prevention (Legal, Financial, Data) (entry in this package). Checking and confirming before consequential submissions.
- SC 3.3.6 Error Prevention (All) is Level AAA and not a requirement here.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Judging whether a message suggests a fix means reading it after triggering the error, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
