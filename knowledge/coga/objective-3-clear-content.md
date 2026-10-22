# COGA Objective 3: Use clear and understandable content

- Source: W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021
- Tier: 2, informative from W3C. A Working Group Note is guidance, not a conformance requirement. Meeting it is not needed to conform to WCAG 2.2, and missing it is not a WCAG failure.
- Objective: https://www.w3.org/TR/coga-usable/#x4-4-objective-3-use-clear-and-understandable-content
- User stories: https://www.w3.org/TR/coga-usable/#x3-3-objective-3-use-clear-and-understandable-content
- User-need map: https://www.w3.org/TR/coga-usable/#a-3-objective-3-use-clear-and-understandable-content
- Verified against the live source: 2026-10-22 by Caesar Alam with Claude Code, direct fetch of the Note and of the WCAG 2.2 Recommendation for every criterion cited

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. When the same defect also fails a WCAG criterion, report it once, under that criterion and its entry, and name this entry as context. Reading level is measured and reported under `docs/content-standards.md`, which already cites this Note; this entry is the reason behind that standard, not a second finding.

## The objective in plain words

Write so people can understand on the first read: common words, short sentences, one idea at a time, the present tense and active voice, no double negatives, nothing figurative left unexplained. Lay text out in short chunks with space around them, on a plain background. Summarize long documents and media. Give a non-numerical way to understand numbers. This is the objective most of Harvard's authors will meet, because it is about words, not code.

## User needs it serves

- **Clear language.** People with language, processing, or memory impairments need familiar vocabulary and simple syntax, literal meaning rather than idiom, metaphor, or sarcasm, explanations of implied meaning such as gestures and expressions, short summaries or an easy-read version of long content, and images or diagrams that support the words. Readers of some scripts, such as Arabic and Hebrew, need the vowel marks and diacritics that make words decodable, especially when text is read aloud by software.
- **Visual presentation.** People with dyslexia, language impairments, or memory impairments need small chunks of content separated by white space so a page is not overwhelming.
- **Math concepts.** People who do not process numerical concepts, such as people with dyscalculia, need words or other alternatives to percentages, quantities, and calculations.

## Patterns W3C lists

- [Use clear words](https://www.w3.org/TR/coga-usable/#x4-4-1-use-clear-words-pattern): common words; explain or drop jargon, acronyms, and invented terms.
- [Use a simple tense and voice](https://www.w3.org/TR/coga-usable/#x4-4-2-use-a-simple-tense-and-voice-pattern): in English, usually present tense, active voice, addressed to the reader.
- [Avoid double negatives or nested clauses](https://www.w3.org/TR/coga-usable/#x4-4-3-avoid-double-negatives-or-nested-clauses-pattern): simple sentence structure.
- [Use literal language](https://www.w3.org/TR/coga-usable/#x4-4-4-use-literal-language-pattern): concrete terms; explain any metaphor or simile.
- [Keep text succinct](https://www.w3.org/TR/coga-usable/#x4-4-5-keep-text-succinct-pattern): short paragraphs with one topic, short sentences with one point, lists, short headings.
- [Use clear, unambiguous formatting and punctuation](https://www.w3.org/TR/coga-usable/#x4-4-6-use-clear-unambiguous-formatting-and-punctuation-pattern): formats for text, numbers, and symbols that reduce ambiguity.
- [Include symbols and letters necessary to decipher the words](https://www.w3.org/TR/coga-usable/#x4-4-7-include-symbols-and-letters-necessary-to-decipher-the-words-pattern): vowel marks and diacritics where the language needs them.
- [Provide summary of long documents and media](https://www.w3.org/TR/coga-usable/#x4-4-8-provide-summary-of-long-documents-and-media-pattern): a short, plain summary with the key words emphasized.
- [Separate each instruction](https://www.w3.org/TR/coga-usable/#x4-4-9-separate-each-instruction-pattern): one step at a time, none left out, numbered, with an if-then table for complex cases.
- [Use white spacing](https://www.w3.org/TR/coga-usable/#x4-4-10-use-white-spacing-pattern): space around text and objects so sections separate clearly.
- [Ensure foreground content is not obscured by background](https://www.w3.org/TR/coga-usable/#x4-4-11-ensure-foreground-content-is-not-obscured-by-background-pattern): plain backgrounds behind text; background sound that does not mask speech.
- [Explain implied content](https://www.w3.org/TR/coga-usable/#x4-4-12-explain-implied-content-pattern): spell out jokes, sarcasm, gestures, and emotions.
- [Provide alternatives for numerical concepts](https://www.w3.org/TR/coga-usable/#x4-4-13-provide-alternatives-for-numerical-concepts-pattern): words or visuals alongside numbers.

## WCAG criteria that touch it

Numbers, titles, and levels checked against the WCAG 2.2 Recommendation of 12 December 2024. Level AAA rows are not our target; they show how far WCAG reaches.

| SC | Title | Level | Entry | Overlap |
|---|---|---|---|---|
| 2.4.6 | Headings and Labels | AA | `wcag/sc-2.4.6-headings-and-labels.md` | Headings describe; says nothing about the words beneath them |
| 1.4.3 | Contrast (Minimum) | AA | `wcag/sc-1.4.3-contrast-minimum.md` | Text against its background, including over images |
| 1.4.12 | Text Spacing | AA | `wcag/sc-1.4.12-text-spacing.md` | Content survives a user increasing spacing; does not require spacing by default |
| 1.1.1 | Non-text Content | A | `wcag/sc-1.1.1-non-text-content.md` | Images that carry meaning have text alternatives |
| 3.1.3 | Unusual Words | AAA | no entry yet | A way to find definitions of idioms, jargon, and unusual words |
| 3.1.4 | Abbreviations | AAA | no entry yet | A way to find what an abbreviation stands for |
| 3.1.5 | Reading Level | AAA | no entry yet | Supplemental content or a simpler version when text is above lower secondary level |
| 3.1.6 | Pronunciation | AAA | no entry yet | A way to find pronunciation where meaning depends on it |
| 1.4.8 | Visual Presentation | AAA | no entry yet | Line length, spacing, and color choices for blocks of text |

## Where WCAG stops

Every WCAG criterion about the meaning of words (unusual words, abbreviations, reading level, pronunciation) is Level AAA. At A and AA, WCAG checks that text can be perceived, not that it can be understood. Nothing at our target requires plain words, short sentences, literal language, summaries, chunking, white space by default, or alternatives to numbers. That gap is why `docs/content-standards.md` exists and sets a house reading-level target of grade 8; this entry is the W3C reasoning behind it.

## How it is used

- **Content** applies it while writing, together with `docs/content-standards.md`: measure reading level, cut nested clauses and double negatives, explain idioms, summarize long pages.
- **Verify** reports under its Content heading, never under WCAG findings: a paragraph above the spec's reading-level target (likely, with the measured number); an idiom or metaphor left unexplained (manual review); a key figure given only as a percentage (manual review).
- **Consult** asks whether the audience in the spec includes readers who need an easy-read version or a summary.
