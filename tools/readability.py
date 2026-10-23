"""Flesch-Kincaid Grade Level over the main content of an HTML, Markdown, or text file.

Usage:
    python tools/readability.py <file> [--target 8]

The formula is the recalculated Flesch formula for grade level in
Kincaid, Fishburne, Rogers, and Chissom, "Derivation of New Readability Formulas
(Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy
Enlisted Personnel", Research Branch Report 8-75, 1975, Table 3 (report page 14):

    GL = .39 (words/sentence) + 11.8 (syllables/word) - 15.59

What is measured follows docs/content-standards.md section 2: the main content only.
The text inside <main> is used if the page has one, otherwise <body>. Navigation,
headings, code, scripts, styles, hidden content, and form controls are left out.
Only the text in the file is seen: content a script adds when the page runs is not.
In a Markdown file with ```html fences, only the fences are measured. Proper nouns
are not removed; the house standard says "where practical", and doing
it well needs a person.

Syllables are counted by rule, not from a dictionary, so the count is an estimate
per word (see count_syllables). The score is a signal that sends a person to read
the text, never a pass (knowledge/content/reading-level.md).
"""

import argparse
import html.parser
import re
import sys

VERSION = "readability.py 1.0 (2026-10-23)"

# Elements whose text is not main content (house standard, section 2).
SKIP = {
    "script", "style", "noscript", "template", "nav", "svg",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "code", "pre", "kbd", "samp",
    "button", "select", "option", "textarea", "label",
}
# Elements that end a run of text, so text before and after is not joined.
BLOCKS = {
    "p", "div", "li", "ul", "ol", "dl", "dt", "dd", "td", "th", "tr", "table",
    "caption", "blockquote", "section", "article", "aside", "header", "footer",
    "main", "body", "figure", "figcaption", "form", "fieldset", "legend", "br", "hr",
    "details", "summary", "dialog",
} | SKIP
VOID = {"br", "hr", "img", "input", "meta", "link", "area", "base", "col", "embed",
        "source", "track", "wbr", "param"}

# Abbreviations whose full stop does not end a sentence.
ABBREVIATIONS = {"a.m.", "p.m.", "e.g.", "i.e.", "etc.", "dr.", "mr.", "mrs.", "ms.",
                 "st.", "vs.", "no.", "approx.", "dept."}


class _MainText(html.parser.HTMLParser):
    """Collects text blocks, separately for <main> and for the whole <body>."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # open element names
        self.skip_depth = 0      # >0 while inside a skipped element
        self.in_main = 0
        self.main_seen = False
        self.body_blocks, self.main_blocks = [[]], [[]]
        self.skipped = {}

    def _break(self):
        for blocks in (self.body_blocks, self.main_blocks):
            if blocks[-1]:
                blocks.append([])

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        hidden = "hidden" in a or a.get("aria-hidden") == "true"
        if tag in BLOCKS:
            self._break()
        if tag in VOID:
            return
        self.stack.append(tag)
        if tag == "main":
            self.in_main += 1
            self.main_seen = True
        if self.skip_depth or tag in SKIP or hidden:
            if not self.skip_depth:
                self.skipped[tag] = self.skipped.get(tag, 0) + 1
            self.skip_depth += 1

    def handle_endtag(self, tag):
        if tag in VOID or tag not in self.stack:
            return
        while self.stack:
            t = self.stack.pop()
            if self.skip_depth:
                self.skip_depth -= 1
            if t == "main":
                self.in_main -= 1
            if t == tag:
                break
        if tag in BLOCKS:
            self._break()

    def handle_data(self, data):
        if self.skip_depth:
            return
        self.body_blocks[-1].append(data)
        if self.in_main:
            self.main_blocks[-1].append(data)


def extract_html(source):
    """Return (blocks of text, notes) from HTML."""
    p = _MainText()
    p.feed(source)
    p.close()
    main = [" ".join("".join(b).split()) for b in p.main_blocks]
    main = [b for b in main if b]
    if p.main_seen:
        blocks = main
        scope = "<main>" if main else "<main>, which has no text in the file (content built by script is not seen)"
    else:
        blocks = [" ".join("".join(b).split()) for b in p.body_blocks]
        blocks, scope = [b for b in blocks if b], "<body> (no <main> found)"
    skipped = ", ".join(f"{k} x{v}" for k, v in sorted(p.skipped.items())) or "none"
    return blocks, [f"measured: {scope}", f"left out: {skipped}"]


def extract_markdown(source):
    """Return (blocks, notes) from Markdown. If the file has ```html fences, only
    they are measured: the prose around them is the request and its context, as in
    the content skill's text.md evals. Otherwise the prose is measured, with other
    fences and headings left out."""
    blocks, notes = [], []
    has_html_fence = re.search(r"^```(html|htm)\b", source, flags=re.M | re.I) is not None
    parts = re.split(r"^```([\w-]*)[^\n]*\n(.*?)^```[^\n]*$", source, flags=re.M | re.S)
    # parts: text, lang, body, text, lang, body, ...
    for i in range(0, len(parts), 3):
        text = parts[i]
        if has_html_fence:
            text = ""
        for para in re.split(r"\n\s*\n", text):
            lines = [l for l in para.splitlines() if l.strip() and not l.lstrip().startswith("#")]
            para = " ".join(" ".join(lines).split())
            para = re.sub(r"`[^`]*`", " ", para)          # inline code
            para = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", para)
            para = re.sub(r"^>\s*", "", para)
            if para.strip():
                blocks.append(para.strip())
        if i + 2 < len(parts):
            lang, body = parts[i + 1].lower(), parts[i + 2]
            if lang in ("html", "htm"):
                b, n = extract_html(body)
                blocks += b
                notes.append("an html fence was read as HTML; " + "; ".join(n))
            else:
                notes.append(f"a ```{lang or 'plain'} fence was left out as code")
    if has_html_fence:
        notes.insert(0, "measured: the html fences only; the prose around them is context")
    return blocks, notes or ["measured: the Markdown text; headings left out"]


