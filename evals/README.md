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

Phase 3 skills are tested with a different input. Instead of `input.html`, the folder holds `request.md`: a short feature request as a developer would type it, plus the project context the skill is given (the spec's audience and AT list, any code pasted). `expected.md` says what a good answer contains and what it must not do. To run one, start a fresh Claude Code session in a copy of the repo, load the skill (for example `/consult`), paste the request, and compare the answer to `expected.md`. The `content` skill's evals hold `text.md` instead: the words under review, as a snippet, with the same project context. `evals/run.sh -s` runs them headless (below). Record a run the same way as any other: a row in `RESULTS.md`, and for a hand run the full answer in a `run-YYYY-MM-DD-<skill>.md` file beside the request or text.

## Running one

From a Claude Code session in this repo:

1. Run axe on the input first, for the automated baseline:
   `npx --yes @axe-core/cli "file://$PWD/evals/NNN-slug/input.html"`.
   The default run skips rules tagged for WCAG 2.2 (observed with axe-core 4.14.0 on eval 010). To include them, add `--tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`. Record which form you ran in `RESULTS.md`.
   Or run `python tools/axe.py evals/NNN-slug/input.html`, which passes the tags, saves the raw JSON outside the repo, prints every bucket, and works around the Windows path problem below.
   If it complains about ChromeDriver, run `npx --yes browser-driver-manager install chrome` once.
   On Windows, if axe then fails with `spawn ... ENOENT` and the driver path broken across two lines, the user folder name is being read as an escape (`C:\Users\rua126` loses its `\r`). Pass the paths the driver manager printed, with forward slashes: `--chromedriver-path C:/Users/<you>/.browser-driver-manager/chromedriver/<version>/chromedriver-win64/chromedriver.exe --chrome-path C:/Users/<you>/.browser-driver-manager/chrome/<version>/chrome-win64/chrome.exe`. Observed with axe-core 4.14.0 on 2026-10-23.
2. Ask for the verifier agent on `evals/NNN-slug/input.html`. Tell it not to open `expected.md` or `RESULTS.md`. Claude Code registers project agents at launch, so an agent added during a session is available only after a restart.
3. Compare both to `expected.md`.
4. Add a row to `RESULTS.md` and cite it in the pull request.

A pull request that changes `.claude/` or `knowledge/` states which evals were run and the result.

## Running them all

`evals/run.sh` runs the verifier on every eval with an `input.html`, or on the evals named, each in its own fresh `claude -p` session using the registered verifier (roadmap 4.3):

```
evals/run.sh                          # every page eval, 3 at a time
evals/run.sh -j 6 001-missing-label   # named evals, 6 at a time
evals/run.sh -o /tmp/reports          # choose where reports go
```

Reports go outside the repo by default, in a dated folder in the temp directory: one `<eval>.md` per eval and an `index.md` listing each eval's finding headings and axe line. Read each report against its `expected.md`, or grade them with `python evals/check.py <reports-folder>` (roadmap 4.4). It checks the criterion, level, tier, and confidence of finding 1 mechanically. A fresh `claude -p` judge with no tools checks the must-not list and the pass condition, quoting the report line behind each failure. It writes `checks.md` beside the reports; `--no-judge` skips the judge. Record what you read in `RESULTS.md` as for any run. Each session costs a verifier run's tokens. For axe, Node.js must be on PATH or `DOCTOR_A11Y_NODE_DIR` set. `evals/run.sh -s` runs the skill evals instead (`-a` runs both): each session loads the skill its folder name names (`015-consult-...` loads `consult`) and answers `request.md` or `text.md`, with no Write or Edit tool. `check.py` grades those with the judge alone, against the whole key with the request beside it; their keys list what a good answer holds, not one finding to match.

## Adding one

Pick the next number. Write the input first, then the expected findings from the knowledge entry, not from memory. If the knowledge entry does not exist yet, write it first.
