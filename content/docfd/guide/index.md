---
maxwidth: "120ch"
title: Docfd User Guide
---

[**Back to Docfd Main Page**](../index.md)

## Installation

Docfd is primarily distributed as statically linked binaries via [GitHub Releases](https://github.com/darrenldl/docfd/releases)

Refer to the [Installation](https://github.com/darrenldl/docfd#installation) section for other distribution channels.

## Getting Started

### Your First Search

We will use the Docfd Engineering pages of this GitHub site for this walkthrough.

You can git clone this GitHub site via

```
git clone https://github.com/darrenldl/darrenldl.github.io.git
```

But feel free to use any local directory as Docfd is fully offline
and does not modify or move your documents.

> **TODO:** Walk through starting Docfd, entering a search, selecting a result, and opening it.

The Docfd source repository can be used as a concrete practice corpus:

```sh
cd /path/to/docfd
docfd --exts=md,txt --single-line-exts=ml,mli,t .
```

Try searching for `filter`. The results should include relevant
implementation, test, documentation, or changelog files. Navigate between the
matches and open one to verify that the editor is positioned at the result.

> **TODO:** Add the exact keys for entering search mode, accepting the query,
> navigating results, and opening the selected match.

> **RECORDING TODO (15–25 seconds):** Start with a clean terminal, launch
> Docfd, enter one search, move through at least two results, and open one in
> the configured editor or PDF viewer. Keep this simpler than the portfolio
> recording and avoid introducing filters or history yet.

### What to Try Next

> **TODO:** Point users towards filtering, scripts, and configuration without explaining their implementation.

After completing the first search, try narrowing the same result set to `lib`
or `cram`. See [Filtering and navigating results](filtering-and-navigation.md)
for the complete workflow.

## Using Docfd

- [Searching](searching.md)
- [Filtering and navigating results](filtering-and-navigation.md)
- [Scripts and repeatable workflows](scripts.md)
- [Configuration](configuration.md)

## Editing/viewing command history

> **TODO:** Add an up-to-date walkthrough of undo/redo, editing command history, and saving or replaying the resulting commands as a Docfd script.

## Reference and Help

- [Keyboard reference](keyboard-reference.md)
- [Troubleshooting](troubleshooting.md)

> **TODO:** Add links to any additional reference pages once their scope becomes clear.

## Recording TODOs

- [ ] Record a 15–25 second first-search clip: start Docfd, enter a query,
  navigate between results, and open one in its associated application.
- [ ] Reuse or extract the filter/undo segment from the portfolio's
  "Searching Docfd with Docfd" recording.
- [ ] Record a 20–30 second history-and-script clip: perform several actions,
  edit their command history, apply the edit, and save the result as a script.
- [ ] Decide whether `--list-scripts`, `--script`, and `--start-with-script`
  need a short recording or only a terminal transcript.
- [ ] Decide whether search-scope narrowing needs a 15–20 second clip after
  the filtering documentation has been written.
- [ ] Reuse the portfolio PDF recording for PDF conversion and result opening;
  do not make a duplicate guide recording unless the portfolio clip is too
  engineering-focused.

Installation, configuration precedence, non-interactive exit statuses,
supported extensions, and debug logging should normally use commands and
expected output rather than recordings.
