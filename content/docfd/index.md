---
maxwidth: 60%
---

[**Back to Home**](..)

**WIP**

# [Docfd](https://github.com/darrenldl/docfd)

## Introduction

Docfd is in essence a TUI program that allows you to fuzzy search for
a phrase across multiple lines, across text files, PDFs, DOCX, etc.

While the README does a reasonable job briefing over what Docfd is,
I still want to talk about Docfd in greater details.
In part to document the engineering effort that went into
Docfd, and in part as a portfolio building exercise.

### Motivation

Docfd is born out of my personal frustrations with
existing search tools:
- grep, ripgrep, etc
    - Great if I am searching for a single word
    - Bad if I want to search for a phrase across potentially more than 1 line
        - Technically there is a way to encode the problem into a regex,
          e.g. "hello world" becomes `hello.*world`, `hello.*\n.*world`, `hello.*\n.*\n.*world`, and so on, up to a limit.
        - But then the number of regexes grows quickly with the number of words, especialyl if we allow reordering of words
- fzf
    - Great for single line
    - There are workarounds for multiline by replacing the new line character then using the `--read0` flag,
      e.g. [vgc](https://github.com/xkcd386at/scripts/blob/master/vgc),
      but this does not allow searching across blank lines
    - Technically not a problem if you are only interested in searching
      within paragraphs, but this assumes text is always well formed
- Paperless-NGX, Papra
- ElasticSearch, Lucene
