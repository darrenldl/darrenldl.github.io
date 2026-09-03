---
maxwidth: "80ch"
title: Docfd User Guide - Filtering and Navigating Results
---

[**User Guide**](index.md) | [**Engineering Case Study**](../index.md)

## Filter Results

> **TODO:** Explain content and path filtering with concrete examples.

For a Docfd repository search such as `filter`, use path-fuzzy
filters to move between different kinds of results without changing the content
query:

```text
path-fuzzy:lib
path-fuzzy:cram
path-fuzzy:changelog
```

For a directory of technical reports, the same technique can distinguish
domains:

```text
path-fuzzy:automotive
path-fuzzy:coding-standards
path-fuzzy:secure-development
```

This works best when documents are stored under meaningful directory names,
rather than collected into one flat directory.

> **TODO:** Add the exact keys for opening, applying, editing, clearing, and
> cancelling a filter.

> **RECORDING TODO (15–20 seconds):** Reuse the relevant portion of the
> "Searching Docfd with Docfd" portfolio recording if it remains clear without
> its engineering narration. Begin with results for `filter`, apply
> `path-fuzzy:lib`, replace it with `path-fuzzy:cram`, then clear or undo the
> filter.

## Navigate Results

> **TODO:** Explain selection, result movement, and opening documents.

The repository example should culminate in opening an implementation result in
the configured editor. The PDF example should culminate in opening the selected
report at the page containing the match.

## Undo and Redo

> **TODO:** Explain the user-visible history workflow and its limits.

As a practice exercise, switch the repository filter from `lib` to `cram`, then
undo and redo that change while keeping the content search intact.

## Narrow Search Scope

> **TODO:** Explain how narrowing differs from filtering: a filter controls
> which current results are visible, while narrowing constrains the document
> scope used by a subsequent search.

> **OPTIONAL RECORDING TODO (15–20 seconds):** Run a broad search, narrow the
> scope to the current results, run a second search, show that excluded
> documents do not return, and finally reset the scope. Record this only if the
> distinction is still difficult to understand after the written example is
> complete.
