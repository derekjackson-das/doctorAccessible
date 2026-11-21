# Role: meter

- Category: structure (range, read-only).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "meter role", https://www.w3.org/TR/wai-aria-1.2/#meter. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `meter` and `img`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `meter` (3.5.93), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Meter Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/meter/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: meter role", last modified 21 August 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/meter_role
- Related entries: `aria/roles/progressbar.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A measurement within a known range, such as battery level or disk use. WAI-ARIA 1.2: "An element that represents a scalar measurement within a known range, or a fractional value."

## The native element

`meter` (HTML-AAM). MDN: native elements are better supported.

## When writing the role is justified

When `meter` cannot be used or styled. Not for progress (use `progressbar`), and not for a value with no meaningful maximum (APG).

## What the spec asks of authors

- "Authors MAY set aria-valuemin and aria-valuemax to indicate the minimum and maximum values for the meter."
- "Authors SHOULD NOT use the meter role to indicate progress; the progressbar role exists to address that need."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: `aria-valuenow`.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-valuetext` when a percentage alone is not useful, such as "50% (6 hours) remaining" (APG).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `meter` (no other role allowed on it).
- **Allowed:** `img` with alt text, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `meter` (already one), `progress`, form fields, `button`, `li`, headings, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- Children are presentational.

## How it fails in code

- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- No `aria-valuenow`, or a value that does not match what is shown: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a missing value.
- Used to show progress: breaks a WAI-ARIA SHOULD NOT; advice.

## How to check

Each `role="meter"` has a name and a value in range. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
