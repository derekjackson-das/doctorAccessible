# Role: document

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "document role", https://www.w3.org/TR/wai-aria-1.2/#document. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for the elements that allow the role, and the rows for `html` and `body`, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page; lists no HTML equivalent), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: document role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/document_role
- Related entries: `aria/roles/application.md`, `aria/roles/article.md`, `aria/patterns/modal-dialog.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2 and ARIA in HTML text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). Outside a widget or an `application` the role does nothing, so there it is advice at most.

## What it is

The counterpart of `application`: content inside a widget or application that should be read as ordinary content. WAI-ARIA 1.2: "An element containing content that assistive technology users may want to browse in a reading mode."

## The native element

None. APG lists no HTML equivalent. A web page is already treated as a document; ARIA in HTML allows `role="document"` on `html` but marks it "NOT RECOMMENDED".

## When writing the role is justified

In one situation. WAI-ARIA 1.2: "the only circumstance where the document role is useful for changing assistive technology behavior is when the element with role document is a focusable child element of a widget or application." The spec's example is static rich text inside an `application`, given `role="document"` and `tabindex="0"`.

MDN adds that it is not needed inside a dialog: a dialog is a window, not a widget, and its content is read in reading mode already (`aria/patterns/modal-dialog.md`).

## What the spec asks of authors

WAI-ARIA 1.2 places no SHOULD or MUST on authors in this role's text. The duty comes from `application`: static content inside one must be made available, and a focusable `document` is one of the three ways (`aria/roles/application.md`).

- The element has to be focusable for the role to have any effect. The spec's statement is for assistive technology: when focus moves to the element, tools with a reading mode "MAY switch to that reading mode".
- Naming: allowed, from the author; not required ("Accessible Name Required: False").
- MDN: `tabindex="0"` puts the element in the tab order; in a widget that moves focus with arrow keys, make sure there is a way to reach the document and a way back.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- `article` is its subclass, and does the same job for a self-contained piece of content (`aria/roles/article.md`).

**The whole component.** A widget or `application`, and inside it a focusable element with this role holding the content to be read.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `article`, `embed`, `iframe`, `object`, `section`, and the elements that allow any role, such as `div`, `span`, and `p`. On `html` it is allowed but "NOT RECOMMENDED".
- **Not allowed:** `body` (it allows no role but `generic`); `main`, `nav`, `aside`, `header`, `footer`, `form`; `button`; `a` with `href`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On a `section` or `article`, the `region` or `article` role goes. On a `div`, nothing.

## How it fails in code

- `role="document"` on `body` or a page wrapper: not allowed on `body`, and without effect elsewhere. Advice: remove it.
- Inside an `application`, a `role="document"` with no `tabindex`: focus cannot reach it, so the role cannot take effect and the content falls under the `application` MUST. `wcag/sc-4.1.2-name-role-value.md`, likely, per `aria/roles/application.md`.
- `role="document"` inside a `dialog`: advice; it is not needed.

## How to check

Search for `role="document"`. Is it inside a widget or an `application`? Is it focusable? Can focus reach it and leave it by keyboard? Then it goes on the manual test list with the `application` it sits in (`at-test-protocol`). Observed with axe-core 4.14.0 on 2026-11-23: no rule fired on a `role="document"` on a `div`.
