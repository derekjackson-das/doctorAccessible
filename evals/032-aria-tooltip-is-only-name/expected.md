# Eval 032: icon button whose only text is its tooltip

Input: `input.html`. A reading list with one entry and an icon-only download button.

Intended defect: the button contains only an SVG icon, hidden with `aria-hidden="true"`. Its only text, "Download citation (RIS file)", is in a `role="tooltip"` element connected by `aria-describedby`. A description is not a name (`knowledge/aria/accessible-name.md`), so the button has no accessible name. A screen reader announces a button with no name, perhaps followed by the description.

Everything else is clean:
- The tooltip shows on hover and on focus. It touches the button with no gap (the space above it is a transparent border inside the tip), so the pointer can move onto it; it stays while the pointer is over the button or the tip, or while the button has focus; Escape dismisses it. That meets 1.4.13.
- Activating the button navigates to the file, so focus is not lost.
- The button is 2.75rem square, focus is visible, and the icon and border are #005a9c on white (about 7.1:1).
- Tooltip text is white on #1a1a1a.
- Language, title, one `h1`, `main`.

## Expected findings

1. **[Definite]** The download button has no accessible name.
   - Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1, from `knowledge/wcag/sc-4.1.2-name-role-value.md` ("A button whose only content is an icon, image, or SVG with no accessible name. Definite").
   - ARIA entry: `knowledge/aria/patterns/tooltip.md`, which lists this case: `aria-describedby` gives a description, not a name.
   - Where: `button.icon-btn`.
   - Acceptable fix directions: name the button with `aria-labelledby="tip-download"` instead of `aria-describedby`; or add `aria-label="Download citation"`; or add visible or visually hidden text. As a direction, not a patch.

## Also acceptable

- A note, marked advice, that visible text would serve everyone better than a tooltip (`patterns/tooltip.md`).
- A manual-review note that touch users cannot get the tooltip, so the name must not rely on it.
- A note that axe is expected to flag the button, if it was run.

## Must not

- Report the tooltip's behavior under 1.4.13; it is hoverable, persistent, and dismissible.
- Report `role="tooltip"` or `aria-describedby` as invalid ARIA; both are allowed.
- Report the target size, contrast, focus style, heading, landmarks, or language.
- Report the defect twice, under 4.1.2 and again under 1.1.1, 2.4.6, or 2.5.3.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

The 4.1.2 entry says axe has rules for button names and finds a missing name reliably, so axe is expected to flag this button if it is run (confirm the rule ID against the Deque rule descriptions, as the entry says). Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 4.1.2 (Level A), tier 1, and nothing from the Must not list appears.
