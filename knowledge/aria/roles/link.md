# Role: link

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "link role", https://www.w3.org/TR/wai-aria-1.2/#link. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `a` with `href`, `area`, `button`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows for `a` with `href` (3.5.2) and `area` with `href` (3.5.6), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Link Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/link/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: link role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/link_role
- Related entries: `html/links.md`, `aria/roles/button.md`, `content/link-text.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.4-link-purpose-in-context.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="link"` on `a` with `href` is redundant, never a finding.

## What it is

A reference that takes the user somewhere: another page, a place in this page, a file. WAI-ARIA 1.2: "An interactive reference to an internal or external resource that, when activated, causes the user agent to navigate to that resource."

## The native element

`a` with `href`, and `area` with `href` (HTML-AAM). They bring focus, Enter, the browser's link context menu, open-in-new-tab, history, and visited state. A role brings none of these (APG; MDN).

## When writing the role is justified

Almost never. APG strongly encourages the native `a` with `href`; MDN lists the role as one to avoid, included for completeness.

## What the spec asks of authors

- WAI-ARIA 1.2 places no author requirement on this role beyond its characteristics, below.
- APG: applying the role does not give browser link behavior; the author must supply navigation and any context menu.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: `aria-disabled`, `aria-expanded`, `aria-haspopup`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `a` with `href`, `area` with `href` (redundant, "NOT RECOMMENDED").
- **Allowed:** `button`, `input type=button`, `submit`, `reset`, `image`, `img` with alt text, `area` without `href`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `a` without `href` is allowed (it takes any role), but give it an `href` instead; not allowed on `li`, headings, landmark elements, form fields other than those named.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Link Pattern: Enter follows the link and moves focus to its target. Shift+F10 may open a context menu (optional). Links do not answer Space; that is a button's key.

## What an explicit role takes away

- On a `button`, the button role goes; Enter still activates it, but Space now does too, which links do not do. Choose the element by what it does.
- On an `img`, the image role goes; the alt text becomes the link's name.

## How it fails in code

- The role on a `div` or `span` with no `tabindex`, so the control cannot be reached by keyboard: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F42). Report once, as that entry says, not again under 4.1.2.
- The role and `tabindex="0"` but no key handler, so the control can be focused but not operated: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F54).
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- A `span role="link"` with a click handler that navigates, instead of an `a` with `href`: open-in-new-tab, history, and the link context menu are lost. Advice unless a criterion breaks.
- A link that acts as a button (opens a dialog, toggles) or a button that navigates: manual review under `wcag/sc-4.1.2-name-role-value.md`; the role misstates what the control does.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

Search for `role="link"` and for `a` without `href` used as a control. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
