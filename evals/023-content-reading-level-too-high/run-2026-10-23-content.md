# Run 2026-10-23: content skill on eval 023

- Skill: `.claude/skills/content/SKILL.md` at commit 31a632b.
- Method: a general-purpose agent told to read `CLAUDE.md` and the skill, follow it, and answer the request in `text.md`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not applicable (text eval).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, house standard sections 2 and 1, likely, not a WCAG failure: present.
- Measurement: "not measured: no tool available", no score invented, nothing worked out by hand presented as a grade; sentence lengths given (32, 21, 21; about 25 words a sentence), long words and hidden verbs named, marked unverified: yes.
- SC 3.1.5 named as Level AAA, beyond the target, "no entry yet": yes.
- Rewrite offered as a suggestion; text not changed: yes.
- Must not: nothing from the list. The heading was checked and not reported.

Observation: the answer added a second finding at manual review on organization (the task buried in one paragraph, no contact details). The key neither expects nor forbids it, and it is graded correctly as manual review. Its summary of Digital.gov's grade 8 point names only expert readers; the entry gives a wider list.

## The answer, as given

I'd hold this paragraph before you ship. It doesn't fail WCAG 2.2 AA, but it misses the house standards your spec keeps. I used `a11y-spec.md` at the repo root. Its content section keeps the `docs/content-standards.md` defaults, so the target is grade 8 by Flesch-Kincaid Grade Level. The readers are Harvard staff and graduate students on a work laptop or a phone.

**Reading level not measured: no tool available.** `tools/readability.py` doesn't exist yet (roadmap 4.7), and no versioned readability tool is installed here. I didn't install one or work out a score by hand. The counts below are word counts (from `wc -w`), not a grade level.

**WCAG findings:** none. The heading "How to claim back your conference fee" says what the section covers, and there are no links, images or form fields. No Level A or AA criterion sets plain language or reading level (`knowledge/content/plain-language.md`). The criterion that does, SC 3.1.5 Reading Level, is Level AAA, outside our target, and has no entry yet.

```
Content finding (house standard, not a WCAG failure):
Standard: docs/content-standards.md section 2 (reading level, grade 8 target kept by the spec) and section 1 (plain language)
Confidence: likely (unverified: reading level not measured, no tool available)
Where: the whole <p>. Sentence 1, "Eligibility for reimbursement ... the conclusion of the event.", has 32 words. Sentence 2, "Applications submitted following the expiration ... prior to consideration.", has 21. Sentence 3, "Reimbursement determinations are communicated electronically ... the administrative office.", has 21. That is 74 words in 3 sentences, about 25 words per sentence.
What: The sentences are long and the words are long and abstract, so this text is very likely above the grade 8 target. Many long words: eligibility, reimbursement, expenditures, contingent, documentation, substantiating, subsequent, necessitate, supplementary, determinations, reconsideration. Hidden verbs: "submission of", "expiration of", "conclusion of", "prior to consideration". Passive voice: "are communicated", "are declined". None of it says who does what.
Content entry: knowledge/content/reading-level.md, knowledge/content/plain-language.md
Suggested rewrite (your choice):
  "To get your conference fee back, send us your receipts and proof that you attended. Send them within 30 days after the conference ends.
   If you send them later, your department administrator must approve your claim first. You will need to explain why it is late.
   We will email you our decision. If we say no, you can ask us to look again. Contact the administrative office to do this."
```

```
Content finding (house standard, not a WCAG failure):
Standard: docs/content-standards.md section 3 (organization)
Confidence: manual review
Where: the whole <p>
What: The reader's task (what to send, by when, what happens if they are late or refused) is packed into one dense paragraph that is hard to scan on a phone. The first sentence opens with "Eligibility" rather than the action. The two places the reader is pointed to (the departmental administrator and the administrative office) come with no contact details.
Content entry: knowledge/content/organization.md
Suggested rewrite (your choice): start with the action and the 30-day deadline. Put the two things to send in a real <ul> ("itemized receipts", "proof that you attended"). Give the late and declined cases their own short sentences. Add how to reach the administrative office, for example a link that names it.
```

**Sources disagree on grade 8 for these readers.** Digital.gov (tier 3) advises against a blanket grade 8 for expert readers and gives doctoral students as an example. The house default (`docs/content-standards.md` section 2) and principle 13 take the stricter reading, and your spec keeps grade 8, so that target applies here. Either way, the sentence lengths and hidden verbs make this hard going even for graduate readers.

**Left for a person to test.** Get a score with a named tool once one is available. Then ask someone who wasn't involved in writing it to say back what to send, by when, and what to do if refused (paraphrase testing, `knowledge/content/plain-language.md`).

I haven't changed your text; these rewrites are suggestions.
