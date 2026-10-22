# How we work

A guide for contributors who are new to GitHub, new to Claude Code, or new to development. Read it once. Every work issue links back here.

The short version: you will read an official web page about one accessibility rule, explain it in plain words in a text file, build a tiny web page that breaks that rule, and ask for your work to be added to the project. Claude Code does the technical steps for you when you ask it to.

## The words you will see

**Repository, or repo.** The project folder, stored on GitHub so everyone can share it. This one is called `doctorAccessible`.

**Clone.** Making your own copy of the repo on your computer. You do this once.

**Issue.** A to-do item on GitHub. Each issue is one piece of work with a number, like #14. The issue describes the work and has a checklist you tick as you go.

**Branch.** A separate copy of the files inside your repo where you make your changes. The main copy is called `main`. Nobody edits `main` directly. You work on a branch, and your changes join `main` only after review. Think of it as a draft that sits beside the published version.

**Commit.** A saved snapshot of your changes with a short note saying what you did. You can make many commits on a branch.

**Push.** Sending your branch and its commits from your computer up to GitHub, so others can see them.

**Pull request, or PR.** Asking for your branch to be merged into `main`. A PR has a description, and a reviewer reads your changes before saying yes. It is called a pull request because you are asking the project to pull your changes in.

**Review.** Someone else reads your PR and checks it against the same list you used. They may ask for changes. That is normal and not a judgment.

**Merge.** Your branch joins `main`. Your work is now part of the project.

**Markdown.** The plain-text format all our documents use. A `#` makes a heading, a `-` makes a list item, backticks make `code`. You can write it in any text editor.

## You do not need to learn Git commands

Git is the tool that handles branches, commits, and pushes. Developers type commands for it. You do not have to. Claude Code can do every Git step when you ask in plain English. Examples of things you can type to it:

- "Make a new branch from main called wp-2.4-robust."
- "Commit what I have changed with the message: Add the entry for SC 4.1.3 Status Messages."
- "Push this branch and open a pull request. Use the pull request template and link issue #14."
- "Show me what I have changed since my last commit."
- "Switch back to main and get the latest changes."

Claude Code will show you what it is about to do and ask before it does it. Read what it says. If you do not understand, ask it to explain. That is allowed.

## The workflow, start to finish

Here is one piece of work from beginning to end. The example is issue #14, the one for Status Messages, because it is the smallest.

### 1. Set up, once

1. Install Claude Code. Instructions are at https://docs.claude.com/en/docs/claude-code. Sign in with the account you were given.
2. Clone the repo. In your terminal: `git clone https://github.com/derekjackson-das/doctorAccessible.git`, then `cd doctorAccessible`. If that is unfamiliar, install Claude Code first, start it in any folder, and say "Clone the doctorAccessible repo from derekjackson-das on GitHub into my Documents folder." It will do it.
3. Start Claude Code: type `claude` in the repo folder. It reads the project rules and says hello.

### 2. Claim the issue

Open the issue on GitHub. Click the pencil icon to edit the description and type your name after **Owner.** Save. Now everyone knows it is yours.

### 3. Make a branch

Tell Claude Code: "Make a new branch from main called wp-2.4-robust." The issue tells you what to call the branch.

### 4. Do the work

For a knowledge entry, this is the heart of it:

1. Open the official W3C page for the rule in your browser. The issue links it. Read it. Then read the "Understanding" page, which explains why the rule exists and how to meet it.
2. Tell Claude Code: "Copy knowledge/wcag/_template.md to knowledge/wcag/sc-4.1.3-status-messages.md and fill in the heading block from the W3C page." It will fill the metadata. Check it against the page yourself.
3. Write the rest in your own words. You can draft it yourself, or say "Draft the 'What it requires, in our words' section from the Understanding page, in plain language, and show me." Then read it, fix it, make it yours. The W3C text itself is quoted exactly, once, in the "Normative text" section. Everything else is your explanation.
4. Verify. Open the live W3C page one more time and confirm the quoted text and the level match. Write today's date and your name on the "Verified" line. This is the step that matters most. We never trust memory, including Claude's.
5. Tell Claude Code: "Add a row for SC 4.1.3 to knowledge/INDEX.md, matching the existing row."

