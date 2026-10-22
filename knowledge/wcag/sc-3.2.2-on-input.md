# SC 3.2.2 On Input

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 3 Understandable / 3.2 Predictable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#on-input
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/on-input.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Changing the setting of any user interface component does not automatically cause a change of context unless the user has been advised of the behavior before using the component.

## What it requires, in our words

Changing a value must not, by itself, move the user somewhere else. The classic failure is the "jump menu": a select list that navigates to a new page the moment an option is chosen. A keyboard user arrowing through the options to hear them triggers the first one and is gone. Checking a box must not submit the form; filling the last field must not auto-submit; choosing a radio button must not open a window. If a control does need to cause a change of context on change, the page must say so before the user reaches it. Updating other content on the same page without moving the user, such as showing a dependent field, is allowed.

## How it fails in code

- A `select` with a `change` handler that navigates, with no "Go" button and no advance notice. Definite. The classic jump menu.
- A form that submits automatically when the last field is filled or a radio button is chosen, with no warning. Definite. F36.
- A checkbox, radio button, or select that opens a new window on change without warning. Definite. F37.
- A select that reveals extra fields on the same page when changed. Not a failure; no change of context.
- A control that does cause a change of context on change, with instructions before it saying so. Passes; a person confirms the notice is reachable before the control.

## How to meet it

- Technique G80, "Providing a submit button to initiate a change of context": a "Go" or "Apply" button beside the select.
- Technique G13, "Describing what will happen before a change to a form control that causes a change of context to occur is made", when the automatic behavior must stay.
- Technique SCR19, "Using an onchange event on a select element without causing a change of context", for updating content in place.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.2.1 On Focus (entry in this package). The same rule for merely focusing a control.
- SC 2.2.1 Timing Adjustable (`wcag/sc-2.2.1-timing-adjustable.md`). Automatic submission on a timer rather than on input.
- SC 3.3.2 Labels or Instructions (entry in this package). Where the advance notice lives.
- SC 3.2.5 Change on Request is Level AAA and not a requirement here.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Change handlers are found by reading the script or by operating the control with a keyboard. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
