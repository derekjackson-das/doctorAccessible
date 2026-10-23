# Tools

## readability.py

Flesch-Kincaid Grade Level over the main content of an HTML, Markdown, or text file (roadmap 4.7). Standard library only.

```
python tools/readability.py page.html --target 8
python -m unittest tools/test_readability.py
```

- **Formula:** as printed in Kincaid, Fishburne, Rogers, and Chissom, Research Branch Report 8-75 (1975), Table 3: grade = .39 (words per sentence) + 11.8 (syllables per word) - 15.59.
- **What it measures:** the text inside `<main>`, or `<body>` if there is no `<main>`. It leaves out navigation, headings, code, scripts, styles, hidden content, and form controls, and says what it left out. In a Markdown file with `html` fences, it measures only the fences (the prose around them is context, as in the content skill's evals).
- **Limits:** syllables are counted by rule, an estimate per word. Proper nouns are not removed, so names can raise the grade. Text a script adds at run time is not seen. Under 100 words, the score means little, and the tool says so.
- **Checked against** hand counts on the three samples in `samples/`, by `test_readability.py`.
- **Not a verdict:** a score sends a person to read the text (`knowledge/content/reading-level.md`).

## build_axe_rules.py

Rebuilds `knowledge/axe-rules.md` from axe-core's own rule list, with titles, levels, and entries from `knowledge/INDEX.md` (roadmap 4.2): `python tools/build_axe_rules.py --axe-dir <npm cache>/_npx/<hash>/node_modules/axe-core`.

## axe.py

Runs axe on a page with the WCAG 2.2 tags and prints every result bucket (roadmap 4.1). Standard library only; needs Node.js for `npx`.

```
python tools/axe.py evals/001-missing-label/input.html
```

- **Command:** `npx --yes @axe-core/cli <url> --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa --stdout`. A file path is turned into a `file://` URL.
- **Output:** the axe version; the path of the raw JSON, saved in a temporary folder and never in the repository; each violation and incomplete result with its rule, impact, WCAG tags, and targets; the pass and inapplicable counts; and a trimmed raw block for the verifier's report.
- **Setup it handles:** no `npx` (it says "axe: not run" and exits 2; set `DOCTOR_A11Y_NODE_DIR` to a Node.js folder that is not on PATH). It also reads the Chrome and ChromeDriver paths that `npx browser-driver-manager install chrome` saves and passes them with forward slashes, which avoids the Windows path problem in `evals/README.md`.
- **Not a verdict:** axe finds a minority of defects. A clean run is not a pass.

## check_links.py

Checks every link and every repo path named in the library's Markdown: `knowledge/`, `.claude/`, `docs/`, `templates/`, each `evals/*/expected.md`, and the top-level README, CONTRIBUTING, and CLAUDE files. Standard library only.

```
python tools/check_links.py            # paths and links
python tools/check_links.py --no-web   # paths only, in a second
```

- **Paths:** a backticked path such as `knowledge/wcag/sc-1.1.1-non-text-content.md`, or `wcag/...` read from `knowledge/`, must exist. Placeholders (`<name>`, `x.x.x`, `...`, `NNN`) are skipped, and so is the roadmap, whose paths are planned files.
- **Links:** each page is requested once (anchors dropped), one host at a time with a pause, so W3C does not rate-limit the run. Sites that refuse scripts (401, 403, 405, 429, 999) are listed apart and not counted as broken; open those by hand.
- Run records, `RESULTS.md`, and baselines are history and are not scanned. Exit 0 if nothing is broken.
