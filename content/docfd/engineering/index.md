---
maxwidth: "80ch"
title: Docfd - Engineering
---

[**Back to Docfd Main Page**](../index.md)

Docfd utilises OCaml 5 and Eio for multithreading, and uses a custom search
engine backed by on-disk SQLite DB.
Architecture wise, Docfd uses
the "functional core, imperative shell" as the core design and
actor model for organising concurrent entities.

![Figure: Workflow Overview](docfd-workflow-overview.svg)

Discussions of specific topics:

- [Design Context](design-context.md)
- [Indexing](indexing.md)
- [Session Manager](session-manager.md)
- [Search Engine](search-engine.md)
