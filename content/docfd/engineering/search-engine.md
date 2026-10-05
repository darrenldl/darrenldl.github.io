---
maxwidth: "100ch"
title: Docfd - Search Engine
---

[**Back to Engineering Page**](index.md)

## Introduction

- The dictionary is first searched through once to find the
  matches for the first word in the search phrase.
- DFS through the inverted index is then used for the remaining words,
  where the word is searched within a specified distance from the
  previous word. In other words, the path in this DFS is the
  list/sequence of words in the document matching the search phrase.
- Fuzzy matching is handled by using the Levenshtein distance as part of
  the matching criteria for each word. An automaton is computed for
  each word of the search phrase for optimised repeated matching.

## Search Procedure

User input in the search field are tokenized
in the same way as document content (see [here](indexing.md#tokenization)).
A search phrase is then a list of said tokens.

Search procedure is a DFS through the document index,
where the search range for a word is fixed
to a configured range surrounding the previous word (when applicable).

A token in the index matches a token in the search phrase if they fall
into one of the following cases:
- They are a case-insensitive exact match
- They are a case-insensitive substring match (token in search phrase being the substring)
- They are within the configured case-insensitive edit distance threshold

Search results are then ranked using a heuristic.

### First-word Candidate Generation and Pruning

> **TODO:** Explain global first-word candidate generation, document pruning, search scopes, and how the search is divided into parallel jobs.

### Depth-first Search

### Ranking

> **TODO:** Explain the result-ranking heuristic and the interaction between content relevance, path ordering, and path fuzzy ranking.
