# SC 2.4.4 Link Purpose (In Context)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.4 Navigable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#link-purpose-in-context
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> The purpose of each link can be determined from the link text alone or from the link text together with its programmatically determined link context, except where the purpose of the link would be ambiguous to users in general.

## What it requires, in our words

A person should be able to tell where a link goes from its text, or from its text plus the sentence, list item, or table cell it sits in. Screen reader users often pull up a list of all links on a page and pick one; "click here", "read more", and "learn more" repeated ten times tell them nothing. Context counts only when it is programmatically attached: the same paragraph, the same list item, the same table cell with its headers. A heading above the link is not enough at this level. If the link is an image, its alt text is the link text.

## How it fails in code

- Links whose text is generic ("click here", "read more", "more", "here") with no programmatic context that completes the purpose. Definite.
- Several links with the same text going to different destinations, with no distinguishing context. Definite.
- A link whose only content is an image with no accessible name. Definite; also 1.1.1 and 4.1.2. F89.
- Context for a link placed somewhere not programmatically related, such as a heading above or a paragraph elsewhere. Definite. F63.
- A link that is a bare URL. Likely; a long URL read aloud rarely conveys purpose. Content standards call for descriptive text.
- Generic text inside a sentence that completes it: "Read the <a>full accessibility policy</a>." Passes.

## How to meet it

- Technique G91, "Providing link text that describes the purpose of a link", and Technique H30 for anchor elements. The content standards in `docs/content-standards.md` say what good link text is.
- Technique G53, "Identifying the purpose of a link using link text combined with the text of the enclosing sentence", and H77, H78, H79, H81 for list items, paragraphs, table cells, and nested lists.
- Technique ARIA8, "Using aria-label for link purpose", or ARIA7 with `aria-labelledby`, when the visible text cannot change; the visible text must still be part of the name (2.5.3).
- Technique C7, "Using CSS to hide a portion of the link text", to add visually hidden words.
- Technique H24 for image-map areas.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.4.9 Link Purpose (Link Only) is Level AAA and removes the context allowance; not a requirement here.
- SC 1.1.1 Non-text Content (`wcag/sc-1.1.1-non-text-content.md`). Image links need alt text that states the destination.
- SC 2.5.3 Label in Name (entry in this package). If `aria-label` is used, it must contain the visible text.
- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). Whether the link has a name at all.
- SC 2.4.6 Headings and Labels (entry in this package). The parallel requirement for headings.

## Automated coverage (tier 3)

axe-core tags `link-name` and `area-alt` to this criterion. They flag links and image-map areas with no accessible name. Whether a name that exists describes the destination is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
