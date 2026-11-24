# Role: tooltip

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "tooltip role", https://www.w3.org/TR/wai-aria-1.2/#tooltip. ARIA in HTML, W3C Recommendation 11 August 2026, section 4 (no row names this role), https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): the ARIA Authoring Practices Guide "Tooltip Pattern" is covered in `aria/patterns/tooltip.md`.
- Reference (tier 3): MDN Web Docs, "ARIA: tooltip role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tooltip_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): awareness only. The draft prohibits naming a tooltip with `aria-label` or `aria-labelledby`.
- Related entries: `aria/patterns/tooltip.md`, `patterns/tooltip.md`, `aria/accessible-name.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.4.13-content-on-hover-or-focus.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: how to build a tooltip, how it fails, and the manual tests are in `aria/patterns/tooltip.md` and `patterns/tooltip.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Whether `role="tooltip"` is present is advice; what matters is that the control has a name and the tip is connected to it (`aria/patterns/tooltip.md`).

## What it is

A popup that describes the element it belongs to. WAI-ARIA 1.2: "A contextual popup that displays a description for an element." It is a description, not a name, and not a container for controls.

## The native element

None. The `title` attribute is not a substitute (`patterns/tooltip.md`).

## What the spec asks of authors

- "Authors SHOULD ensure that elements with the role tooltip are referenced through the use of aria-describedby before or at the time the tooltip is displayed."

The role goes on the tip. `aria-describedby` goes on the element the tip describes.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**. The tip's text is its name, so an empty tip has none.
- MDN advises against `aria-label` or `aria-labelledby` on the tip: the label, not the tip's text, then becomes the description of the element it is tied to.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** only the elements that allow any role, such as `div`, `span`, and `p`. No row names `tooltip`.
- **Not allowed:** `button`, `a` with `href`, `section`, `aside`, `dialog`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

Nothing native on a `div` or `span`. The role does not show, hide, or position anything, and does not connect the tip to its trigger; `aria-describedby` and script do that.

## Where the detail lives

- Build, naming, keyboard, failures: `aria/patterns/tooltip.md`. Whether to use one, toggletips, and the manual tests: `patterns/tooltip.md`. What is required of content shown on hover or focus: `wcag/sc-1.4.13-content-on-hover-or-focus.md`.
- axe: `aria-tooltip-name` fires on a `tooltip` with no text (mapped to 4.1.2; observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`).
