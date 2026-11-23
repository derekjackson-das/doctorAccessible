# Role: name

Saved as `aria/roles/<role>.md`, one per WAI-ARIA 1.2 role an author might write. Abstract roles get no entry; authors must not use them. A role whose widget has an `aria/patterns/` entry gets a short entry that points there. Roles that only mirror an HTML element (`paragraph`, `strong`, `code`, and the like) share `aria/roles/structural.md`.

What the role is, which native element already provides it, when writing the role is justified, what the spec asks of authors, and what an explicit role takes away from the element it sits on. How to build the thing the role describes lives in `html/` or `aria/patterns/`; this entry links there and does not repeat it.

- Category: landmark, document structure, widget, live region, or window, from the role's superclass in WAI-ARIA 1.2.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "<role> role", https://www.w3.org/TR/wai-aria-1.2/#<role>. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for the native element and for any element the role is often put on, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft (date), the row for each native element, https://www.w3.org/TR/html-aam/#el-<element>
- Practice (tier 2): ARIA Authoring Practices Guide, the page that covers the role (for example "Landmark Regions" or "Structural Roles"), URL. Patterns, not requirements.
- Reference (tier 3): MDN Web Docs, "ARIA: <role> role", last modified (date), URL. Never the sole source for what is required.
- WAI-ARIA 1.3 (Working Draft): awareness only. Note a change only if the draft changes this role.
- Related entries: `html/...`, `aria/aria-in-html.md`, `aria/using-aria.md`, `aria/patterns/...`
- WCAG: the criteria a misuse of this role can break, each with its entry.
- Verified against the live sources: YYYY-MM-DD by <name>

## Status and reporting

A role is not a criterion. Misuse is reported once, under the WCAG criterion it breaks, at the confidence that criterion's entry gives. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is a conformance error against that specification: advice, not a WCAG finding (`aria/aria-in-html.md`). A redundant role, such as this role on its own native element, is never a finding.

## What it is

The role's definition in our words, then the defining sentence quoted from WAI-ARIA 1.2.

## The native element

Which HTML element maps to this role (HTML-AAM), and any condition: scope, an accessible name, an ancestor. What ARIA in HTML says about writing the role on that element (usually "NOT RECOMMENDED"). "None" when no element maps to it.

## When writing the role is justified

Usually only when the element cannot be used: a legacy page being retrofitted, a design constraint, better tested support (APG, "Structural Roles"; `aria/using-aria.md`, rule 1). Say if the role is for browsers only.

## What the spec asks of authors

Each SHOULD, MUST, or MAY that WAI-ARIA 1.2 places on authors for this role, quoted, with the section. Then naming: whether a name is required, allowed, or prohibited ("Name From" and "Accessible Name Required" in the role's characteristics).

## Attributes and context it needs

From the "Characteristics" table under the role in WAI-ARIA 1.2. Say "none" where a row is absent; do not leave a row out.

- **Required context role:** the role its parent must have. A role with one is not valid on its own: `tab` must sit in a `tablist`, `option` in a `listbox`, `listitem` in a `list`.
- **Required owned elements:** the roles it must contain: a `tablist` must own `tab` elements, a `list` must own `listitem` elements.
- **Required states and properties:** attributes that must be set, such as `aria-checked` on `checkbox`, or `aria-level` on `heading` where the host gives none.
- **Supported states and properties:** the role-specific attributes that may be used, beyond the global ones.
- **Prohibited states and properties,** and the global attributes WAI-ARIA 1.2 marks as deprecated on this role.
- **Naming:** name from author, contents, or prohibited; whether a name is required.

When the role is one part of a component, list the other parts and point to the `aria/patterns/` entry that puts them together. A `role="tab"` with no `tablist` around it, no `tabpanel`, and no `aria-selected` is not a tab; it is a broken one. A role missing its required context, owned elements, or states misreports the control: 4.1.2 or 1.3.1, at that entry's confidence.

## Where it can and cannot be used

From ARIA in HTML, section 4. Three lists, plus any rule from WAI-ARIA 1.2 that makes browsers ignore the role:

- **Its native element,** where writing the role is redundant ("NOT RECOMMENDED").
- **Allowed:** the elements whose row names this role, and the elements that allow any role (`div`, `span`, `p`, `table`, `a` without `href`, and others). `div`, `span`, and `p` are "Naming Prohibited" unless the role itself allows a name.
- **Not allowed:** every other element. Name the ones authors are most likely to try, such as `ul`, `li`, `h1` to `h6`, `a` with `href`, `button`, `main`, form fields.

Using a role where ARIA in HTML does not allow it is a conformance error against that specification: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

For widget roles only; leave the section out for landmark and structure roles. A widget role tells assistive technology the element behaves like that control, so the keys that control is expected to answer must work. List them from the APG pattern, in our words, marked as a pattern, not a requirement, and say where focus goes (one tab stop, roving `tabindex`, or `aria-activedescendant`). The native element provides these keys itself; an ARIA build has to script every one. A role whose keys do not work misreports the control (`wcag/sc-4.1.2-name-role-value.md`) and may fail `wcag/sc-2.1.1-keyboard.md`.

## What an explicit role takes away

What happens when this role is put on an element that already has a role: the native role is replaced, and with it its children's roles where they depend on it (a list's items, a table's rows and cells). And what happens when another role is put on this role's native element. Name the role lost. This is the check the verifier makes under #97.

## How it fails in code

The mistakes seen most often, each tied to the criterion it breaks and that entry's confidence, or marked advice.

## How to check

What to look for in code, and what the accessibility tree in the browser's developer tools shows. Name the axe rules that cover the role, from `knowledge/axe-rules.md`.
