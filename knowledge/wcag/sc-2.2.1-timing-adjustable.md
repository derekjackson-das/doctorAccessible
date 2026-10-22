# SC 2.2.1 Timing Adjustable

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.2 Enough Time
- Tier 1 source: https://www.w3.org/TR/WCAG22/#timing-adjustable
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> For each time limit that is set by the content, at least one of the following is true:
>
> **Turn off.** The user is allowed to turn off the time limit before encountering it; or
>
> **Adjust.** The user is allowed to adjust the time limit before encountering it over a wide range that is at least ten times the length of the default setting; or
>
> **Extend.** The user is warned before time expires and given at least 20 seconds to extend the time limit with a simple action (for example, "press the space bar"), and the user is allowed to extend the time limit at least ten times; or
>
> **Real-time Exception.** The time limit is a required part of a real-time event (for example, an auction), and no alternative to the time limit is possible; or
>
> **Essential Exception.** The time limit is essential and extending it would invalidate the activity; or
>
> **20 Hour Exception.** The time limit is longer than 20 hours.
>
> Note: This success criterion helps ensure that users can complete tasks without unexpected changes in content or context that are a result of a time limit. This success criterion should be considered in conjunction with Success Criterion 3.2.1, which puts limits on changes of content or context as a result of user action.

## What it requires, in our words

If the page imposes a clock, such as a session that expires, a form that times out, a page that redirects after a delay, or content that advances on its own, the user needs a way around it: switch it off beforehand, make it at least ten times longer, or get a warning with at least twenty seconds to extend it, repeatedly. People who read slowly, use a screen reader, or type with difficulty need more time than the default assumes. Exceptions exist for real-time events like auctions, for limits that are the point of the activity like a timed test, and for limits over twenty hours.

## How it fails in code

- A `meta http-equiv="refresh"` with a delay that redirects or reloads the page. Definite. F40, F41.
- A server-side session timeout that redirects to a login page with no warning and no way to extend. Definite once confirmed. F58.
- A script-driven timeout that ends a form or session with no warning, or with a warning shorter than twenty seconds, or that cannot be extended ten times. Definite once the behavior is observed.
- Auto-advancing content such as a slideshow that cannot be paused. Definite; also 2.2.2.
- A timed exam. Not a failure if the limit is essential; manual review.

## How to meet it

- Technique G198, "Providing a way for the user to turn the time limit off", and Technique G180, "Providing the user with a means to set the time limit to 10 times the default time limit".
- Technique G133, "Providing a checkbox on the first page of a multipart form that allows users to ask for longer session time limit or no session time limit".
- Techniques SCR16 and SCR1 together: warn before expiry and let the user extend.
- Technique G4, "Allowing the content to be paused and restarted from where it was paused", and SCR33 or SCR36 for moving or auto-updating text.
- Do not use `meta refresh` for redirects or reloads.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.2.2 Pause, Stop, Hide (entry in this package). Moving and auto-updating content.
- SC 3.2.1 On Focus and 3.2.5 Change on Request (no entries yet). Unexpected changes of context; 3.2.5 is Level AAA.
- SC 2.2.3 No Timing, 2.2.4 Interruptions, and 2.2.6 Timeouts are Level AAA and not requirements here.

## Automated coverage (tier 3)

axe-core tags `meta-refresh` to this criterion. It flags a delayed `meta refresh`. Script and server timeouts are found by reading the code or waiting for them, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
