# Role: textbox

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "textbox role", https://www.w3.org/TR/wai-aria-1.2/#textbox. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for text `input` types, `textarea`, and form-associated custom elements, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows for `input type=text` (3.5.76) and `textarea` (3.5.132, with `aria-multiline` true), https://www.w3.org/TR/html-aam/
- Reference (tier 3): MDN Web Docs, "ARIA: textbox role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role
- Related entries: `aria/roles/searchbox.md`, `aria/roles/spinbutton.md`, `aria/patterns/autocomplete.md`, `html/forms.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-3.3.2-labels-or-instructions.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="textbox"` on a text `input` is redundant, never a finding.

## What it is

A field for free-form text. WAI-ARIA 1.2: "A type of input that allows free-form text as its value."

## The native element

`input type=text` (and email, tel, url with no `list`) for one line; `textarea` for several (HTML-AAM). They bring editing, selection, `required`, `readonly`, `placeholder`, and form submission.

## When writing the role is justified

For a `contenteditable` element that must be exposed as a field. MDN: use the native elements whenever possible; with the role, every state and the Enter behavior must be scripted.

## What the spec asks of authors

- WAI-ARIA 1.2 places no author requirement on this role beyond its characteristics, below.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: `aria-activedescendant`, `aria-autocomplete`, `aria-errormessage`, `aria-haspopup`, `aria-invalid`, `aria-multiline`, `aria-placeholder`, `aria-readonly`, `aria-required`.
- Prohibited states and properties: none.
- Naming: name from author; **required**.
- `aria-multiline="true"` when Enter adds a line; ARIA does not change what Enter does, script must (MDN).
- Prefer the native `required`, `readonly`, and `placeholder` attributes over `aria-required`, `aria-readonly`, and `aria-placeholder` (MDN).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `input type=text` and other text types with no `list`, `textarea` (redundant).
- **Allowed:** form-associated custom elements, and the elements that allow any role, such as `div`, `span`, `p`, and `table` (with `contenteditable`).
- **Not allowed:** `input type=search`, `number`, `range` and the other non-text types, `button`, `a`, `li`, headings, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

Text editing keys. Single line: Enter submits the form. Multi-line: Enter adds a line break (MDN). Script must not capture the editing keys.

## What an explicit role takes away

- On a `div` with `contenteditable`, nothing is lost; every field behavior must be scripted.

## How it fails in code

- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- A `contenteditable` field with no role: its value and editing are not exposed as a field. `wcag/sc-4.1.2-name-role-value.md`, likely.
- Required, invalid, or read-only state shown visually but not exposed: `wcag/sc-4.1.2-name-role-value.md`, per that entry.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

Each `role="textbox"` is focusable, editable, named, and exposes its states. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
