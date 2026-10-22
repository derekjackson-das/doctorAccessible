# Evals

Known-defect snippets and the findings a correct verifier must produce. This is how the team tells whether a change to an agent, a skill, or a knowledge entry made things better or worse.

## Layout

```
evals/
  NNN-slug/
    input.html      the page or snippet under test
    expected.md     the findings a correct run must produce, and what it must not produce
```

One intended defect per eval unless its `expected.md` says otherwise. Everything else in the input is kept clean on purpose, so a false positive is visible.

## Running one

From a Claude Code session in this repo:

1. Ask for the verifier agent on `evals/NNN-slug/input.html`.
2. Compare its report to `expected.md`.
3. Record pass or fail, and anything the verifier said that was not expected, in the pull request.

A pull request that changes `.claude/` or `knowledge/` states which evals were run and the result.

## Adding one

Pick the next number. Write the input first, then the expected findings from the knowledge entry, not from memory. If the knowledge entry does not exist yet, write it first.
