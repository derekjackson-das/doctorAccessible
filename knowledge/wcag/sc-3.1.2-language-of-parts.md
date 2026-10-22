# SC 3.1.2 Language of Parts

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 3 Understandable / 3.1 Readable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#language-of-parts
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> The human language of each passage or phrase in the content can be programmatically determined except for proper names, technical terms, words of indeterminate language, and words or phrases that have become part of the vernacular of the immediately surrounding text.

## What it requires, in our words

When a page in one language contains a passage in another, the passage is marked with its own language so a screen reader switches voice for it. A French quotation in an English article, a Spanish-language navigation link to a translated version of the site, a block of German instructions: each gets a `lang` attribute on the element that contains it. Single borrowed words that English has absorbed, such as "rendezvous" or "café", do not need marking, and neither do proper names or technical terms. The judgment is whether a reader would hear the passage as foreign.

## How it fails in code

- A passage, sentence, or quotation in a language other than the page language, with no `lang` attribute on it or any ancestor. Definite once a person confirms it is a different language and not a name or a borrowed word.
- A link to another-language version of the site whose text is in that language ("Español", "Français") without `lang` on the link. Likely; the Understanding page treats these as passages in another language.
- A `lang` attribute with an invalid value on a passage. Definite.
- A proper name, a technical term, or an absorbed word left unmarked. Not a failure; the exception covers it.

## How to meet it

- Technique H58, "Using language attributes to identify changes in the human language": `<blockquote lang="fr">`, `<span lang="de">`, `<a lang="es" href="/es/">Español</a>`.
- Content: when quoting, keep the quotation in one element so one attribute covers it.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 3.1.1 Language of Page (entry in this package). The page default this criterion departs from.
- SC 2.4.4 Link Purpose (In Context) (`wcag/sc-2.4.4-link-purpose-in-context.md`). A language-switch link should say where it goes, in the target language, with `lang` set.

## Automated coverage (tier 3)

axe-core tags `valid-lang` to this criterion. It checks that any `lang` attribute present has a valid value. It cannot detect an unmarked passage in another language, which is the common failure; that is found by reading. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
