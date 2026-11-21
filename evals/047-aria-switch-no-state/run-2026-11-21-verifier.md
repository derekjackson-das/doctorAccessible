## Checked

- File: `/Users/derekjackson/Documents/CCode/doctorAccessible/evals/047-aria-switch-no-state/input.html` (54 lines: one page, inline CSS and script).
- Method: I read the file in full, ran `tools/axe.py` (axe-core 4.14.0, WCAG 2.2 tags) and ran `tools/readability.py`. `python` is not on this machine's PATH, so both ran with `python3`.
- Spec: no `a11y-spec.md` beside the input, at the repo root, or in `docs/`. Checked against WCAG 2.2 AA alone.
- As instructed, I did not open `expected.md`, `evals/RESULTS.md`, or any `run-*.md`. No files were created, edited, or moved in the repository.

## Findings

### [Definite] Custom switches expose no on/off state, and the script never sets one

- Where: lines 32 and 36 (`div.switch[role="switch"]`), and the script at lines 45 to 51.
- What: Both `role="switch"` elements lack `aria-checked`, and the toggle function only flips the CSS class `on`. The state is therefore shown by colour and thumb position only and is never programmatically exposed or updated.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1.
- Source: `knowledge/wcag/sc-4.1.2-name-role-value.md` lists a custom toggle that changes state visually without exposing it as definite when the state is user-settable. `knowledge/aria/roles/switch.md` records `aria-checked` as a required state for this role (WAI-ARIA 1.2, W3C Rec 6 June 2023, tier 1) and maps "No `aria-checked`, or not updated" to 4.1.2.
- Supported by axe: `aria-required-attr` fired on both nodes.
- Fix direction: Give each switch `aria-checked` matching its initial visual state and update it in the same handler that toggles the class, or use a native `input type=checkbox`, which carries its own state.

Note, not a second finding: the first switch renders as on (`class="switch on"`) and the second as off, and neither state is exposed. This is the same defect on two nodes.

### [Likely] none

### [Manual review] none from WCAG criteria

The items a person must confirm are under "Manual checks remaining".

**Checked and not findings**

- **Name and role (SC 4.1.2):** each switch has `role="switch"` and a name through `aria-labelledby` pointing at an existing id (`due-label`, `hold-label`).
- **Keyboard (SC 2.1.1, `knowledge/wcag/sc-2.1.1-keyboard.md`):** both switches have `tabindex="0"` and a `keydown` handler for Space and Enter alongside `click`.
- **Focus visible (SC 2.4.7, `knowledge/wcag/sc-2.4.7-focus-visible.md`):** an author `:focus-visible` outline is declared for switches, links, and buttons, and nothing removes an outline.
- **Text contrast (SC 1.4.3, threshold 4.5:1 from `knowledge/wcag/sc-1.4.3-contrast-minimum.md`):** all ratios below were computed from the declared colours with the Recommendation's formula.
  - Body text `#1a1a1a` on `#fff`: 17.4:1.
  - Links `#0b4f9c` on `#fff`: 8.04:1.
  - Button text `#fff` on `#0b4f9c`: 8.04:1.
- **Non-text contrast (SC 1.4.11, threshold 3:1 from `knowledge/wcag/sc-1.4.11-non-text-contrast.md`):** computed the same way.
  - Off-state border and thumb `#1a1a1a` against `#fff`: 17.4:1.
  - On-state fill `#0b4f9c` against the page and against its white thumb: 8.04:1.
  - Focus outline `#0b4f9c` against `#fff`: 8.04:1.
- **Use of colour (SC 1.4.1, `knowledge/wcag/sc-1.4.1-use-of-color.md`):** the on state also moves the thumb (`left: .15rem` to `1.45rem`), so colour is not the only visual cue. Links keep the browser's default underline.
- **Target size (SC 2.5.8, threshold 24 by 24 CSS pixels from `knowledge/wcag/sc-2.5.8-target-size-minimum.md`):** the switch is declared at 3rem by 1.75rem, which computes to 48 by 28 CSS pixels at a 16px root, before borders. axe's `target-size` rule did not fire.
- **Page title, language, landmarks, heading:** `title` present, `lang="en"`, `header`/`main`/`footer`, one `h1`.

**Advice, not a WCAG finding**

- The labels are `span` elements, so clicking the label text does not toggle the switch. The name is still associated, so 4.1.2 and 1.3.1 are met. A native checkbox with a `label` would give this for free (`knowledge/aria/roles/switch.md`, "The native element").
- Outside accessibility scope but worth a look: the switches are `div`s with `data-name` and no form control behind them, so their values do not appear to be submitted with the form.

