# Eval 025: a link that says "click here"

Input: `text.md`. A transcript eval for the `content` skill: a "What workshops cost" section with one paragraph holding one link.

Intended defect: the link text is "click here". The sentence it sits in, "For the full fee schedule, click here.", completes its purpose, so it meets SC 2.4.4 through the enclosing sentence (technique G53, in the 2.4.4 entry). It still misses the house standard: out of context, in a screen reader's list of links, "click here" says nothing. Everything else is clean: the heading describes the section, and the text is plain (textstat 0.7.13 `flesch_kincaid_grade` 0.8).

Eval 009 tests generic link text with no completing context, which fails 2.4.4. This eval tests the other side of that line.

## Expected findings

1. **[Likely]** The link text "click here" does not say where the link goes.
   - Standard: `docs/content-standards.md` section 5. A house-standard finding, not a WCAG failure.
   - Content entry: `knowledge/content/link-text.md`.
   - WCAG: the answer says SC 2.4.4 Link Purpose (In Context) (Level A) is met, or likely met, because the enclosing sentence completes the purpose, citing `knowledge/wcag/sc-2.4.4-link-purpose-in-context.md`.
   - Where: `<a href="/workshops/fees">click here</a>`.
   - Acceptable fix directions: make the destination the link text, for example "See the <a>full fee schedule</a>." Offered as a suggestion.

## Also acceptable

- A note that SC 2.4.9 Link Purpose (Link Only) is Level AAA, beyond the target, which this link would not meet.
- Stating the finding as a 2.4.4 cross-reference rather than a separate WCAG finding.

## Must not

- Report the link as a definite SC 2.4.4 failure.
- Report it twice, under WCAG and under the house standard.
- Report the heading, the reading level, or the other sentences.
- Speak as, or for, a reader with a disability.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Replace the writer's text without offering it as a suggestion.

## Pass condition

Finding 1 is present as likely under the house standard, with 2.4.4 explained as met by the sentence's context and not reported as a failure, and nothing from the Must not list appears.
