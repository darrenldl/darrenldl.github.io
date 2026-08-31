---
maxwidth: "80ch"
title: Docfd - Search Engine and Indexing
---

[**Back to Docfd**](index.md)

## How does Docfd address my complaints?

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
- Docfd only processes the current directory or the specified directories and
  files upon startup. Hashing is used to check if file has been
  previously indexed. This means there is no central storage requirement,
  and no background indexing.
    - In principle this causes slower start-up time in the general case
      compared to programs with background indexing. But since the set
      of documents of interest is usually small (<1k documents), the
      start-up is often instantaneous.
    - And if the set of documents is really large, then one can always
      fall back to having a long running session of docfd.
- A common speed up tactic for search engines is to load the inverted indices
  into memory, as they are on the hottest paths. Docfd instead keeps it only in
  the on-disk SQLite DB to minimise memory usage, to avoid impacting
  performance of other desktop applications. The tradeoff is that at larger
  scale (say a few thousand documents, depending on the sizes), Docfd will
  noticeably struggle - results will take seconds instead of less than a second
  to show up.

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

## Candidate Generation and Pruning

> **TODO:** Explain global first-word candidate generation, document pruning, search scopes, and how the search is divided into parallel jobs.

## Ranking

> **TODO:** Explain the result-ranking heuristic and the interaction between content relevance, path ordering, and path fuzzy ranking.

## Storage and Performance Trade-offs

> **TODO:** Add measured data for index size, startup time, search latency, and memory use. State the corpus and hardware used for each measurement.

## Search Language

> **TODO:** Decide whether to include a small representative example here or link to the complete [search-language documentation](https://github.com/darrenldl/docfd/wiki/Content-searching).
