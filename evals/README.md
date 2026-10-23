# Evals

Known-defect snippets and the findings a correct verifier must produce. This is how the team tells whether a change to an agent, a skill, or a knowledge entry made things better or worse.

## Layout

```
evals/
  RESULTS.md        one row per run, newest first
  NNN-slug/
    input.html      the page or snippet under test
    expected.md     the findings a correct run must produce, and what it must not produce
    request.md      instead of input.html, for a transcript eval (see below)
    text.md         instead of input.html, for a content eval (see below)
```

One intended defect per eval unless its `expected.md` says otherwise. Everything else in the input is kept clean on purpose, so a false positive is visible.

## Transcript evals

Phase 3 skills are tested with a different input. Instead of `input.html`, the folder holds `request.md`: a short feature request as a developer would type it, plus the project context the skill is given (the spec's audience and AT list, any code pasted). `expected.md` says what a good answer contains and what it must not do. To run one, start a fresh Claude Code session in a copy of the repo, load the skill (for example `/consult`), paste the request, and compare the answer to `expected.md`. The `content` skill's evals hold `text.md` instead: the words under review, as a snippet, with the same project context. Until Phase 4 automates this, record the run the same way: a row in `RESULTS.md` and the full answer in a `run-YYYY-MM-DD-<skill>.md` file beside the request or text.

## Running one

From a Claude Code session in this repo:

1. Run axe on the input first, for the automated baseline:
   `npx --yes @axe-core/cli "file://$PWD/evals/NNN-slug/input.html"`.
   The default run skips rules tagged for WCAG 2.2 (observed with axe-core 4.14.0 on eval 010). To include them, add `--tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`. Record which form you ran in `RESULTS.md`.
   If it complains about ChromeDriver, run `npx --yes browser-driver-manager install chrome` once.
   On Windows, if axe then fails with `spawn ... ENOENT` and the driver path broken across two lines, the user folder name is being read as an escape (`C:\Users\rua126` loses its `\r`). Pass the paths the driver manager printed, with forward slashes: `--chromedriver-path C:/Users/<you>/.browser-driver-manager/chromedriver/<version>/chromedriver-win64/chromedriver.exe --chrome-path C:/Users/<you>/.browser-driver-manager/chrome/<version>/chrome-win64/chrome.exe`. Observed with axe-core 4.14.0 on 2026-10-23.
2. Ask for the verifier agent on `evals/NNN-slug/input.html`. Tell it not to open `expected.md` or `RESULTS.md`. Claude Code registers project agents at launch, so an agent added during a session is available only after a restart.
3. Compare both to `expected.md`.
4. Add a row to `RESULTS.md` and cite it in the pull request.

A pull request that changes `.claude/` or `knowledge/` states which evals were run and the result.

## Adding one

Pick the next number. Write the input first, then the expected findings from the knowledge entry, not from memory. If the knowledge entry does not exist yet, write it first.
