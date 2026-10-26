# Doctor Accessible: the short version

Doctor Accessible is a set of files that teach Claude Code to help you build web pages that work for people with disabilities, to the WCAG 2.2 Level AA standard. It is an assistant. It does not make a page accessible by itself, and it does not replace a person testing with real assistive technology. You do both of those. It makes them easier to do well.

## What it does

Three modes, in order:

1. **Consult.** Before you build, it asks who the thing is for, what they are trying to do, and what the smallest thing that meets that need is. Sometimes the answer is "build less" or "this is already met." It writes the answer into your project's spec.
2. **Build.** While you write code or words, it loads short skills that point at a library of reference entries: every WCAG criterion, plus native HTML patterns, ARIA, design, content, and the research on interface patterns.
3. **Verify.** A separate agent that did not see your conversation reads your page cold, runs the axe scanner, and reports what fails, what probably fails, and what a person still has to test.

Every claim it makes cites a source and a tier. If it has no source, it says so.

## What you need

- Claude Code, signed in.
- Node.js, for the axe scanner.
- Python 3, for the reading-level tool and the eval runner.

## Get it into your project

The plan is a Claude Code plugin. Until it ships, copy these from this repo into your project's root, keeping the folder names:

```
.claude/              the skills and the verifier
knowledge/            the library the skills read
tools/                axe and the reading-level tool
docs/content-standards.md
docs/principles.md
templates/a11y-spec.md
```

Then copy `templates/a11y-spec.md` a second time, to your project root as `a11y-spec.md`.

## First run

1. Open a terminal in your project and run `claude`.
2. Type `/planning`. It walks you through filling `a11y-spec.md`: the conformance target, who the project serves, and the assistive technology you test with. Ten minutes.
3. For your first feature, type `/consult` and describe it. Answer the three questions. Agree to the need statement it proposes; it writes it into the spec.
4. Build. Load `/wcag` for structure, forms, focus, color, or media. Load `/html-patterns` before you reach for ARIA. Load `/content` for words. Load `/design` for contrast, focus rings, target sizes, motion. Load `/react-jsx` if you are in React.
5. Ask: "Use the verifier agent on `path/to/page.html`." Read the report. Fix what it found. Run it again.
6. Type `/at-test-protocol` and name the component. It writes the test script. A person follows it with a keyboard, a screen reader, zoom, reduced motion, and forced colors, and records what happened.

## Commands you will use

```
/planning            fill the spec for a new project
/consult             the pause before any feature
/wcag  /html-patterns  /content  /design  /react-jsx     build-side skills
/at-test-protocol    the human test script
python tools/axe.py page.html            axe with the WCAG 2.2 tags
python tools/readability.py page.html --target 8
```

## What it will not do

- Pretend to be a user with a disability, or say what a screen reader "would" announce.
- Cite a criterion, a number, or a threshold from memory.
- Rewrite your code without being asked.
- Treat a clean axe run as a pass. axe finds a minority of defects.
- Make the final call. Every finding is reviewed by a person, and every page is tested by a person with assistive technology before it ships.

## Where to read more

- `docs/FAQ.md` for the questions people ask first.
- `docs/how-it-works.md` for how it is put together and how to extend it.
- `docs/how-we-work.md` if you want to contribute and are new to GitHub or Claude Code.
