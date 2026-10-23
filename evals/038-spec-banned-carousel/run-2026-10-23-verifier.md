# Run 2026-10-23: verifier on eval 038 (WP 4.6)

- Method: `evals/run.sh` (fresh `claude -p` session, registered verifier, axe via `tools/axe.py`), graded by `evals/check.py` (mechanical spec-deviation check plus a tool-less judge).
- History: the first run (verifier before it labeled spec deviations) left 038 and 039 unlabeled, failing "at definite or likely". The verifier's Spec deviations format now asks for a confidence on each, and this run passed. For 040, the first check of this report failed on a key that forbade any definite. The key was narrowed: it still forbids a definite claim that the need is unserved, but allows a definite note that the thing the need statement says to build is absent. Re-checked: pass.
- Result: **pass.**

## The verifier's report, as given

## Checked

- **Input:** `evals/038-spec-banned-carousel/input.html`, a "This week" news section in `main`. It has Previous and Next buttons, three slides marked as `div role="group"` with headings, and a script that sets `hidden` on every slide except the current one.
- **Spec:** `evals/038-spec-banned-carousel/a11y-spec.md`, beside the page. I read it first. Target is WCAG 2.2 AA, reading level target is grade 8, and the spec lists VoiceOver on iOS, NVDA with Chrome, keyboard only, and 400% zoom.
- **Method:** I read the code in full, ran `tools/axe.py` and ran `tools/readability.py --target 8`. Entries opened: `knowledge/INDEX.md`, `patterns/carousel.md`, `aria/patterns/carousel.md`, `wcag/sc-1.4.3-contrast-minimum.md`, `wcag/sc-2.5.8-target-size-minimum.md`, `wcag/sc-4.1.3-status-messages.md`, and `docs/content-standards.md`.

## Findings

No Definite or Likely WCAG 2.2 AA failures were found in the code.

These are the checks I computed or read against the entries:
- **Text contrast (SC 1.4.3, Level AA, `wcag/sc-1.4.3-contrast-minimum.md`):** threshold 4.5:1 for normal text. I computed the ratios from the declared colors, each against `#fff`, with the WCAG relative luminance formula:
  - `#005a9c` (links, button text and border): 7.14:1
  - `#1a1a1a` (body text and focus outline): 17.40:1
  - `#4a4a4a` (slide border): 8.86:1

  All pass.
- **Target size (SC 2.5.8, Level AA, `wcag/sc-2.5.8-target-size-minimum.md`):** threshold 24 by 24 CSS pixels. I computed the button height from the CSS as about 44 CSS pixels at the default 16 px font: 24 px line box (1.5 line-height), plus 16 px of padding, plus 4 px of border. Passes.
- **Hidden slides:** they use the `hidden` attribute, which applies `display: none`, so their links cannot take focus. I found no SC 2.4.3 problem in the code.
- **Names:** the buttons have visible text names. Each slide group takes its name from its heading through `aria-labelledby`. The section takes its name from "This week".

### [Manual review] No announcement when the slide changes
- **Where:** `input.html` lines 26–28 (the slide wrappers) and line 34 (`show()`).
- **What:** Next and Previous swap the visible slide without moving focus, and nothing marks the change as a live region.
- **Criterion:** this is probably not a WCAG failure. The SC 4.1.3 entry covers status messages and excludes "content that is not a status message". A new slide is new content, not a status message. The polite live region for a slide the person chose comes from the APG pattern and is best practice, tier 2, not a requirement.
- **Source:** `knowledge/wcag/sc-4.1.3-status-messages.md`, `knowledge/aria/patterns/carousel.md`.
- **Fix direction:** decide whether a person changing slides needs to learn of the change without going to look for it, and confirm with the spec's screen readers. This question goes away if the spec's list is built instead (see Spec deviations).

## Content

