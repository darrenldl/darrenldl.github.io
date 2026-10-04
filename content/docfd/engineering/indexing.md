---
maxwidth: "100ch"
title: Docfd - Indexing
---

[**Back to Main Page**](index.md)

The core data structures behind Docfd search engine are a dictionary
(collection of words observed across all documents) and inverted
indices for documents, which are constructed by the indexing pipeline.

## Document Discovery

## Hashing

TODO

## Main Indexing Work

### Tokenization

Document content is tokenized based on:

- Contiguous alphanumeric characters
- Individual symbols
- Individual UTF-8 characters
- Spaces

## Indexing Pipeline

Docfd uses the typical pipelining setup to avoid CPU bound tasks waiting on I/O bound tasks and vice versa.

We begin by examining the naive setup:

![Figure: Single-threaded Naive Timeline](docfd-indexing-naive-timeline.svg)

This is a classic case of unnecessary delay where I/O of a work item
waits for CPU work of the previous work item, and vice versa.

A more ideal timeline would look closer to:

![Figure: Single-threaded Optimal Timeline](docfd-indexing-optimal-timeline.svg)

This is straightforward to implement by using an actor model design:

![Figure: Single-threaded Pipeline Design](docfd-indexing-pipeline-simple.svg)

Finally, we also try to saturate I/O and CPU by changing the first two
layers into using multiple workers intead of just one worker. The final
DB write layer remains a single worker as there is no benefit to
parallel writes for SQLite DB unless WAL is used, but WAL is not
enabled for simplicity and some minor reliability issues observed
during development (likely some errors on my end, but did not have time
to investigate fully).

![Figure: Final Pipeline Design](docfd-indexing-pipeline.svg)

## Evolution of Index Storage

### JSON and Compression

> **TODO:** Version 7.1.0: Explain why GZIP compression was added to the JSON index and what it improved without changing the fully materialized index design.

### Moving to CBOR

> **TODO:** Version 9.0.0-rc1: Explain why JSON+GZIP was replaced by CBOR+GZIP, and which serialization costs or limitations remained.

### Moving to SQLite

> **TODO:** Version 9.0.0: Explain why CBOR+GZIP was replaced by SQLite after the in-memory index reached 1.9 GB on the 1.4 GB PDF corpus, including the reduction to 39 MB and the resulting search-speed trade-off.

### Subsequent SQLite Optimisation

> **TODO:** Version 10.0.0: Explain why the database schema was redesigned, how this reduced index size by roughly 60%, and why the change required rebuilding existing indexes.

> **TODO:** Version 12.0.0-alpha.13: Explain why a global word table was introduced, how it reduced duplication and improved search speed, and why this caused another breaking database change.

## Storage and Performance Trade-offs

> **TODO:** Add measured data for index size, startup time, search latency, and memory use. State the corpus and hardware used for each measurement.
