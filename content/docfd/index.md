---
maxwidth: "80ch"
title: Docfd
---

[**Back to Home**](..)

## Introduction

[Online Demo](https://demo.docfd.sh) | [GitHub](https://github.com/darrenldl/docfd) | [Wiki](https://github.com/darrenldl/docfd/wiki)

[Docfd](https://github.com/darrenldl/docfd) is in a TUI program that allows you to fuzzy search for
a phrase across multiple lines, across text files, PDFs, DOCX, etc.

While the README does a reasonable job briefing over what Docfd is,
I still want to talk about Docfd in greater details.
In part to document the engineering effort that went into
Docfd, and in part as a portfolio building exercise.

> **TODO:** Add a concise project summary, the principal technical constraints, and the main technologies used.

![Docfd interactive demonstration](gifs/repo.gif)

## Product Walkthrough

> **TODO:** Describe the interactive workflow shown above: startup and incremental indexing, multiline search, filtering, navigation, and opening a result.

![Docfd non-interactive demonstration](gifs/repo-non-interactive.gif)

> **TODO:** Describe the non-interactive and scripting workflow shown above.

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

> **TODO:** Describe the unit, expect, and cram tests; container builds; release process; and dependency-version safeguards.

## Constraints and Measured Trade-offs

> **TODO:** Add measured performance results and describe the test corpus and hardware.

> **TODO:** Summarise the trade-offs between startup work, memory usage, SQLite-backed search, current-file validation, asynchronous responsiveness, and snapshot reconstruction.

## Project Status

> **TODO:** Add current release status, supported platforms and document formats, installation links, and any planned work worth highlighting.

## Structure of Remaining Text

The rest of the Docfd text will revolve around showcasing the different vertical slices
(the specific scenarios or workflows) of Docfd in the form of recordings,
each followed by a technical write-up of how the
implementation all worked together into delivering said vertical slice.

I believe this both delivers a nice feature exploration experience for
new and existing users, and splits the technical writing naturally by
tangible, focused scenarios.
