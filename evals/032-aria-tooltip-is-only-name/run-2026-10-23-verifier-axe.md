# Run 2026-10-23: the registered verifier runs axe itself on eval 032 (WP 4.1)

- Method: a fresh headless Claude Code session (`claude -p`, Claude Code 2.1.309, Windows) in the repo, asked to use the registered `verifier` agent on `evals/032-aria-tooltip-is-only-name/input.html` and told not to open `expected.md`, `evals/RESULTS.md`, or any run file, or edit files. Session tools: Read, Glob, Grep, Bash, PowerShell, Task, Agent. `DOCTOR_A11Y_NODE_DIR` pointed at a portable Node.js 24.22.1.
- Verifier at commit b1c4339 (tools now include PowerShell). An earlier attempt at e29455a, without PowerShell, had no shell and ran no axe; see the PR.
- axe: run by the verifier itself through `tools/axe.py`; raw output in the report below.

## The session's reply, as given

## Checked

- **Input:** `C:\Users\rua126\AppData\Local\Temp\claude\C--Users-rua126\cf68331b-fb24-46e9-a990-751e07481e93\scratchpad\repo\doctorAccessible\evals\032-aria-tooltip-is-only-name\input.html` (46 lines). It's a "Reading list" page with one citation and an icon-only download button. The button has a custom tooltip that a script shows on hover and focus.
- **How it was checked:** I read the whole file, ran axe through `tools/axe.py`, and ran `tools/readability.py`.
- **No spec:** there is no `a11y-spec.md` at the repo root or in `docs/`, so the check is against WCAG 2.2 AA and `docs/content-standards.md` only.
- **Files not opened:** `expected.md` and the `run-*.md` files, as you asked.

## Findings

### [Definite] Icon-only button has no accessible name; its only text is a description
- **Where:** `input.html` lines 23–26, `button.icon-btn[aria-describedby="tip-download"]`.
- **What:** The button has no text, `aria-label`, `aria-labelledby` or `title`, and its SVG is `aria-hidden="true"`. That leaves it with no accessible name. The words "Download citation file for reference managers" reach it only through `aria-describedby`, which supplies a description, not a name.
- **Criterion:** WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1. The entry lists "A button whose only content is an icon, image, or SVG with no accessible name" as definite. `aria/patterns/tooltip.md` lists this exact pattern as a definite 4.1.2 failure.
- **Overlap:** SC 2.5.3 Label in Name (Level A) lists "visible label text but no accessible name" as shared with 4.1.2 (F111). I report it once, here, as that entry directs.
- **Source:** `knowledge/wcag/sc-4.1.2-name-role-value.md`, `knowledge/aria/patterns/tooltip.md`, `knowledge/aria/accessible-name.md`, `knowledge/wcag/sc-2.5.3-label-in-name.md`.
- **Fix direction:** Give the button its own name that doesn't depend on the tip being shown. The options are visible text, `aria-labelledby` pointing at the tip, or an `aria-label` that contains the tip's visible words (so 2.5.3 holds).

### [Manual review] Tooltip hover, dismiss and persistence behaviour
- **Where:** `input.html` lines 13–14 and 32–42.
- **What the code shows:** Escape hides the tip, and there is no timer. The tip sits inside `.wrap`, so moving the pointer onto it shouldn't fire `mouseleave`. The transparent 0.5rem top border with `background-clip: padding-box` seems meant to bridge the gap between button and tip.
- **Why it's manual:** The entry says these three behaviours are observed by hovering, focusing and pressing Escape. Reading the code suggests it passes, but that isn't a verdict.
- **Criterion:** WCAG 2.2 SC 1.4.13 Content on Hover or Focus (Level AA), tier 1.
- **Source:** `knowledge/wcag/sc-1.4.13-content-on-hover-or-focus.md`.
- **Fix direction:** None unless testing shows the tip closes when the pointer moves onto it, or when Escape is pressed while hovering and then the mouse moves within it.

### [Manual review, best practice, not a WCAG finding] Touch users get the icon only
- **What:** The tip opens only on hover or focus. On touch, a tap activates the button straight away, so the tip text is never shown.
- **Source:** `knowledge/patterns/tooltip.md` (tier 2/3, Higley 2019). It says touch could not reach tooltips on buttons, and that showing the text, or using a toggletip, is the simpler alternative.
- **Status:** Advice only. Whether the down-arrow icon is clear enough on its own is for a person to judge.

### [Best practice, not a WCAG finding] A button used for navigation
- **Where:** `input.html` line 43.
- **What:** A click handler sets `window.location.href` to a `.ris` file, so a `<button>` is acting as a link to a download.
- **Fix direction:** Native HTML first (principle 5): a link with `href`, and possibly `download`, would expose that this goes somewhere and fetches a file. No criterion entry ties the current build to a failure.

### Checked and passing, from computed values
These are my computations from the declared hex colours and CSS, using the formula the entries refer to:

- **Button border and icon stroke:** `#005a9c` on `#fff`, about 7.1:1. That's at or above the 3:1 in `sc-1.4.11-non-text-contrast.md`.
- **Focus outline:** `#1a1a1a` on `#fff`, about 17.4:1. That's at or above 3:1 in the same entry.
- **Tooltip text:** `#fff` on `#1a1a1a`, about 17.4:1. That's at or above the 4.5:1 in `sc-1.4.3-contrast-minimum.md`.
- **Target size:** `2.75rem` square, which is 44 CSS px at the default 16px root. That's at or above the 24 by 24 in `sc-2.5.8-target-size-minimum.md`.
- **Other basics:** `lang="en"` is present, the title is "Reading list", the page has one `h1`, and the content is inside `main`.

