# Content: Reading level

- House standard: `docs/content-standards.md`, section 2. Default target: grade 8 or below by Flesch-Kincaid Grade Level over the main content.
- Sources:
  - W3C, WCAG 2.2 SC 3.1.5 Reading Level, Level AAA, W3C Recommendation 12 December 2024. https://www.w3.org/TR/WCAG22/#reading-level Tier 1, beyond our target. No entry yet.
  - W3C, "Understanding Success Criterion 3.1.5: Reading Level", updated 28 June 2026. https://www.w3.org/WAI/WCAG22/Understanding/reading-level.html Tier 2.
  - Digital.gov, "Principles of plain language", no date shown on the page; page metadata gives publication in September 2025; accessed 2026-10-23. https://digital.gov/guides/plain-language/principles Tier 3.
  - Readability formulas (Flesch-Kincaid Grade Level and similar), the row in `knowledge/SOURCES.md`, tier 3: a signal computed locally, never a pass on its own. The grade-level formula is from J. Peter Kincaid, Robert P. Fishburne Jr., Richard L. Rogers, and Brad S. Chissom, "Derivation of New Readability Formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel", Research Branch Report 8-75, Chief of Naval Technical Training, 1975, Table 3, report page 14. https://stars.library.ucf.edu/istlibrary/56/
- Related: `content/plain-language.md`, `coga/objective-3-clear-content.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

Reading level is not a Level A or AA requirement. A text above the spec's target is reported under the verifier's Content heading as **likely**, with the measured score, never definite and never a WCAG failure. A score at or below the target is not a pass on its own. A project's `a11y-spec.md` may change the target; the spec wins.

## What it is

An estimate of how much schooling a reader needs to follow a text, from a formula that counts sentence length and word length (syllables per word). The house default is Flesch-Kincaid Grade Level 8 or below. SC 3.1.5, Level AAA, uses a related bar: if text needs more than lower secondary education, which the Understanding page puts at no more than nine years of school, provide a simpler version or a summary (W3C).

## Why it matters

Text above that level, the Understanding page explains, is a severe obstacle for people with reading disabilities, and hard too for readers with no disability who finished upper secondary school. A score is a quick way to notice that a text may be one of them.

## Limits, and a conflict between sources

- **The formula does not measure clarity.** It counts lengths; short sentences full of jargon pass it (house standard, section 2).
- **Digital.gov rejects a blanket grade 8.** It says to write for the readers' own knowledge, and not to write for an 8th-grade class when the readers are, for example, doctoral students, people who run small businesses, or parents at work. The house standard keeps grade 8 as its default. Following principle 13, both are named and the stricter reading, the house default, applies unless a project's spec sets a different target for its readers and says why (house standard, section 2).
- **Multilingual pages.** The Understanding page says to measure, on full sentences, each language that is 5% or more of the content, and judge the page by the worst result.

## How to do it

Write short sentences and common words (`content/plain-language.md`). Where a text must stay complex, such as a legal notice, add a plain summary at the top. The Understanding page names a text summary at the lower secondary level as one way to meet SC 3.1.5 (technique G86).

## How to check it

1. Take the main content only: leave out navigation, headings, code, and, where practical, proper nouns (house standard).
2. Compute Flesch-Kincaid Grade Level with `tools/readability.py` (roadmap 4.7). It uses the formula as printed in Kincaid et al. (1975), counts syllables by rule (an estimate per word, checked against hand counts on three samples in `tools/test_readability.py`), sees only the text in the file (content a script adds at run time is missed), and warns below 100 words. If it cannot run, use a named, versioned tool run locally, and name it. A formula the reviewer writes on the spot is an estimate, marked unverified. Do not install anything without asking. If no tool is available, say "not measured", count the words per sentence and point out long sentences and long words, and mark the result unverified.
3. Report the number, the tool, and the target. Then read the text: a score is a reason to read, not a verdict.
