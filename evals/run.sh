#!/usr/bin/env bash
# Run the verifier on evals, headless, one fresh Claude Code session per eval (roadmap 4.3).
#
# Usage, from the repo root:
#   evals/run.sh                         every eval with an input.html
#   evals/run.sh 001-missing-label 010-small-targets
#   evals/run.sh -j 4 -o /tmp/reports    4 at a time, reports in /tmp/reports
#
# Each eval gets its own `claude -p` session, so no run sees another's answer. The
# session uses the registered `verifier` agent and is told not to open expected.md,
# RESULTS.md, or run files, and not to edit files. Reports go outside the repo by
# default: one <eval>.md per eval and an index.md listing each eval's finding
# headings and axe line, so a person can read them against expected.md in one sitting.
# Nothing here grades the reports; that is roadmap 4.4.
#
# Needs: the `claude` CLI, signed in. For axe, Node.js on PATH or DOCTOR_A11Y_NODE_DIR
# (tools/axe.py). Each session costs a verifier run's worth of tokens.

set -u
cd "$(dirname "$0")/.." || exit 1

jobs=3
out="${TMPDIR:-${TEMP:-/tmp}}/doctor-a11y-evals/$(date +%Y%m%d-%H%M%S)"
while getopts "j:o:h" opt; do
  case $opt in
    j) jobs=$OPTARG ;;
    o) out=$OPTARG ;;
    h) sed -n '2,16p' "$0"; exit 0 ;;
    *) exit 2 ;;
  esac
done
shift $((OPTIND - 1))

command -v claude >/dev/null || { echo "claude CLI not found"; exit 2; }

if [ $# -gt 0 ]; then
  evals=("$@")
else
  evals=()
  for f in evals/*/input.html; do evals+=("$(basename "$(dirname "$f")")"); done
fi
mkdir -p "$out"

run_one() {
  e=$1; out=$2
  [ -f "evals/$e/input.html" ] || { echo "skipped: no input.html" > "$out/$e.md"; return; }
  prompt="Use the verifier agent on evals/$e/input.html. Tell it not to open any expected.md, evals/RESULTS.md, or any run-*.md file, and not to edit files. Reply with the verifier's full report exactly as it returns it, and nothing else."
  start=$(date +%s)
  claude -p "$prompt" --allowedTools "Read,Glob,Grep,Bash,PowerShell,Task,Agent" --output-format text > "$out/$e.md" 2>&1
  status=$?
  echo "$e|$status|$(( $(date +%s) - start ))" > "$out/$e.status"
}
export -f run_one

printf '%s\n' "${evals[@]}" | xargs -P "$jobs" -I{} bash -c 'run_one "$1" "$2"' _ {} "$out"

{
  echo "# Eval reports, $(date '+%Y-%m-%d %H:%M')"
  echo
  echo "Commit $(git rev-parse --short HEAD). One fresh \`claude -p\` session per eval, registered verifier. Read each report against \`evals/<eval>/expected.md\`."
  echo
  for e in "${evals[@]}"; do
    IFS='|' read -r _ status secs < "$out/$e.status" 2>/dev/null || { status="?"; secs="?"; }
    echo "## $e"
    echo
    echo "- Report: \`$e.md\` (exit $status, ${secs}s). Key: \`evals/$e/expected.md\`."
    grep -E '^#{2,4} \[' "$out/$e.md" | sed 's/^#* /- Finding: /' | head -8
    axe=$(grep -m1 -E 'axe-core [0-9]+[.][0-9]+' "$out/$e.md" || grep -m1 -iE 'axe: not run|^\*?\*?not run' "$out/$e.md")
    axe=$(printf '%s' "$axe" | tr -d '*`' | sed 's/^[- ]*//' | cut -c1-160)
    echo "- axe: ${axe:-no axe line found}"
    echo
  done
} > "$out/index.md"

echo "reports: $out"
echo "index:   $out/index.md"
