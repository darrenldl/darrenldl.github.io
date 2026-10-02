---
maxwidth: "120ch"
title: Docfd - Reliability and Testing
---

[**Back to Main Page**](../index.md)

## Failure Model

> **TODO:** Describe the main failure classes: recoverable document conversion failures, OCaml exceptions, worker cancellation, SQLite busy/transaction failures, native crashes, and apparent UI freezes.

## SQLite Hardening

> **TODO:** Describe exclusive connection checkout, `FULLMUTEX` connections, statement finalization, transaction cleanup, bounded busy retries, and connection disposal after callback failure.

## Worker Failure Reporting

> **TODO:** Describe worker exception capture, preservation of raw backtraces, debug-log reporting, and why native signals require core dumps rather than OCaml exception handling.

## Native Crash Case Study

> **TODO:** Document the investigation from a rare SIGSEGV, through the `sqlite3_finalize`/invalid-mutex backtrace, to the sqlite3-ocaml 5.4.2 GC-rooting fix and the raised dependency floor.

## Testing

Docfd is tested in two ways: CLI behavioural tests (cram tests), and direct testing of internal components.

For the cram tests, initial basic test cases are added as part of development, with the more complicated test cases
slowly accumulated as I dogfood Docfd. The main benefit is to establish a corpos of expected behaviour and to guard
against regression in future releases systematically. These include:

| Test suite | Description |
| --- | --- |
| `file-collection-tests` | Recursive scanning behaviour, e.g. scan depth, filter by extension and glob, filtering precedence |
| `line-wrapping-tests` | Text rendering with line wrapping at word boundary, and word breaking as last resort when width is less size of word |
| `misc-behavior-tests` | Temp file handling when text is piped through stdin, search result printing with `--underline` formatting flag |
| `printing-tests` | Non-interactive mode search result printing behaviour |
| `match-type-tests` | Search expression edge cases testing |
| `open-with-tests` | `--open-with` variable substitution and command invocation |
| `non-interactive-mode-return-code-tests` | Exit code of Docfd command in non-interactive mode |
| `search-scope-narrowing-tests` | Correctness of search scope narrowing |
| `script-tests` | Docfd script loading and lookup behaviour |
| `config-tests` | Docfd config loading behaviour |

Since the CLI interface of Docfd can already trigger majority of the code paths,
direct testing of the internal library components is not heavily utilised.
Though some particularly error prone components are directly tested in the form of unit tests:

- Search expression parsing which includes some Abstract Syntax Tree (AST) rewriting/normalisation
- Normalisation of file system paths to absolute paths

## Lessons and Remaining Limits

> **TODO:** Summarise what the hardening work changed, which risks are intentionally accepted, and what diagnostics remain available if another rare freeze or native crash occurs.