## Content

- **Reading level:** `readability.py 1.0 (2026-10-23)` measured `<main>` and gave Flesch-Kincaid grade 7.6 against the house default target of 8 (there is no spec, so no project target).
  - What it counted: 5 words, 1 sentence, 9 syllables (estimated by rule).
  - What it left out: the button, the `h1`, the script, the span (the tooltip), and the style block.
  - The tool notes that under 100 words the score means little. It's a signal, not a pass.
- **Headings:** The single `h1`, "Reading list", says what the page is. It meets the headings standard.
- **Button name (the tooltip text):** "Download citation file for reference managers" says what the control does and that it fetches a file. The links standard asks for that, and this text meets it. It's right for the name once it is wired as one (see the Definite finding). Whether "reference managers" means anything to this site's readers is a manual review call.
- **Alt text:** The SVG is decorative inside a control and hidden correctly. The text alternative belongs to the button's name.
- **Error messages:** None on the page; not applicable.
- **Language:** `lang="en"` is declared. "RIS" appears only in the URL, not in the visible text.

## Spec deviations

No `a11y-spec.md` was found at the repo root or in `docs/`, so there is nothing to compare against.

## Manual checks remaining

1. **Accessibility tree:** In browser developer tools, inspect the button and record the computed name and description, and where each comes from.
2. **Keyboard only:**
   - Tab to the button. Record whether the focus outline is visible and whether the tip appears.
   - Press Escape. Record whether the tip hides while focus stays on the button.
   - Press Enter, then Space. Record what each one does.
3. **Mouse:**
   - Hover the button, then move the pointer slowly down onto the tip, including across the 0.5rem transparent band. Record whether the tip stays open.
   - Wait about 30 seconds while hovering. Record whether it stays.
   - Press Escape while hovering. Record the result.
4. **Touch:** On a phone or tablet, record whether the button's purpose can be learned before activating it.
5. **Screen reader** (NVDA with Firefox or Chrome, VoiceOver with Safari; the project has no spec naming AT): Move to the button by Tab and by the virtual cursor. Record exactly what is spoken for the name, the role and any description, with verbosity settings noted.
6. **Speech recognition** (if in scope): Try to activate the button by saying the words in its tip, and record the result.
7. **Zoom at 400% and reflow at 320 CSS px wide:** Record whether the `white-space: nowrap` tip is fully visible or clipped or causes horizontal scrolling. My reading is that it could overflow at narrow widths. I didn't open the 1.4.10 entry, so this is a lead, not a finding.
8. **Forced colours (Windows Contrast Themes):** Record whether the tip's background and edge stay distinguishable, and whether the button border and focus outline stay visible.

## Automated scan

- **Version and tags:** axe-core 4.14.0 via @axe-core/cli; tags `wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`.
- **Page:** `file:///C:/Users/rua126/AppData/Local/Temp/claude/C--Users-rua126/cf68331b-fb24-46e9-a990-751e07481e93/scratchpad/repo/doctorAccessible/evals/032-aria-tooltip-is-only-name/input.html`
- **Raw JSON:** `C:\Users\rua126\AppData\Local\Temp\doctor-a11y-axe\032-aria-tooltip-is-only-name-20261023-134502.json`
- **Violations: 1**
  - `button-name` (critical; tags `wcag2a`, `wcag412`), "Buttons must have discernible text", target `button`.
  - Failure summary: no visible inner text, no `aria-label`, no `aria-labelledby`, no `title`, no implicit or explicit `<label>`, and no `role="none"` or `role="presentation"`.
- **Incomplete:** 0
- **Passes:** 15 rules. **Inapplicable:** 48 rules.

Raw block as printed:
```
{
  "violations": [
    {
      "id": "button-name",
      "impact": "critical",
      "tags": ["wcag2a","wcag412"],
      "help": "Buttons must have discernible text",
      "helpUrl": "https://dequeuniversity.com/rules/axe/4.14/button-name?application=webdriverjs",
      "nodes": [{ "target": ["button"], "failureSummary": "Fix any of the following: Element does not have inner text that is visible to screen readers / aria-label attribute does not exist or is empty / aria-labelledby attribute does not exist, references elements that do not exist or references elements that are empty / Element has no title attribute / Element does not have an implicit (wrapped) <label> / Element does not have an explicit <label> / Element's default semantics were not overridden with role=\"none\" or role=\"presentation\"" }]
    }
  ],
  "incomplete": []
}
```

- **`button-name`:** supports the Definite finding, "Icon-only button has no accessible name" (SC 4.1.2).
- **What axe doesn't cover here:** axe has no rule for 1.4.13 or 1.4.11 (per those entries), so its clean result on those areas is not a pass.

Shell tool used: PowerShell. `python tools/axe.py evals/032-aria-tooltip-is-only-name/input.html`; `python tools/readability.py evals/032-aria-tooltip-is-only-name/input.html`

---

The verifier says it used PowerShell, not Bash, to run `tools/axe.py` and `tools/readability.py`. That comes from the verifier's own report, because I can't see its tool calls.
