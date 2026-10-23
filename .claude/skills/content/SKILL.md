---
name: content
description: The writing mode. Use when writing, editing, or reviewing words on a page - body text, headings, link text, alt text, form instructions and error messages, and language markup. Applies docs/content-standards.md and the spec's content section, measures reading level as a signal, and maps each question to a knowledge entry. House-standard findings are likely or manual review, never definite.
---

# Content

This skill is a map and a set of rules. The standards are in `docs/content-standards.md`; the reasoning and methods are in `knowledge/content/`, which rests on `knowledge/wcag/` where a criterion applies. The rules for citing are in the `wcag` skill and apply here unchanged.

## When this applies

Any change or review that adds or edits words a reader will see or hear: page copy, headings, links, buttons, image `alt`, form labels, instructions and errors, notices, and the page's language. Words are part of the build (principle 16).

## Before writing or reviewing

1. Read the project's `a11y-spec.md` (repo root, then `docs/`). Find its content section: who the readers are, the reading-level target, and any standard it tightens or overrides. The spec wins over the house defaults; say so when it does.
2. No spec, or no content section: use `docs/content-standards.md` as written, and say that the house defaults were used.
3. Note who the reader is. The right words depend on it (`content/plain-language.md`).

## Rules

1. **WCAG failures and house-standard misses are separate.** Where text fails a Level A or AA criterion, report it once, under the criterion, at the confidence the `wcag/` entry gives, and name the content entry as context. Where it meets WCAG but misses the house standard or the spec, report it as likely or manual review, never definite, and never as a WCAG failure.
2. **One finding per defect.** Where the `wcag/` entry already covers a defect, report it there and name the house standard as context; do not file it twice.
3. **Reading level is a signal, not a verdict.** Never report a score as a pass, and never as a WCAG failure; `content/reading-level.md` says why.
4. **Measure, do not guess.** A grade level is computed, with the tool named. A number from memory or a feeling is not a measurement.
5. **Suggest, do not replace.** Offer a rewrite as a suggestion the writer can take or leave. Never silently change their words (principle 8).
6. **Never speak for readers with disabilities.** Say what the sources say and what a human should test (principle 7).
7. Never state a criterion number, title, or level from memory. Open the entry. If there is none, say "no entry yet" and mark the claim unverified.

## Measuring reading level

1. Take the main content only: no navigation, headings, code, or, where practical, proper nouns.
2. Compute Flesch-Kincaid Grade Level with `python tools/readability.py <file> --target <spec target>`. It keeps the main content, leaves out navigation, headings, and code, and says what it left out; for a Markdown file with `html` fences it measures only the fences. If it cannot run, use a named, versioned tool that runs locally, and name it with its version. A formula written on the spot is an estimate: mark it unverified. Do not install anything without asking.
3. **No tool available:** say "reading level not measured: no tool available". Count words per sentence, point out the longest sentences and the long or technical words, and mark the result unverified. Do not invent a score.
4. Report the score, the tool, and the target from the spec or the house default. Then read the text, because the formula counts lengths, not clarity.
5. Above the target: likely, with the score. Not measured but plainly long: likely, unverified, with the sentence lengths. The spec may set a different target for its readers; the source conflict on grade 8 is named in `content/reading-level.md`.

## Where to look

| Question | Read |
|---|---|
| Is this clear? Sentences, voice, words, paragraphs | `knowledge/content/plain-language.md` |
| How hard is it to read, and how is that measured | `knowledge/content/reading-level.md` |
| What comes first, how it is chunked, lists and tables | `knowledge/content/organization.md` |
| Does each heading say what its section holds | `knowledge/content/headings.md` |
| Does each link say where it goes | `knowledge/content/link-text.md` |
| Is this the right alt text, or should it be empty | `knowledge/content/alt-text.md` |
| Labels, instructions, error messages | `knowledge/content/error-messages.md` |
| Page language, other languages, abbreviations | `knowledge/content/language.md` |
| Readers with cognitive and learning disabilities | `knowledge/coga/` |
| The criteria themselves | `knowledge/INDEX.md`, then the `wcag/` entry |

## Output shape for a finding

```
WCAG finding:
WCAG 2.2 SC x.x.x Title (Level A or AA), tier 1
Confidence: definite | likely | manual review (from the wcag/ entry)
Where: <selector, file:line, or the quoted text>
What: <one sentence>
Content entry: knowledge/content/<topic>.md
Suggested rewrite: <the writer's choice>

Content finding (house standard, not a WCAG failure):
Standard: docs/content-standards.md section n, or the spec's content section
Confidence: likely | manual review
Where: <the quoted text>
What: <one sentence, with the measured score if there is one>
Content entry: knowledge/content/<topic>.md
Suggested rewrite: <the writer's choice>
```
