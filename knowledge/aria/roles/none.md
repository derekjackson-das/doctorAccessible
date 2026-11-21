# Role: none

- Category: document structure. Synonym of `presentation`.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "none role", https://www.w3.org/TR/wai-aria-1.2/#none
- Reference (tier 3): MDN Web Docs, "ARIA: none role", last modified 12 May 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role
- Related entries: `aria/roles/presentation.md`, which holds everything below in full.
- WCAG: as for `presentation`.
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2 text checked against a downloaded copy.

## What it is

The same role as `presentation`, under a clearer name. WAI-ARIA 1.2 defines it with the same sentence: "An element whose implicit native role semantics will not be mapped to the accessibility API." The spec's note says the working group added `none` in ARIA 1.1 because many people read "presentation" as meaning hidden, which it does not.

## Which to write

WAI-ARIA 1.2 says that until support for `none` is sufficient, authors are advised to use `role="presentation"` alone, or `role="none presentation"` as a fallback. That advice is from 2023 and gives no support data; no source on our list reports a recent test of `none` on its own. Writing `role="none presentation"` costs nothing and follows the spec.

## Attributes and context it needs

The same as `presentation` in practice, with one wrinkle. WAI-ARIA 1.2's characteristics table for `presentation` prohibits `aria-label` and `aria-labelledby` and gives "Name From: prohibited". The table for `none` lists both as inherited and gives "Name From: author". The two roles are defined as synonyms, so the difference looks like an inconsistency in the spec. Following principle 13, take the stricter reading: never name an element with `role="none"`.

## Where it can and cannot be used

The same elements as `presentation`; ARIA in HTML lists the two together on every row (`aria/roles/presentation.md`).

## Everything else

Rules, exceptions, and failures are identical to `presentation`: see `aria/roles/presentation.md`. Report a misuse once, under the criterion it breaks.
