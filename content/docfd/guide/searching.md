---
maxwidth: "80ch"
title: Docfd User Guide - Searching
---

[**User Guide**](index.md) | [**Engineering Case Study**](../index.md)

## Search Modes

> **TODO:** Explain the available search modes from the user's perspective.

## Multiline and Fuzzy Search

> **TODO:** Provide task-oriented examples and describe the expected results.

Useful searches against the Docfd repository include:

```text
filter
configuration file
command history
search results
cancellation
```

To exercise document conversion separately, start Docfd over a directory of
technical PDFs and try phrases such as:

```text
verification and validation
requirements traceability
static analysis
```

A misspelling such as `maintainence and testing` can be used to demonstrate
fuzzy matching.

> **TODO:** Explain how to tune fuzzy and proximity behaviour and how users can
> tell which search mode is being used.

## Search PDFs

Public-use government technical reports make a reproducible example corpus.
Keep related documents in descriptive subdirectories so the same corpus can
also be used to practise filtering:

```text
technical-reports/
├── automotive/
├── coding-standards/
├── secure-development/
└── software-process/
```

> **TODO:** Add the final report download links, attribution, optional PDF
> converter requirements, and the exact command used to start Docfd.

## Non-interactive Search

> **TODO:** Document relevant command-line workflows and exit behaviour.
