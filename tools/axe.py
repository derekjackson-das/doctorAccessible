"""Run axe on a page with the WCAG 2.2 tags and print every result bucket.

Usage:
    python tools/axe.py <file-or-url> [--out-dir DIR]

Runs `npx --yes @axe-core/cli <url> --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa --stdout`.
The default axe run skips rules tagged for WCAG 2.2, so the tags are always passed
(evals/README.md). The raw JSON is saved outside the repository, in a temporary
directory, and its path is printed. Then the axe version, the violations and
incomplete results in full (rule, impact, tags, targets, failure summary), and the
counts of passes and inapplicable rules are printed, for the verifier to paste into
its report. A clean run is not a pass (.claude/agents/verifier.md).

Setup problems it handles:
- No `npx`: prints "axe: not run" with the reason and exits 2. Set DOCTOR_A11Y_NODE_DIR
  to a folder holding npx if Node.js is installed somewhere not on PATH.
- On Windows, the paths `npx browser-driver-manager install chrome` writes to
  ~/.browser-driver-manager/.env can be read back wrongly by axe (a `\\r` in a user
  folder name becomes a line break). This script reads that file itself and passes
  `--chromedriver-path` and `--chrome-path` with forward slashes.
"""

import argparse
import datetime
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

TAGS = "wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa"


def find_npx():
    for name in ("npx", "npx.cmd"):
        found = shutil.which(name)
        if found:
            return found
    folder = os.environ.get("DOCTOR_A11Y_NODE_DIR")
    if folder:
        for name in ("npx.cmd", "npx"):
            p = os.path.join(folder, name)
            if os.path.exists(p):
                return p
    return None


def driver_flags():
    """Chrome and ChromeDriver paths from browser-driver-manager, if it was run."""
    env = pathlib.Path.home() / ".browser-driver-manager" / ".env"
    if not env.exists():
        return []
    values = {}
    for line in env.read_text(encoding="utf-8").splitlines():
        m = re.match(r'\s*(\w+)\s*=\s*"?([^"]*)"?\s*$', line)
        if m:
            values[m.group(1)] = m.group(2)
    flags = []
    for key, flag in (("CHROMEDRIVER_TEST_PATH", "--chromedriver-path"), ("CHROME_TEST_PATH", "--chrome-path")):
        path = values.get(key)
        if path and os.path.exists(path):
            flags += [flag, path.replace("\\", "/")]
    return flags


def to_url(target):
    if re.match(r"^[a-z]+://", target, re.I):
        return target
    return pathlib.Path(target).resolve().as_uri()


def brief(result):
    return {
        "id": result.get("id"),
        "impact": result.get("impact"),
        "tags": [t for t in result.get("tags", []) if t.startswith("wcag")],
        "help": result.get("help"),
        "helpUrl": result.get("helpUrl"),
        "nodes": [{"target": n.get("target"), "failureSummary": n.get("failureSummary")}
                  for n in result.get("nodes", [])],
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description="Run axe with WCAG 2.2 tags and print every bucket.")
    ap.add_argument("target", help="an HTML file or a URL")
    ap.add_argument("--out-dir", default=os.path.join(tempfile.gettempdir(), "doctor-a11y-axe"),
                    help="where to save the raw JSON (default: a temp folder, never the repo)")
    args = ap.parse_args(argv)

    npx = find_npx()
    if not npx:
        print("axe: not run: npx not found (Node.js is not installed or not on PATH; "
              "set DOCTOR_A11Y_NODE_DIR if it is installed elsewhere)")
        return 2
    url = to_url(args.target)
    cmd = [npx, "--yes", "@axe-core/cli", url, "--tags", TAGS, "--stdout"] + driver_flags()
    env = dict(os.environ)
    env["PATH"] = os.path.dirname(npx) + os.pathsep + env.get("PATH", "")  # npx needs node beside it
    # Parallel `npx --yes` runs race on the npm cache (seen as MODULE_NOT_FOUND from npx-cli.js
    # when evals/run.sh ran six at once), so scans take turns through a lock file, and retry once.
    os.makedirs(args.out_dir, exist_ok=True)
    lock = os.path.join(args.out_dir, ".axe.lock")
    for _ in range(600):
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError:
            if time.time() - os.path.getmtime(lock) > 300:
                os.remove(lock)                      # a stale lock from a crashed run
            time.sleep(1)
    else:
        fd = None
    try:
        for attempt in range(2):
            proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
            if "MODULE_NOT_FOUND" not in (proc.stderr + proc.stdout) or attempt:
                break
            time.sleep(3)
    finally:
        if fd is not None:
            os.close(fd)
            os.remove(lock)
    out = proc.stdout.strip()
    start = out.find("[")
    try:
        data = json.loads(out[start:]) if start >= 0 else None
    except json.JSONDecodeError:
        data = None
    if not data:
        print("axe: not run: the scan did not return results")
        print("command:", " ".join(cmd))
        err = (proc.stderr or out).strip().splitlines()
        print("error:", "\n       ".join(err[-8:]) if err else "(none)")
        return 3

    os.makedirs(args.out_dir, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    t = pathlib.Path(args.target)
    name = t.parent.name if t.stem in ('input', 'index') and t.parent.name else (t.stem or 'page')
    raw_path = os.path.join(args.out_dir, f"{name}-{stamp}.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    r = data[0]
    engine = r.get("testEngine", {})
    runner = r.get("testRunner", {})
    print(f"axe-core {engine.get('version', '?')} via @axe-core/cli ({runner.get('name', '?')}), tags {TAGS}")
    print(f"page: {r.get('url', url)}")
    print(f"raw JSON: {raw_path}")
    for bucket in ("violations", "incomplete"):
        items = r.get(bucket, [])
        print(f"\n{bucket}: {len(items)}")
        for it in items:
            tags = ", ".join(t for t in it.get("tags", []) if t.startswith("wcag")) or "no wcag tag"
            print(f"  - {it.get('id')} ({it.get('impact') or 'no impact'}; {tags}): {it.get('help')}")
            for n in it.get("nodes", []):
                print(f"      at {' '.join(map(str, n.get('target', [])))}")
    print(f"\npasses: {len(r.get('passes', []))} rules   inapplicable: {len(r.get('inapplicable', []))} rules")
    print("\nraw (violations and incomplete):")
    print(json.dumps({"violations": [brief(x) for x in r.get("violations", [])],
                      "incomplete": [brief(x) for x in r.get("incomplete", [])]}, indent=2))
    print("\na clean run is not a pass: read the code as well (.claude/agents/verifier.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
