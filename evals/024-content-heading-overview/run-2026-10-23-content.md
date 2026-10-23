# Run 2026-10-23: content skill on eval 024

- Skill: `.claude/skills/content/SKILL.md` at commit 31a632b.
- Method: a general-purpose agent told to read `CLAUDE.md` and the skill, follow it, and answer the request in `text.md`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not applicable (text eval).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, SC 2.4.6 Headings and Labels (Level AA), tier 1, at likely, with the entry's reason (definite once a person confirms): present.
- Reported once, with the house standard named as context, not as a second finding: yes.
- Reading level: "not measured, no tool available", with words per sentence counted and marked unverified, no score invented, not called a pass: yes.
- Must not: nothing from the list. The `h1`, the levels, the list, and the wording were checked and not reported.

## The answer, as given

Spec used: `a11y-spec.md` at the repo root, as you gave it to me. The readers are Harvard staff and graduate students, on a work laptop or a phone. The content section keeps the house defaults from `docs/content-standards.md`, including the grade 8 reading level.

One finding: the heading. Everything else meets the standards.

```
WCAG finding:
WCAG 2.2 SC 2.4.6 Headings and Labels (Level AA), tier 1
Confidence: likely (wcag/sc-2.4.6-headings-and-labels.md: judgment is involved, so likely from the text alone; definite once a person reads the section and confirms the heading does not fit it)
Where: <h2>Overview</h2>
What: "Overview" does not say what the section holds, which is how to renew a library card online or at a desk, so someone skimming headings or moving by heading with a screen reader cannot tell what is here.
Content entry: knowledge/content/headings.md (house standard: docs/content-standards.md section 4 says "Overview" is not a heading; the source conflict with Digital.gov is named in the entry and the stricter house reading applies, principle 13)
Suggested rewrite: "How to renew your library card", or the shorter "Renew your card". Your choice.
```

I filed this once, under the criterion, and did not file it again as a house-standard miss (rule 2). The heading structure itself is fine: there is one `h1` that says what the page is, then an `h2`, with no skipped levels.

Reading level: not measured, because no tool is available. `tools/readability.py` does not exist yet, `textstat` is not installed on this machine, and I did not install anything. The result is unverified. I counted words per sentence instead, over the main content only, leaving out headings:
- "You can renew your library card online before it ends." 10 words
- "Each card lasts one year." 5
- "Sign in with your Harvard Key." 6
- "Choose "My account", then "Renew card"." 5
- "The new end date shows right away." 7
- "If your card has already ended, bring your Harvard ID card to any library desk." 15, the longest
- "Staff can renew it for you there." 7

That is 7 sentences, 55 words, about 8 words per sentence. The words are common and the sentences are in active voice. Nothing here is plainly long, so I have no reading-level finding to report. This is not a pass, and the target is still grade 8 from the spec.

Organization (`knowledge/content/organization.md`) is fine. The first sentence carries the point. The two steps are an ordered list. The fallback for a card that has already ended comes last, which is where a reader who needs it will look.

Before you ship: a person should read the section under the new heading and confirm it fits. That check makes the 2.4.6 finding definite or closes it.