def split_sentences(block):
    """Split a block into sentences. A block with no closing punctuation, such as a
    list item or a table cell, counts as one sentence."""
    tokens = block.split()
    sentences, current = [], []
    for tok in tokens:
        current.append(tok)
        bare = tok.lower().strip("\"')]}»”’")
        if re.search(r"[.!?]$", bare) and bare not in ABBREVIATIONS:
            sentences.append(current)
            current = []
    if current:
        sentences.append(current)
    return sentences


def words_in(tokens):
    out = []
    for tok in tokens:
        w = re.sub(r"[^A-Za-z0-9'’-]", "", tok).strip("'’-")
        if re.search(r"[A-Za-z0-9]", w):
            out.append(w)
    return out


def count_syllables(word):
    """Estimate syllables by rule: count vowel groups (a e i o u, and y except at
    the start), then drop a silent final e, a silent -es, and a silent -ed.
    A number counts as one syllable per word. Never less than one."""
    w = word.lower().replace("’", "'")
    if re.fullmatch(r"[\d,.']+", w):
        return 1
    w = re.sub(r"[^a-z]", "", w)
    if not w:
        return 1
    groups = re.findall(r"[aeiouy]+", w[0].replace("y", "b") + w[1:])
    n = len(groups)
    if n > 1:
        if w.endswith("e") and not re.search(r"[^aeiouy]le$", w) and not w.endswith("ee"):
            n -= 1                                   # time, deadline, require
        elif w.endswith("ed") and not re.search(r"[td]ed$", w) and not w.endswith("eed"):
            n -= 1                                   # opened, closed (not wanted)
        elif w.endswith("es") and not re.search(r"(s|x|z|ch|sh|c|g)es$", w):
            n -= 1                                   # times (not boxes, pages)
    return max(1, n)


def measure(blocks):
    sentences = []
    for b in blocks:
        sentences += [s for s in split_sentences(b) if words_in(s)]
    words = [w for s in sentences for w in words_in(s)]
    syllables = sum(count_syllables(w) for w in words)
    if not words:
        return None
    wps = len(words) / len(sentences)
    spw = syllables / len(words)
    grade = 0.39 * wps + 11.8 * spw - 15.59
    return {"grade": grade, "words": len(words), "sentences": len(sentences),
            "syllables": syllables, "words_per_sentence": wps, "syllables_per_word": spw}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Flesch-Kincaid Grade Level over main content.")
    ap.add_argument("file")
    ap.add_argument("--target", type=float, default=8.0,
                    help="grade to compare against (house default 8; the spec may set another)")
    args = ap.parse_args(argv)
    source = open(args.file, encoding="utf-8").read()
    if args.file.lower().endswith((".md", ".markdown")):
        blocks, notes = extract_markdown(source)
    elif args.file.lower().endswith((".html", ".htm")) or re.search(r"<\s*(html|body|main|p)\b", source, re.I):
        blocks, notes = extract_html(source)
    else:
        blocks = [" ".join(p.split()) for p in re.split(r"\n\s*\n", source) if p.strip()]
        notes = ["measured: plain text, paragraphs as blocks"]
    r = measure(blocks)
    print(VERSION)
    print(f"file: {args.file}")
    for n in notes:
        print(n)
    if r is None:
        print("result: no words found in the main content; not measured")
        return 1
    print(f"words: {r['words']}  sentences: {r['sentences']}  syllables: {r['syllables']} (estimated by rule)")
    print(f"words per sentence: {r['words_per_sentence']:.1f}  syllables per word: {r['syllables_per_word']:.2f}")
    print(f"Flesch-Kincaid Grade Level: {r['grade']:.1f} (target {args.target:g}: "
          f"{'above' if r['grade'] > args.target else 'at or below'})")
    if r["words"] < 100:
        print("note: fewer than 100 words; the score means little on so short a text")
    print("a signal, not a verdict: a person still reads the text (knowledge/content/reading-level.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
