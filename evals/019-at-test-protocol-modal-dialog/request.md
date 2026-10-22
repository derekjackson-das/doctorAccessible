# Request

The developer types:

> We've built a confirmation dialog for deleting a saved search. Can you write the manual test script for it?
>
> It's a native `<dialog>` opened with `showModal()` when someone presses the "Delete" button next to a saved search. The dialog has a heading "Delete this saved search?", a sentence explaining it can't be undone, and two buttons: "Cancel" and "Delete search". Initial focus goes to "Cancel". Escape closes it. On close, focus goes back to the "Delete" button that opened it. The dialog fades in over 300 ms. After deleting, a message "Saved search deleted" appears at the top of the list in a `role="status"` region.

Project context given with the request: `a11y-spec.md` exists. "Who we are building for" lists: "Tested with NVDA with Firefox, VoiceOver with Safari on macOS, keyboard only, 200% and 400% zoom, reduced motion."
