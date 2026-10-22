# Eval 013: password field that blocks paste and password managers

Input: `input.html`. A sign-in form with a username and a password.

Intended defect: the password field has `autocomplete="off"`, which tells password managers not to fill it, and `onpaste` and `ondrop` handlers that return false, which block pasting. Remembering and re-typing a password is a cognitive function test, and the page removes both mechanisms that would help with it. There is no alternative sign-in method on the page. Everything else is clean: language set, title present, one `h1`, landmarks, both fields have visible associated labels, the username field carries the right `autocomplete` token, visible focus, contrast above the thresholds.

## Expected findings

1. **[Definite]** Password entry blocks paste and password managers, with no alternative method.
   - Criterion: WCAG 2.2 SC 3.3.8 Accessible Authentication (Minimum) (Level AA), tier 1
   - Source: `knowledge/wcag/sc-3.3.8-accessible-authentication-minimum.md`
   - Where: the `input#pass` and its `autocomplete`, `onpaste`, and `ondrop` attributes
   - Acceptable fix directions: remove the paste and drop blocking and set `autocomplete="current-password"` (technique H100); or offer an alternative such as an email sign-in link (technique G218). The entry names F109 as the matching failure.

## Also acceptable

- A note that the username field is correctly marked up and is not part of the finding.
- A second Definite finding under SC 1.3.5 Identify Input Purpose for `autocomplete="off"` on the password field. The Recommendation's Input Purposes list includes `current-password`, so the field is covered and the 1.3.5 entry grades `off` on a covered field as Definite (F107). The first run of this eval raised it that way after fetching the W3C list in-run; the key originally expected Likely and was corrected. Strictly this page has two defects from one attribute set; the key accepts both.
- A manual-review note that the server's response to a failed sign-in is not in the input, so 3.3.1 and 3.3.3 cannot be judged.

## Must not

- Report SC 4.1.2, 1.3.1, or 3.3.2; both fields are labeled and associated.
- Report the heading, landmarks, focus style, language, or contrast.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report no violations. Its `autocomplete-valid` rule accepts `off`, and it has no rule for paste blocking. A verifier that treats the clean scan as a pass has failed this eval.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
