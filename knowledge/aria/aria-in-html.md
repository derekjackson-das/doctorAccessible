# ARIA: What each HTML element allows

- Sources:
  - W3C, "ARIA in HTML", W3C Recommendation 11 August 2026. https://www.w3.org/TR/html-aria/ Tier 1 for sections 1, 4, and 6, except their notes and examples, which section 6 makes non-normative. Sections 2, 3, 5, and 7 are marked non-normative, so tier 2.
  - W3C, "HTML Accessibility API Mappings 1.0", W3C Working Draft 21 October 2026. https://www.w3.org/TR/html-aam/ Tier 2: where the implicit roles in the table come from.
  - W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023. https://www.w3.org/TR/wai-aria-1.2/ Tier 1: the roles and attributes themselves.
- Related: `aria/using-aria.md`, `aria/accessible-name.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

ARIA in HTML is a W3C Recommendation, but it is not part of WCAG. Breaking one of its rules is a conformance error against ARIA in HTML, not a WCAG failure by itself. Report a WCAG failure only when the misuse breaks a criterion, such as a role that misreports the control (4.1.2) or hides structure (1.3.1), at the confidence the `wcag/` entry gives. A rule broken with no barrier shown is advice, not a finding; if a barrier is suspected, it is manual review under the criterion it may break, with this entry named as the cause. A redundant role is not a finding.

## What it is

The rulebook for which `role` values and `aria-*` attributes may go on which HTML element. Section 4 is one large table, one row per element.

## How to read the table

Each row has three cells (section 4):

1. **The element,** sometimes with a condition: "`a` with `href`", "`img` with empty `alt` and no accessible name".
2. **Its implicit semantics:** the role and states the browser already exposes, for example `role=link` for `a` with `href`. These come from HTML-AAM.
3. **What authors may add.** One of:
   - **A list of roles.** Only those roles may replace the implicit one. A `button` may become, for example, a `checkbox` or a `switch`, but not a `heading`.
   - **Any role.** Any role may be used, but the specification says not to repeat the implicit role, and not to use `generic` or a deprecated role.
   - **No role.** The specification says authors must not override the element's semantics.
   - **Naming Prohibited.** `aria-label` and `aria-labelledby` must not be used unless a role that allows naming is also set. A plain `div`, `span`, or `p` is in this group.
   - **Which `aria-*` attributes are allowed:** the global ones, plus those that belong to the role.

The normative core, quoted from section 1:

> Authors MUST NOT use the ARIA role and aria-* attributes in a manner that conflicts with the semantics described in the 4. Document conformance requirements for use of ARIA attributes in HTML and 4.2 Requirements for use of ARIA attributes in place of equivalent HTML attributes tables.

## The other rules

- **Native attribute wins.** Where an HTML attribute and an `aria-*` attribute say the same thing, browsers must ignore the ARIA one. Do not set both. `<input type="checkbox" checked aria-checked="false">` is exposed as checked (section 4.2; section 3.4 example).
- **Deprecated.** The `directory` role (marked for deprecation in WAI-ARIA 1.2; use a list), the Digital Publishing roles `doc-biblioentry` and `doc-endnote`, and the attributes `aria-grabbed` and `aria-dropeffect`. Conformance checkers must warn about them. ARIA has nothing to replace the drag-and-drop pair (section 4.3).
- **Lowercase** role and token values; some assistive technology does not parse others (section 4.4).
- **HTML's rules still apply.** A role does not change how HTML is parsed: a `div` given `role="link"` inside a `p` still ends the paragraph. Use a `span` (section 3.5, non-normative).

## Common mistakes the specification warns about

All from section 3, non-normative, in our words:

- **An interactive element given a non-interactive role,** such as `<button role="heading">`. The button's behavior stays and conflicts with what is announced.
- **Redundant roles,** such as `role="button"` on `button`, `role="main"` on `main`. Not recommended. One exception: `role="list"` on a `ul` whose bullets have been removed, because some browsers then stop exposing it as a list.
- **Side effects,** such as `role="button"` on `summary`, which can stop its expanded state being exposed.
- **Abstract roles,** such as `role="select"`, are not for authors; `combobox` was probably meant (section 3.4).
- **`role="generic"`** is meant for browsers, not authors; ARIA discourages it, and the table says it should not be used (sections 3.4 and 4).

## How to check it

- For each element with a `role` or `aria-*` attribute, find its row in section 4 and check the third cell.
- Look for `aria-label` or `aria-labelledby` on a `div`, `span`, or `p` with no role.
- Look for an ARIA attribute repeating or contradicting a native one (`aria-checked` with `checked`, `aria-disabled` with `disabled`, `aria-required` with `required`).
- axe has rules for allowed roles and attributes; the Deque rule descriptions say which.
