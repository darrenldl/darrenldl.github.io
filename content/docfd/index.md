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

Docfd was born out of my personal frustrations with
existing search tools in the context of human text search.

This is not to say I think the tools are not well implemented or
not well designed, this is just me saying I don't fit into the usage patterns
that these tools are designed for.
In fact, given the specific intended usage patterns and constraints, I think
most of these tools are likely implemented as well as one could.

So the following are not necessarily criticisms, but more of
why they didn't fit my (perhaps admittedly niche) criteria of
being able to run locally on a not very powerful machine:

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
    - These are optimised for central storage of documents, where the storage
      is not necessarily designed to be accessible to external programs (which
      is fair enough, cause you want storage consistency).
    - I still want to use the file system as the main organisation mechanism to avoid vendor lock-in,
      and to allow usage of other tools. In principle I can use both the central storage and file system, but then I am
      using twice the storage space adn also need to keep things in sync somehow.
    - That said, if I ever need to deploy for a use case for multi-user or concurrent access, then software with DB backed storage
      is still likely my top pick. But here I am just looking to use locally on a single machine myself.
- Recoll, Baloo
    - These (from my point of view) expect either stable main collection of folders to scan from, or scan the whole home directory barring
      ones like `Downloads`. They also utilise background daemon to index periodically.
    - I usually jump to a specific project folder to search than to search over the whole home directory, and I want
      the index to be fully up-to-date with respect to the underlying files.
    - I don't want to have to wait for a background update to occur, and while I can trigger the reindexing manually,
      as I only want to reindex the specific folder I am looking at right now, but the entire home.
    - I don't want the periodic CPU spike from reindexing, especially for files I am not interested in (similar to the above point).
- ElasticSearch, Lucene, etc
    - Nothing beats the search quality of actual search engines, especially taking semantic search into account.
      But the setup and running cost of these are not trivial.
    - Which are all fair enough, cause ultimately you need in-memory indices for hot data to serve at the scale needed,
      which takes time to build and they occupy memory space etc.
    - But I don't want anything long running. I just want to jump into a
      folder, do my search, and be done. I don't want to have to wait
      for more than a few seconds just to do a quick search, so starting up a fresh
      search engine instance per session is a no-go.
    - And I don't want the tool to disrupt other deskop applications I am running, so the typical resource usage requirements
      of search engines also render them not viable for me.
    - But if I am deploying onto a dedicated hardware/host, then these remain the natural first choices obviously.
- Local LLM
    - I have found these to be quite quick to load, and a lot of tooling exists to make using them very easy.
      But they are still very computationally heavy.
    - Arguments of the energy efficiency aside, I simply don't want to build my core workflow around needing very powerful hardware.
      Even CPU optimised LLMs run quite sluggishly on my laptop last I tried.
    - If one day extremely powerful hardware is extremely prevalent and cheap,
      where computational inefficiency is simply strong-armed into irrelevance,
      then sure, local LLM why not. Or alternatively LLM becomes so efficient
      that we can use it on the most modest of machines, that would suffice as well.
    - But I am not confident we are close to that age yet, so there are still merits to the traditional
      approaches to searching, especially since LLMs still hallucinate wildly, and even if not,
      cannot give guarantee for its exhaustiveness.
