# Eval 048: star ratings marked role="img" with no name

Input: `input.html`. A "Study room reviews" page with two reviews. Each shows its rating as five star characters, filled or empty, in a `span` with `role="img"`.

Intended defect: neither `span[role="img"]` has `aria-label` or `aria-labelledby`. WAI-ARIA 1.2 requires an accessible name for `img`, taken from the author only, and makes the role's children presentational. So the star characters inside are not exposed and nothing takes their place. The rating appears nowhere else on the page.

Everything else is clean:
- `header`, `main`, `footer`, one `h1`, an `h2` per review inside an `article`, `lang`, `title`.
- Text is #1a1a1a on white, links #0b4f9c, borders #767676. Focus is visible.
- Filled and empty stars differ by shape, not color.
- Nothing on the page is interactive except three links.

## Expected findings

1. **[Definite]** The star ratings have no text alternative.
   - Criterion: WCAG 2.2 SC 1.1.1 Non-text Content (Level A), tier 1, from `knowledge/wcag/sc-1.1.1-non-text-content.md` ("An `svg` or an element with `role="img"` that has no accessible name. Definite.").
   - Role entry: `knowledge/aria/roles/img.md`, where the name is required and comes from the author only, and the children are presentational.
   - Where: both `span[role="img"]`.
   - Acceptable fix directions: give each an accessible name that states the rating, such as "4 out of 5 stars", with `aria-label`; or write the rating as visible text and hide the stars. As a direction, not a patch.

Reporting both ratings in one finding, or as one finding with two locations, is correct. Two separate findings for the same defect is not.

## Also acceptable

- A note that the star characters inside the `span` are not exposed, because the `img` role makes its children presentational.
- A note, marked advice, that visible text for the rating would serve more people than a label on a picture.
- A note that axe reported it, with the rule named.
- Manual-review notes that a criterion appears met and needs a browser check.

## Must not

- Report the defect more than once, or under 4.1.2 or 1.3.1 as well as 1.1.1.
- Report the ratings as conveyed by color alone (1.4.1); the stars differ by shape.
- Report `role="img"` on a `span` as not allowed; ARIA in HTML allows any role on `span`.
- Report the `article` elements, the headings, or the landmarks.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Say what a screen reader user would hear or experience.
- Rewrite the page.

## Automated scan

axe-core has a rule for this (`role-img-alt`); whether it fired is recorded in `RESULTS.md`. The finding does not depend on it.

## Pass condition

Finding 1 is present as definite under SC 1.1.1 (Level A), tier 1, once, and nothing from the Must not list appears.
