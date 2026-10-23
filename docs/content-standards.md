# Content standards

What good content looks like in a project that uses Doctor Accessible. These are the house defaults. A project's `a11y-spec.md` imports them and may tighten or override them in its "Content standards" section. The `content` skill applies them while writing; the verifier checks against them and reports under its "Content" heading.

Each standard names its source and tier. Where a WCAG criterion applies, the knowledge entry is cited when it exists; until then the line says "no entry yet" and links the W3C text, unverified, per principle 3.

## 1. Plain language

Write for the reader who knows least and has the least time. Common words over technical ones, unless the technical word is the one the reader will search for. Active voice. Short sentences, one idea each. Define a term the first time it appears if the reader may not know it.

- Source: W3C, "Writing for Web Accessibility", tier 2, https://www.w3.org/WAI/tips/writing/
- Source: W3C, "Making Content Usable for People with Cognitive and Learning Disabilities", W3C Working Group Note, 29 April 2021, tier 2, https://www.w3.org/TR/coga-usable/
- Source: US Federal Plain Language Guidelines, now Digital.gov's plain language guide series, tier 3, https://digital.gov/guides/plain-language

## 2. Reading level

House default: body text reads at or below a grade 8 level, measured by the Flesch-Kincaid Grade Level formula over the main content, excluding navigation, headings, code, and proper nouns where practical. A project may set a different target in its spec and must say why.

The formula counts sentence length and syllables. It does not measure clarity, and short sentences full of jargon will pass it. Treat the score as a signal that sends a human to read, never as a pass on its own.

- Source: WCAG 2.2 SC 3.1.5 Reading Level (Level AAA), which asks for content no harder than the lower secondary education level once proper names and titles are removed. Not part of our AA target; the house default borrows its bar. No entry yet, unverified: https://www.w3.org/TR/WCAG22/#reading-level
- Source: W3C, "Making Content Usable", tier 2, as above.

## 3. Organization

Front-load. The first sentence of a page or section carries its point. One idea per paragraph. Parallel items go in a list. Long pages get a short summary at the top. The order on the page is the order a reader needs, not the order the writer thought of it.

- Source: W3C, "Writing for Web Accessibility", tier 2.
- Source: Nielsen Norman Group research on how people read online, which finds scanning rather than reading, tier 3, https://www.nngroup.com/ (summarize and link; never paste).
- How to apply and check it: `knowledge/content/organization.md`, which rests on Digital.gov's plain language guide (tier 3), the W3C writing tips, and COGA objectives 2 and 3 (tier 2). It does not yet draw on the NN/g research.

## 4. Headings

Every heading describes the section under it, so a reader skimming headings alone can tell what the page covers and where to go. One `h1` per page that says what the page is. No skipped levels. "Overview", "Introduction", and "More" are not headings; "How to apply", "What the fee covers", and "Deadlines for spring term" are.

- Source: WCAG 2.2 SC 2.4.6 Headings and Labels (Level AA), tier 1: `knowledge/wcag/sc-2.4.6-headings-and-labels.md`.
- Source: WCAG 2.2 SC 2.4.2 Page Titled (Level A), tier 1: `knowledge/wcag/sc-2.4.2-page-titled.md`.
- Source: W3C WAI Tutorials, Page Structure, tier 2, https://www.w3.org/WAI/tutorials/page-structure/

## 5. Links

Link text says where the link goes or what it does, on its own, out of context. "Click here", "read more", and a bare URL are not link text. Two links with the same text go to the same place. A link that opens a file or a new window says so.

- Source: WCAG 2.2 SC 2.4.4 Link Purpose (In Context) (Level A), tier 1: `knowledge/wcag/sc-2.4.4-link-purpose-in-context.md`.
- Source: W3C, "Writing for Web Accessibility", tier 2.

## 6. Alternative text

Every image has an `alt` attribute. Decorative images get an empty one. Informative images get text that conveys what the image is for in its context, then stops. Do not start with "image of" or "picture of". A chart or diagram gets a short `alt` and its data or meaning in the surrounding text. Images of text are avoided; when unavoidable, the `alt` carries the text. No standard sets a length. Say the purpose and stop.

- Source: WCAG 2.2 SC 1.1.1 Non-text Content (Level A), tier 1: `knowledge/wcag/sc-1.1.1-non-text-content.md`.
- Source: W3C WAI Tutorials, Images, including the alt decision tree, tier 2, https://www.w3.org/WAI/tutorials/images/decision-tree/

## 7. Error messages and instructions

An error says what went wrong and what to do next, in the reader's words, next to the field. Instructions come before the field they apply to, not after. Required fields are marked in text, not by color alone.

- Source: WCAG 2.2 SC 3.3.1 Error Identification (Level A), SC 3.3.2 Labels or Instructions (Level A), SC 3.3.3 Error Suggestion (Level AA), tier 1: `knowledge/wcag/sc-3.3.1-error-identification.md`, `knowledge/wcag/sc-3.3.2-labels-or-instructions.md`, `knowledge/wcag/sc-3.3.3-error-suggestion.md`.
- Source: W3C WAI Tutorials, Forms, tier 2, https://www.w3.org/WAI/tutorials/forms/

## 8. Language

The page declares its language. A passage in another language is marked. Abbreviations are expanded on first use.

- Source: WCAG 2.2 SC 3.1.1 Language of Page (Level A), SC 3.1.2 Language of Parts (Level AA), tier 1: `knowledge/wcag/sc-3.1.1-language-of-page.md`, `knowledge/wcag/sc-3.1.2-language-of-parts.md`.

## How these are checked

- The `content` skill applies them while writing and measures reading level before handing text back.
- The verifier reports content under its own heading: reading level measured against the spec target; headings, links, alt text, and errors judged against these standards. Judgment calls are marked manual review.
- Evals for content are text in, findings out. See the roadmap, packages 3.3 and 4.7.
