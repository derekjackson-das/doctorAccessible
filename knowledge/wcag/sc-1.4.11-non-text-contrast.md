# SC 1.4.11 Non-text Contrast

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#non-text-contrast
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s):
>
> **User Interface Components.** Visual information required to identify user interface components and states, except for inactive components or where the appearance of the component is determined by the user agent and not modified by the author;
>
> **Graphical Objects.** Parts of graphics required to understand the content, except when a particular presentation of graphics is essential to the information being conveyed.

## What it requires, in our words

The parts of a control that tell you it is a control, and what state it is in, must contrast with what is next to them by at least 3:1. That means the border of a text field against the page, the outline of a checkbox, the focus ring against the background, the icon on an icon button. The same applies to the parts of a graphic you need in order to understand it, such as the lines in a chart or the shapes in an icon. Text inside the control is SC 1.4.3. A control's visual identity does not have to come from a border; a filled button whose fill contrasts with the page passes. Controls styled entirely by the browser are exempt, and so are disabled controls.

## How it fails in code

- A text input whose only visual boundary is a border below 3:1 against the page, with no other cue that it is a field. Definite when measured.
- A focus indicator below 3:1 against the adjacent colors, or an author style that removes the outline without replacing it. Definite. F78.
- A custom checkbox or radio whose checked state is shown by a color change below 3:1 from the unchecked state and no other cue. Definite when measured.
- An icon-only button whose icon is below 3:1 against its background. Definite when measured.
- Chart lines or pie segments that cannot be told apart from each other or the background at 3:1, with no labels or patterns. Likely; definite once measured and no other cue.
- A light gray placeholder-styled border on a field that also has a visible label and sits in a clear layout. Manual review; the question is whether the border is required to identify the component.

## How to meet it

- Technique G195, "Using an author-supplied, visible focus indicator", and Technique C40, "Creating a two-color focus indicator to ensure sufficient contrast with all components".
- Technique G207, "Ensuring that a contrast ratio of 3:1 is provided for icons".
- Technique G209, "Provide sufficient contrast at the boundaries between adjoining colors".
- Technique G174, "Providing a control with a sufficient contrast ratio that allows users to switch to a presentation that uses sufficient contrast".
- Leaving native controls unstyled passes by the exception.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.4.3 Contrast (Minimum) (entry in this package). Text, including text inside controls.
- SC 2.4.7 Focus Visible (`wcag/sc-2.4.7-focus-visible.md`) and 2.4.11 Focus Not Obscured (Minimum) (`wcag/sc-2.4.11-focus-not-obscured-minimum.md`). Whether focus is visible at all and whether it is covered; this criterion is how strongly it contrasts.
- SC 1.4.1 Use of Color (entry in this package). Whether color is the only cue for state.
- SC 1.1.1 Non-text Content (entry in this package). A graphic also needs a text alternative.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Its `color-contrast` rule covers text only. Control borders, focus rings, and graphics are measured by hand or with a color picker. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
