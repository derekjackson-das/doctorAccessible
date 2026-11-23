# Role: group

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "group role", https://www.w3.org/TR/wai-aria-1.2/#group. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `fieldset`, `details`, `optgroup`, `address`, `hgroup`, and the elements that allow the role, https://www.w3.org/TR/html-aria/#el-fieldset
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.40 (`fieldset`), 3.5.31 (`details`), 3.5.98 (`optgroup`), 3.5.5 (`address`), 3.5.51 (`hgroup`), https://www.w3.org/TR/html-aam/#el-fieldset
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: group role", last modified 20 October 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role
- Related entries: `html/forms.md`, `aria/roles/region.md`, `aria/roles/radiogroup.md`, `aria/roles/toolbar.md`, `aria/roles/tree.md`, `aria/roles/listbox.md`, `aria/roles/menu.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="group"` on a `fieldset` is redundant and never a finding.

## What it is

A set of related things that belong together but are not a landmark. WAI-ARIA 1.2: "A set of user interface objects that is not intended to be included in a page summary or table of contents by assistive technologies." The spec contrasts it with `region`, which is listed in a page summary (`aria/roles/region.md`).

## The native element

`fieldset` is the one the spec names as the related concept, and the one to use for form controls: with a `legend` it is a named group (`html/forms.md`). HTML-AAM also maps `details`, `optgroup`, `address`, and `hgroup` to `group`.

The sources disagree here. APG's "Structural Roles" table lists `group` with no HTML equivalent. ARIA in HTML (tier 1) gives five elements the role implicitly. Take ARIA in HTML.

## When writing the role is justified

- Related controls that cannot be wrapped in a `fieldset`, named with `aria-labelledby` or `aria-label`.
- Inside a composite widget, to collect siblings: the children of a tree node, a set of options in a listbox, a set of items in a menu (`aria/roles/tree.md`, `aria/roles/listbox.md`, `aria/roles/menu.md`).
- A scrolling container made focusable with `tabindex="0"` needs a role and a name. MDN: use `group` when no native role fits and the content does not merit a landmark (`aria/roles/region.md` says the same from the other side).

## What the spec asks of authors

- "Authors SHOULD use a group to form a logical collection of items in a widget, such as children in a tree widget forming a collection of siblings in a hierarchy."
- "when a group is used in the context of a listbox, authors MUST limit its children to option elements."
- "Authors MAY nest group elements. If a section is significant enough to warrant inclusion in the web page's table of contents, the author SHOULD assign it a role of region or a standard landmark role."
- Naming: allowed, from the author; not required by the spec.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-activedescendant`, `aria-disabled`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- Its subclass roles are `row`, `select` (abstract), and `toolbar`. `radiogroup` is the role for a set of radio buttons (`aria/roles/radiogroup.md`).

It can stand alone. Inside a widget, what it may contain depends on the widget: only `option` elements in a `listbox`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native elements:** `fieldset`, `details`, `optgroup`, `address`, `hgroup` (redundant, "NOT RECOMMENDED"). `details` and `optgroup` allow no other role.
- **Allowed:** `dl`, `figcaption`, `footer`, `header`, `menu`, `ol`, `ul`, `search`, `section`, a form-associated custom element, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `nav`, `main`, `aside`, `article`, `form`; an `li` inside a list; `button`; `a` with `href`; `h1` to `h6`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- On a `ul` or `ol`, the list goes, and its `li` children stop being list items (`aria/roles/list.md`).
- On a `section` with a name, the `region` landmark goes. That is the intended use when the section should not be a landmark.
- On a `header` or `footer` at the top level of the page, the `banner` or `contentinfo` landmark goes (`aria/roles/banner.md`, `aria/roles/contentinfo.md`).
- On a `fieldset`, ARIA in HTML allows only `none`, `presentation`, and `radiogroup`; each replaces the group.

## How it fails in code

- Related controls under one question with no `fieldset` and `legend` and no named group: `wcag/sc-1.3.1-info-and-relationships.md`, likely per that entry; definite when the question is not otherwise associated. A `role="group"` with a name is the equivalent grouping that entry asks for.
- `role="group"` around such controls with no name: the grouping is exposed but the question is not. `wcag/sc-1.3.1-info-and-relationships.md`, at the same confidence as the line above.
- A `group` inside a `listbox` holding anything but options: breaks the WAI-ARIA MUST. `wcag/sc-4.1.2-name-role-value.md`, likely (`aria/roles/listbox.md`).
- `role="group"` used where a landmark was meant, or the reverse: advice.

## How to check

For each `role="group"`: what does it group, does it have a name where a name is the only thing that says what the group is, and is it sitting on a list or landmark element it has just replaced? In the browser's accessibility tree, confirm the group and its name. Observed with axe-core 4.14.0 on 2026-11-23: no rule fired on a `role="group"` with no name. `aria-allowed-role` (best practice) covers the role on an element that does not allow it (`knowledge/axe-rules.md`).
