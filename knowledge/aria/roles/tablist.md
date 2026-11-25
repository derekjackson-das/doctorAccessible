# Role: tablist

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "tablist role", https://www.w3.org/TR/wai-aria-1.2/#tablist. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `ul`, `ol`, `menu`, `nav`, and `li`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): the ARIA Authoring Practices Guide "Tabs Pattern" is covered in `aria/patterns/tabs.md`.
- Reference (tier 3): MDN Web Docs, "ARIA: tablist role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tablist_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): awareness only. The draft turns the SHOULD on managing focus into a MUST.
- Related entries: `aria/patterns/tabs.md`, `patterns/tabs.md`, `aria/roles/tab.md`, `aria/roles/tabpanel.md`, `aria/roles/list.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: how to build tabs, the keys they promise, how they fail, and the manual tests are in `aria/patterns/tabs.md` and `patterns/tabs.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

The container for a set of tabs. WAI-ARIA 1.2: "A list of tab elements, which are references to tabpanel elements."

## The native element

None.

## What the spec asks of authors

- "To be keyboard accessible, authors SHOULD manage focus of descendants for all instances of this role".
- "For a single-selectable tablist, authors SHOULD hide other tabpanel elements from the user until the user selects the tab associated with that tabpanel."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `tab`.
- Required states and properties: none.
- Supported states and properties: `aria-multiselectable`, `aria-orientation` (default horizontal), and `aria-activedescendant`, inherited from `composite`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author. WAI-ARIA 1.2 has no "Accessible Name Required" row for this role; MDN and `aria/patterns/tabs.md` label it with `aria-labelledby` or `aria-label`.

**The whole component.** See `aria/patterns/tabs.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `ul`, `ol`, `menu`, `nav`, and the elements that allow any role, such as `div`.
- **Not allowed:** `section`, `article`, `fieldset`, `h1` to `h6`, `button`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- On a `ul`, `ol`, or `menu` the list role is replaced. Each `li` inside is then exposed as `generic` and may take a role such as `tab` (ARIA in HTML, row for `li`).
- On a `nav` the navigation landmark is replaced (`aria/roles/navigation.md`).

## Where the detail lives

- Build, states, keyboard, failures: `aria/patterns/tabs.md`. Whether to use tabs at all, and the manual tests: `patterns/tabs.md`.
- axe: `aria-required-children` came back as incomplete, needing review, on a `tablist` with no `tab` inside (mapped to 1.3.1; observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`). A lead, not a finding.
