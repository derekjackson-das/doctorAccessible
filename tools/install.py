#!/usr/bin/env python3
"""Install Doctor Accessible into a project folder (the interim route until the plugin, roadmap 5.4).

Usage, from the repo root:
    python3 tools/install.py <project-folder>            dry run: shows the plan, writes nothing
    python3 tools/install.py <project-folder> --apply    writes the files
    python3 tools/install.py <project-folder> -v         also lists every file

It copies .claude/, knowledge/, tools/, templates/, docs/content-standards.md, and
docs/principles.md. It creates a11y-spec.md from the template if the project has none.
It never creates or changes CLAUDE.md, and it never overwrites a11y-spec.md.

Running it again is the update. For each library file:
- missing in the project: copied.
- already the same as the repo: left alone.
- changed in the repo, and still exactly as this tool last wrote it: updated.
- changed in the project (a local edit), or present but never installed by this tool:
  skipped and listed, so nothing you wrote is overwritten.
- no longer in the repo: listed, and left in place.

The tool records what it wrote in .doctor-accessible.json at the project root: a SHA-256
per file and the repo commit it came from. Commit that file with the project.

Standard library only.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LIBRARY_DIRS = [".claude", "knowledge", "tools", "templates"]
LIBRARY_FILES = ["docs/content-standards.md", "docs/principles.md"]
SPEC_TEMPLATE = "templates/a11y-spec.md"
SPEC_NAME = "a11y-spec.md"
MANIFEST_NAME = ".doctor-accessible.json"
IGNORE = {"__pycache__", ".DS_Store", "settings.local.json"}  # local machine files, never shared


class InstallError(Exception):
    pass


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_repo(repo):
    missing = [p for p in LIBRARY_DIRS + LIBRARY_FILES + [SPEC_TEMPLATE]
               if not os.path.exists(os.path.join(repo, p))]
    if missing:
        raise InstallError("this is not a Doctor Accessible repo; missing: " + ", ".join(missing))


def check_target(repo, target):
    if not os.path.isdir(target):
        raise InstallError(f"project folder does not exist: {target} (create it first)")
    if target == repo or target.startswith(repo + os.sep):
        raise InstallError("install into a project folder, not into the Doctor Accessible repo itself")


def library_files(repo):
    """Repo-relative paths of every file the install copies, sorted."""
    found = []
    for d in LIBRARY_DIRS:
        for root, dirs, files in os.walk(os.path.join(repo, d)):
            dirs[:] = [x for x in dirs if x not in IGNORE]
            for name in files:
                if name in IGNORE or name.endswith(".pyc"):
                    continue
                found.append(os.path.relpath(os.path.join(root, name), repo))
    found.extend(LIBRARY_FILES)
    return sorted(found)


def load_manifest(target):
    path = os.path.join(target, MANIFEST_NAME)
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f).get("files", {})
    except (OSError, ValueError) as err:
        raise InstallError(f"cannot read {MANIFEST_NAME}: {err}")


def repo_version(repo):
    """The repo's short commit, marked -dirty if the working tree has changes."""
    try:
        commit = subprocess.run(["git", "-C", repo, "rev-parse", "--short", "HEAD"],
                                capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(["git", "-C", repo, "status", "--porcelain"],
                               capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return commit + ("-dirty" if dirty else "")


def make_plan(repo, target, manifest):
    """Return (actions, retired, spec_action). actions is a list of (action, rel, new_hash)."""
    files = library_files(repo)
    actions = []
    for rel in files:
        new = sha256(os.path.join(repo, rel))
        dst = os.path.join(target, rel)
        if not os.path.exists(dst):
            action = "copy"
        else:
            current = sha256(dst)
            if current == new:
                action = "unchanged"
            elif manifest.get(rel) == current:
                action = "update"
            else:
                action = "skip"
        actions.append((action, rel, new))
    retired = sorted(p for p in manifest if p not in set(files))
    spec_action = "keep" if os.path.exists(os.path.join(target, SPEC_NAME)) else "create"
    return actions, retired, spec_action


def apply_plan(repo, target, manifest, actions, retired, spec_action, version):
    new_manifest = {}
    for action, rel, new in actions:
        if action in ("copy", "update"):
            dst = os.path.join(target, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(os.path.join(repo, rel), dst)
        if action in ("copy", "update", "unchanged"):
            new_manifest[rel] = new
        elif action == "skip" and rel in manifest:
            new_manifest[rel] = manifest[rel]  # still the last thing we wrote; keep it
    if spec_action == "create":
        shutil.copyfile(os.path.join(repo, SPEC_TEMPLATE), os.path.join(target, SPEC_NAME))
    data = {"installed_from": version, "files": dict(sorted(new_manifest.items()))}
    with open(os.path.join(target, MANIFEST_NAME), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def report(target, actions, retired, spec_action, applied, verbose):
    counts = Counter(action for action, _, _ in actions)
    mode = "Installed into" if applied else "Dry run, nothing written, into"
    print(f"{mode} {target}")
    if verbose:
        for action, rel, _ in actions:
            print(f"  {action:<9} {rel}")
    for rel in retired:
        print(f"  retired   {rel}  (no longer in the repo; left in place)")
    skipped = [rel for action, rel, _ in actions if action == "skip"]
    for rel in skipped:
        print(f"  skipped   {rel}  (differs from the library; not overwritten)")
    print()
    print(f"copy {counts['copy']}, update {counts['update']}, unchanged {counts['unchanged']}, "
          f"skipped {counts['skip']}, retired {len(retired)}")
    print(f"{SPEC_NAME}: {'created from the template' if spec_action == 'create' else 'kept (already exists)'}")
    if not applied:
        print("Run again with --apply to write these files.")
    elif skipped:
        print("Skipped files differ from the library. Compare them with the repo copy, merge by hand, "
              "then run again.")


def main(argv=None, repo=REPO):
    parser = argparse.ArgumentParser(description="Install Doctor Accessible into a project folder.")
    parser.add_argument("project", help="project folder to install into (must already exist)")
    parser.add_argument("--apply", action="store_true", help="write the files (default is a dry run)")
    parser.add_argument("-v", "--verbose", action="store_true", help="list every file")
    args = parser.parse_args(argv)
    try:
        repo = os.path.realpath(repo)
        check_repo(repo)
        target = os.path.realpath(os.path.expanduser(args.project))
        check_target(repo, target)
        manifest = load_manifest(target)
        actions, retired, spec_action = make_plan(repo, target, manifest)
        if args.apply:
            apply_plan(repo, target, manifest, actions, retired, spec_action, repo_version(repo))
        report(target, actions, retired, spec_action, args.apply, args.verbose)
    except InstallError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
