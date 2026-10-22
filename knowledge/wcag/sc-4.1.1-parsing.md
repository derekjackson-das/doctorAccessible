# SC 4.1.1 Parsing (obsolete and removed in WCAG 2.2)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: none in WCAG 2.2. The criterion is marked "Obsolete and removed". It was Level A in WCAG 2.0 and 2.1.
- Principle and guideline: 4 Robust / 4.1 Compatible
- Tier 1 source: https://www.w3.org/TR/WCAG22/#parsing
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/parsing.html
- Also in: WCAG 2.1 (https://www.w3.org/TR/WCAG21/#parsing, W3C Recommendation 6 May 2025) and WCAG 2.0 (https://www.w3.org/TR/WCAG20/#ensure-compat-parses, W3C Recommendation 11 December 2008), Level A in both, same criterion text. The 2.1 Recommendation carries two notes, and the WCAG 2.0 errata (https://www.w3.org/WAI/WCAG20/errata/, page dated 6 September 2023), that say to treat it as always satisfied for HTML and XML.
- Verified against the live source: 2026-10-22 by Claude Code for Jennifer Dee, by direct fetch of the WCAG 2.2, 2.1, and 2.0 Recommendations, the Understanding page, and the WCAG 2.0 errata

## Normative text (tier 1, quoted)

WCAG 2.2, W3C Rec 12 Dec 2024, in place of the criterion:

> This criterion was originally adopted to address problems that assistive technology had directly parsing HTML. Assistive technology no longer has any need to directly parse HTML. Consequently, these problems either no longer exist or are addressed by other criteria. This criterion no longer has utility and is removed.

WCAG 2.1, W3C Rec 6 May 2025, Level A:

> In content implemented using markup languages, elements have complete start and end tags, elements are nested according to their specifications, elements do not contain duplicate attributes, and any IDs are unique, except where the specifications allow these features.
>
> Note 1: This success criterion should be considered as always satisfied for any content using HTML or XML.
>
> Note 2: Since this criterion was written, the HTML Living Standard has adopted specific requirements governing how user agents must handle incomplete tags, incorrect element nesting, duplicate attributes, and non-unique IDs. [HTML] Although the HTML standard treats some of these cases as non-conforming for authors, it is considered to "allow these features" for the purposes of this success criterion because the specification requires that user agents support handling these cases consistently. In practice, this criterion no longer provides any benefit to people with disabilities in itself. Issues such as missing roles due to inappropriately nested elements or incorrect states or names due to a duplicate ID are covered by different success criteria and should be reported under those criteria rather than as issues with 4.1.1.

WCAG 2.0, W3C Rec 11 Dec 2008, Level A: same criterion text as 2.1, with this note:

> Note: Start and end tags that are missing a critical character in their formation, such as a closing angle bracket or a mismatched attribute value quotation mark are not complete.

The WCAG 2.0 errata add the same explanation as the 2.1 Note 2 and end with: "This criterion should be considered as always satisfied for any content using HTML or XML."

## What it requires, in our words

Nothing, for our target. WCAG 2.2 removed the criterion, so there is no 4.1.1 finding to make against a WCAG 2.2 AA page. It once mattered because screen readers read raw markup themselves, and broken tags or duplicate IDs could garble what they presented. Assistive technology now reads the browser's accessibility tree, and the HTML standard fixes how browsers repair bad markup, so the original harm is gone. Under WCAG 2.0 and 2.1, the W3C now says the criterion is always satisfied for HTML and XML. The real harms that malformed markup can still cause, such as a broken name or a lost role, belong to other criteria.

## How it fails in code

It does not fail, under any WCAG version, for content in HTML or XML. Report the consequence, not the markup:

- A duplicate `id` that an `aria-labelledby`, `aria-describedby`, or `label for` points at, so a control gets the wrong name or description. Report under SC 4.1.2 (`wcag/sc-4.1.2-name-role-value.md`) or SC 1.3.1 (`wcag/sc-1.3.1-info-and-relationships.md`). Definite when the name or relationship is wrong in the accessibility tree.
- Nesting that breaks a structure, such as an `li` outside any list, or interactive content inside a `button` or `a`, so a role or relationship is lost. Report under SC 1.3.1 or SC 4.1.2. Likely until the accessibility tree is checked.
- A duplicate `id` that nothing references, or an unclosed tag the browser repairs with no change to names, roles, or structure. No WCAG finding. It may still be worth fixing as code quality; say so without citing WCAG.
- Never report "4.1.1 Parsing" as a failure against a WCAG 2.2 target. If a project's conformance target is 2.0 or 2.1, say the criterion is always satisfied for HTML and XML and cite the note or errata above.

## How to meet it

- Write valid HTML anyway. It is cheap, and it removes the main cause of broken references and lost roles. HTML Living Standard, tier 1, https://html.spec.whatwg.org/multipage/, accessed 2026-10-22.
- Keep every `id` unique, especially ones used by `label for`, `aria-labelledby`, `aria-describedby`, `aria-controls`, and `headers`.
- The Understanding page keeps the original intent for historical purposes only and lists no techniques for WCAG 2.2.

## Related criteria

- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). Where duplicate-ID name and state problems go.
- SC 1.3.1 Info and Relationships (`wcag/sc-1.3.1-info-and-relationships.md`). Where nesting that breaks structure goes.

## Automated coverage (tier 3)

axe-core 4.14.0 (checked in the package source, 2026-10-22) has two rules tagged for this criterion, `duplicate-id` and `duplicate-id-active`. Both are also tagged `wcag2a-obsolete` and `deprecated`, and both are off by default, so a normal axe run reports nothing under 4.1.1. A third rule, `duplicate-id-aria`, is tagged for SC 4.1.2, not 4.1.1, and is set to review on fail. That matches this entry: a duplicate ID used in an ARIA reference is a 4.1.2 problem. Check the Deque rule descriptions at https://dequeuniversity.com/rules/axe/ before relying on a specific rule ID in another version.
