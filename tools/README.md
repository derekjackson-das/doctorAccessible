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
