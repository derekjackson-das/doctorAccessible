# Run 2026-10-23: content skill on eval 025

- Skill: `.claude/skills/content/SKILL.md` at commit 31a632b.
- Method: a general-purpose agent told to read `CLAUDE.md` and the skill, follow it, and answer the request in `text.md`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not applicable (text eval).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, house standard section 5, likely, not a WCAG failure: present.
- SC 2.4.4 (Level A) explained as met through the enclosing sentence, G53, from the 2.4.4 entry; not reported as a failure: yes.
- Reported once: yes.
- Reading level: "not measured, no tool available", words per sentence counted and marked unverified, not called a pass: yes.
- Must not: nothing from the list.

## The answer, as given

Spec read: `a11y-spec.md` at the repo root. Its content section keeps the house defaults from `docs/content-standards.md`, so the house standards apply here unchanged. The readers are Harvard staff and graduate students, on a work laptop or a phone.

There is no WCAG failure. There is one house-standard finding.

**Why the link passes SC 2.4.4.** `knowledge/wcag/sc-2.4.4-link-purpose-in-context.md` gives WCAG 2.2 SC 2.4.4 Link Purpose (In Context) as Level A, tier 1. Context counts there when it is in the same paragraph or sentence. Here the link sits in the sentence "For the full fee schedule, click here." That sentence says where the link goes, which is technique G53 (tier 2). So the purpose can be worked out from the link text plus its context, and it passes. `knowledge/content/link-text.md` says that case is reported as a house-standard miss, not as a WCAG failure.

```
Content finding (house standard, not a WCAG failure):
Standard: docs/content-standards.md section 5 (Links), kept by the spec's content section
Confidence: likely
Where: "For the full fee schedule, <a href="/workshops/fees">click here</a>."
What: The link text "click here" does not say where the link goes on its own; it passes SC 2.4.4 only because the sentence explains it, and the house standard asks for link text that makes sense out of context.
Content entry: knowledge/content/link-text.md
Suggested rewrite (your choice): "See the <a href="/workshops/fees">full workshop fee schedule</a>." or "<a href="/workshops/fees">Workshop fees for guests</a> are listed by session." Either way the destination words sit inside the link, and "click", which suits a mouse more than a phone, goes away.
```

**Reading level not measured: no tool available.** The repo has no `tools/readability.py`, and nothing else is installed locally (`textstat` is not on this machine). I installed nothing, so there is no Flesch-Kincaid score. The target is grade 8, the house default kept by the spec. Counted by hand, and unverified:
- "Workshops are free for staff and students." 7 words
- "Guests pay a small fee to cover lunch." 8 words
- "For the full fee schedule, click here." 7 words
- "You can pay by card when you sign up." 9 words

Every sentence is short and uses common words, and there are no technical terms. Nothing here is plainly long, so I have no reading-level finding. This is a signal, not a pass.

**Also checked, no finding:**
- **Heading.** "What workshops cost" describes the section under it (`knowledge/content/headings.md`, house standard section 4).
- **Order.** The paragraph puts its main point first: free for staff and students.

**Manual check before shipping.** Pull up the page's list of links in a screen reader. Confirm that the new link text says where it goes when heard on its own, and that no other link on the "Workshops" page uses the same text for a different place.
