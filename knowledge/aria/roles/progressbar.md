# Role: progressbar

- Category: widget (range, read-only).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "progressbar role", https://www.w3.org/TR/wai-aria-1.2/#progressbar. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `progress`, `img`, and form-associated custom elements, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `progress` (3.5.105), which sets the value attributes from the element, https://www.w3.org/TR/html-aam/
- Reference (tier 3): MDN Web Docs, "ARIA: progressbar role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/progressbar_role
- Related entries: `aria/roles/meter.md`, `aria/live-regions.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-4.1.3-status-messages.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

Shows how far a long task has got. WAI-ARIA 1.2: "An element that displays the progress status for tasks that take a long time."

## The native element

`progress` (HTML-AAM), with a `label`.

## When writing the role is justified

When `progress` cannot be used or styled.

## What the spec asks of authors

- "Authors MAY set aria-valuemin and aria-valuemax to indicate the minimum and maximum progress indicator values."
- "The author SHOULD supply a value for aria-valuenow unless the value is indeterminate, in which case the author SHOULD omit the aria-valuenow attribute."
- "Authors SHOULD update this value when the visual progress indicator is updated."
- "If the progressbar is describing the loading progress of a particular region of a page, the author SHOULD use aria-describedby to point to the status, and set the aria-busy attribute to true on the region until it is finished loading."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-valuenow` while the progress is known; leave it off when it is indeterminate (WAI-ARIA 1.2, below).
- `aria-valuemin` defaults to 0 and `aria-valuemax` to 100 (MDN).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `progress` (no other role allowed on it).
- **Allowed:** `img` with alt text, form-associated custom elements, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `progress` (already one), `meter`, form fields, `button`, `li`, headings, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- Children are presentational: text inside it is read as plain text.

## How it fails in code

- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- `aria-valuenow` not updated as the visual bar moves: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- A loading region with no `aria-busy` and no `aria-describedby` pointing to the progress: breaks a WAI-ARIA SHOULD; advice.
- Progress that ends with no status message to say it is done: see `wcag/sc-4.1.3-status-messages.md` and `aria/live-regions.md`.
- Used for a measurement that is not progress: use `meter` (`aria/roles/meter.md`). Advice.

## How to check

Each `role="progressbar"` has a name and a current value that changes; completion is announced some other way. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
