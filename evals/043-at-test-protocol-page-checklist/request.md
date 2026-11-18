# Request

The developer types:

> Can you write a manual AT testing checklist for our Saved reports page, with the expected outcomes, so I can work through it myself? Here's the whole page.
>
> ```html
> <!doctype html>
> <html lang="en">
> <head>
>   <meta charset="utf-8">
>   <title>Saved reports</title>
>   <style>
>     button:focus-visible { outline: 2px solid #1d5fb0; outline-offset: 1px; }
>     .menu { position: absolute; background: #fff; border: 1px solid #ccc; }
>     .toast { position: fixed; bottom: 24px; left: 24px; background: #1c1f24; color: #fff; padding: 10px 14px; }
>   </style>
> </head>
> <body>
>   <main>
>     <h1>Saved reports</h1>
>     <ul id="reports">
>       <li data-id="r1"><span class="name">Monthly sign-ups</span>
>         <button type="button" class="more" aria-haspopup="menu" aria-label="More actions">⋯</button></li>
>       <li data-id="r2"><span class="name">Course completion by term</span>
>         <button type="button" class="more" aria-haspopup="menu" aria-label="More actions">⋯</button></li>
>       <li data-id="r3"><span class="name">Support tickets, last 30 days</span>
>         <button type="button" class="more" aria-haspopup="menu" aria-label="More actions">⋯</button></li>
>     </ul>
>   </main>
>
>   <div id="menu" class="menu" hidden>
>     <button type="button" data-action="rename">Rename</button>
>     <button type="button" data-action="delete">Delete</button>
>   </div>
>
>   <dialog id="rename-dialog">
>     <form method="dialog">
>       <h2>Rename report</h2>
>       <label>Report name <input type="text" name="name"></label>
>       <button type="button" id="rename-cancel">Cancel</button>
>       <button type="submit">Save</button>
>     </form>
>   </dialog>
>
>   <div id="toast" class="toast" hidden>
>     <span>Report deleted</span> <button type="button" id="undo">Undo</button>
>   </div>
>
>   <script>
>     const menu = document.getElementById("menu");
>     const dialog = document.getElementById("rename-dialog");
>     const toast = document.getElementById("toast");
>     let current = null, removed = null, timer = null;
>
>     document.querySelectorAll(".more").forEach((btn) => {
>       btn.addEventListener("click", () => {
>         current = btn.closest("li");
>         const r = btn.getBoundingClientRect();
>         menu.style.left = r.left + "px";
>         menu.style.top = r.bottom + "px";
>         menu.hidden = false;
>         menu.querySelector("button").focus();
>       });
>     });
>
>     document.addEventListener("keydown", (e) => {
>       if (e.key === "Escape") menu.hidden = true;
>     });
>
>     menu.addEventListener("click", (e) => {
>       const action = e.target.dataset.action;
>       menu.hidden = true;
>       if (action === "rename") {
>         dialog.querySelector("input").value = current.querySelector(".name").textContent;
>         dialog.showModal();
>       }
>       if (action === "delete") {
>         removed = { node: current, next: current.nextSibling };
>         current.remove();
>         toast.hidden = false;
>         clearTimeout(timer);
>         timer = setTimeout(() => { toast.hidden = true; removed = null; }, 5000);
>       }
>     });
>
>     document.getElementById("rename-cancel").addEventListener("click", () => dialog.close());
>     dialog.querySelector("form").addEventListener("submit", () => {
>       current.querySelector(".name").textContent = dialog.querySelector("input").value;
>     });
>
>     document.getElementById("undo").addEventListener("click", () => {
>       if (removed) document.getElementById("reports").insertBefore(removed.node, removed.next);
>       toast.hidden = true;
>     });
>   </script>
> </body>
> </html>
> ```

Project context given with the request: no `a11y-spec.md` exists. The developer is on macOS and checks in Chrome and Safari.
