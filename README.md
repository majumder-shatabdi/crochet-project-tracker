# StitchCraft — Crochet Sizing & Project Tracker

An application designed to calculate exact crochet cast-on stitches based on body size presets and custom tension gauge, while managing ongoing project progress.

---

## Numbered Requirements

### Essential Core Logic
* **REQ-M1:** Store standard chest width measurement presets for standard sizes (Baby: 16", Toddler: 20", Child: 28", Adult S: 34", Adult M: 38", Adult L: 42").
* **REQ-M2:** Calculate foundation stitches dynamically using the formula: `Stitches = Width (inches) * Gauge (stitches per inch)`, rounded to the nearest integer.
* **REQ-M3:** Reject invalid gauge inputs (values <= 0) and raise a `ValueError`.
* **REQ-M4:** Create a project record containing: name, hook size, target rows, and current row count.
* **REQ-M5:** Save active project data to a persistent `projects.json` file and reload it on startup.

### Progress & Management
* **REQ-S1:** Increment (`+1`) and decrement (`-1`) a project's active row counter, strictly preventing row counts below 0.
* **REQ-S2:** Calculate completion percentage as `(current_row / target_rows) * 100`, rounded to 1 decimal place.
* **REQ-S3:** Allow the user to input and save a custom body width measurement.

### Enhancements
* **REQ-C1:** Calculate estimated yarn yardage required based on total stitches.
* **REQ-C2:** Automatically flag a project as `Completed` when `current_row == target_rows`.

---

## Project Architecture
* `core.py`: Pure business logic and calculations (no UI code).
* `test_core.py`: Automated unit tests covering edge cases and calculations.
* `cli_app.py`: Text-based terminal interface (Phase 1).
* `gui_app.py`: Tkinter graphical user interface (Phase 2).
