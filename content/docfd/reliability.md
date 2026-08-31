---
maxwidth: "80ch"
title: Docfd - Reliability and Debugging
---

[**Back to Docfd**](index.md)

## Failure Model

> **TODO:** Describe the main failure classes: recoverable document conversion failures, OCaml exceptions, worker cancellation, SQLite busy/transaction failures, native crashes, and apparent UI freezes.

## SQLite Hardening

> **TODO:** Describe exclusive connection checkout, `FULLMUTEX` connections, statement finalization, transaction cleanup, bounded busy retries, and connection disposal after callback failure.

## Worker Failure Reporting

> **TODO:** Describe worker exception capture, preservation of raw backtraces, debug-log reporting, and why native signals require core dumps rather than OCaml exception handling.

## Native Crash Case Study

> **TODO:** Document the investigation from a rare SIGSEGV, through the `sqlite3_finalize`/invalid-mutex backtrace, to the sqlite3-ocaml 5.4.2 GC-rooting fix and the raised dependency floor.

## Testing

> **TODO:** Describe unit and expect tests for search behavior, cram tests for complete CLI workflows and exit statuses, and clean container builds for native dependency changes.

## Lessons and Remaining Limits

> **TODO:** Summarise what the hardening work changed, which risks are intentionally accepted, and what diagnostics remain available if another rare freeze or native crash occurs.
