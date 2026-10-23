#!/usr/bin/env bash
# Run evals headless, one fresh Claude Code session per eval (roadmap 4.3).
#
# Usage, from the repo root:
#   evals/run.sh                         every page eval (input.html)
#   evals/run.sh -s                      every skill eval (request.md or text.md)
#   evals/run.sh -a                      both
#   evals/run.sh 001-missing-label 015-consult-events-carousel
#   evals/run.sh -j 4 -o /tmp/reports    4 at a time, reports in /tmp/reports
#
# Each eval gets its own `claude -p` session, so no run sees another's answer. A page
# eval uses the registered `verifier` agent. A skill eval loads the skill its folder
# names (015-consult-... loads consult) and answers request.md or text.md. Every
# session is told not to open expected.md, RESULTS.md, or run files, and gets no
# Write or Edit tool. Reports go outside the repo by default: one <eval>.md per eval
# and an index.md, so a person can read them against expected.md in one sitting.
# evals/check.py grades them (roadmap 4.4).
#
# Needs: the `claude` CLI, signed in. For axe, Node.js on PATH or DOCTOR_A11Y_NODE_DIR
# (tools/axe.py). Each session costs a verifier run's worth of tokens.

set -u
cd "$(dirname "$0")/.." || exit 1

jobs=3
out="${TMPDIR:-${TEMP:-/tmp}}/doctor-a11y-evals/$(date +%Y%m%d-%H%M%S)"
kinds="page"
while getopts "j:o:sah" opt; do
  case $opt in
    j) jobs=$OPTARG ;;
    o) out=$OPTARG ;;
    s) kinds="skill" ;;
    a) kinds="page skill" ;;
    h) sed -n '2,19p' "$0"; exit 0 ;;
    *) exit 2 ;;
  esac
done
shift $((OPTIND - 1))

command -v claude >/dev/null || { echo "claude CLI not found"; exit 2; }

if [ $# -gt 0 ]; then
  evals=("$@")
else
  evals=()
  for d in evals/[0-9]*/; do
    e=$(basename "$d")
    if [ -f "$d/input.html" ]; then k=page; elif [ -f "$d/request.md" ] || [ -f "$d/text.md" ]; then k=skill; else continue; fi
    case " $kinds " in *" $k "*) evals+=("$e") ;; esac
  done
fi
mkdir -p "$out"

# The skill an eval tests is the first part of its folder name after the number that
# names a skill: 015-consult-..., 019-at-test-protocol-..., 023-content-....
skill_of() {
  for s in at-test-protocol html-patterns react-jsx consult planning content design wcag; do
    case "${1#[0-9][0-9][0-9]-}" in "$s"-*) echo "$s"; return ;; esac
  done
}
export -f skill_of

run_one() {
  e=$1; out=$2
  off="Do not open any expected.md, evals/RESULTS.md, or any run-*.md file, and do not create or edit files."
  if [ -f "evals/$e/input.html" ]; then
    prompt="Use the verifier agent on evals/$e/input.html. Tell it not to open any expected.md, evals/RESULTS.md, or any run-*.md file, and not to edit files. Reply with the verifier's full report exactly as it returns it, and nothing else."
    tools="Read,Glob,Grep,Bash,PowerShell,Task,Agent"
  else
    in=request.md; [ -f "evals/$e/text.md" ] && in=text.md
    s=$(skill_of "$e")
    [ -n "$s" ] || { echo "skipped: no skill named in the folder name" > "$out/$e.md"; return; }
    prompt="Load the $s skill (.claude/skills/$s/SKILL.md) and follow it. Then read evals/$e/$in: it holds what the developer types and the project context. Treat that context as the project's a11y-spec, and answer the developer as the skill directs, in full. $off"
    tools="Read,Glob,Grep,Bash,PowerShell,Skill"
  fi
  start=$(date +%s)
  claude -p "$prompt" --allowedTools "$tools" --disallowedTools "Write,Edit,NotebookEdit" --output-format text > "$out/$e.md" 2>&1
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
    if [ -f "evals/$e/input.html" ]; then
      grep -E '^#{2,4} \[' "$out/$e.md" | sed 's/^#* /- Finding: /' | head -8
      axe=$(grep -m1 -E 'axe-core [0-9]+[.][0-9]+' "$out/$e.md" || grep -m1 -iE 'axe: not run|^\*?\*?not run' "$out/$e.md")
      axe=$(printf '%s' "$axe" | tr -d '*`' | sed 's/^[- ]*//' | cut -c1-160)
      echo "- axe: ${axe:-no axe line found}"
    else
      echo "- Skill: $(skill_of "$e"). $(wc -w < "$out/$e.md" | tr -d ' ') words."
      grep -E '^#{1,3} ' "$out/$e.md" | sed 's/^#* /- Section: /' | head -8
    fi
    echo
  done
} > "$out/index.md"

echo "reports: $out"
echo "index:   $out/index.md"
