---
maxwidth: "100ch"
title: Docfd User Guide - Key Bindings
toc: true
---

[**Back to User Guide**](index.md)

Docfd is modal: most keys in NAVIGATE mode either perform an action or
open a short-lived mode with its own bindings. The current mode is shown
at the left of the status bar.

Press `<` or `>` in NAVIGATE mode to rotate the on-screen key binding
grid, and press `?` to show or hide it.

## Navigate

### Selection and Opening

| Key | Action |
|---|---|
| `j`, `Down`, or `Page Down` | Select the next document. If only one document is listed, select its next search result instead. |
| `k`, `Up`, or `Page Up` | Select the previous document. If only one document is listed, select its previous search result instead. |
| `Shift`+`j`, `Shift`+`Down`, or `Shift`+`Page Down` | Select the next search result in the current document. |
| `Shift`+`k`, `Shift`+`Up`, or `Shift`+`Page Up` | Select the previous search result in the current document. |
| `g` | Select the first document. |
| `Shift`+`g` | Select the last document. |
| `Enter` | Open the selected document at the selected search result, when possible. |
| `Space` | Toggle the mark on the selected document. |

### Search, Filter, and Ranking

| Key | Action |
|---|---|
| `/` | Enter SEARCH mode. |
| `f` | Enter FILTER mode. |
| `Shift`+`f` | Enter PATH-FUZZY-RANK mode. |
| `x` | Enter CLEAR mode. |
| `n` | Enter NARROW mode. |

### Views and Session History

| Key | Action |
|---|---|
| `-` / `=` | Scroll the document content view up/down. |
| `Left` / `Right` | Adjust the screen split. |
| `v` | Show or hide the content/search-result pane. |
| `?` | Show or hide the key binding pane. |
| `<` / `>` | Rotate the on-screen key binding grid. |
| `l` | Enter LINKS mode for links found in the selected document. |
| `u` or `Ctrl`+`z` | Undo. |
| `Ctrl`+`r` or `Ctrl`+`y` | Redo. |
| `h` | Edit the complete command history in an external editor. |

### Actions and Scripts

| Key | Action |
|---|---|
| `s` | Enter ascending SORT mode. |
| `Shift`+`s` | Enter descending SORT mode. |
| `y` | Enter COPY mode for search results. |
| `Shift`+`y` | Enter COPY-PATHS mode. |
| `d` | Enter DROP mode. |
| `m` | Enter MARK mode. |
| `Shift`+`m` | Enter UNMARK mode. |
| `r` | Enter RELOAD mode. |
| `Ctrl`+`s` | Save the session as a Docfd script. |
| `Ctrl`+`o` | Open the script picker. |
| `Ctrl`+`c` or `Ctrl`+`q` | Exit Docfd. |

## Search and Filter Inputs

SEARCH and FILTER update their results as text is entered.

| Key | SEARCH | FILTER |
|---|---|---|
| Printable character | Insert at the cursor. | Insert at the cursor. |
| `Backspace` | Delete before the cursor. | Delete before the cursor. |
| `Left` / `Right` | Move the cursor. | Move the cursor. |
| `Enter` or `Esc` | Commit the current text and return to NAVIGATE. | Commit the current text and return to NAVIGATE. |
| `Tab` | No action. | Autocomplete the current filter keyword. |

## Action Modes

Pressing `Esc` cancels any of the modes in this section and returns to
NAVIGATE.

### Clear and Sort

| Mode | Key | Action |
|---|---|---|
| CLEAR | `/` | Clear the search field. |
| CLEAR | `f` | Clear the filter field. |
| CLEAR | `h` | Clear the command history and restore the starting state. |
| SORT-ASC / SORT-DESC | `s` | Sort by search-result score. |
| SORT-ASC / SORT-DESC | `p` | Sort by path. |
| SORT-ASC / SORT-DESC | `d` | Sort by path date. |
| SORT-ASC / SORT-DESC | `m` | Sort by modification time. |

### Drop, Mark, and Narrow

| Mode | Key | Action |
|---|---|---|
| DROP | `d` | Drop the selected document. |
| DROP | `Shift`+`d` | Drop every document except the selected one. |
| DROP | `l` / `Shift`+`l` | Drop listed/unlisted documents. |
| DROP | `m` / `Shift`+`m` | Drop marked/unmarked documents. |
| MARK | `l` | Mark all listed documents. |
| UNMARK | `l` | Unmark all listed documents. |
| UNMARK | `a` | Unmark all documents. |
| NARROW | `0`--`9` | Narrow the search scope to level N. |

Dropping removes documents from the current session, not from the
filesystem.

### Copy

| Mode | Key | Action |
|---|---|---|
| COPY | `y` | Copy the selected search result. |
| COPY | `a` | Copy all results from the selected document. |
| COPY | `m` | Copy results from marked documents. |
| COPY | `l` | Copy results from listed documents. |
| COPY-PATHS | `y` | Copy the selected document path. |
| COPY-PATHS | `m` / `Shift`+`m` | Copy paths of marked/unmarked documents. |
| COPY-PATHS | `l` / `Shift`+`l` | Copy paths of listed/unlisted documents. |

### Reload

| Key | Action |
|---|---|
| `r` | Reload the selected document. |
| `a` | Rescan and reload the complete document source. |

## Links and Path Ranking

### Links

| Key | Action |
|---|---|
| `j`, `Down`, or `Page Down` | Select the next link. |
| `k`, `Up`, or `Page Up` | Select the previous link. |
| `Enter` | Open the selected link and return to NAVIGATE. |
| `o` | Open the selected link and remain in LINKS mode. |
| `y` | Copy the selected link and return to NAVIGATE. |
| `Esc` | Return to NAVIGATE. |

### Path Fuzzy Rank

Typing updates the path ranking. `Up` and `Down` select a document,
`Enter` pins the current ranking and returns to NAVIGATE, and `Esc`
returns without pinning it.

## Script Inputs and Dialogs

### Save Script

| Key | Action |
|---|---|
| Printable character, `Backspace`, `Left`, or `Right` | Edit the script name. |
| `Tab` | Autocomplete the name from existing scripts. |
| `Enter` | Submit the name. A new script is saved immediately, an existing script opens the overwrite confirmation. |
| `Esc` | Cancel and return to NAVIGATE. |

If the name is invalid, `Enter` or `Esc` dismisses the message and
returns to name editing with the entered name restored.

| Prompt | Key | Action |
|---|---|---|
| Overwrite existing script | `y` | Overwrite it, then show the edit prompt. |
| Overwrite existing script | `n` or `Esc` | Cancel and return to NAVIGATE. |
| Edit saved script | `y` | Open the script in an external editor. |
| Edit saved script | `n` or `Esc` | Skip editing and return to NAVIGATE. |

### Open or Delete Script

Typing filters the script list.

| Key | Action |
|---|---|
| `Up` / `Down` | Select a script. |
| `Enter` | Run the selected script. |
| `Ctrl`+`x` | Ask to delete the selected script. |
| `Esc` | Cancel and return to NAVIGATE. |

At the deletion prompt, press `y` to delete the script, or `n`/`Esc`
to return to the script picker.

## Command History Editing

`h` leaves the TUI temporarily and opens the session command history in
the configured external editor. The editor's own keyboard bindings apply
there. Saving and exiting causes Docfd to replay the edited history.
Exiting without changing the file leaves the session unchanged.

If a command cannot be parsed or run, Docfd reopens the editor at the
first error and inserts a temporary `;` diagnostic below the offending
line. Lines beginning with `#` are persistent user comments, while blank
lines and `;` system comments are omitted when the history is rebuilt.