- **Reading level:** `readability.py 1.0 (2026-10-23)` measured `<main>`. Result: 13 words, 2 sentences, Flesch-Kincaid Grade Level 5.1, which is at or below the grade 8 target.
  - **Left out:** buttons, headings, script and style.
  - **Hidden slides not measured:** the counts suggest the tool read only the visible slide, so the text of the two hidden slides was probably not measured.
  - **Too short to mean much:** the tool notes fewer than 100 words, so the score means little. It is a signal, not a pass.
- **Headings:** there is one `h1` and no skipped levels (h1, h2, h3). The slide headings describe their items.
  - Manual review: "This week" is short but readable in context. Whether a reader skimming headings knows it means library news is for a person to judge.
  - Manual review: the page `<title>` is "Library news" and the `h1` is "Harvard Library". Someone should decide whether the two should match more closely.
- **Link text:** "See all opening hours", "Book a study room" and "Sign up for the workshop" each say where they go, out of context. Meets the house standard.
- **Alt text and error messages:** there are no images or forms, so these do not apply.
- **Language:** `lang="en"` is declared, and there are no passages in other languages.

## Spec deviations

### [Definite] Banned pattern used: a carousel instead of the agreed list
- **Where:** `input.html` lines 22–36: Previous and Next controls, three slides showing one at a time, and the slide script.
- **Spec lines broken:**
  - Banned patterns: "**Carousels and slideshows, rotating or not.** Decided 2026-09-30 in consult: in our user testing, readers missed most slides. Use a short list of linked items instead."
  - Pattern decisions: "2026-10-01 | Home page news | A list, not a carousel | See the need statement"
  - Need statement, We will build: "a short list of this week's news items, each a heading and one sentence with a link." Instead of: "a news carousel."
- **What the code exposes:** a non-rotating slideshow. Only one of the three news items is shown at a time, and the others are reached only through Previous and Next. The spec bans this pattern even when it does not rotate, and a recorded decision replaced it with a list. This is reported once: the banned pattern and the ignored decision are the same piece of code.

### [Manual review] Need statement: does the page let readers "see what is new at the library this week"?
- **Spec:** "Trying to: see what is new at the library this week." "Why this is right: a list shows every item at once and needs no controls."
- **What the code exposes:** one item is visible on load, two are `hidden`, and nothing shows how many items exist (no "1 of 3"). The need statement's manual test, "VoiceOver on iOS reads the list in order", cannot be run as written, because there is no list in the markup.
- **For a human:** whether staff and students glancing on a phone find all three items is for a person to judge, with the spec's assistive technology.

## Manual checks remaining

- **Keyboard only:**
  - Tab to Previous and Next and press each one several times.
  - Record whether focus stays on the button, whether the focus outline is visible, and whether any link in a hidden slide takes focus.
- **VoiceOver on iOS:**
  - Swipe through the "This week" section from the heading.
  - Record which news items are reached without using the buttons, and what is spoken after you activate Next.
- **NVDA with Chrome:**
  - Use the same steps in browse mode and in focus mode.
  - Record what, if anything, is spoken when the slide changes after you press Next. Also record whether the region and group names are spoken.
- **400% zoom (and 320 CSS px width):**
  - Record whether the controls and slide content reflow without horizontal scrolling, and whether both buttons stay visible and usable.
- **Content:**
  - A person should read all three items, including the hidden two, against the grade 8 target and the plain-language standard.
- **Spec housekeeping (not a WCAG matter):**
  - The spec's "Open manual tests" says "None owed", but the need statement lists one test owed (VoiceOver on iOS). Someone on the project should reconcile the two.

## Automated scan

```
axe-core 4.14.0 via @axe-core/cli (axe), tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa
raw JSON: C:\Users\rua126\AppData\Local\Temp\doctor-a11y-axe\038-spec-banned-carousel-20261023-144522.json
violations: 0
incomplete: 0
passes: 21 rules   inapplicable: 43 rules
raw (violations and incomplete):
{
  "violations": [],
  "incomplete": []
}
```

There are no violations or incomplete results to map to findings. The clean run does not count as a pass on its own. axe does not check spec deviations, and per the SC 4.1.3 entry it has no rule that checks whether a live region is present.
