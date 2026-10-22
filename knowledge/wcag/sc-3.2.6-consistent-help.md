# SC 3.2.6 Consistent Help

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 3 Understandable / 3.2 Predictable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#consistent-help
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html
- Also in: WCAG 2.2 only. New in 2.2; not in 2.0 or 2.1.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> If a web page contains any of the following help mechanisms, and those mechanisms are repeated on multiple web pages within a set of web pages, they occur in the same order relative to other page content, unless a change is initiated by the user:
>
> - Human contact details;
> - Human contact mechanism;
> - Self-help option;
> - A fully automated contact mechanism.
>
> Note 1: Help mechanisms may be provided directly on the page, or may be provided via a direct link to a different page containing the information.
>
> Note 2: For this success criterion, "the same order relative to other page content" can be thought of as how the content is ordered when the page is serialized. The visual position of a help mechanism is likely to be consistent across pages for the same page variation (e.g., CSS break-point). The user can initiate a change, such as changing the page's zoom or orientation, which may trigger a different page variation. This criterion is concerned with relative order across pages displayed in the same page variation (e.g., same zoom level and orientation).

## What it requires, in our words

If a site offers help, such as a phone number, a contact form, a chat widget, a help page link, or a frequently asked questions link, and offers it on more than one page, it sits in the same place in the page order each time. Someone who is stuck needs to find help without a search; knowing it is always at the end of the footer, or always at the top right, is what makes that possible. The criterion does not require help to exist. It requires that help, where it repeats, be findable in the same place. Position is judged in the serialized order of the page, so a different layout at a phone width is fine as long as it is consistent at that width.

## How it fails in code

- A "Contact us" link in the header on some pages and the footer on others. Definite once two pages are compared.
- A chat widget that appears on some pages and, where it appears, in a different place in the source order. Definite once compared.
- Help offered only on one page. Not a failure; nothing repeats.
- Help in the footer on every page, with the footer in the same relative position. Passes.

## How to meet it

- Technique G220, "Provide a contact-us link in a consistent location": one shared template region for help links and contact details.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.2.3 Consistent Navigation (entry in this package). The broader rule for repeated navigation; this one adds help mechanisms at Level A.
- SC 2.4.5 Multiple Ways (`wcag/sc-2.4.5-multiple-ways.md`). Finding pages; a help page is often one of the ways.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Judged by comparing pages, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
