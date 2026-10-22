# Verifier run, 2026-10-22, eval 004

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), same conditions as the other runs.

Result against `expected.md`: **pass**. This is the eval axe cannot catch, and the agent found the defect by reading: one Definite finding, SC 1.3.1 Info and Relationships (Level A), tier 1, sourced to the entry with the line quoted, at the first row and first column of the table, with H51 and H63 as fix directions. It did not treat the clean axe run as a pass. Nothing from the must-not list; the caption, contrast, and the border color were checked and declared passing, with a correct note that a table border is not a user interface component under 1.4.11. No file modified.

Observation, acted on in this PR: the agent reported that `td-has-header` is tagged experimental in axe-core 4.14 and did not run. The 1.3.1 entry's automated-coverage section now says so.

## Report as returned (findings and scan)

### [Definite] Data table has no header cells
- Where: `input.html`, lines 21 to 53 (`main > table`); specifically lines 23 to 28 (first row) and the first cell of each of lines 29 to 52.
- What: The table presents a header row ("Paper size", "Black and white", "Color", "Double-sided") and a header column (Letter, Legal, Tabloid, Poster) entirely as `td` cells, with the header appearance supplied only by CSS (`tr:first-child td { font-weight: bold; background: #f2f2f2; }`), so no cell is programmatically a header and no data cell is associated with its column or row label.
- Criterion: WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), tier 1
- Source: knowledge/wcag/sc-1.3.1-info-and-relationships.md ("Data in a table without any `th` header cells, or header cells not marked as such. Definite. F91.")
- Fix direction: Mark the first row's cells as `th scope="col"` and the first cell of each data row as `th scope="row"` (Techniques H51 and H63), wrapping the header row in `thead` if the structure is to be explicit; the CSS can then target `th`.

No other defects found. Text contrast 17.4:1 on white and 15.55:1 on the header-row background. Border `#767676` measures 4.54:1 on white, but a table cell border is neither a user interface component nor a graphical object required to understand content, so 1.4.11 does not apply. `lang`, `title`, landmarks, single `h1`, zoom not blocked. No images, media, forms, links, scripts, or motion.

Content: reading level grade 0.5 on an eleven-word sample; heading and title match; caption describes the table; "ID" unexpanded raised as manual review; "Not available" as cell text noted as the better choice.

Manual checks remaining: screen reader cell navigation before and after the fix; confirm both axes are the labels readers use; 400% reflow of the four-column table; text-spacing override in cells; "ID card" comprehension.

Automated scan: axe-core 4.14.0. 0 violations, 0 incomplete, 20 passes, 70 inapplicable. Rules that ran and passed on the table: `color-contrast`, `table-duplicate-name`, `td-headers-attr`, `th-has-data-cells`. `td-has-header`, which would flag this, is tagged experimental and is not part of the default run. This defect is a manual-read catch, not an axe catch.
