# ARIA: When to use it at all

- Sources:
  - W3C, "Using ARIA", W3C Discontinued Draft 24 February 2026. https://www.w3.org/TR/using-aria/ Tier 2, informative. The document calls itself discontinued and says it should be cited only as abandoned work. It keeps its four rules as a historical reference, plans no further work, and points to the Authoring Practices Guide for live guidance. Cite the rules as historical W3C guidance, dated, never as a requirement.
  - W3C, "Using ARIA", W3C Working Draft 27 September 2018. https://www.w3.org/TR/2018/WD-using-aria-20180927/ Tier 2, historical. The last version before 2026; it had a fifth rule, on accessible names, which its editors marked as a work in progress and the 2026 text dropped.
  - W3C WAI, ARIA Authoring Practices Guide, "Read Me First", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/ Tier 2. The source of the heading "No ARIA is better than Bad ARIA", which is in neither version of Using ARIA.
  - W3C, "ARIA in HTML", W3C Recommendation 11 August 2026. https://www.w3.org/TR/html-aria/ Tier 1 for what is allowed; see `aria/aria-in-html.md`.
- Related: `aria/aria-in-html.md`, `aria/accessible-name.md`, `patterns/` (whether to build the widget at all)
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.5.3-label-in-name.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

Using ARIA where native HTML would do is never a WCAG failure on its own. It becomes one when the result breaks a criterion: a role with no keyboard support (2.1.1), a role or state that misreports the control (4.1.2), structure that ARIA hides or changes (1.3.1), a name that drops the visible label (2.5.3). Report it once, under that criterion, at the confidence its `wcag/` entry gives, and name this entry as the cause. Otherwise, preferring native HTML is advice, not a finding. If a barrier is suspected but not shown, it is manual review under the criterion it may break, with this entry named as the cause. A redundant role, such as `role="button"` on a `button`, is not a finding; at most a note.

## What it is

ARIA is a set of attributes (`role` and `aria-*`) that tell assistive technology what an element is, what state it is in, and what it is called. It changes only what is exposed to assistive technology. The APG puts it plainly: a role gives no keyboard behavior and no styling. `<div role="button">` is a promise that the author has also written the script for a button's keys (APG, "a role is a promise").

## Why it matters

The APG opens with that warning: bad ARIA is worse than none. Wrong ARIA misreports the page to a screen reader user, sometimes worse than no ARIA at all. ARIA can add meaning a native element lacks, such as `aria-pressed` on a toggle button. It can also cover up meaning that was there: `role="navigation"` on a `ul` removes the list (APG).

## The rules

From Using ARIA, 2026, in our words:

1. **Native first.** If an HTML element or attribute already has the meaning and behavior you need, use it, rather than repurposing another element and adding ARIA. The exceptions it names: the feature exists in HTML but is not implemented or not accessibly supported; the native element cannot be styled as the design needs; or HTML has no such feature.
2. **Leave an element's own meaning alone** unless there is no other way. Its example: to make a tab that contains a heading, put the heading inside an element with `role="tab"`; do not put `role="tab"` on the `h2`.
3. **Every interactive ARIA control works by keyboard.** It can be reached, and it responds to the keys expected for its role. For `role="button"`, that is focus plus both Enter and Space.
4. **No `role="presentation"` or `role="none"`, and no `aria-hidden="true"`, on a focusable element.** And no `aria-hidden="true"` on an ancestor of one, because it hides everything inside. Keyboard users land on something that is not there for a screen reader.

The 2018 draft also had a fifth rule, which its editors marked as a work in progress and the 2026 text dropped: every interactive element has an accessible name. The requirement itself stands in WCAG (`wcag/sc-4.1.2-name-role-value.md`), and a visible word next to a control is not its name unless it is associated with it (`aria/accessible-name.md`).

## How to do it

- Start from the native element: `button`, `a href`, `input`, `select`, `details`/`summary`, `dialog`, `fieldset`/`legend`, headings, lists, and landmarks.
- When ARIA is needed, check what the element allows (`aria/aria-in-html.md`) and follow the APG pattern for the widget, which is a pattern, not a requirement (`patterns/`).
- Add only what native HTML cannot say: a state such as `aria-expanded` or `aria-pressed`, a relationship such as `aria-controls` or `aria-describedby`, or a name where there is no visible text.
- Write the keyboard behavior the role promises, and test it with the assistive technology in the spec. The APG says its examples deliberately do not work around gaps in browser and screen reader support, so a working APG example is not proof of support.

## How to check it

- For every `role`: is there a native element that does this? If so, why was it not used?
- For every interactive role: can it be reached by Tab and operated with the keys its role expects (`wcag/sc-2.1.1-keyboard.md`)?
- Search for `aria-hidden="true"` and `role="presentation"` or `role="none"`: is anything inside focusable?
- For every `aria-label` and `aria-labelledby`: does the computed name still contain the visible text (`wcag/sc-2.5.3-label-in-name.md`)?
- axe checks many ARIA rules, such as allowed roles and attributes and hidden focusable elements; see the Deque rule descriptions for what each covers. Whether the ARIA was needed at all is manual.
