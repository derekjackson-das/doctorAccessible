# Run 2026-10-23: verifier on eval 036, with the readability tool

- Why: WP 4.7 done-when, as for eval 033.
- axe: given, 0 violations, default and WCAG 2.2-tagged.
- Result: **pass.** One definite finding naming SC 2.1.1 and SC 4.1.2 (Level A), tier 1, in one finding; nothing from the must-not list. **Content section: grade 10.5 from `readability.py 1.0`, over `<main>`, 11 words, 3 sentences, 23 syllables, above the house default of 8, reported as manual review, not a finding.** The run noted that proper nouns ("Elinor Ostrom", "Widener Library") drive the score; the tool does not remove proper nouns, which is a stated limit.
