"""Checks tools/install.py against a fake repo in a temporary folder.

Run: python -m unittest tools/test_install.py   (from the repo root)

The real repo is never written to. Each test builds a small fake repo with the same
layout, installs into a fresh project folder, then changes the fake repo or the project
and checks what the tool plans and writes.
"""

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import install as inst  # noqa: E402

SOURCE = {
    ".claude/agents/verifier.md": "agent v1\n",
    ".claude/skills/wcag/SKILL.md": "skill v1\n",
    "knowledge/INDEX.md": "index v1\n",
    "tools/install.py": "# installer\n",
    "tools/__pycache__/install.cpython-313.pyc": "junk",
    ".claude/settings.local.json": "{\"personal\": true}\n",
    "templates/a11y-spec.md": "# Accessibility spec: <project name>\n",
    "docs/content-standards.md": "standards v1\n",
    "docs/principles.md": "principles v1\n",
    # Not part of the library: must never be copied.
    "README.md": "readme\n",
    "docs/ROADMAP.md": "roadmap\n",
}


def write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as f:
        return f.read()


def run(repo, project, *args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
        code = inst.main([project, *args], repo=repo)
    return code, out.getvalue()


class InstallTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = os.path.realpath(self._tmp.name)
        self.repo = os.path.join(self.root, "repo")
        self.project = os.path.join(self.root, "project")
        os.makedirs(self.repo)
        os.makedirs(self.project)
        for rel, text in SOURCE.items():
            write(self.repo, rel, text)

    def tearDown(self):
        self._tmp.cleanup()

    def actions(self):
        manifest = inst.load_manifest(self.project)
        actions, retired, _ = inst.make_plan(self.repo, self.project, manifest)
        return {rel: action for action, rel, _ in actions}, retired

    def test_fresh_install_copies_library_and_creates_spec(self):
        code, _ = run(self.repo, self.project, "--apply")
        self.assertEqual(code, 0)
        self.assertEqual(read(self.project, ".claude/agents/verifier.md"), "agent v1\n")
        self.assertEqual(read(self.project, "docs/principles.md"), "principles v1\n")
        self.assertEqual(read(self.project, "templates/a11y-spec.md"), SOURCE["templates/a11y-spec.md"])
        self.assertEqual(read(self.project, "a11y-spec.md"), SOURCE["templates/a11y-spec.md"])

    def test_non_library_files_and_pycache_are_not_copied(self):
        run(self.repo, self.project, "--apply")
        self.assertFalse(os.path.exists(os.path.join(self.project, "README.md")))
        self.assertFalse(os.path.exists(os.path.join(self.project, "docs", "ROADMAP.md")))
        self.assertFalse(os.path.exists(os.path.join(self.project, "tools", "__pycache__")))
        self.assertFalse(os.path.exists(os.path.join(self.project, ".claude", "settings.local.json")))

    def test_dry_run_writes_nothing(self):
        code, out = run(self.repo, self.project)
        self.assertEqual(code, 0)
        self.assertEqual(os.listdir(self.project), [])
        self.assertIn("Dry run", out)

    def test_rerun_leaves_everything_unchanged(self):
        run(self.repo, self.project, "--apply")
        actions, retired = self.actions()
        self.assertEqual(set(actions.values()), {"unchanged"})
        self.assertEqual(retired, [])

    def test_untouched_file_is_updated_when_repo_changes(self):
        run(self.repo, self.project, "--apply")
        write(self.repo, ".claude/agents/verifier.md", "agent v2\n")
        actions, _ = self.actions()
        self.assertEqual(actions[".claude/agents/verifier.md"], "update")
        run(self.repo, self.project, "--apply")
        self.assertEqual(read(self.project, ".claude/agents/verifier.md"), "agent v2\n")

    def test_local_edit_is_skipped_and_kept(self):
        run(self.repo, self.project, "--apply")
        write(self.project, "knowledge/INDEX.md", "index, edited by Derek\n")
        write(self.repo, "knowledge/INDEX.md", "index v2\n")
        actions, _ = self.actions()
        self.assertEqual(actions["knowledge/INDEX.md"], "skip")
        run(self.repo, self.project, "--apply")
        self.assertEqual(read(self.project, "knowledge/INDEX.md"), "index, edited by Derek\n")

    def test_preexisting_file_not_installed_by_tool_is_skipped(self):
        write(self.project, "docs/principles.md", "our own copy\n")
        actions, _ = self.actions()
        self.assertEqual(actions["docs/principles.md"], "skip")
        run(self.repo, self.project, "--apply")
        self.assertEqual(read(self.project, "docs/principles.md"), "our own copy\n")

    def test_existing_spec_is_never_overwritten(self):
        write(self.project, "a11y-spec.md", "# Our spec, filled in\n")
        run(self.repo, self.project, "--apply")
        self.assertEqual(read(self.project, "a11y-spec.md"), "# Our spec, filled in\n")

    def test_project_claude_md_is_never_touched(self):
        write(self.project, "CLAUDE.md", "mine\n")
        run(self.repo, self.project, "--apply")
        self.assertEqual(read(self.project, "CLAUDE.md"), "mine\n")

    def test_retired_file_is_reported_and_left_in_place(self):
        run(self.repo, self.project, "--apply")
        os.remove(os.path.join(self.repo, ".claude/skills/wcag/SKILL.md"))
        _, retired = self.actions()
        self.assertEqual(retired, [".claude/skills/wcag/SKILL.md"])
        run(self.repo, self.project, "--apply")
        self.assertTrue(os.path.exists(os.path.join(self.project, ".claude/skills/wcag/SKILL.md")))
        manifest = inst.load_manifest(self.project)
        self.assertNotIn(".claude/skills/wcag/SKILL.md", manifest)

    def test_manifest_records_hashes_and_source(self):
        run(self.repo, self.project, "--apply")
        with open(os.path.join(self.project, inst.MANIFEST_NAME), encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("installed_from", data)
        self.assertEqual(data["files"]["knowledge/INDEX.md"], inst.sha256(
            os.path.join(self.repo, "knowledge/INDEX.md")))

    def test_refuses_to_install_into_the_repo_itself(self):
        code, _ = run(self.repo, self.repo, "--apply")
        self.assertEqual(code, 1)
        self.assertFalse(os.path.exists(os.path.join(self.repo, inst.MANIFEST_NAME)))

    def test_refuses_missing_project_folder(self):
        code, _ = run(self.repo, os.path.join(self.root, "nope"), "--apply")
        self.assertEqual(code, 1)

    def test_refuses_a_folder_that_is_not_a_repo(self):
        other = os.path.join(self.root, "other")
        os.makedirs(other)
        code, _ = run(other, self.project, "--apply")
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
