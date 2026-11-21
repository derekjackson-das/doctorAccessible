**Short answer: no, not as written.** The Undo button is the problem. With a control in it, this stops being a toast, and `role="alert"` does not make the button usable. I read the code only; nothing was run.

## Findings

```
WCAG 2.2 SC 2.2.1 Timing Adjustable (Level A), tier 1
Confidence: likely (the entry has no toast case yet; check its exceptions)
Where: toast.js:30, setTimeout(() => toast.remove(), 4000)
What: Undo exists only inside a message that removes itself after 4 seconds, with no way to turn off, adjust, or extend the limit.
Native fix: keep the message and its button on the page until the user dismisses it or moves on.
Entry: knowledge/wcag/sc-2.2.1-timing-adjustable.md; knowledge/aria/live-regions.md
```

```
WCAG 2.2 SC 2.4.3 Focus Order (Level A), tier 1
Confidence: likely; a person confirms (also touches SC 2.1.1 Keyboard, Level A; reported once, here)
Where: toast.js:29, document.body.appendChild(toast)
What: The Undo button is inserted at the end of the document, far from the Delete button that produced it, so a keyboard user must tab past every remaining message to reach it before it is removed.
Native fix: insert the message and its button immediately after the trigger, in the list where the item was (technique SCR26, tier 2).
Entry: knowledge/wcag/sc-2.4.3-focus-order.md
```

```
WCAG 2.2 SC 2.4.3 Focus Order (Level A), tier 1
Confidence: manual review (the entry has no case for a focused element being hidden)
Where: toast.js:37, item.hidden = true
What: The Delete button that has focus sits inside the li being hidden, so focus is left on nothing; where it lands next needs testing in each browser.
Native fix: place focus deliberately after the delete, on the inline message or the next message's control.
Entry: knowledge/wcag/sc-2.4.3-focus-order.md
```

```
WCAG 2.2 SC 4.1.3 Status Messages (Level AA), tier 1
Confidence: likely; behavior varies by assistive technology, a person confirms
Where: toast.js:24-29
What: The live region is created and filled in the same moment, so the message is often not announced.
Native fix: an empty role="status" container (or an output element) in the HTML at load, with text written into it later.
Entry: knowledge/wcag/sc-4.1.3-status-messages.md
```

```
Advice, not a WCAG finding: role="alert" is the wrong level for "Message deleted".
Source: WAI-ARIA 1.2 (W3C Rec, 6 June 2023), tier 1: authors "SHOULD NOT use the assertive value unless the interruption is imperative." Understanding SC 4.1.3 (updated 4 October 2026), tier 2, lists a failure technique for this with no ID yet: pending.
Confidence: likely per knowledge/aria/live-regions.md. The 4.1.3 entry says manual review on fit; I took the stricter reading.
Where: toast.js:26
Fix: role="status".
```

```
Advice, not a WCAG finding: a button inside a live region is announced as text only.
Source: knowledge/aria/live-regions.md. Soueidan, 2024, tier 3, recorded a button in a live region announced as its text with no role (VoiceOver with Safari, no versions given). Treat it as a lead to test.
Where: toast.js:27
```

## What I would build instead

The library entry is direct on this: a message that holds a button is not a live region and not a toast (Soueidan 2024, O'Hara 2019, Roselli 2020, all tier 3). The smallest thing that works is to keep the message in the page:

1. Where the deleted item was, show a row in the list: "Message deleted" and a real `<button type="button">Undo</button>`.
2. Leave it there until the user dismisses it, deletes another message, or leaves the page. No timer.
3. Move focus to that row after the delete. That is a direct result of the user's action, so it is a legitimate focus move, and 4.1.3 then does not apply because the message receives focus.

That clears all four findings without ARIA.

If the design must keep the bottom-right toast visually, the fallback is:
- Announce "Message deleted" through one `role="status"` region that exists at load and holds plain text only.
- Keep Undo reachable somewhere that does not expire.
- Still handle focus after the delete.

It is more moving parts for the same result.

I did not check the slide and fade against `knowledge/design/motion.md`; load the `design` skill for that.

## Tests for a person to run

With NVDA and Firefox, VoiceOver and Safari, and keyboard only, per the spec. Record versions with each result.

1. Delete a message with focus on Delete. Record whether anything was announced, the exact words, and whether anything was cut off.
2. Record where focus is immediately after the delete.
3. Reach and activate Undo by keyboard alone, and with each screen reader. Record whether it was possible and how many key presses it took.
4. Delete two messages in quick succession and record what was announced.

The spec has no pattern decision recorded for notifications. Tell me which way you want to go and I will propose the wording for `a11y-spec.md`; I have not changed any files.
