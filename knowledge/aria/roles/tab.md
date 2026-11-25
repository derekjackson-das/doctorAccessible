# Role: tab

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "tab role", https://www.w3.org/TR/wai-aria-1.2/#tab. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `button`, `a`, `h1` to `h6`, and `li`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): the ARIA Authoring Practices Guide "Tabs Pattern" is covered in `aria/patterns/tabs.md`.
- Reference (tier 3): MDN Web Docs, "ARIA: tab role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): awareness only. The draft makes a name required for `tab` and adds a MUST that the panel for an active tab is rendered.
- Related entries: `aria/patterns/tabs.md`, `patterns/tabs.md`, `aria/roles/tablist.md`, `aria/roles/tabpanel.md`, `aria/roles/button.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: how to build tabs, the keys they promise, how they fail, and the manual tests are in `aria/patterns/tabs.md` and `patterns/tabs.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

One tab in a set: the control that shows its panel. WAI-ARIA 1.2: "A grouping label providing a mechanism for selecting the tab content that is to be rendered to the user."

## The native element

None. HTML has no tab element. The plainer alternatives are in `patterns/tabs.md`.

## What the spec asks of authors

- "Authors MUST ensure elements with role tab are contained in, or owned by, an element with the role tablist."
- "Authors SHOULD ensure the tabpanel associated with the currently active tab is perceivable to the user."
- Authors SHOULD set `aria-selected` to true on the selected tab and false on the others, and show the selected tab visually.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `tablist`.
- Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-selected` (default false), `aria-disabled`, `aria-expanded`, `aria-haspopup`, `aria-posinset`, `aria-setsize`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage` and `aria-invalid` as deprecated on this role.
- Naming: name from contents or author. WAI-ARIA 1.2 has no "Accessible Name Required" row for this role.
- Children are presentational: anything inside a tab is exposed as plain text.

**The whole component.** A `tablist` holding the `tab` elements, and a `tabpanel` for each: `aria/patterns/tabs.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `button`, `a` with `href`, `h1` to `h6`, `img` with alt text, `input` of type `button`, `image`, `reset`, or `submit`, and the elements that allow any role, such as `div` and `span`. An `li` only when its parent no longer exposes a list role, as in `ul role="tablist"`.
- **Not allowed:** an `li` in a list that is still a list; `input type="radio"`; `section`, `nav`, `ul`, `ol`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- On a `button` the button role is replaced by `tab`, which is the intended use (`aria/patterns/tabs.md`).
- On an `a` with `href` the link role is replaced; MDN advises preventing the link's default behavior, ideally by removing or changing the `href`.
- On `h1` to `h6` the heading is replaced, and the text is no longer a heading.
- A heading or other element inside a tab loses its role, because the role's children are presentational (WAI-ARIA 1.2, "Children Presentational: True"; MDN).

## Where the detail lives

- Build, states, keyboard, failures: `aria/patterns/tabs.md`. Whether to use tabs at all, and the manual tests: `patterns/tabs.md`.
- axe: `aria-required-parent` fires on a `tab` outside a `tablist` (mapped to 1.3.1; observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`). It cannot tell whether the arrow keys work.
