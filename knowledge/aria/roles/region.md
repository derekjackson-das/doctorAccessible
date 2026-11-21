# Role: region

- Category: landmark.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "region role", https://www.w3.org/TR/wai-aria-1.2/#region. ARIA in HTML, W3C Recommendation 11 August 2026, row for `section`, https://www.w3.org/TR/html-aria/#el-section
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.114, https://www.w3.org/TR/html-aam/#el-section
- Practice (tier 2): ARIA Authoring Practices Guide, "Landmark Regions", region section (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- Reference (tier 3): MDN Web Docs, "ARIA: region role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/region_role
- Related entries: `html/landmarks.md`, `aria/roles/complementary.md`, `aria/roles/generic.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). A `section` with no name is not a landmark and not a finding.

## What it is

A general landmark for a part of the page important enough to jump to, when no other landmark fits. WAI-ARIA 1.2: "A landmark containing content that is relevant to a specific, author-specified purpose and sufficiently important that users will likely want to be able to navigate to the section easily and to have it listed in a summary of the page."

## The native element

`section`, but only with an accessible name. HTML-AAM 3.5.114: `region` "if the section element has an accessible name. Otherwise, the generic role." ARIA in HTML allows `role="region"` on `section` but marks it "NOT RECOMMENDED", and says `role="generic"` should not be used on it.

## When writing the role is justified

On a `div` when a `section` cannot be used. More often the fix is a name on a `section` that already exists.

## What the spec asks of authors

- "Authors SHOULD limit use of the region role to sections containing content with a purpose that is not accurately described by one of the other landmark roles, such as main, complementary, or navigation."
- "Authors MUST give each element with role region a brief label that describes the purpose of the content in the region." "Authors SHOULD reference a visible label with aria-labelledby if a visible label is present." "Authors SHOULD include the label inside of a heading whenever possible."
- Naming: required ("Accessible Name Required: True").
- MDN: use it sparingly; many regions on one page suggest the structure needs another look.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; **required** ("Accessible Name Required: True").
- It stands alone: it is not one part of a larger component, so it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `section` with an accessible name (redundant, "NOT RECOMMENDED").
- **Allowed:** `article`, `aside`, `search`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`. A `div` given `role="region"` may then be named, because the role allows a name.
- **Not allowed:** `nav`, `header`, `footer`, `main`, `form`; `ul`, `ol`, `li`; `h1` to `h6`; `a` with `href`; `button`; form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- ARIA in HTML allows many roles on `section`, including `alert`, `dialog`, `group`, `navigation`, `none`, `search`, `status`, and `tabpanel`. Each replaces `region` (or `generic`, if unnamed).
- `role="region"` on a `table` (allowed: `table` takes any role) replaces the table role and, with it, its rows and cells. On a `ul` it is not allowed (above); where a browser honors it anyway, the list is lost.
- MDN: a scrolling area made focusable with `tabindex="0"` is not thereby a landmark; give it `role="group"` and a name if it needs a role, not `region` by default.

## How it fails in code

- `role="region"` or a `section` meant as a landmark with no name: breaks the WAI-ARIA MUST, and the browser exposes no landmark. Advice; not a WCAG failure by itself.
- Every `section` on the page named so it becomes a region, swamping the landmark list. Advice.
- A scrolling container with no keyboard access: `wcag/sc-2.1.1-keyboard.md`, whatever role it has. A role does not fix it.

## How to check

For each `section` and `role="region"`: does it have a name, and is it meant to be a landmark? If named, would `main`, `complementary`, `navigation`, or `search` describe it better? axe: `region` (best practice: all content in landmarks).
