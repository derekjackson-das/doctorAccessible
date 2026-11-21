# Role: form

- Category: landmark.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "form role", https://www.w3.org/TR/wai-aria-1.2/#form. ARIA in HTML, W3C Recommendation 11 August 2026, row for `form`, https://www.w3.org/TR/html-aria/#el-form
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.45, https://www.w3.org/TR/html-aam/#el-form
- Practice (tier 2): ARIA Authoring Practices Guide, "Landmark Regions", form section (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- Reference (tier 3): MDN Web Docs, "ARIA: form role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/form_role
- Related entries: `html/forms.md`, `aria/roles/search.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-3.2.2-on-input.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). An unnamed `form` that is not a landmark is not a finding: most forms do not need to be landmarks.

## What it is

A landmark around a form, so a screen reader user can jump to it. WAI-ARIA 1.2: "A landmark region that contains a collection of items and objects that, as a whole, combine to create a form."

## The native element

`form`, but it is exposed as a landmark only once it has an accessible name (HTML-AAM 3.5.45: "If a form has no accessible name, do not expose the element as a landmark"; ARIA in HTML note). ARIA in HTML allows `role="form"` on `form` but marks it "NOT RECOMMENDED".

## When writing the role is justified

Rarely. MDN warns against `role="form"` in place of the `form` element without a very good reason: the element brings native submission, which the role does not, and MDN notes a `role="form"` needs script to handle submitting.

## What the spec asks of authors

- "Authors MUST give each element with role form a brief label that describes the purpose of the form." "Authors SHOULD reference a visible label with aria-labelledby if a visible label is present." "Authors SHOULD include the label inside of a heading whenever possible."
- "If the purpose of a form is to submit search criteria, authors SHOULD use the search role instead of the generic form role." See `aria/roles/search.md`.
- "Authors are reminded to use native host language semantics to create form controls whenever possible."
- If script submits the form on an action that would not normally submit it (such as changing a control's value), the author "SHOULD provide the user with advance notification of the behavior." That is also the ground of `wcag/sc-3.2.2-on-input.md`.
- Naming: required ("Accessible Name Required: true").

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; **required** ("Accessible Name Required: true").
- It stands alone: it is not one part of a larger component, so it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `form` (redundant, "NOT RECOMMENDED").
- **Allowed:** the `search` element, and the elements that allow any role, such as `div`, `span`, `p`, and `table`. A `div` given `role="form"` may then be named, because the role allows a name.
- **Not allowed:** `section`, `aside`, `article`, `nav`, `header`, `footer`, `main`; `ul`, `ol`, `li`; `h1` to `h6`; `a` with `href`; `button`; `fieldset` (use `group` or `radiogroup` there); form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- ARIA in HTML allows `none`, `presentation`, or `search` on a `form`. `search` makes it a search landmark instead; `none` or `presentation` remove the form role.
- APG: do not put `role="form"` on individual fields.

## How it fails in code

- `role="form"` with no name: breaks the WAI-ARIA MUST, and the browser may not expose a landmark. Advice; not a WCAG failure by itself.
- A form that submits when a select changes, with no warning: `wcag/sc-3.2.2-on-input.md`, at that entry's confidence. Report it there, not here.
- `role="form"` on a `div` of scripted controls in place of a `form` element: advice; check that the controls themselves are real controls (`html/forms.md`).

## How to check

Does any form need to be a landmark (a page with several forms a user moves between)? If so, it has a name from a visible heading. Is any search form marked as `search` instead? Is `role="form"` used anywhere a `form` element would do?
