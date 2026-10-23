# Run 2026-10-23: the registered verifier on eval 007, using knowledge/axe-rules.md (WP 4.2)

- Method: fresh headless `claude -p` session in the repo, registered `verifier` agent, verifier.md at f901025 (step 2 looks fired rules up in `knowledge/axe-rules.md`). axe run by the verifier through `tools/axe.py`.
- Result: **pass.** One definite finding, SC 2.2.1 Timing Adjustable (Level A), tier 1, as the key expects. axe's `meta-refresh` violation was mapped through `axe-rules.md` to 2.2.1 and its entry. The verifier noted that the raw JSON is written outside the repo, by design.

## The session's reply, as given

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.
## Checked
- I checked `C:\Users\rua126\AppData\Local\Temp\claude\C--Users-rua126\cf68331b-fb24-46e9-a990-751e07481e93\scratchpad\repo\doctorAccessible\evals\007-meta-refresh\input.html` (23 lines). I read the code in full and ran axe through `tools/axe.py`.
- **No spec.** There is no `a11y-spec.md` at the repo root or in `docs/`, so I checked against WCAG 2.2 AA alone and used the house content defaults in `docs/content-standards.md`.
- **One file was written.** `tools/axe.py` saves its raw JSON by design, so this run created one file outside the repository: `C:\Users\rua126\AppData\Local\Temp\doctor-a11y-axe\007-meta-refresh-20261023-135615.json`. Your constraint said to create no files; I read it as covering the repository. No file in the repository was created, edited or deleted.
- I did not open `expected.md`, `RESULTS.md`, or any `run-*.md`.

## Findings

### [Definite] Timed meta refresh redirects the page after 20 seconds
- **Where:** line 6, `<meta http-equiv="refresh" content="20; url=/registration/step-2">` (selector `meta[http-equiv="refresh"]`)
- **What:** The page sends the user to `/registration/step-2` after a 20-second delay. The user cannot turn the limit off, adjust it, or extend it.
- **Criterion:** WCAG 2.2 SC 2.2.1 Timing Adjustable (Level A), tier 1.
  - None of the criterion's options applies: turn off, adjust, extend, real-time, essential, or the "20 Hour Exception".
  - The entry lists a delayed `meta http-equiv="refresh"` redirect as a definite failure (F40, F41, tier 2).
- **Source:** `knowledge/wcag/sc-2.2.1-timing-adjustable.md`
- **Fix direction:** Remove the timed refresh. The page already has a "Continue to contact details" link, so the user can move on when ready (or the server can redirect with no delay).

No other defects found:
- Landmarks are present (`header`, `main`).
- There is one `h1`, a descriptive `title`, and a valid `lang="en"`.
- The link has a name, and there is a visible `:focus-visible` outline.

I did not compute contrast ratios by hand. The axe `color-contrast` rule passed.

## Content
- **Reading level:** measured with `tools/readability.py` 1.0 (2026-10-23) against the house default target of grade 8.
  - Flesch-Kincaid Grade Level 2.9, which is at or below the target.
  - Counts: 20 words, 4 sentences, 28 syllables (estimated by rule).
  - It measured `<main>` only and left out the `h1` and the `style` block.
  - The tool notes that under 100 words the score means little. It is a signal, not a verdict.
- **Headings:** One `h1`, "Registration received". It matches the `title` and says what the page is. Meets standard 4.
- **Links:** "Continue to contact details" says where it goes, out of context. Meets standard 5.
- **Alt text:** No images, so not applicable.
- **Error messages:** No form or errors, so not applicable.
- **Language:** `lang="en"` is declared. No passages in other languages and no abbreviations.
- **Plain language and organization:** The first sentence carries the point and the text is short and active. Whether it says enough about what happens next is a manual review item.

## Spec deviations
None reported: there is no `a11y-spec.md` to check against.

## Manual checks remaining
- **Timing (after the fix):** Load the page, leave it open well past 20 seconds, and record whether the page or the focus changes without user action.
- **Screen reader:** With each screen reader the team tests with (no spec names them), load the page. Record the page title and heading reported, and whether the link is reachable and its name matches the visible text.
- **Keyboard:** Tab to the link and record whether the focus outline is visible against the background. Activate it with Enter and record where you land.
- **Server-side behavior:** Check whether `/registration/step-2` or the registration flow sets a session timeout. If it does, check it against 2.2.1 separately. This cannot be judged from this file.
- **Zoom and reflow:** At 200% and 400% zoom, record whether any text is clipped or needs horizontal scrolling.

## Automated scan
- **Version and tags:** axe-core 4.14.0 via @axe-core/cli, tags wcag2a, wcag2aa, wcag21a, wcag21aa, wcag22aa.
- **Page:** `file:///C:/Users/rua126/AppData/Local/Temp/claude/C--Users-rua126/cf68331b-fb24-46e9-a990-751e07481e93/scratchpad/repo/doctorAccessible/evals/007-meta-refresh/input.html`
- **Raw JSON:** `C:\Users\rua126\AppData\Local\Temp\doctor-a11y-axe\007-meta-refresh-20261023-135615.json`
- **Violations: 1**
  - `meta-refresh` (impact critical; tags wcag2a, wcag221): "Delayed refresh under 20 hours must not be used", at `meta[http-equiv="refresh"]`
- **Incomplete:** 0
- **Passes:** 9 rules (aria-hidden-body, bypass, color-contrast, document-title, html-has-lang, html-lang-valid, link-name, meta-viewport, target-size)
- **Inapplicable:** 54 rules

Raw block printed by the tool:
```
{
  "violations": [
    {
      "id": "meta-refresh",
      "impact": "critical",
      "tags": ["wcag2a", "wcag221"],
      "help": "Delayed refresh under 20 hours must not be used",
      "helpUrl": "https://dequeuniversity.com/rules/axe/4.14/meta-refresh?application=webdriverjs",
      "nodes": [
        {
          "target": ["meta[http-equiv=\"refresh\"]"],
          "failureSummary": "Fix any of the following:\n  <meta> tag forces timed refresh of page (less than 20 hours)"
        }
      ]
    }
  ],
  "incomplete": []
}
```

What each violation supports:
- `meta-refresh` supports the Definite finding above. `knowledge/axe-rules.md` maps it to 2.2.1 Timing Adjustable (A), `wcag/sc-2.2.1-timing-adjustable.md`.
- The related rule `meta-refresh-no-exceptions` maps to 2.2.4 and 3.2.5. Those are not Level A or AA, so they are beyond our target and have no entry. That rule is not in the run's tag set and did not fire.
