---
maxwidth: "80ch"
title: Docfd - Engineering
---

Docfd utilises OCaml 5 and Eio for multithreading, and uses a custom search
engine backed by on-disk SQLite DB.
Architecture wise, Docfd uses
the "functional core, imperative shell" as the core design and
actor model for organising concurrent entities.

See the following for discussions of specific topics:

- [Design Context](design-context.md)
- [Search Engine and Indexing](search-engine.md)
- [Responsive Asynchronous UI](async-ui.md)
- [Session History, Snapshots, and Replay](session-history.md)
- [Reliability and Testing](reliability.md)
