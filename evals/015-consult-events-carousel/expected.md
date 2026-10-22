# Eval 015: consult on an auto-rotating events carousel

Input: `request.md`. A developer asks for an auto-advancing, swipeable carousel of five upcoming events on a homepage, with a spec that names the audience and the assistive technology.

Intended outcome: the skill asks the three questions in order, and the right answer to the second one is "build less": a list of the five events, not a carousel. The need the carousel is meant to serve, letting a student see what is on this week, is met better by five visible items than by one at a time.

## Expected

1. **Who and what** is taken from the spec, not invented: students and staff on phones between classes, trying to see what is on this week. The answer names the assistive technology from the spec.
2. **Smallest thing** says plainly that a list of the five events, each with date, title, and link, meets the need, and that a carousel is more than the need requires. "Build less" or equivalent words appear.
3. **Patterns** opens `knowledge/patterns/` for the carousel, finds no entry, says "no entry yet", and still asks what is lost by choosing a list. It does not assert usability statistics about carousels from memory; if it mentions that research exists, it says there is no `ux` entry and marks the claim unverified.
4. **Criteria** are pulled from `knowledge/INDEX.md` and each is cited with level and tier from its entry. The ones a carousel would touch and a list avoids include, at minimum, SC 2.2.2 Pause, Stop, Hide (auto-rotation) and SC 2.5.1 Pointer Gestures (swipe). SC 2.1.1 Keyboard, SC 2.4.3 Focus Order, SC 1.1.1 Non-text Content (the images), and SC 2.3.3 noted as Level AAA are acceptable additions. The list's own criteria, SC 1.3.1 for list markup and SC 2.4.4 for link text, are acceptable.
5. **Options** include at least the list and, if the developer insists on motion, a carousel with no auto-advance, visible previous and next buttons, and a pause control, with what each costs. Marketing's request is acknowledged, not dismissed.
6. **Manual tests owed** name the spec's AT: VoiceOver, NVDA, keyboard, 400% zoom, reduced motion, and say what to do with each on the chosen thing.
7. **Need statement** is in the template's format, dated, with "Instead of: an auto-rotating carousel" and a one-or-two-sentence "Why this is right". It is proposed, not written into the spec without agreement.
8. **Content** is consulted: event titles as headings or list items, link text that says where it goes, image alt text purpose, against `docs/content-standards.md`.

## Also acceptable

- A proposed pattern decision row for the spec's table recording that carousels are not used on the homepage, and why.
- Asking the developer one or two clarifying questions before answering, as long as the answer still arrives in the same response with stated assumptions.

## Must not

- Write HTML, CSS, or JavaScript.
- Accept "users" or "visitors" as the answer to question one.
- Skip question two and go straight to how to make the carousel accessible.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Cite the ARIA Authoring Practices carousel pattern as a requirement.
- Write into `a11y-spec.md` without the developer's agreement.

## Pass condition

Items 1 through 7 are present, the answer to question two is a list rather than a carousel, and nothing from the Must not list appears.
