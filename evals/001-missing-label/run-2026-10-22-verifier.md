# Verifier run, 2026-10-22, eval 001

Blind run. The agent was given the file path, the index, the content standards, and the axe command. It was told not to open `expected.md` or `RESULTS.md`.

Caveat: the `verifier` agent was created during the session that ran this, and Claude Code registers project agents at launch, so it was not available by name. The run used a general-purpose agent with the body of `.claude/agents/verifier.md` as its instructions. This tests the prompt, not the agent wiring. Package 1.6 onboarding runs should use the registered agent.

Result against `expected.md`: **pass**. One definite finding, SC 4.1.2 Level A tier 1, sourced to the knowledge entry, at `#q`, with a fix direction from the entry. Related criteria 1.3.1 and 3.3.2 were cross-referenced as "no entry yet" with W3C URLs, not reported as findings. The shared word "Search" on label and button was raised as manual review. Nothing from the must-not list appeared. No file was modified.

Observation for the agent prompt: in its list of things it found no problem with, the agent stated the contrast minimum as a number from memory. Nothing in the rules forbids that for an observation of a pass, but principle 3 would. Consider tightening the rule to cover thresholds, not only criterion numbers.

## Report as returned

## Checked
Given: one local HTML file, `evals/001-missing-label/input.html` (28 lines: a page titled "Site search" with a `header` holding an `h1`, and a `main` holding a GET form with a `span`, a text `input`, and a submit `button`; inline CSS only, no JavaScript, no images, no links).

Checked by both: axe-core CLI run as instructed, and a full read of the markup and CSS.

Project spec: none. Looked for `a11y-spec.md` at the repo root, in `docs/`, and beside the page; none exists. Checked against WCAG 2.2 AA alone.

Knowledge base: `knowledge/INDEX.md` lists one entry, `wcag/sc-4.1.2-name-role-value.md` (verified 2026-10-22). Read before citing. The index records 1.3.1, 3.3.2, 2.4.6, 2.1.1, 2.4.3, 2.4.7, 1.4.3, and 1.1.1 as gaps with no entry yet.

## Findings

### [Definite] Search text input has no accessible name
- Where: `input.html` line 22, `<input type="text" id="q" name="q">` (selector `#q`)
- What: The text input has no `label` element associated with it, no `aria-label`, no `aria-labelledby`, and no `title`; the visible word "Search" on line 21 sits in a plain `<span>` beside the input and is not programmatically associated with it, so no accessible name is exposed.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
- Source: `knowledge/wcag/sc-4.1.2-name-role-value.md`, which lists exactly this pattern under "How it fails in code".
- Fix direction: Turn the existing visible "Search" text into a `label` associated with the input (the entry points to technique H44 as the native-HTML route), so the name that is already on screen becomes the programmatic name.
- Related criteria, not reported as separate findings: the entry notes SC 1.3.1 Info and Relationships is often cited alongside for unassociated labels and that SC 3.3.2 Labels or Instructions covers whether a label exists at all. Neither has a knowledge entry yet, so they are not cited as findings; a visible label does exist, so the defect is association, which the 4.1.2 entry covers. Unverified W3C text: https://www.w3.org/TR/WCAG22/#info-and-relationships and https://www.w3.org/TR/WCAG22/#labels-or-instructions.

No other defects found on reading. Checked and found no problem with: `lang="en"`; a `title`; one `h1` matching the title; `header` and `main` landmarks; native `input` and `button`; a visible `:focus-visible` outline; body text #1a1a1a on #fff. Those last items (focus, keyboard, contrast) have no knowledge entry yet, so they are stated as observations rather than cited passes.

## Content
- Reading level: not measured. No measurement tool is installed, and the page has no body prose to measure. Its entire visible text is "Site search", "Search", and "Search".
- Headings: one `h1`, "Site search", describes the page and matches the `title`. No skipped levels.
- Link text: no links. Alt text: no images. Error messages: no validation, no error state in the markup. The instruction text "Search" appears before the field.
- Language: `lang="en"` declared. No foreign-language passages, no abbreviations.
- Manual review: the visible label "Search" and the button text "Search" are the same word side by side. Not a defect under any standard listed; a human may want to judge whether the label would read better as a noun phrase that distinguishes the field from the button.

## Spec deviations
No `a11y-spec.md` exists for this page. Checked against WCAG 2.2 AA alone.

## Manual checks remaining
1. Confirm with a screen reader that the input announces a name and role and that the button announces its name and role; the project's AT list is not defined, since there is no spec.
2. Tab through with a keyboard only and confirm the focus indicator is visible on both controls in the browsers the project supports.
3. Submit the form and check what the `/search` results page does, including whether focus and page title change meaningfully; that page was not given.
4. Check the rendered size of the submit button against SC 2.5.8 Target Size (Minimum), Level AA (no entry yet, unverified: https://www.w3.org/TR/WCAG22/#target-size-minimum). Rendered size depends on the user's font settings.
5. Zoom to 200% and 400% and confirm the `.row` flexbox does not clip or hide the input or button.

## Automated scan
axe-core 4.14.0 via `@axe-core/cli`, chrome-headless. Result: 1 violation. Rule `label`, 1 occurrence, at `#q`. Rule reference: https://dequeuniversity.com/rules/axe/4.14/label. Corresponds to the Definite finding above.

No files were modified. `expected.md` and `RESULTS.md` were not opened.
