# Verifier run, 2026-10-22, eval 002

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), given the file path, the index, the content standards, and the axe command, and told not to open `expected.md`, `RESULTS.md`, or any run file.

Result against `expected.md`: **pass**. One Definite finding, SC 1.1.1 Non-text Content (Level A), tier 1, sourced to the entry, at `main > img`, with H37 and H67 as fix directions. Whether the image is informative or decorative was raised as manual review, as the key allows. Nothing from the must-not list. axe inside the agent: one violation, `image-alt`. No file modified.

Observation: the agent wrote a small Flesch-Kincaid script in the scratchpad to measure reading level, and said so. Useful; package 4.7 would make it a repo tool.

## Report as returned (findings and scan)

### [Definite] Image has no `alt` attribute
- Where: `input.html`, line 20, selector `main > img`
- What: The `img` element (an SVG data URI drawing a gray rectangle with a building-roof outline) has `src`, `width`, and `height` but no `alt` attribute at all, so it has no text alternative and is not marked as something assistive technology may ignore.
- Criterion: WCAG 2.2 SC 1.1.1 Non-text Content (Level A), tier 1. The entry lists "An `img` with no `alt` attribute at all" as Definite, failure technique F65 (tier 2).
- Source: knowledge/wcag/sc-1.1.1-non-text-content.md
- Fix direction: Decide what the drawing is for in this context and either give it an `alt` that states that purpose (Technique H37) or, if it carries nothing the text does not already say, give it `alt=""` so it is skipped (Technique H67). Which of the two is correct is a content judgment.

No other defects found. Checked and passing from code: text contrast (body 17.40:1, link 7.14:1, both set with their backgrounds); link underlined, not color alone; `lang="en"`, `title`, one `h1`, `header` and `main`, viewport allows zoom, `:focus-visible` outline defined.

Content: reading level measured at Flesch-Kincaid grade 1.5 with a script written for the run. Heading matches the title. Link text "See weekend hours" says where it goes. Alt text fails section 6; empty or descriptive is manual review. "ID" unexpanded raised as a judgment call.

Manual checks remaining: decide the image's purpose; screen reader confirmation after the fix; keyboard focus on the link; 400% reflow; follow the link in deployment.

Automated scan: axe-core 4.14.0, 1 violation, rule `image-alt`, selector `img`. Same defect as the finding, not an additional one.
