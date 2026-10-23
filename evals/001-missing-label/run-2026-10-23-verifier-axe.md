# Run 2026-10-23: the registered verifier runs axe itself on eval 001 (WP 4.1)

- Method: a fresh headless Claude Code session (`claude -p`, Claude Code 2.1.309, Windows) in the repo, asked to use the registered `verifier` agent on `evals/001-missing-label/input.html` and told not to open `expected.md`, `evals/RESULTS.md`, or any run file, or edit files. Session tools: Read, Glob, Grep, Bash, PowerShell, Task, Agent. `DOCTOR_A11Y_NODE_DIR` pointed at a portable Node.js 24.22.1.
- Verifier at commit b1c4339 (tools now include PowerShell). An earlier attempt at e29455a, without PowerShell, had no shell and ran no axe; see the PR.
- axe: run by the verifier itself through `tools/axe.py`; raw output in the report below.

## The session's reply, as given

## Checked

- **File:** `C:\Users\rua126\AppData\Local\Temp\claude\C--Users-rua126\cf68331b-fb24-46e9-a990-751e07481e93\scratchpad\repo\doctorAccessible\evals\001-missing-label\input.html`. It is 28 lines: a search form with one text input and one submit button.
- **Method:** I ran `tools/axe.py`, read every line of the code, and ran `tools/readability.py`.
- **Project spec:** none. There is no `a11y-spec.md` at the repo root or in `docs/`; the only copy is `templates/a11y-spec.md`, which is the blank template. This check is against WCAG 2.2 AA and `docs/content-standards.md` only.
- **Entries opened:** `knowledge/INDEX.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-3.3.2-labels-or-instructions.md`, `wcag/sc-2.4.6-headings-and-labels.md`, `wcag/sc-1.4.3-contrast-minimum.md`, and `docs/content-standards.md`.

## Findings

### [Definite] Search input has no programmatic label
- **Where:** line 22, `<input type="text" id="q" name="q">` (selector `#q`). The visible text `<span>Search</span>` is on line 21.
- **What:** The text field has no `label`, `aria-label`, `aria-labelledby`, or `title`. The visible word "Search" next to it is a plain `span` and is not linked to the field, so the field has no accessible name.
- **Criterion:** WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1. It is also SC 1.3.1 Info and Relationships (Level A), tier 1: the 1.3.1 entry says an unlinked label fails both criteria and should be reported once with both named.
- **Source:** `knowledge/wcag/sc-4.1.2-name-role-value.md`, `knowledge/wcag/sc-1.3.1-info-and-relationships.md`. W3C Rec 12 Dec 2024.
- **Fix direction:** Link the visible "Search" text to the field with a native `label` element (Technique H44).

This is the only defect found.

### Checked and met (not findings)
- **SC 3.3.2 Labels or Instructions:** met. A visible label exists ("Search"), and the next-door "Search" button also labels the field's purpose (G167). The 3.3.2 entry says a visible label that is not linked belongs to 1.3.1 and 4.1.2, not 3.3.2.
- **SC 2.4.6 Headings and Labels:** met. "Search" and the `h1` "Site search" both describe their purpose.
- **SC 1.4.3 Contrast (Minimum):** met for body text. I computed the ratio myself from the declared colors, `#1a1a1a` on `#fff`, using the WCAG luminance formula: about 17.4:1. The entry's threshold for normal text is 4.5:1. The button and input use browser default colors; I did not compute those.
- **Language and title:** `lang="en"` is set, and `<title>Site search</title>` is present.
- **Structure:** a `header` and a `main` landmark, and one `h1`.

## Content

- **Reading level:** measured with `readability.py 1.0 (2026-10-23)` over `<main>`. Result: Flesch-Kincaid grade -3.4 on 1 word and 1 sentence. The tool left out 1 button, 1 h1, and 1 style block. With no spec, there was no spec target to pass, so I ran without `--target` and the tool used its default of 8, which matches the house default. The tool notes that a text under 100 words gives a score that means little. Treat it as not meaningful here.
- **Headings:** one `h1`, "Site search", which says what the page is. No skipped levels. This meets content standard 4.
- **Link text and alt text:** none on the page.
- **Error messages and instructions:** none on the page. The form has no validation or error state to judge.
- **Language:** declared. Meets content standard 8.

## Spec deviations

None to report, because no `a11y-spec.md` exists. Per CLAUDE.md principle 15, the project has no spec to check against.

## Manual checks remaining

- **Screen reader (NVDA on Windows, and VoiceOver; there is no spec list of assistive technology, so these are the repo's defaults in `knowledge/testing/`):**
  - Tab to the text field. Record the name, role, and value the screen reader reports, and whether a name is reported at all.
  - Tab to the button. Record the same.
- **Speech input:** say "click Search" or the equivalent command. Record which element is targeted: the field, the button, or neither. Once the label is fixed, both elements carry the visible word "Search".
- **Keyboard only:**
  - Confirm the tab order is field, then button.
  - Confirm the 3px `#005a9c` focus outline is visible on both elements.
  - Confirm that pressing Enter in the field submits the form.
- **Zoom:** at 200% and 400%, record whether the `.row` flex layout reflows without horizontal scrolling.
- **Forced colors:** record whether the field's border, the button's border, and the focus outline are still visible.
- **Contrast of controls:** measure the browser-default border of the input and button against white (SC 1.4.11). I did not compute this.

## Automated scan

- **Tool:** axe-core 4.14.0 via @axe-core/cli, run with tags wcag2a, wcag2aa, wcag21a, wcag21aa, wcag22aa.
- **Raw JSON:** `C:\Users\rua126\AppData\Local\Temp\doctor-a11y-axe\001-missing-label-20261023-134339.json`
- **Violations (1):** `label`, impact critical, tags wcag2a and wcag412, "Form elements must have labels", target `#q`.
- **Incomplete:** 0.
- **Passes:** 10 rules. **Inapplicable:** 53 rules.

Raw block as printed:
```
{
  "violations": [
    {
      "id": "label",
      "impact": "critical",
      "tags": ["wcag2a", "wcag412"],
      "help": "Form elements must have labels",
      "helpUrl": "https://dequeuniversity.com/rules/axe/4.14/label?application=webdriverjs",
      "nodes": [
        {
          "target": ["#q"],
          "failureSummary": "Fix any of the following:\n  Element does not have an implicit (wrapped) <label>\n  Element does not have an explicit <label>\n  aria-label attribute does not exist or is empty\n  aria-labelledby attribute does not exist, references elements that do not exist or references elements that are empty\n  Element has no title attribute\n  Element has no placeholder attribute\n  Element's default semantics were not overridden with role=\"none\" or role=\"presentation\""
        }
      ]
    }
  ],
  "incomplete": []
}
```

- **`label` on `#q`:** this supports the Definite finding "Search input has no programmatic label".

Shell tool used: PowerShell

---

The verifier used PowerShell, and never Bash. That comes from its own closing line, which I asked it to add; I can't see its tool calls directly, so I haven't checked it.