## Content

- **Reading level:** `readability.py 1.0 (2026-10-23)` measured `<main>` and left out button x1, h1 x1, script x1, style x1.
  - 14 words, 3 sentences, 21 syllables (estimated by rule).
  - Flesch-Kincaid Grade Level 3.9 against the house default target of 8 (at or below); no spec sets a different one.
  - The tool notes the text is under 100 words, so the score means little. A signal, not a verdict.
- **Headings:** one `h1`, "Notification settings", which describes the page and matches the title. No skipped levels. Meets `docs/content-standards.md` section 4.
- **Link text:** "Campus Libraries" and "Accessibility statement" each say where they go. Meets section 5.
- **Alt text:** no images.
- **Labels and instructions:** "Due date reminders" and "Hold ready alerts" are short and the names do not change with state. The instruction "Choose which emails you get from the library." comes before the controls. Meets section 7.
- **Error messages:** none in the page. What the server returns after submit cannot be judged from this file.
- **Language:** `lang="en"` declared, with no other-language passages and no unexpanded abbreviations. Meets section 8.
- **Manual review:** whether "Hold ready alerts" is clear to someone who does not know the library term "hold" is a judgement for a person.

## Spec deviations

None reportable: there is no `a11y-spec.md` for this input.

## Manual checks remaining

1. **Screen reader, each switch, before the fix.** Move to each switch and record what is reported for name, role, and state. Activate with Space and record whether any state change is reported. Repeat on each assistive technology the team tests with; the tester reports the result.
2. **Same steps after a fix.** Also inspect the browser's accessibility tree and record whether `aria-checked` flips on each activation, by click, Space, and Enter.
3. **Keyboard only.** Tab through the page and record the focus order: header link, switch 1, switch 2, Save settings, footer link. Confirm Space on a switch does not scroll the page, and record whether Enter on a switch toggles it or submits the form.
4. **Focus indicator on the Save button.** The outline is the same colour as the button fill, separated by a 2px offset. Confirm by eye that the ring is distinguishable.
5. **Forced colours (Windows Contrast Themes).** The on and off states rely on author background colours on the track and the `::after` thumb. Record whether the thumb and the on/off difference remain visible.
6. **Zoom at 200% and 400%, and text spacing overrides.** Record whether the label and switch rows reflow without loss or overlap.
7. **Voice control.** Record whether saying the visible label text ("Due date reminders") activates the switch.
8. **After submit.** How confirmation or errors are presented cannot be judged from this file (SC 4.1.3 and SC 3.3.1 may apply to the response page).

## Automated scan

- axe-core 4.14.0 via `@axe-core/cli`, tags `wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`.
- Page: `file:///Users/derekjackson/Documents/CCode/doctorAccessible/evals/047-aria-switch-no-state/input.html`
- Raw JSON, outside the repo: `/var/folders/th/2_b8_m913qv7cv3ydxpt5tdm0000gq/T/doctor-a11y-axe/047-aria-switch-no-state-20261121-002733.json`
- Violations: 1
  - `aria-required-attr` (critical; `wcag2a`, `wcag412`): "Required ARIA attributes must be provided"
    - `.on`: Required ARIA attribute not present: aria-checked
    - `div[aria-labelledby="hold-label"]`: Required ARIA attribute not present: aria-checked
- Incomplete: 0
- Passes: 20 rules. Inapplicable: 43 rules.

Raw block as printed:

```
{
  "violations": [
    {
      "id": "aria-required-attr",
      "impact": "critical",
      "tags": ["wcag2a", "wcag412"],
      "help": "Required ARIA attributes must be provided",
      "helpUrl": "https://dequeuniversity.com/rules/axe/4.14/aria-required-attr?application=webdriverjs",
      "nodes": [
        { "target": [".on"],
          "failureSummary": "Fix any of the following:\n  Required ARIA attribute not present: aria-checked" },
        { "target": ["div[aria-labelledby=\"hold-label\"]"],
          "failureSummary": "Fix any of the following:\n  Required ARIA attribute not present: aria-checked" }
      ]
    }
  ],
  "incomplete": []
}
```

- `aria-required-attr` supports the one Definite finding above. `knowledge/axe-rules.md` maps it to SC 4.1.2 and `wcag/sc-4.1.2-name-role-value.md`.
- axe sees the missing attribute. It cannot see that the script never updates state; that part of the finding comes from reading lines 45 to 51.
