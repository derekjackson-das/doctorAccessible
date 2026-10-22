# Evals

Known-defect snippets and the findings a correct verifier must produce. This is how the team tells whether a change to an agent, a skill, or a knowledge entry made things better or worse.

## Layout

```
evals/
  RESULTS.md        one row per run, newest first
  NNN-slug/
    input.html      the page or snippet under test
    expected.md     the findings a correct run must produce, and what it must not produce
```

One intended defect per eval unless its `expected.md` says otherwise. Everything else in the input is kept clean on purpose, so a false positive is visible.

## Running one

From a Claude Code session in this repo:

1. Run axe on the input first, for the automated baseline:
   `npx --yes @axe-core/cli "file://$PWD/evals/NNN-slug/input.html"`.
   If it complains about ChromeDriver, run `npx --yes browser-driver-manager install chrome` once.
2. Ask for the verifier agent on `evals/NNN-slug/input.html`. Tell it not to open `expected.md` or `RESULTS.md`. Claude Code registers project agents at launch, so an agent added during a session is available only after a restart.
3. Compare both to `expected.md`.
4. Add a row to `RESULTS.md` and cite it in the pull request.

A pull request that changes `.claude/` or `knowledge/` states which evals were run and the result.

## Adding one

Pick the next number. Write the input first, then the expected findings from the knowledge entry, not from memory. If the knowledge entry does not exist yet, write it first.
