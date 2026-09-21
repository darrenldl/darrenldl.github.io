---
maxwidth: "80%"
title: Docfd - Search Engine and Indexing
---

[**Back to Docfd**](index.md)

- Docfd accomplishes multiline search through a straightforward combination of
  inverted index and proximity search between words.
    - The inverted index (i.e. a mapping from a word to all its
      appearing positions) is first searched through once to find the
      matches for the first word in the search phrase.
    - DFS is then used for the remaining words, where the word is searched
      within a specified distance from the previous word.
      In other words, the path in this DFS is the list/sequence of words in the document matching the search phrase.
- Fuzzy matching is handled by using the Levenshtein distance as part of
  the matching criteria for each word. An automaton is computed for
  each word of the search phrase for optimised repeated matching.

## Search Phrase and Search Procedure

Document content and user input in the search field are tokenized/segmented
in the same way, based on:

- Contiguous alphanumeric characters
- Individual symbols
- Individual UTF-8 characters
- Spaces

A search phrase is a list of said tokens.

Search procedure is a DFS through the document index,
where the search range for a word is fixed
to a configured range surrounding the previous word (when applicable).

A token in the index matches a token in the search phrase if they fall
into one of the following cases:
- They are a case-insensitive exact match
- They are a case-insensitive substring match (token in search phrase being the substring)
- They are within the configured case-insensitive edit distance threshold

Search results are then ranked using a heuristic.

## Indexing Pipeline

> **TODO:** Describe document discovery, format detection, PDF/DOCX conversion, tokenization, document ID allocation, incremental hashing, and SQLite transactions.

We begin by examining the naive setup:

![Figure: Single-threaded Naive Timeline](docfd-indexing-naive-timeline.png)

This is a classic case of unnecessary delay where I/O of a work item
waits for CPU work of the previous work item, and vice versa.

A more ideal timeline would look closer to:

![Figure: Single-threaded Optimal Timeline](docfd-indexing-optimal-timeline.png)

This is straightforward to implement by using an actor model design:

![Figure: Single-threaded Pipeline Design](docfd-indexing-pipeline-simple.png)

Finally, we also try to saturate I/O and CPU by changing the first two
layers into using multiple workers intead of just one worker. The final
DB write layer remains a single worker as there is no benefit to
parallel writes for SQLite DB unless WAL is used, but WAL is not
enabled for simplicity and some minor reliability issues observed
during development (likely some errors on my end, but did not have time
to investigate fully).

![Figure: Final Pipeline Design](docfd-indexing-pipeline.png)

### Hashing Performance

> **TODO:** Version 9.0.0-rc1: Explain why detecting changed files made hashing part of startup performance, and why the BLAKE2B implementation was moved from the OCaml backend to the C backend.

## Candidate Generation and Pruning

> **TODO:** Explain global first-word candidate generation, document pruning, search scopes, and how the search is divided into parallel jobs.

## Ranking

> **TODO:** Explain the result-ranking heuristic and the interaction between content relevance, path ordering, and path fuzzy ranking.

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

## Search Language

> **TODO:** Decide whether to include a small representative example here or link to the complete [search-language documentation](https://github.com/darrenldl/docfd/wiki/Content-searching).

An expression in the search language is one of:

- Search phrase
- `?expression` (optional)
- `(expression)`
- `expression | expression` (or), e.g. `go ( left | right )`

To use literal `?`, `(`, `)` or `|`, a backslash (`\`) needs to be placed in front
of the character.

A search phrase is a sequence of tokens where a token is one of:

- Unannotated (fuzzy match, e.g. `hello` means fuzzy match `hello`)
- `'tok` (`'` prefix means exact match the token)
- `^tok` (`^` prefix means prefix match the token)
- `tok$` (`$` suffix means suffix match the token)
- `~` (explicit spaces, i.e. contiguous sequence of spaces, tabs, etc)

Tokens that are not separated by spaces, operators, or  parentheses
are treated specially, we call these linked tokens. For example,
`12`, `:`, `30` are linked in `12:30`, but not in `12 : 30`. Linked
tokens have a much stricter search distance by default, e.g. in
`12:30`, Docfd will search for `:` only up to a few tokens away
from `12`, and so on. This allows user to state intention of
reduced fuzziness.

To link spaces to tokens, one needs to be make use of `~`. For
example, to search for "John Smith" ("John" and "Smith" separated
by some number of spaces), one can use `John~Smith` to establish
linkage.

For `'`, `^`, `$` to be considered annotation markers, there cannot
be space between the marker and token, e.g. `^abc` means "prefix
match `abc`", but `^ abc` means "fuzzy match `^` and fuzzy match
`abc`".

Annotated linked tokens are also treated specially:

- `^12:30` is equivalent to `'12` `':` `^30`
- `'12:30` is equivalent to `'12` `':` `'30`
- `12:30$` is equivalent to `12$` `':` `'30`

But with even stricter search restriction than the normal linked
tokens, namely the next matching token must follow immediately from
the current match, e.g. `^12:3` will not match `12 : 30` but will
match `12:30`

### ? operator handling specifics

For a phrase with the optional operator, such as `?word0 word1 ...`,
the first word is grouped implicitly,
i.e. it is treated as `(?word0) word1 ...`.

### Why is there no & operator?

This one comes more from author's personal preference than implementation difficulty.

### Explanation

There are a lot of similar software that provide a `&` operator in the primary search/filter field, so it seems natural for Docfd to carry it in the search language as well.
However, there is a mismatch in where a search result sits in the hierarchy of data between Docfd and other programs, which
means the design in Docfd demands different considerations.

For programs that carry `&` operator or something comparable,
the search result is often limited at the container boundary level, e.g. document, section.
For instance, searching `a & b` in a document management system will give you documents that contain both "a" and "b".
At this level, a conjunction makes sense as a filter/membership test.
It is obvious that when document satisfies `a & b`.

And indeed, the filter language of Docfd supports this, e.g. one may use `"a" and "b"` or `content:"a" and content:"b"` to distill down to the set of documents
with both "a" and "b" in the content.

In Docfd, however, a search result is not just "the relevant document", it's a selection in document content that may cross arbitrary boundaries.

As a search phrase, e.g. "hello world", already implies proximity search in Docfd, it does not make sense to assign the same meaning to `&`.
Now, suppose we assign `&` to mean "less nearby", e.g. `hello world & good morning` assigns an independent search distance between "hello world" and "good morning", what defines a search result then?
If we have "hello world" at start of a long paragraph, and "good morning" at the end of it, do we record the entire paragraph as a search result?
What about when the matches span across multiple paragraphs, do we record all of them?
Even if we skip the inner text of the paragraphs,
this still pose a scalability/generalisation problem of how to extend the rendering algorithm for an arbitrarily long `&` chain.


If we instead show a joined list of matches for `a` and `b`, then we run into a different issue - none of the search results
actually satisfies `a & b`. "hello world", for instance, does not satisfy `hello world & good morning`.
Or if it does, then we are drawing an equivalence between `a | b` and `a & b`, which would immediately beg
the question of why introduce `&` at all.

Filter language on the other hand lives only at the level of documents, and thus there is no issue with the inclusion of `AND` operator there.
