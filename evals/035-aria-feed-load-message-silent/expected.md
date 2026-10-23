# Eval 035: feed whose "more loaded" message is never announced

Input: `input.html`. A "Library stories" page: a feed of short stories with a "Load more stories" button.

Intended defect: pressing "Load more stories" adds three stories and writes a visible message, "3 more stories loaded. Showing 6 of 9.", into a plain `p`. The `p` has no live-region role or `aria-live`, and focus stays on the button. A screen reader user is not told that anything happened.

Everything else is clean:
- The feed has `role="feed"`, named by its heading. Each story is an `article`, named by its title and described by its text, with `aria-posinset` and `aria-setsize` kept current. `aria-busy` is set and reset to false around each update.
- Loading is by a button, not by scrolling, so the footer link is always reachable.
- After the last load, the button stays focused and changes to "All stories loaded", with `aria-disabled="true"`.
- Focus is visible; contrast is about 7.1:1 or better; language, title, headings in order, `main`, and a footer.

## Expected findings

1. **[Definite]** The "more stories loaded" message is not exposed as a status message.
   - Criterion: WCAG 2.2 SC 4.1.3 Status Messages (Level AA), tier 1, from `knowledge/wcag/sc-4.1.3-status-messages.md` ("Script that inserts or changes a visible message ... in an element with no live-region role or `aria-live`, and does not move focus to it. Definite. F103").
   - ARIA entry: `knowledge/aria/patterns/infinite-scroll.md`, which lists this case.
   - Where: `p#loaded`; the click handler that sets its text.
   - Acceptable fix directions: give `p#loaded` `role="status"` (present in the page before it is filled). As a direction, not a patch.

## Also acceptable

- A note, marked advice, that the APG suggests Page Down, Page Up, Control+End, and Control+Home in a feed, and that these are not required.
- A note, marked advice, on the `feed` role's untested support (the testing gap in the entry).
- Manual-review notes that a criterion appears met and needs a browser check.
- A note that axe is not expected to catch this.

## Must not

- Report the feed's ARIA (role, names, descriptions, position, set size, `aria-busy`) as failures.
- Report keyboard access, the footer, or focus after the last load as failures.
- Report contrast, focus style, headings, landmarks, or language as failures.
- Report the defect twice, under 4.1.3 and again under 4.1.2 or 1.3.1.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe does not track text inserted after a click, so it is not expected to report this defect. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 4.1.3 (Level AA), tier 1, and nothing from the Must not list appears.
