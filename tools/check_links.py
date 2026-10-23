"""Check every link and every repo path named in the library's Markdown.

Usage, from the repo root:
    python tools/check_links.py [--no-web]

Scans the Markdown in knowledge/, .claude/, docs/, templates/, evals/*/expected.md, and
the top-level README.md, CONTRIBUTING.md, and CLAUDE.md. Two checks:

- Paths: every backticked path such as `knowledge/wcag/sc-1.1.1-non-text-content.md`,
  `wcag/sc-1.1.1-...md` (read from knowledge/), `docs/...`, `tools/...`, `evals/...`,
  `templates/...`, or `.claude/...` must exist. Placeholders (<name>, x.x.x, ..., *)
  are skipped.
- Links: every http(s) URL is requested (HEAD, then GET) and must answer below 400.
  Some sites refuse scripts (403 or 429); those are listed apart, not counted as broken.

Run records (run-*.md), RESULTS.md, and baselines are history and are not scanned; the
roadmap's paths are planned deliverables and are not checked.
Exit 0 if nothing is broken.
"""

import concurrent.futures
import glob
import os
import re
import sys
import time
import urllib.parse
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_DIRS = ("wcag", "aria", "html", "patterns", "ux", "coga", "design", "content", "testing")
PATH_RE = re.compile(r"`((?:knowledge/|\.claude/|docs/|tools/|evals/|templates/|(?:%s)/)[^`\s]+?)`" % "|".join(KNOWLEDGE_DIRS))
URL_RE = re.compile(r"https?://[^\s)>\]`\"'|]+")
REFUSING = {401, 403, 405, 429, 999}


def files():
    pats = ["knowledge/**/*.md", ".claude/**/*.md", "docs/**/*.md", "templates/**/*.md",
            "evals/*/expected.md", "evals/README.md", "tools/README.md",
            "README.md", "CONTRIBUTING.md", "CLAUDE.md"]
    out = set()
    for p in pats:
        out.update(glob.glob(os.path.join(ROOT, p), recursive=True))
    return sorted(out)


def resolve(path):
    path = path.rstrip(".,;:")
    if re.search(r"[<>*]|x\.x\.x|\.\.\.|NNN|YYYY", path):
        return None
    first = path.split("/")[0]
    full = os.path.join(ROOT, "knowledge", path) if first in KNOWLEDGE_DIRS else os.path.join(ROOT, path)
    return full


def status(url):
    for attempt in range(3):
        s = _status(url)
        if s != 429:
            return s
        time.sleep(5 * (attempt + 1))                 # rate-limited: back off and retry
    return s


def _status(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": "Mozilla/5.0 doctor-a11y-link-check"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405, 501):
                last = e.code
                if method == "GET":
                    return last
        except Exception as e:  # network error, timeout
            last = type(e).__name__
    return last


def main(argv=None):
    web = "--no-web" not in (argv or sys.argv[1:])
    bad_paths, urls = [], {}
    for f in files():
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        text = open(f, encoding="utf-8").read()
        for m in PATH_RE.finditer(text if rel != "docs/ROADMAP.md" else ""):  # the roadmap names planned files
            full = resolve(m.group(1))
            if full and not os.path.exists(full.split("#")[0]):
                bad_paths.append((rel, m.group(1)))
        for u in URL_RE.findall(text):
            u = u.rstrip(".,;:")
            urls.setdefault(u, rel)
    print(f"files scanned: {len(files())}")
    print(f"missing paths: {len(bad_paths)}")
    for rel, p in bad_paths:
        print(f"  {rel}: `{p}`")
    if not web:
        return 1 if bad_paths else 0
    # One request per page (anchors dropped), one host at a time per worker, with a pause,
    # so W3C and others do not rate-limit the check.
    pages = {}
    for u, rel in urls.items():
        pages.setdefault(u.split("#")[0], rel)
    by_host = {}
    for u in pages:
        by_host.setdefault(urllib.parse.urlparse(u).netloc, []).append(u)

    def run_host(us):
        out = {}
        for u in us:
            out[u] = status(u)
            time.sleep(0.5)
        print(f"  checked {urllib.parse.urlparse(us[0]).netloc}: {len(us)}", file=sys.stderr, flush=True)
        return out

    results = {}
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        for part in pool.map(run_host, by_host.values()):
            results.update(part)
    urls = pages
    broken = [(u, s) for u, s in results.items() if not (isinstance(s, int) and (s < 400 or s in REFUSING))]
    refused = [(u, s) for u, s in results.items() if isinstance(s, int) and s in REFUSING]
    print(f"urls checked: {len(urls)}   broken: {len(broken)}   refused scripts (not counted): {len(refused)}")
    for u, s in sorted(broken):
        print(f"  {s}  {u}  (first in {urls[u]})")
    for u, s in sorted(refused):
        print(f"  refused {s}  {u}")
    return 1 if (bad_paths or broken) else 0


if __name__ == "__main__":
    sys.exit(main())
