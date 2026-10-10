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

- If this was a PDF file, then Docfd would open up your default
  PDF viewer.
    - Special handling for Linux: the default PDF viewer is extracted
      via `xdg-mime` to generate the final command that opens the PDF
      viewer to the page of the search result and with the most unique
      word of the search result put in the search bar. This should work
      even if the PDF viewer is installed via Flatpak.

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
  `; Failed to parse the above command ...`.

![Figure: Docfd TUI After Command History Step 4](docfd-screenshot-command-history-after-step-4.png)

## What to Try Next

### Docfd Script

If you often repeat some search or repeat some starting steps for a particular project,
you may find the scripting capability handy. Docfd script follows the same format as the command history

Steps to save a script:

- Type `Ctrl`+`S`

![Figure: Docfd TUI After Docfd Script Saving Step 1](docfd-screenshot-docfd-script-save-after-step-1.png)

Steps to open a script:

- Type `Ctrl`+`O`

![Figure: Docfd TUI After Docfd Script Opening Step 1](docfd-screenshot-docfd-script-open-after-step-1.png)

Steps to delete a script:

- Type `Ctrl`+`O`
- Type `Ctrl`+`X`

![Figure: Docfd TUI After Docfd Script Deletion Step 2](docfd-screenshot-docfd-script-delete-after-step-2.png)

### Common Cli Arguments

Here we list some common cli arguments that you may find useful.

Limit to just specific extensions, e.g. `.md`, `.txt`:

- `docfd --exts md,txt`

Add onto the default list of extensions, e.g. `.js`:

- `docfd --add-exts js`

Scan by globbing:

- `docfd --glob 'content/**'`

Use list of paths from other programs, e.g. `fd`:

- `fd | docfd --paths-from -`

### Config File

#### Location

Docfd looks up the config file in the following order:

- If `--config FILE` was provided as a cli argument, then `FILE` is used
- Closest `.docfd-config` (scanning from current directory up to root directory)
- Home directory config `$XDG_CONFIG_HOME/docfd/config` (Linux) or `$HOME/Library/Application Support/docfd/config`

Note that only one config file is picked, i.e. there is no merging of cli arguments from multiple config files.

Typical usage would be a `.docfd-config` at the project root for project specific configurations.

#### Format

Docfd config file uses the "one cli argument per line" format. For instance, if
we are to store one of the examples from previous section into a config file,
we would have:

```
--exts
md,txt
```

or

```
--exts=md,txt
```

### LINKS Mode

Docfd provides a quick way to open and copy links within a document.
We will use the `design-context.md` file from engineering directory for this.

Steps:

- Filter with `path-fuzzy:design`
- Type `l` to enter LINKS mode

![Figure: Docfd TUI After LINKS Step 2](docfd-screenshot-LINKS-after-step-2.png)

Types of links currently supported are:

- Simple markdown links: `[text](link)`
- Simple Wiki links: `[[link]]`
- Contiguous string that begin with one of: `http://`, `https://`, `file://`

Note that link detection and extraction is not quite complete yet
as of 13.1.3, but will be enhanced in a future release.

## Troubleshooting

### Debug Log

You can enable debug log via:

```
$ docfd --debug-log FILE
```

where `FILE` is the log file for Docfd to output to.

**When you might need this**:

- Docfd gets stuck when indexing some files and you want to narrow down the files.
- You want to check which config file Docfd is loading exactly.

Note that the debug log is not very structured as it's only intended for ad hoc
diagnostics.

### Cache Directory Location

You can find the cache directory location in the help message:

```
$ docfd --help=plain | grep -- --cache-dir
```

**When you might need this**:

- You may need to navigate to this location to clear Docfd index DB during some
  version upgrades (CHANGELOG will note explicitly in this case).
- Docfd index DB becomes corrupted and causes Docfd to freeze. Though this
  should be unlikely as there are already precautions in place, e.g. careful
  ordering of writes to ensure consistency and use of SQLite transactions.

### Data Directory Location

You can find the data directory location in the help message:

```
$ docfd --help=plain | grep -- --data-dir
```

**When you might need this**:

- You may need to navigate to this location to back up your Docfd scripts, for instance.

## References

- [Search Language](search-language.md)
- [Filter Language](filter-language.md)
- [Key Bindings](key-bindings.md)
