# Run 2026-10-23: content skill on eval 026

- Skill: `.claude/skills/content/SKILL.md` at commit 31a632b.
- Method: a general-purpose agent told to read `CLAUDE.md` and the skill, follow it, and answer the request in `text.md`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not applicable (text eval).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, house standard section 6, likely, not a WCAG failure, with WebAIM tier 3 as the source of the "image of" point: present.
- SC 1.1.1 (Level A) explained as met: yes.
- Reported once: yes.
- Also acceptable, used: a manual-review note that a person who knows the photo's purpose should confirm it, with `alt=""` named as the choice if it is only for mood, without calling the current alt a failure.
- Reading level: "not measured, no tool available", marked unverified, not a score: yes.
- Must not: nothing from the list.

## The answer, as given

I reviewed the "Study spaces" section against your `a11y-spec.md`. Its content section keeps the house defaults from `docs/content-standards.md`, including the grade 8 reading level, so those are the standards I used. The readers are Harvard staff and graduate students, on a work laptop or a phone.

There is one finding, and it is not a WCAG failure. The alt text does its job (WCAG 2.2 SC 1.1.1 Non-text Content, Level A, W3C Rec 12 Dec 2024, tier 1, `knowledge/wcag/sc-1.1.1-non-text-content.md`). It just misses the house wording rule.

Content finding (house standard, not a WCAG failure):
Standard: docs/content-standards.md section 6
Confidence: likely
Where: `alt="Image of rows of wooden desks under tall windows"`
What: The alt starts with "Image of", which the house standard rules out. WebAIM's point is that screen readers already say it is an image (WebAIM, "Alternative Text", updated 19 Oct 2021, tier 3).
Content entry: knowledge/content/alt-text.md
Suggested rewrite: `alt="Rows of wooden desks under tall windows"`. This is only a suggestion; the wording is yours.

The rest of the section:
- **Alt text purpose (manual review, no finding):** The alt describes the room, and the paragraph doesn't repeat it: the paragraph says "quiet desks" and "a view of the yard", the alt says "wooden desks" and "tall windows". A person who knows what the photo is for on this page should confirm it shows what the reader needs. If it is only for mood, `alt=""` is the other choice.
- **Heading (no finding):** "The reading room" describes what the section covers. That meets the house standard in section 4 (`knowledge/content/headings.md`). The snippet alone doesn't show the page's `h1` or the heading levels, so check those on the full page.
- **Reading level: not measured, no tool available.** `tools/readability.py` doesn't exist, and no local readability library is installed. Word counts per sentence are 8, 15 and 10, and the words are common. Nothing looks plainly above grade 8, so there is no finding. This is unverified, not a score.

Still for a human to check: compare the alt against the actual photo, and read the section in context on the full page.
