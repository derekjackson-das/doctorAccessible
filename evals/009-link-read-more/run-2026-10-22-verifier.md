# Verifier run, 2026-10-22, eval 009

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), given the file path, the index, the content standards, and the axe command, and told not to open `expected.md`, `RESULTS.md`, or any run file.

Result against `expected.md`: **pass**. One Definite finding covering all three links, SC 2.4.4 Link Purpose (In Context) (Level A), tier 1, sourced to the entry with F63 and F89 named, with descriptive text, enclosing-sentence context, or hidden text as fix directions and the warning that `aria-label` must keep the visible words (2.5.3). The agent said plainly that the `h2` above each link is not programmatic context. The content standards' link-text rule was cited as the same defect, not counted twice. Nothing from the must-not list. axe inside the agent: 0 violations, expected. No file modified.

## Report as returned (findings and scan)

### [Definite] Three "Read more" links with identical text go to different destinations
- Where: `input.html` lines 22, 27, 32 (`main article p a`)
- What: Each link's text is "Read more", each `href` differs, and the only text that distinguishes them is the `h2` above, which is not programmatically determined link context; the enclosing `p` holds nothing but the link itself.
- Criterion: WCAG 2.2 SC 2.4.4 Link Purpose (In Context) (Level A), tier 1
- Source: knowledge/wcag/sc-2.4.4-link-purpose-in-context.md (entry lists this exact pattern as Definite, with F63 and F89)
- Fix direction: Make the link text name the destination ("Read more about extended exam hours"), or complete the sentence inside the same paragraph so the context is programmatic, or add visually hidden text; `aria-label` is acceptable only if it still contains the visible words "Read more" (SC 2.5.3).

Noted and passing: landmarks and headings meet 2.4.1 by the entry's own reading; headings describe their sections (2.4.6); `lang`, descriptive title, focus outline, link contrast about 7:1.

Content: reading level grade 4.4; headings pass; link text fails standard 5, same defect as the finding; "PDFs" and "a.m." unexpanded, manual review.

Manual checks remaining: focus outline visible on each link; screen reader links list after the fix; destinations exist and titles match; 400% reflow; abbreviation judgment.

Automated scan: axe-core 4.14.0, 0 violations. Matches the entry's note that `link-name` checks only that a name exists.
