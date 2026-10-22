# Verifier run, 2026-10-22, eval 001, registered agent

Blind run through the registered `verifier` agent (`.claude/agents/verifier.md` at commit 6a54d17). The session was launched after the agent file existed, so this is the first run that tests the agent wiring, not only the prompt. The agent was given the file path, the index, the content standards, and the axe command, and told not to open `expected.md`, `RESULTS.md`, or any `run-*.md`.

Result against `expected.md`: **pass**. One definite finding, SC 4.1.2 Level A tier 1, sourced to the knowledge entry, at `input#q`, with fix directions from the entry (H44 label, or `aria-labelledby`). SC 1.3.1 and 3.3.2 cross-referenced as "no entry yet", unverified, not reported as findings. The shared word "Search" on label and button raised as manual review. Nothing from the must-not list appeared. No file was modified. axe ran inside the agent and returned the same single `label` violation as the CLI baseline.

Observations for the agent prompt, no change made:

1. The agent again stated numbers from memory in its pass list, this time computed contrast ratios for the focus outline and body text. The rule forbids criterion numbers, titles, and levels from memory; it does not cover thresholds or computations. Same observation as the previous run.
2. In the manual checks it wrote what a screen reader is "expected" to announce before and after the fix. Framed as a test expectation rather than a simulation, but close to the rule against saying what a user would experience. Worth a look when the prompt is next tightened.

## Report as returned

## Checked
One local HTML file: `evals/001-missing-label/input.html` (28 lines, a single-field site search form). Checked by both reading the full source and running axe. No `a11y-spec.md` exists at the repo root or in `docs/`, so there is no project spec; the check is against WCAG 2.2 AA alone plus the house content standards in `docs/content-standards.md`. The knowledge library has one entry, SC 4.1.2; every other criterion mentioned below is marked "no entry yet" and unverified. I did not open `expected.md`, `RESULTS.md`, or any `run-*.md`.

## Findings

### [Definite] Search text input has no accessible name
- Where: `evals/001-missing-label/input.html` line 22, `input#q` (`<input type="text" id="q" name="q">`)
- What: The input has no `label` element, no `aria-label`, no `aria-labelledby`, and no `title`; the visible word "Search" on line 21 is a plain `<span>` sitting beside the input with no programmatic association, so the control exposes no name.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1, W3C Recommendation 12 December 2024
- Source: `knowledge/wcag/sc-4.1.2-name-role-value.md` (section "How it fails in code", first bullet: a text input with none of those attributes, where adjacent visible text does not count unless associated, is Definite)
- Confirmed by axe-core 4.14.0 rule `label`, impact critical, target `#q`, tagged `wcag2a` and `wcag412`.
- Fix direction: Make the existing visible "Search" text the label by turning the span into a `<label for="q">` (Technique H44, tier 2, listed as sufficient in the entry), or associate it with `aria-labelledby` (ARIA16) if the markup must stay a span.
- Related, not a separate finding: the entry notes SC 1.3.1 Info and Relationships is often cited alongside for unassociated labels (no entry yet, unverified: https://www.w3.org/TR/WCAG22/#info-and-relationships). SC 3.3.2 Labels or Instructions is about whether a label exists at all; a visible one does, so I am not reporting it (no entry yet, unverified).

No other defects found. Checked and clean from code, with the caveat that the criteria below have no knowledge entry and are cited unverified:
- `lang="en"` declared on `html`; `<title>Site search</title>` present and matches the `h1`.
- `header` and `main` landmarks present; one `h1`, no skipped levels.
- Submit control is a native `button` with text content "Search"; name and role come from HTML.
- No `tabindex`, no scripting, no custom widgets, so DOM order is the focus order.
- `:focus-visible` outline is 3px solid `#005a9c` with 2px offset. Computed contrast of `#005a9c` against the white background is about 7.1:1.
- Body text `#1a1a1a` on `#fff` computes to about 17:1.
- Viewport meta does not set `maximum-scale` or `user-scalable=no`.
- No images, links, media, motion, or dynamic content.

## Content
- Reading level: not measured. The main content contains one word ("Search") and a one-word button; there is no body text to run a Flesch-Kincaid formula over. The house default (grade 8 or below, content-standards.md section 2) is not testable on this page.
- Headings (section 4): one `h1`, "Site search", describes the page and matches the `title`. Meets the standard.
- Link text (section 5): no links on the page. Not applicable.
- Alt text (section 6): no images. Not applicable.
- Error messages and instructions (section 7): no error handling and no instructions. The label text "Search" precedes the field, which is the required order. Whether a single-word label is enough instruction for this field is a judgment call: manual review.
- Language (section 8): page language declared. No foreign-language passages, no abbreviations.
- Note on wording: the visible label and the button both read "Search". Not a defect under any criterion I can cite, but the two identical strings side by side are worth a human glance for clarity. Manual review.

## Spec deviations
No `a11y-spec.md` found at the repo root or in `docs/`. Nothing to check against. No need statement exists for this page, so I cannot say whether it serves anyone; that is for the project owner.

## Manual checks remaining
1. Screen reader (the project's chosen AT; none is named without a spec): tab to the text field and confirm what name, if any, is announced. Expected before fix: role "edit text" with no name. After fix: "Search, edit text".
2. Keyboard only: Tab through the page and confirm focus lands on the input, then the button, and that the blue outline is visible on both against the white background and against the controls' own backgrounds.
3. Submit the form with Enter from the text field and from the button; confirm both work and that `/search?q=...` is the destination. Then check whether the results page (not provided) announces that results loaded.
4. Speech recognition (for example Dragon or Voice Control): say "click Search" and confirm whether the input or the button is targeted; two visible "Search" strings may make the voice command ambiguous.
5. 200% browser zoom and 320px-wide viewport: confirm the flex row wraps or scrolls without clipping the input or button (reflow has no entry yet; unverified).
6. Windows High Contrast / forced-colors mode: confirm the focus outline remains visible, since it is drawn in a fixed color.

## Automated scan
axe-core 4.14.0 via `@axe-core/cli`, run in chrome-headless on `file://.../evals/001-missing-label/input.html`.
- Violations: 1. Rule `label` ("Ensure every form element has a label"), impact critical, 1 node, target `#q`, tags include `wcag2a`, `wcag412`, `cat.forms`. Rule reference: https://dequeuniversity.com/rules/axe/4.14/label
- Passes: 21. Incomplete (needs review): 0. Inapplicable: 68.
- axe's own notice: it detects an estimated 20 to 50 percent of issues; manual testing is still required. The axe rule-to-criterion mapping is tier 3 and was checked against the 4.1.2 entry's note on automated coverage, which says axe finds a missing name reliably.
