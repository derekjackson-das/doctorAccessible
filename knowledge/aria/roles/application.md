# Role: application

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "application role", https://www.w3.org/TR/wai-aria-1.2/#application. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for the elements that allow the role, and the row for `body`, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page; lists no HTML equivalent), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: application role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role
- Related entries: `aria/roles/document.md`, `aria/roles/article.md`, `aria/using-aria.md`, `html/custom-controls.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2 and ARIA in HTML text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

This role changes how assistive technology handles keys, so its effect cannot be read from the code alone. A finding about it is likely at most, and names the test a person has to run with the assistive technology in the project's spec. Do not say what a user would experience.

## What it is

A container for a control that follows no standard widget pattern, where the page itself handles every key. WAI-ARIA 1.2: "A structure containing one or more focusable elements requiring user input, such as keyboard or gesture events, that do not follow a standard interaction pattern supported by a widget role."

The spec explains why it exists. Some assistive technologies have a browse mode that intercepts keys such as the arrow keys to move a reading cursor. Inside an `application`, the spec says those tools "SHOULD switch to a mode that passes most or all standard input events through to the web application."

The consequence is the reason for caution. WAI-ARIA 1.2: "only the focusable elements contained in an application element are accessible to users of some assistive technologies".

## The native element

None. APG lists no HTML equivalent.

## When writing the role is justified

Rarely. WAI-ARIA 1.2 allows it "When there is a need to create an element with an interaction model that is not supported by any of the WAI-ARIA widget roles", and gives a slide editor as the example, where arrow keys move objects on a slide. If a widget role fits (`grid`, `tree`, `listbox`, `slider`, and the rest in `aria/roles/`), use that role: it brings a keyboard model assistive technology already knows.

MDN: put it on the smallest container that needs it, never on `body`, and test it with assistive technology. Most web apps are not applications in this sense.

## What the spec asks of authors

- "authors MAY give that element role application."
- "authors MUST use one of the following techniques to ensure all non-decorative static text or image content inside an application is accessible:" associate the content with a focusable element through `aria-labelledby` or `aria-describedby`; or place it in a focusable element with role `document` or `article`; or manage focus of owned elements and update `aria-activedescendant` to point at the element holding the content.
- Naming: required ("Accessible Name Required: True"), from the author.
- The spec's example adds `aria-roledescription` to say what the thing is and `aria-describedby` for instructions. MDN: a role description has to be translated with the rest of the page.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-activedescendant`, `aria-disabled`, `aria-errormessage`, `aria-expanded`, `aria-haspopup`, `aria-invalid`.
- Prohibited states and properties: none. No global attribute is marked deprecated on this role.
- Naming: name from author; **required**.

**The whole component.** An `application` contains at least one focusable element, a name, key handling for everything a user needs to do in it, and a way out. Static content inside is tied to a focusable element or placed in a focusable `document` or `article` (`aria/roles/document.md`).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `article`, `audio`, `embed`, `iframe`, `object`, `section`, `video`, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `body` (it allows no role but `generic`) and `html`; `main`, `nav`, `aside`, `header`, `footer`, `form`; `ul`, `ol`, `li`; `button`; `a` with `href`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

It promises no pattern, which is the point: the author defines every key. MDN: Tab, Space, Enter, and Escape must be handled by the application, unless focus is on a standard control inside it, and the author is responsible for making sure focus can leave. Whatever keys are chosen have to be discoverable; the spec's example uses `aria-describedby` for that.

## What an explicit role takes away

- On a `section` or `article`, the `region` or `article` role goes.
- More important is what it takes from everything inside. Per the spec, only the focusable elements are available in some assistive technologies. The browse mode the spec describes, with its reading cursor, is what the role asks those tools to leave.

## How it fails in code

- `role="application"` on `body`, on a page wrapper, or around ordinary content such as text, forms, and links: not allowed on `body` by ARIA in HTML, and it misreports ordinary content as a custom control. `wcag/sc-4.1.2-name-role-value.md`, likely; the entry does not list this case, and a person confirms with the spec's assistive technology whether the content can still be read. The fix direction is to remove the role.
- Static text or images inside an `application` with none of the three techniques: breaks the WAI-ARIA MUST. `wcag/sc-4.1.2-name-role-value.md`, likely, on the same test.
- A control inside it that cannot be operated by keyboard: `wcag/sc-2.1.1-keyboard.md`, at that entry's confidence.
- Focus cannot leave the application by keyboard: `wcag/sc-2.1.2-no-keyboard-trap.md`, definite once observed, per that entry.
- No accessible name: breaks the WAI-ARIA requirement. `wcag/sc-4.1.2-name-role-value.md`, likely.
- The role where a widget role would fit: advice.

## How to check

Search for `role="application"`. For each: is there an interaction no widget role covers? Is it on the smallest container? Does it have a name, does every piece of static content inside use one of the three techniques, do the keys work, and can focus leave? Then it goes on the manual test list for the project's assistive technology (`at-test-protocol`). Observed with axe-core 4.14.0 on 2026-11-23: no rule fired on a `role="application"` with no name wrapping static text. A clean scan says nothing about this role.
