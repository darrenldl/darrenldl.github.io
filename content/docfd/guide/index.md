---
maxwidth: "100ch"
title: Docfd User Guide
toc: true
---

[**Back to Docfd Main Page**](../index.md)

## Installation

Docfd is primarily distributed as statically linked binaries via [GitHub Releases](https://github.com/darrenldl/docfd/releases)

Refer to the [Installation](https://github.com/darrenldl/docfd#installation) section for other distribution channels.

## Getting Started

We will use the Docfd Engineering pages of this GitHub site for this walkthrough, which can be cloned by:

```
$ git clone https://github.com/darrenldl/darrenldl.github.io.git
```

But feel free to use any local directory as Docfd is fully offline
and does not modify or move your documents.

### Startup

```
$ cd darrenldl.github.io/
$ docfd
```

![Figure: Docfd TUI Overview at Startup](docfd-tui-overview.svg)

**Useful tip about looking up key bindings:**

- Press `<` or `>` to rotate the key binding info grid.
- Generally the most commonly used key bindings are put closer to the
  left side of the grid.

### Filtering

Steps:

- Type `f` to enter FILTER mode
- Type `p` and press Tab to autocomplete to `path-`

![Figure: Docfd TUI After Filtering Step 2](docfd-screenshot-filtering-after-step-2.png)

- Type `f` and press Tab to autocomplete to `path-fuzzy:` as a whole

![Figure: Docfd TUI After Filtering Step 2](docfd-screenshot-filtering-after-step-3.png)

- Type `"content engineering"` to complete the full string to `path-fuzzy:"content engineering"`

- Press Enter to exit FILTER mode

![Figure: Docfd TUI After Filtering Step 5](docfd-screenshot-filtering-after-step-5.png)

### Dropping

To keep the UI less cluttered, it's often useful to "clear the table"
and just focus on the documents at hand with input fields ready for new
filter or search criteria.

Steps:

- Type `d` to enter DROP mode

![Figure: Docfd TUI After Dropping Step 1](docfd-screenshot-dropping-after-step-1.png)

- Type `Shift`+`L` to drop the unlisted documents (documents that do
  not match the filter and search criteria). In this specific case, we
  saw `7/44 documents listed` on the status bar prior, that means we will be
  dropping 37 documents. After which the status bar should read `7/7 documents listed`.
- Type `xf` to clear the filter field now that we don't need to keep
  seeing the filter expression.

![Figure: Docfd TUI After Dropping Step 3](docfd-screenshot-dropping-after-step-3.png)

### Searching

Steps:

- Type `/` to enter SEARCH mode
- Type `search engine`.
- Press Enter to submit and exit SEARCH mode. Note that since Docfd is
  "search as you type", a lot of the times the search is already done by
  the time you hit Enter.

![Figure: Docfd TUI After Searching Step 3](docfd-screenshot-searching-after-step-3.png)

- Use `Shift` + `j`/`k` or up/down to select a search result within a document.
- Use `j`/`k` or up/down to select a document.

![Figure: Docfd TUI After Searching Step 5](docfd-screenshot-searching-after-step-5.png)

- Press Enter to open the search result in editor. Docfd recognises
  common text editors from `$VISUAL` or `$EDITOR`, and invokes the
  editor with the line number to open to when possible.

![Figure: Docfd TUI After Searching Step 6](docfd-screenshot-searching-after-step-6.png)

### Undo/redo

Steps:

- Type `u` or `Ctrl`+`Z` to undo
- Type `Ctrl`+`R` or `Ctrl`+`Y` to redo

Note that as Docfd only stores a limited number of session snapshots at
a time, sometimes undoing or redoing requires recomputation of search
or filter results and can take a bit longer.

### Editing Command History

If you want to undo in bulk, add new actions, or just look at the actions done
in the session thus far, you can make use of the command history editing functionality.

Steps:

- Type `h` to bring up the session command history into the editor.

![Figure: Docfd TUI After Command History Step 1](docfd-screenshot-command-history-after-step-1.png)

- Remove or add commands as desired, and upon saving Docfd will
  recompute the session based on the revised history.
  In this case we change our filter query to be `path-fuzzy:"search engine"` and
  our search query to be `search: depth` instead.

![Figure: Docfd TUI After Command History Step 2](docfd-screenshot-command-history-after-step-2.png)

- Save and exit the editor, Docfd should now display the newest session state according to the new version of session history.

![Figure: Docfd TUI After Command History Step 3](docfd-screenshot-command-history-after-step-3.png)

- If Docfd fails to parse any line, you would be brought back to the editor
  (similar to `git rebase -i`), where the problematic line would be followed by
  `# Failed to parse the above command`.

![Figure: Docfd TUI After Command History Step 4](docfd-screenshot-command-history-after-step-4.png)

## What to Try Next

### Docfd Script

If you often repeat some search or repeat some starting steps for a particular project,
you may find the scripting capability handy. Docfd script follows the same format as the command history

Steps to save a script:

- Type `Ctrl`+`S`

Steps to open a script:

- Type `Ctrl`+`O`

Steps to delete a script:

- Type `Ctrl`+`O`

### Config File

TODO

## Reference and Help

- [Searching](searching.md)
- [Filtering and navigating results](filtering-and-navigation.md)
- [Scripts and repeatable workflows](scripts.md)
- [Configuration](configuration.md)
- [Keyboard reference](keyboard-reference.md)
- [Troubleshooting](troubleshooting.md)
