# Eval 023: a paragraph far above the grade 8 target

Input: `text.md`. A transcript eval for the `content` skill: one section of a conference-travel page, a descriptive heading over one paragraph of reimbursement rules, with a spec that keeps the house grade 8 reading level and no readability tool in the repo.

Intended defect: the paragraph reads far above grade 8. It is 74 words in 3 sentences, about 25 words a sentence, built from long Latinate words ("contingent", "substantiating", "subsequent", "necessitate") and hidden verbs ("the submission of documentation", "initiate a reconsideration procedure"), in the passive ("are communicated"). Measured for this answer key with textstat 0.7.13, `flesch_kincaid_grade`: 26.4. Everything else is clean: the heading describes the section, there are no links or images, and the page language is not in question.

## Expected findings

1. **[Likely]** The paragraph reads well above the spec's grade 8 target.
   - Standard: `docs/content-standards.md` section 2, kept by the spec's content section. A house-standard finding, not a WCAG failure.
   - Content entry: `knowledge/content/reading-level.md`, with `knowledge/content/plain-language.md` for the fixes.
   - Measurement: with no tool in the repo, the answer says the reading level was not measured by a tool, or names the tool it used. If it gives a grade, it names how it got it; if it estimates, it marks the estimate unverified. Either way it reports the sentence length (about 25 words a sentence) or points out the longest sentences and the long words.
   - Where: the paragraph under "How to claim back your conference fee".
   - Acceptable fix directions: short sentences with one idea each, active voice, common words ("you must send", "within 30 days", "after"), verbs instead of hidden verbs, and possibly a list of what to send. Offered as a suggestion the writer can take or leave.

## Also acceptable

- A note that SC 3.1.5 Reading Level is Level AAA, beyond the target, marked "no entry yet" (there is no `wcag/` entry for it), whether or not the content entry is named as where it came from.
- A suggested rewrite of the paragraph, clearly offered as a suggestion.
- A note that the formula counts lengths, not clarity, so a person should still read the rewrite.

## Must not

- Report the paragraph as a WCAG failure, or as definite.
- Invent a precise score with no tool named, or present a grade worked out by hand as measured.
- Call the score, or any rewrite's score, a pass on its own.
- Report the heading, which describes its section.
- Speak as, or for, a reader with a disability.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Replace the writer's text without offering it as a suggestion.

## Pass condition

Finding 1 is present as likely, under the house standard and not WCAG, with an honest account of how reading level was or was not measured, and nothing from the Must not list appears.
