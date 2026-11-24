# Role: tabpanel

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "tabpanel role", https://www.w3.org/TR/wai-aria-1.2/#tabpanel. ARIA in HTML, W3C Recommendation 11 August 2026, row for `section`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): the ARIA Authoring Practices Guide "Tabs Pattern" is covered in `aria/patterns/tabs.md`.
- Reference (tier 3): MDN Web Docs, "ARIA: tabpanel role", last modified 12 September 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tabpanel_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): awareness only. The draft adds a MUST that the panel for an active tab is rendered.
- Related entries: `aria/patterns/tabs.md`, `patterns/tabs.md`, `aria/roles/tab.md`, `aria/roles/tablist.md`, `aria/roles/region.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: how to build tabs, the keys they promise, how they fail, and the manual tests are in `aria/patterns/tabs.md` and `patterns/tabs.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

The content a tab shows. WAI-ARIA 1.2: "A container for the resources associated with a tab, where each tab is contained in a tablist."

## The native element

None.

## What the spec asks of authors

- "Authors SHOULD associate a tabpanel element with its tab, either by using the aria-controls attribute on the tab to reference the tab panel, or by using the aria-labelledby attribute on the tab panel to reference the tab."
- Naming: required ("Accessible Name Required: True"), from the author. `aria-labelledby` pointing at the tab gives the name and the association in one attribute.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; **required**.

**The whole component.** See `aria/patterns/tabs.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `section`, and the elements that allow any role, such as `div`.
- **Not allowed:** `article`, `aside`, `main`, `fieldset`, `ul`, `ol`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On a `section` with an accessible name, the `region` landmark is replaced by `tabpanel` (`aria/roles/region.md`).

## Where the detail lives

- Build, states, keyboard, failures: `aria/patterns/tabs.md`. Whether to use tabs at all, and the manual tests: `patterns/tabs.md`.
- axe: no rule fired on a `tabpanel` with no name (axe-core 4.14.0, WCAG tags, 2026-11-23). Check the name by reading the code or the browser's accessibility tree.
