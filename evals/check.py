"""Grade verifier reports from evals/run.sh against each eval's expected.md (roadmap 4.4).

Usage, from the repo root:
    python evals/check.py <reports-dir> [--no-judge] [-j 4]

Two checks per eval; both must pass.

1. Mechanical, in Python. From expected.md: finding 1's criterion (the first
   "SC x.y.z" on its Criterion line), its level, and the confidences the pass
   condition allows (finding 1's bracket, plus any confidence the pass-condition
   paragraph names). The report passes if some finding heading
   ("### [Definite] ...") is at an allowed confidence and its block names that
   criterion, "Level <level>", and "tier 1".
2. Judge, for the rest of the key: the must-not list and the pass condition. A fresh
   `claude -p` session with no tools gets only the key and the report, inline, and
   must answer "VERDICT: PASS" or "VERDICT: FAIL" with a quoted report line behind
   each failure. Skip it with --no-judge.

Writes checks.md in the reports folder and prints the table. Exit 0 if every eval
passes, 1 otherwise. Transcript and text evals are not covered (no report from run.sh).
"""

import argparse
import concurrent.futures
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF = {"definite": "Definite", "likely": "Likely", "manual review": "Manual review"}

JUDGE = """You are grading an accessibility verifier's report against an answer key. Read the key and the report below. Judge only what is written; do not use outside knowledge about the page.

The report passes if:
- the key's "Pass condition" is met, and
- nothing on the key's "Must not" list appears in the report as a finding. A note that the key's "Also acceptable" list allows does not count against it. A manual-review note saying a criterion appears met is not "reporting" that criterion.

Answer in this exact shape, and nothing else:
VERDICT: PASS
or
VERDICT: FAIL
then one line per reason, each quoting the report line it rests on.

=== ANSWER KEY (expected.md) ===
{key}

=== VERIFIER REPORT ===
{report}
"""


def parse_key(text):
    m = re.search(r"^1\.\s+(.*)$", text, re.M)
    head = m.group(1) if m else ""
    confs = [c.strip().lower() for c in re.findall(r"\[([^\]]+)\]", head.split("**")[0] + "**".join(head.split("**")[:4]))]
    crit = re.search(r"Criterion:.*?SC (\d+\.\d+\.\d+)[^\n]*?\(Level (A{1,3})\)", text)
    pc = re.search(r"## Pass condition\s*\n(.*?)(\n## |\Z)", text, re.S)
    pass_text = pc.group(1).lower() if pc else ""
    allowed = set(confs)
    for word in CONF:
        # A confidence the pass condition names, unless it is ruled out ("it is not definite").
        for m in re.finditer(rf"\b{word}\b", pass_text):
            if not re.search(r"\bnot\s+(?:be\s+|as\s+|at\s+)?$", pass_text[max(0, m.start() - 12):m.start()]):
                allowed.add(word)
    # A confidence the "Also acceptable" list allows, such as "downgrades to Likely".
    also = re.search(r"## Also acceptable\s*\n(.*?)(\n## |\Z)", text, re.S)
    for m in re.finditer(r"downgrades? (?:it )?to (likely|manual review)", also.group(1).lower() if also else ""):
        allowed.add(m.group(1))
    return {"sc": crit.group(1) if crit else None, "level": crit.group(2) if crit else None,
            "allowed": {a for a in allowed if a in CONF}}


def findings(report):
    """(confidence, block text) for each finding heading in the report."""
    parts = re.split(r"^(#{2,4} \[[^\]]+\][^\n]*)$", report, flags=re.M)
    out = []
    for i in range(1, len(parts), 2):
        head, body = parts[i], parts[i + 1] if i + 1 < len(parts) else ""
        m = re.match(r"#{2,4} \[([^\]]+)\]", head)
        conf = m.group(1).strip().lower()
        conf = next((c for c in CONF if conf.startswith(c)), conf)
        out.append((conf, head + body))
    return out


def mechanical(key, report):
    if not key["sc"]:
        # A practice-only key (no Criterion line): check the confidence; the judge checks the rest.
        got = [c for c, _ in findings(report) if c in key["allowed"]]
        if got:
            return True, f"no criterion in the key (practice finding); a finding at {got[0]} is present"
        return False, f"no finding at an allowed confidence ({', '.join(sorted(key['allowed']))})"
    sc_re = re.compile(rf"(?<![\d.]){re.escape(key['sc'])}(?![\d])")
    lvl_re = re.compile(rf"Level {key['level']}(?!A)")
    seen = []
    for conf, block in findings(report):
        if sc_re.search(block):
            seen.append(conf)
            if conf in key["allowed"] and lvl_re.search(block) and re.search(r"tier 1", block, re.I):
                return True, f"SC {key['sc']} (Level {key['level']}), tier 1, at {conf}"
    if seen:
        return False, (f"SC {key['sc']} found at {', '.join(seen)}, but an allowed confidence "
                       f"({', '.join(sorted(key['allowed']))}) with level and tier was not")
    return False, f"no finding names SC {key['sc']}"


def judge(key_text, report):
    prompt = JUDGE.format(key=key_text, report=report)
    p = subprocess.run(["claude", "-p", "--output-format", "text", "--allowedTools", ""],
                       input=prompt, capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (p.stdout or "").strip()
    m = re.search(r"VERDICT:\s*(PASS|FAIL)", out)
    if not m:
        return False, "judge gave no verdict: " + out[:200].replace("\n", " ")
    reasons = " ".join(l.strip() for l in out[m.end():].splitlines() if l.strip())
    return m.group(1) == "PASS", reasons[:600] or "no reasons given"


def check(name, reports_dir, use_judge):
    report_path = os.path.join(reports_dir, f"{name}.md")
    key_path = os.path.join(ROOT, "evals", name, "expected.md")
    report = open(report_path, encoding="utf-8").read()
    key_text = open(key_path, encoding="utf-8").read()
    mech_ok, mech_why = mechanical(parse_key(key_text), report)
    if use_judge:
        judge_ok, judge_why = judge(key_text, report)
    else:
        judge_ok, judge_why = True, "not run (--no-judge)"
    return name, mech_ok, mech_why, judge_ok, judge_why


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("reports")
    ap.add_argument("--no-judge", action="store_true")
    ap.add_argument("-j", type=int, default=4)
    args = ap.parse_args(argv)
    names = sorted(f[:-3] for f in os.listdir(args.reports)
                   if f.endswith(".md") and f != "index.md" and f != "checks.md"
                   and os.path.exists(os.path.join(ROOT, "evals", f[:-3], "expected.md")))
    with concurrent.futures.ThreadPoolExecutor(args.j) as pool:
        results = list(pool.map(lambda n: check(n, args.reports, not args.no_judge), names))
    lines = ["# Eval checks", "", f"Reports: `{args.reports}`. Mechanical: criterion, level, tier, confidence. "
             "Judge: must-not list and pass condition (fresh `claude -p`, no tools).", "",
             "| Eval | Result | Mechanical | Judge |", "|---|---|---|---|"]
    failed = 0
    for name, mok, mwhy, jok, jwhy in results:
        ok = mok and jok
        failed += not ok
        cell = lambda good, why: ("pass: " if good else "**fail**: ") + why.replace("|", "/")
        lines.append(f"| {name} | {'PASS' if ok else '**FAIL**'} | {cell(mok, mwhy)} | {cell(jok, jwhy)} |")
    lines += ["", f"{len(results) - failed} of {len(results)} passed."]
    text = "\n".join(lines) + "\n"
    open(os.path.join(args.reports, "checks.md"), "w", encoding="utf-8", newline="\n").write(text)
    print(text)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
