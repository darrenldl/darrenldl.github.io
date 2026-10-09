---
maxwidth: "100ch"
title: Docfd - Search Language
---

[**Back to User Guide**](index.md)

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
