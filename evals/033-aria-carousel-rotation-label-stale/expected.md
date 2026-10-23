# Eval 033: carousel pause button whose name never changes

Input: `input.html`. A "Library news" section with three slides that rotate every six seconds.

Intended defect: the rotation control is a native `button` with `aria-label="Pause slides"`. When pressed, rotation stops and the icon changes from pause to play, but the name stays "Pause slides". No state such as `aria-pressed` is exposed. The APG pattern changes the name to match the action. So a screen reader user hears "Pause slides" whether the carousel is moving or stopped, and cannot tell its state or what the button will do.

Everything else is clean:
- Rotation can be stopped, and it stops on hover and when focus enters the section (2.2.2 met).
- The rotation button is first in the carousel's tab order, and pressing a control leaves focus in place.
- The previous and next buttons are named.
- The section is a named region, and the slides are named groups; hidden slides use `hidden`, so their links are not focusable.
- Buttons are 2.75rem square, focus is visible, and the colors are about 7.1:1 or better.
- Language, title, one `h1`, `main`.
- No `aria-roledescription` and no live region; both are optional in the APG.

## Expected findings

1. **[Definite]** The rotation control's state is not exposed: its name stays "Pause slides" after rotation stops.
   - Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1, from `knowledge/wcag/sc-4.1.2-name-role-value.md` (a custom "toggle ... that changes state visually without exposing that state", definite when user-settable).
   - ARIA entry: `knowledge/aria/patterns/carousel.md`, which lists this case.
   - Where: `button#rotate`; `setPlaying()` in the script.
   - Acceptable fix directions: change the `aria-label` in `setPlaying()` to match the action ("Pause slides" or "Play slides"), as the APG does; or keep one name and expose `aria-pressed`. As a direction, not a patch.

## Also acceptable

- Noting that the stale name is also a poor label, as context inside the same finding.
- A note, marked advice, on the `aria-roledescription` conflict or the optional live region, without calling either a defect.
- A note, marked advice, that a non-rotating list may serve better (`patterns/carousel.md`).
- A note that axe is not expected to catch this.

## Must not

- Report 2.2.2; rotation can be paused and stops on focus and hover.
- Report the previous and next buttons, the slide or region names, or the hidden slides.
- Report the missing `aria-roledescription` or live region as defects.
- Report target size, contrast, focus style, headings, landmarks, or language.
- Report the defect twice, under 4.1.2 and again under 2.4.6 or 2.5.3.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

The button has a valid name, so axe has nothing to flag. It cannot compare the name with the icon or the rotation state, so it is not expected to report this defect. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 4.1.2 (Level A), tier 1, and nothing from the Must not list appears.
