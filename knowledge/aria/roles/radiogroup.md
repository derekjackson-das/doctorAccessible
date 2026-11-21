# Role: radiogroup

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "radiogroup role", https://www.w3.org/TR/wai-aria-1.2/#radiogroup. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `fieldset`, `ul`, `ol`, `menu`, and form-associated custom elements, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Radio Group Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/radio/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: radiogroup role", last modified 8 October 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radiogroup_role
- Related entries: `aria/roles/radio.md`, `html/forms.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

The container that groups radios that set the same value. WAI-ARIA 1.2: "A group of radio buttons."

## The native element

None maps to it. A set of `input type=radio` with the same `name`, inside a `fieldset` with a `legend`, is the native equivalent; the `fieldset` itself maps to `group` (HTML-AAM 3.5.40). `role="radiogroup"` on that `fieldset` is optional (MDN).

## When writing the role is justified

Around custom `role="radio"` elements, always. Around native radios, optional.

## What the spec asks of authors

- "Authors SHOULD enforce that only one radio button in a group can be checked at the same time."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `radio`.
- Required states and properties: none.
- Supported states and properties: `aria-errormessage`, `aria-invalid`, `aria-readonly`, `aria-required`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-haspopup` as deprecated on this role.
- Naming: name from author; **required**.
- `aria-required` and `aria-invalid` belong on the group, not on each radio (MDN); `aria-checked` belongs on the radios, not the group.

**The whole component.** It must own at least one `radio`, have a name (usually from a visible group label with `aria-labelledby`), and keep exactly one radio checked. The keyboard model lives on the radios: see `aria/roles/radio.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `fieldset`, `ul`, `ol`, `menu`, form-associated custom elements, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li`, headings, `form`, `section` and the other landmark elements, `table`-family cells, form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

The group itself takes one tab stop; the keys are the radios' (Tab in to the checked radio, arrows to move and check). See `aria/roles/radio.md`.

## What an explicit role takes away

- On a `fieldset`, `group` is replaced by `radiogroup`, which is what is wanted for radios.
- On a `ul` or `ol`, the list and its items lose their roles; the `li` elements should then carry `role="radio"` or `none`.

## How it fails in code

- No name on the group, so the question the radios answer is lost: `wcag/sc-1.3.1-info-and-relationships.md` or `wcag/sc-4.1.2-name-role-value.md`, at those entries' confidence.
- A `radiogroup` that owns no `radio`: the component is broken; report under the criterion the radios fail.
- More than one radio checked at a time: manual review under `wcag/sc-4.1.2-name-role-value.md`.

## How to check

Each `radiogroup` has a name, owns its radios, and only one is checked. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
