---
maxwidth: "100ch"
title: Docfd User Guide
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

### Searching

Steps:

- Type `/` to enter SEARCH mode
- Type `search engine`
- Press Enter to exit SEARCH mode
- Use `Shift` + `j`/`k` or up/down to select a search result within a document
- Use `j`/`k` or up/down to select a document
- Press Enter to open the search result in editor

TODO: final screenshot

TODO: opening a search result in editor

#### Undo/redo

## What to Try Next

### Config File

TODO

### Editing Command History

TODO

### Docfd Script

TODO

## Reference and Help

- [Searching](searching.md)
- [Filtering and navigating results](filtering-and-navigation.md)
- [Scripts and repeatable workflows](scripts.md)
- [Configuration](configuration.md)
- [Keyboard reference](keyboard-reference.md)
- [Troubleshooting](troubleshooting.md)
