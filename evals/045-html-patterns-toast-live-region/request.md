# Request

The developer types:

> I'm adding a toast for when someone deletes a message. It slides in at the bottom right, says "Message deleted" with an Undo button, and fades out after 4 seconds. For screen readers I create a `role="alert"` div when it fires. Is this OK?

```html
<!-- inbox.html (excerpt) -->
<main>
  <h1>Inbox</h1>
  <ul id="messages">
    <li>
      <span>Lunch on Friday?</span>
      <button type="button" class="delete" data-id="m1">Delete</button>
    </li>
    <!-- more messages -->
  </ul>
</main>
```

```js
// toast.js
function showToast(text, onUndo) {
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.setAttribute('role', 'alert');
  toast.innerHTML = `<p>${text}</p><button type="button">Undo</button>`;
  toast.querySelector('button').addEventListener('click', onUndo);
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}

document.getElementById('messages').addEventListener('click', e => {
  const btn = e.target.closest('.delete');
  if (!btn) return;
  const item = btn.closest('li');
  item.hidden = true;
  showToast('Message deleted', () => { item.hidden = false; });
});
```

Project context given with the request: `a11y-spec.md` exists at the repo root. "Who we are building for" reads: "Harvard staff reading and managing messages on a work laptop. Tested with NVDA with Firefox, VoiceOver with Safari on macOS, keyboard only." No pattern decisions recorded.
