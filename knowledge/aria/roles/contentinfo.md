# Role: contentinfo

- Category: landmark.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "contentinfo role", https://www.w3.org/TR/wai-aria-1.2/#contentinfo. ARIA in HTML, W3C Recommendation 11 August 2026, row for `footer`, https://www.w3.org/TR/html-aria/#el-footer
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.43 and 3.5.44 for `footer`, https://www.w3.org/TR/html-aam/#el-footer-ancestorbody
- Practice (tier 2): ARIA Authoring Practices Guide, "Landmark Regions", contentinfo section (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- Reference (tier 3): MDN Web Docs, "ARIA: contentinfo role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/contentinfo_role
- Related entries: `html/landmarks.md`, `aria/roles/banner.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.4.1-bypass-blocks.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="contentinfo"` on a page-level `footer` is redundant, never a finding.

## What it is

The landmark for information about the page or site at the bottom: copyright, privacy and accessibility statement links, contact details. WAI-ARIA 1.2: "A landmark that contains information about the parent document."

## The native element

`footer`, but only when it is scoped to the `body`. A `footer` inside `article`, `aside`, `main`, `nav`, or `section` maps to a different role (`sectionfooter` in HTML-AAM; `generic` in ARIA in HTML) and is not a landmark. ARIA in HTML allows `role="contentinfo"` on a body-scoped `footer` but marks it "NOT RECOMMENDED".

## When writing the role is justified

When a `footer` cannot be used, such as a legacy page being retrofitted (APG; `aria/using-aria.md`, rule 1).

## What the spec asks of authors

- "Within any document or application, the author SHOULD mark no more than one element with the contentinfo role." A nested document or application may have its own.
- Naming: name from author; not required. APG: give each a unique label when there is more than one.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required by WAI-ARIA 1.2; APG asks for a unique one when there is more than one.
- It stands alone: it is not one part of a larger component, so it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** a `footer` scoped to the `body` (redundant, "NOT RECOMMENDED").
- **Allowed:** `section`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** a `footer` inside `article`, `aside`, `main`, `nav`, or `section`; `header`, `nav`, `aside`, `article`, `main`, `form`, `search`; `ul`, `ol`, `li`; `h1` to `h6`; `a` with `href`; `button`; form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- `role="contentinfo"` on another element replaces its role.
- ARIA in HTML allows only `group`, `presentation`, or `none` on a `footer` (plus `contentinfo` where it already is one). `none` or `presentation` on the page footer removes the landmark.

## How it fails in code

- Missing landmarks contribute to a 2.4.1 failure only together with no skip link and no heading at the start of the main content (`wcag/sc-2.4.1-bypass-blocks.md`). A missing contentinfo alone is not a failure.
- A page footer placed inside `main`, so it is not a contentinfo landmark. Advice.
- Two contentinfo landmarks, or one nested in another landmark. Advice (axe `landmark-no-duplicate-contentinfo`, `landmark-contentinfo-is-top-level`, best practice).

## How to check

Find the page-level `footer` or `role="contentinfo"`; confirm it is not inside a sectioning element or `main`. MDN notes a known VoiceOver issue with `footer` (no version given): check the accessibility tree and test with the spec's screen readers. axe: `landmark-contentinfo-is-top-level`, `landmark-no-duplicate-contentinfo`.
