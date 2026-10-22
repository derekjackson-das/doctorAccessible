# SC 3.1.1 Language of Page

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 3 Understandable / 3.1 Readable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#language-of-page
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> The default human language of each web page can be programmatically determined.

## What it requires, in our words

The page says what language it is written in, in the code, so that a screen reader picks the right voice and pronunciation rules, a browser offers the right translation, and spelling and hyphenation behave. In HTML this is the `lang` attribute on the `html` element with a valid language tag such as `en` or `en-US`. Without it, a screen reader falls back to its own default and may read English with French pronunciation or the reverse, which turns readable text into noise. This is one of the cheapest criteria to meet and one of the most common to miss.

## How it fails in code

- No `lang` attribute on the `html` element. Definite.
- An empty `lang` attribute, or a value that is not a valid language tag, such as `lang="english"`. Definite.
- A `lang` value that names the wrong language for the page's content. Definite once a person confirms the content language.
- `lang` and `xml:lang` both present and disagreeing. Definite.
- `lang` set on `body` instead of `html`. Likely; the default language is meant to be on the root element, and some assistive technology does not look lower.

## How to meet it

- Technique H57, "Using the language attribute on the HTML element": `<html lang="en">`. Use the shortest tag that is correct; a region subtag is optional.
- Advisory: Technique SVR5, "Specifying the default language in the HTTP header", in addition to the attribute, never instead of it.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.1.2 Language of Parts (entry in this package). Passages in another language inside the page.
- SC 2.4.2 Page Titled (`wcag/sc-2.4.2-page-titled.md`). The title is read in the page language.

## Automated coverage (tier 3)

axe-core tags `html-has-lang`, `html-lang-valid`, and `html-xml-lang-mismatch` to this criterion. They catch a missing, empty, invalid, or conflicting attribute reliably. Whether the declared language matches the content is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
