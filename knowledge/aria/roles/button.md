# Role: button

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "button role", https://www.w3.org/TR/wai-aria-1.2/#button. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `button`, `a` with `href`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows for `button` (3.5.20) and `input` type `button`, `submit`, `reset`, and `image`, https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Button Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/button/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: button role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role
- Related entries: `html/buttons.md`, `html/custom-controls.md`, `aria/roles/link.md`, `aria/patterns/modal-dialog.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.5.3-label-in-name.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="button"` on a `button` is redundant, never a finding.

## What it is

A control that does something on this page when activated: submits, opens, toggles, deletes. A link goes somewhere; a button acts. WAI-ARIA 1.2: "An input that allows for user-triggered actions when clicked or pressed."

## The native element

`button`, and `input` of type `button`, `submit`, `reset`, or `image` (HTML-AAM). They bring focus, Enter and Space, the disabled state, and form submission without script.

## When writing the role is justified

Rarely. When markup cannot be changed and a `div` or `span` must act as a button, or when a link is styled and behaves as a button and the visual cannot be changed; APG prefers changing the visuals to keep a link a link. MDN: the role adds no behavior, only semantics.

## What the spec asks of authors

- WAI-ARIA 1.2 places no author requirement on this role beyond its characteristics, below.
- Toggle buttons: `aria-pressed` makes a toggle; APG calls it critical that the label does not change when the state changes ("Mute" stays "Mute"). If the label changes instead, leave `aria-pressed` off.
- Menu buttons: `aria-haspopup` set to `menu` or `true`, with `aria-expanded` (APG, Menu Button Pattern).

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: `aria-disabled`, `aria-haspopup`, `aria-expanded`, `aria-pressed`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-pressed` turns it into a toggle button; `aria-expanded` when it shows and hides something; `aria-haspopup` when it opens a menu or another popup.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `button`, `input type=button`, `submit`, `reset`, `image` (redundant, "NOT RECOMMENDED").
- **Allowed:** `a` with `href`, `img` with alt text, `input type=checkbox` used with `aria-pressed`, `area` without `href`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li`, `h1` to `h6`, `label`, `main`, `nav` and the other landmark elements, form fields other than those named, `summary`, `option`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Button Pattern: Enter and Space activate it. Afterwards focus follows the action: into a dialog it opens, back to the button when that dialog closes, and staying on the button when the action happens in place. A native `button` gives Enter and Space for free; a `div role="button"` needs `tabindex="0"` and a key handler for both. A link given `role="button"` still answers only Enter unless Space is scripted (MDN).

## What an explicit role takes away

- On an `a` with `href`, the link role goes; the element is no longer listed as a link, and Space must be scripted.
- On an `img`, the image role goes; the alt text becomes the button's name.
- Children are presentational: a heading inside a button is no longer a heading.

## How it fails in code

- The role on a `div` or `span` with no `tabindex`, so the control cannot be reached by keyboard: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F42). Report once, as that entry says, not again under 4.1.2.
- The role and `tabindex="0"` but no key handler, so the control can be focused but not operated: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F54).
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- A toggle that changes visually with no `aria-pressed`: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- A toggle whose label changes with its state and also has `aria-pressed`, so the state is announced twice and contradicts itself: manual review under `wcag/sc-4.1.2-name-role-value.md`.
- A visible label that is not part of the accessible name (for example an `aria-label` that replaces the text): `wcag/sc-2.5.3-label-in-name.md`, per that entry.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

Search for `role="button"`. For each: is it focusable, does it answer Enter and Space, does it have a name, and would a `button` element do the job? In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
