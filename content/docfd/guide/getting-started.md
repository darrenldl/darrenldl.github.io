---
maxwidth: "80ch"
title: Docfd User Guide - Getting Started
---

[**User Guide**](index.md) | [**Engineering Case Study**](../index.md)

## Your First Search

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

## What to Try Next

> **TODO:** Point users towards filtering, scripts, and configuration without explaining their implementation.

After completing the first search, try narrowing the same result set to `lib`
or `cram`. See [Filtering and navigating results](filtering-and-navigation.md)
for the complete workflow.

## Related Reading

- [Searching](searching.md)
- [Filtering and navigating results](filtering-and-navigation.md)
