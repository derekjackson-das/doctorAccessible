# Role: generic

- Category: document structure (superclass `structure`).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "generic role", https://www.w3.org/TR/wai-aria-1.2/#generic. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `div` and `span`, https://www.w3.org/TR/html-aria/#el-div
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.35 (`div`) and 3.5.120 (`span`), https://www.w3.org/TR/html-aam/#el-div
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles", which lists `div` and `span` as its HTML equivalents (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: generic role", last modified 12 May 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role
- Related entries: `aria/roles/presentation.md`, `aria/accessible-name.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. `role="generic"` written by an author breaks a WAI-ARIA SHOULD NOT; that is advice unless it removes a role the page relies on, which is then reported under the criterion it breaks.

## What it is

The role of a container with no meaning: what a `div` or `span` already is. WAI-ARIA 1.2: "A nameless container element that has no semantic meaning on its own." The spec says it is "primarily for implementors of user agents", meaning browsers, not authors.

Unlike `presentation`, a `generic` element stays in the accessibility tree, so assistive technology can still read its position and size, and it can carry a few attributes for its contents, such as `aria-live` (WAI-ARIA 1.2; MDN).

## The native element

`div` and `span` (HTML-AAM). Also a `section` with no accessible name, and a `header` or `footer` inside sectioning content, per ARIA in HTML.

## When writing the role is justified

Never. "Authors SHOULD NOT use this role in content." ARIA in HTML says `generic` should not be used on `div`, `span`, or `section`. To remove an element's role, use `presentation` or `none`; to group and name a set of elements, use `group` (WAI-ARIA 1.2; MDN).

## What the spec asks of authors

- "Authors SHOULD NOT use this role in content."
- Naming: prohibited. `aria-label`, `aria-labelledby`, and `aria-roledescription` are prohibited on `generic` ("Name From: prohibited"). That is why ARIA in HTML marks `div` and `span` "Naming Prohibited": an `aria-label` on a plain `div` is not reliably announced (`aria/accessible-name.md`).

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: `aria-label`, `aria-labelledby`, `aria-roledescription`. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: prohibited ("Name From: prohibited").

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `div` and `span`; also an unnamed `section`, and a `header` or `footer` inside sectioning content.
- **Allowed:** nowhere, in practice. Every row that mentions it (`div`, `span`, `section`, `label`, `header`, `footer`, `a` without `href`, `p` and the other any-role elements) says `generic` "SHOULD NOT be used".
- **Not allowed:** everything else.

## What an explicit role takes away

`role="generic"` on any element with a role removes it, as `presentation` would, but leaves the element in the tree. On a heading, list, or table, the meaning is gone.

## How it fails in code

- `role="generic"` on an element whose meaning the page relies on: `wcag/sc-1.3.1-info-and-relationships.md`, at that entry's confidence for removed structure.
- `aria-label` on a plain `div` or `span` with no role, used as the only name for something: the name is prohibited, and browsers and screen readers vary in whether they expose it. Manual review under 4.1.2 or 1.1.1, depending on what it was naming (`aria/accessible-name.md`, "Prohibited does not mean ignored"). Check the accessibility tree.
- `role="generic"` on a `div` or `span`: redundant, advice.

## How to check

Search for `role="generic"` (it should never appear). Search for `aria-label` or `aria-labelledby` on `div`, `span`, or `p` with no role. axe: `aria-prohibited-attr` maps the second case to 4.1.2 (`knowledge/axe-rules.md`).
