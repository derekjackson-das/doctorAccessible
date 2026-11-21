# Role: navigation

- Category: landmark.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "navigation role", https://www.w3.org/TR/wai-aria-1.2/#navigation. ARIA in HTML, W3C Recommendation 11 August 2026, row for `nav`, https://www.w3.org/TR/html-aria/#el-nav
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.94, https://www.w3.org/TR/html-aam/#el-nav
- Practice (tier 2): ARIA Authoring Practices Guide, "Landmark Regions", navigation section (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- Reference (tier 3): MDN Web Docs, "ARIA: navigation role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/navigation_role
- Related entries: `html/landmarks.md`, `html/links.md`, `aria/patterns/tabs.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.4.1-bypass-blocks.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="navigation"` on `nav` is redundant, never a finding.

## What it is

The landmark for a group of links that move around the site or the page. WAI-ARIA 1.2: "A landmark containing a collection of navigational elements (usually links) for navigating the document or related documents."

## The native element

`nav`, always (HTML-AAM). ARIA in HTML allows `role="navigation"` on `nav` but marks it "NOT RECOMMENDED".

## When writing the role is justified

When a `nav` cannot be used, such as a legacy page being retrofitted.

## What the spec asks of authors

- WAI-ARIA 1.2 places no count limit and no naming requirement on navigation. Name from author.
- APG and MDN: when there is more than one, give each a unique label (`aria-labelledby` to a visible heading, else `aria-label`). Two navs with the same links, such as the same menu at top and bottom, share a label. Leave the word "navigation" out of the label; it is announced with the role, so "Site navigation" becomes "Site navigation navigation".

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required by WAI-ARIA 1.2; APG asks for a unique one when there is more than one.
- It stands alone: it is not one part of a larger component, so it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `nav` (redundant, "NOT RECOMMENDED").
- **Allowed:** `section`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `ul` and `ol` (wrap the list in a `nav` instead), `li`, `header`, `footer`, `aside`, `article`, `main`, `form`, `search`; `h1` to `h6`; `a` with `href`; `button`; form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

This is where most navigation mistakes are.

- **Another role on `nav` removes the landmark.** ARIA in HTML allows `menu`, `menubar`, `none`, `presentation`, or `tablist` on `nav`. Each is allowed, and each replaces `navigation`: `<nav role="tablist">` is a tab list and no longer a navigation landmark. Allowed by ARIA in HTML does not mean harmless. If the links are page navigation, keep the `nav` and put the other role on an element inside it.
- **`role="navigation"` on a `ul` is not allowed** (above). Where a browser honors it anyway, the list and its items lose their roles. Put a `nav` around the list instead.
- **`menu` or `menubar` for site navigation** turns links into an application menu with its own keyboard model. Advice: use `nav` with a list of links (`html/links.md`).

## How it fails in code

- Navigation built with no `nav`, no skip link, and no heading at the start of the main content: `wcag/sc-2.4.1-bypass-blocks.md`, definite per that entry.
- `<nav role="tablist">` or `<nav role="menu">` around page navigation: the navigation landmark is gone. Likely under 1.3.1 when the links are site or page navigation and nothing else marks them as such; manual review otherwise. Report once.
- `role="menu"` with links but no menu keyboard behavior: the role misreports the control, 4.1.2, likely (`wcag/sc-4.1.2-name-role-value.md`).
- Several unnamed `nav` elements. Advice (axe `landmark-unique`).

## How to check

Every `nav`, and every element with `role="navigation"`: does it still expose `navigation` in the accessibility tree, or has another role replaced it? If there are several, does each have a distinct name without the word "navigation"? axe: `landmark-unique` (best practice).