For an eval:

1. Tell Claude Code: "Make a folder evals/002-status-message-not-announced with an input.html: a small, clean page that has exactly one defect against SC 4.1.3, as described in my entry." Read what it builds. Keep it tiny.
2. Tell it: "Write expected.md for this eval, from the knowledge entry, following the shape of evals/001-missing-label/expected.md." Read it. Make sure every claim comes from your entry.
3. Tell it: "Run axe on evals/002-status-message-not-announced/input.html, then use the verifier agent on it. Tell the verifier not to open expected.md or RESULTS.md." Compare the verifier's report to your expected.md. Did it find the defect? Did it report anything it should not have?
4. Tell it: "Add a row at the top of evals/RESULTS.md for this run, matching the existing rows."

### 5. Save your work

Tell Claude Code: "Commit everything with the message: Add SC 4.1.3 Status Messages entry and eval 002." Do this as often as you like. Small commits are good.

### 6. Ask for it to be added

Tell Claude Code: "Push this branch and open a pull request using the template. Link issue #14 and say which evals ran and what they produced." It opens the PR and gives you a link. Open the link and read what it wrote. Fix anything that is wrong.

### 7. Review and merge

A reviewer reads your PR. They may leave comments. Reply, make changes on the same branch, commit, and push again; the PR updates by itself. When the reviewer approves, they merge it. Tick the last box on your issue and close it.

### 8. Clean up

Tell Claude Code: "Switch to main, get the latest changes, and delete my merged branch." You are ready for the next issue.

## What the finished product looks like

### A knowledge entry

Open `knowledge/wcag/sc-4.1.2-name-role-value.md` in the repo. That is the model. It has:

- A heading block: standard, level, which guideline it sits under, the two source links, which older WCAG versions include it, and the verified line.
- **Normative text.** The rule, quoted exactly from W3C. The only quotation in the file.
- **What it requires, in our words.** Two to five sentences a developer can act on.
- **How it fails in code.** A list of concrete mistakes, each marked definite, likely, or manual review.
- **How to meet it.** Native HTML first, then the W3C techniques by their ID and title.
- **Related criteria.** Other rules that often come up alongside, and whether they have an entry yet.
- **Automated coverage.** What the axe scanner can and cannot catch for this rule.

Yours will look like that, for a different rule. Length is usually 60 to 100 lines.

### An eval

Open `evals/001-missing-label/`. Two files:

- `input.html`: a web page of about 28 lines. A heading, a search box, a button. Everything is correct except one thing: the word "Search" next to the box is not connected to it, so a screen reader cannot tell what the box is for.
- `expected.md`: the answer key. It names the one defect, the rule it breaks, where it is in the file, acceptable fixes, what the checker may also mention, and what it must not report.

Yours will be the same shape: one tiny page, one deliberate mistake, one answer key.

### A skill

Open `.claude/skills/wcag/SKILL.md`. About a hundred lines. It tells Claude when the skill applies, how to cite, how to judge confidence, and which knowledge entry answers which question. It holds no facts itself. Phase 3 packages write more of these.

## Rules that matter most

- **Your own words.** This repo is public. Explain; do not paste. Only the W3C rule text is quoted, once, with the link.
- **Cite every claim.** Which source, which tier, which version or date. Tier 1 is the standard. Tier 2 is W3C explaining it. Tier 3 is experienced practitioners. The list of allowed sources is `knowledge/SOURCES.md`. If a source is not on it, ask before using it.
- **Verify against the live page yourself.** Claude may draft. You confirm.
- **One issue, one branch, one pull request.** Big issues can be split into several PRs; say so in the issue.
- **Never edit `main` directly.** The repo will stop you, but the habit matters.

## When you are stuck

1. Ask Claude Code. "Explain what a pull request is" or "What does this error mean" are fine questions.
2. Leave a comment on your issue saying where you are stuck. Someone will answer there.
3. Ask Derek.

A recorded problem is as useful as a finished entry. Nobody is expected to know this on day one.
