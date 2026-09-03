---
maxwidth: "80ch"
title: Docfd
---

[**Back to Home**](..)

## Introduction

[Online Demo](https://demo.docfd.sh) | [User Guide](guide/index.md) | [GitHub](https://github.com/darrenldl/docfd)

[Docfd](https://github.com/darrenldl/docfd) is in a local search engine with a Terminal User Interface (TUI) that allows you to fuzzy search for
a phrase across multiple lines, across text files, PDFs, DOCX, etc.

Compared to other local search engines, Docfd allows for a more ad-hoc search style,
where users are not not required to set up a managed central document repository/directory, or pre-configure folders/files
in your home directory to include or exclude.
Instead, Docfd processes unindexed files on-demand when invoked, defaulting to the scanning the current directory recursively.
This overall avoids the sometimes unexpected spikes in CPU and memory usage with periodic indexers which may disrupt other
desktop applications.

Docfd utilises OCaml 5 and Eio for multithreading, and uses a custom search engine
with custom ranking over an inverted index backed by on-disk SQLite DB.

![Docfd interactive demonstration](gifs/repo.gif)

## Walkthrough

This section demonstrates what using Docfd feels like and connects the visible
behaviour to the engineering behind it. For operating instructions, see the
[getting started tutorial](guide/getting-started.md).

### Searching Docfd with Docfd

The primary interactive recording will use the Docfd repository itself as the
corpus. This makes the example real rather than staged: the initial result set
can span implementation files, interfaces, cram tests, documentation, and the
release history.

```sh
docfd --exts=md,txt --single-line-exts=ml,mli,t .
```

The recording should:

1. Search for `filter` across the repository.
2. Show matches from source, tests, and `CHANGELOG.md`.
3. Apply a path-fuzzy filter for `lib`.
4. Replace it with a path-fuzzy filter for `cram`.
5. Navigate to and open a source result in the editor.
6. Undo the filter change to demonstrate session history.

> **TODO:** Record the workflow and explain how asynchronous search,
> cancellation, path ranking, editor integration, and snapshots contribute to
> the visible interaction.

### Searching Technical PDFs

A shorter second recording will use public-use NASA technical reports to show
document conversion and direct navigation to a PDF result. A query such as
`verification and validation`, `requirements traceability`, or a deliberately
misspelled technical phrase should produce results across several reports.

The recording should:

1. Start Docfd over a directory containing several related PDFs.
2. Search for a phrase that returns matches in several documents, including a
   match that crosses line breaks within one document.
3. Filter the results by a meaningful filename or subdirectory such as
   `software-process` or `coding-standards`.
4. Open a selected result at the matching PDF page.

> **TODO:** Select the final public-use corpus, record the workflow, and add
> source attribution next to the recording.

> **TODO:** Describe the non-interactive and scripting workflow shown above.

### Non-interactive use

Docfd also provides a non-interactive mode Although this is not the main use case Docfd is optimised for, a non-interactive mode
is provided for

![Docfd non-interactive demonstration](gifs/repo-non-interactive.gif)

## Engineering Overview

> **TODO:** Add a compact architecture diagram covering document conversion and tokenization, the SQLite inverted index, parallel search, session worker/manager, snapshots, and the Lwd/Nottui UI.

> **TODO:** Summarise the ownership and concurrency boundaries between the UI domain, session manager, worker domain, executor pool, and SQLite connection pool.

## Engineering Deep Dives

- [Search engine and indexing](search-engine.md)
- [Responsive asynchronous UI](async-ui.md)
- [Session history, snapshots, and replay](session-history.md)
- [Reliability and debugging](reliability.md)
- [Design context and alternatives considered](design-context.md)

## Testing and Release Engineering

Formally, Docfd is tested in two ways: CLI behavioural tests (cram tests) and direct testing of internal components.
Many cram tests are regression guards for bugs found through dogfooding, as an actual test suite
interacting with the TUI is not straightforward to accomplish.

The cram tests cover coverage and regression guard, only two internal components are directly tested:

Docfd has been primarily tested at the CLI level via cra, but two specific internal critical components

Unit tests are used to test regression

> **TODO:** Describe the unit, expect, and cram tests; container builds; release process; and dependency-version safeguards.

## Constraints and Measured Trade-offs

> **TODO:** Add measured performance results and describe the test corpus and hardware.

> **TODO:** Summarise the trade-offs between startup work, memory usage, SQLite-backed search, current-file validation, asynchronous responsiveness, and snapshot reconstruction.
