# Content: Link text

- House standard: `docs/content-standards.md`, section 5.
- Sources:
  - W3C WAI, "Writing for Web Accessibility", updated 5 August 2022. https://www.w3.org/WAI/tips/writing/ Tier 2.
  - WebAIM, "Links and Hypertext", no date shown, accessed 2026-10-23. https://webaim.org/techniques/hypertext/ Tier 3.
- WCAG: `wcag/sc-2.4.4-link-purpose-in-context.md` (Level A: the purpose of a link can be determined from its text, or its text together with its context). SC 2.4.9 Link Purpose (Link Only) is Level AAA, beyond our target, with no entry yet.
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

Link text whose purpose cannot be worked out even with its surrounding context fails SC 2.4.4; report it there at the confidence the 2.4.4 entry gives. Link text that passes 2.4.4 because its sentence explains it, but still says "click here" or "read more", misses the house standard. That is reported as likely, never definite and never a WCAG failure. A project's `a11y-spec.md` may change the standard; the spec wins.

## What it is

The words a reader clicks. They should say where the link goes or what it does.

## Why it matters

Screen reader users often pull up a list of a page's links, sometimes sorted alphabetically, and hear each one out of context (WebAIM). "Click here" ten times in that list says nothing.

## How to do it

- **Describe the destination.** Write link text that says what is at the other end; avoid "click here" and "read more" (W3C; WebAIM).
- **Read well on its own.** Wording like "click here", "more", and "click for details" are ambiguous on their own (WebAIM).
- **Put the distinguishing words first.** "Products (opens in a new window)", not "Opens in a new window: Products" (WebAIM).
- **Do not say "link".** Screen readers already announce it (WebAIM).
- **Same text, same destination** (house standard).
- **Say when a link opens a file or a new window** (house standard; W3C advises indicating relevant information about the link target).

## How to check it

- List all the links on the page, out of context. Could a reader tell where each goes?
- Look for "click here", "here", "read more", "more", "learn more", and bare URLs.
- Check repeated link text goes to the same place.
- Where link text is vague but the sentence explains it, the 2.4.4 entry decides whether it passes; the house standard still asks for better text.
