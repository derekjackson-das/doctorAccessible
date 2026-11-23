# Role: searchbox

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "searchbox role", https://www.w3.org/TR/wai-aria-1.2/#searchbox. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `input type=search`, text `input` with no `list`, and form-associated custom elements, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `input type=search` (3.5.73), https://www.w3.org/TR/html-aam/
- Reference (tier 3): MDN Web Docs, "ARIA: searchbox role", last modified 12 May 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/searchbox_role
- Related entries: `aria/roles/search.md`, `aria/roles/textbox.md`, `aria/patterns/autocomplete.md`, `html/forms.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-3.3.2-labels-or-instructions.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="searchbox"` on `input type=search` is redundant, never a finding.

## What it is

A text field for search terms. WAI-ARIA 1.2: "A type of textbox intended for specifying search criteria."

## The native element

`input type=search` (HTML-AAM).

## When writing the role is justified

When `input type=search` cannot be used. Do not add it to `input type=search`: MDN notes the redundant announcements it can cause ("search search this site search box").

## What the spec asks of authors

- WAI-ARIA 1.2 places no author requirement on this role beyond its characteristics, below.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none.
- Naming: name from author; **required**.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `input type=search` with no `list` (no other role allowed on it).
- **Allowed:** a text `input` with no `list` attribute, form-associated custom elements, and the elements that allow any role, such as `div`, `span`, `p`, and `table` (with `contenteditable`).
- **Not allowed:** `input type=search` with any other role, `button`, `a`, `li`, headings, landmark elements; with a `list` attribute the field is a `combobox`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

Text editing keys. Nothing beyond a text field.

## What an explicit role takes away

- On a text `input`, textbox becomes searchbox; nothing is lost.

## How it fails in code

- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- `role="search"` put on the field instead of its container: see `aria/roles/search.md`.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

Each search field has a name (a visible label is best) and is inside the search landmark. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
