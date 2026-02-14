---
maxwidth: 60%
---

[**Back to Home**](..)

# [Docfd](https://github.com/darrenldl/docfd) (Page is WIP)

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
being able to run locally on a not very powerful machine
while providing "good" search results:

- **grep, [ripgrep](https://github.com/BurntSushi/ripgrep), etc**
    - Great if I am searching for a single word
    - Bad if I want to search for a phrase across potentially more than 1 line
        - Technically there is a way to encode the problem into a regex,
          e.g. "hello world" becomes `hello.*world`, `hello.*\n.*world`, `hello.*\n.*\n.*world`, and so on, up to a limit.
        - But then the number of regexes grows quickly with the number of words, especially if we allow reordering of words
- **[fzf](https://github.com/junegunn/fzf), [skim](https://github.com/skim-rs/skim), [television](https://github.com/alexpasmantier/television)**
    - Great for single line
    - There are workarounds for multiline by replacing the new line character then using the `--read0` flag,
      e.g. [vgc](https://github.com/xkcd386at/scripts/blob/master/vgc),
      but this does not allow searching across blank lines
    - Technically not a problem if you are only interested in searching
      within paragraphs, but this assumes text is always well formed,
      which is not necessarily the case with text extracted from PDFs.
- **[Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx), [Papra](https://github.com/papra-hq/papra), [sist2](https://github.com/sist2app/sist2)**
    - These are optimised for central storage of documents, where the storage
      is not necessarily designed to be accessible to external programs (which
      is fair enough, cause you want storage consistency).
    - But I still want to use the file system as the main organisation mechanism to avoid vendor lock-in,
      and to allow usage of other tools. In principle I can use both the central storage and file system, but then I am
      using twice the storage space adn also need to keep things in sync somehow.
    - That said, if I ever need to deploy for a use case for multi-user or concurrent access, then software with DB backed storage
      is still likely my top pick. But here I am just looking to use locally on a single machine myself.
- **[Recoll](https://www.recoll.org/), [Baloo](https://invent.kde.org/frameworks/baloo)**
    - These (from my point of view) expect either a stable main collection of folders to scan from, or scan the whole home directory barring
      ones like `Downloads`. They also utilise background daemon to index periodically.
    - However, I usually jump to a specific project folder to search rather than the whole home directory, and I want
      the index to be fully up-to-date with respect to the underlying files.
      I don't want to wait for a background update to occur.
    - While I can trigger the reindexing manually, I need to update the
      settings in order to just reindex the specific folder I am in.
    - On a similar note, I also don't want the periodic CPU and/or
      memory spike from reindexing of files I am not looking at.
- **[Elasticsearch](https://www.elastic.co/elasticsearch), [Lucene](https://lucene.apache.org/), [meilisearch](https://github.com/meilisearch/meilisearch), etc**
    - Nothing beats the search quality of actual search engines, especially taking semantic search into account.
      But the setup and running cost of these are not trivial.
    - Which are all fair enough, cause ultimately you need in-memory indices for hot data to serve at the scale needed,
      which takes time to build and they occupy memory space etc.
    - But I don't want anything long running. I just want to jump into
      a folder, do my search, and be done. I don't want to wait for
      more than a few seconds just to do a quick search, so starting
      up a fresh search engine instance per session is a no-go.
    - I also don't want the tool to disrupt other deskop applications I am running, so the typical resource usage requirements
      of search engines also render them not viable for me.
    - But if I am deploying onto a dedicated hardware/host, then these remain the natural first choices obviously.
- **Local LLMs, whether for chat or semantic search**
    - I have found these to be quite quick to get started. But they are still very computationally heavy.
    - Arguments of the energy efficiency aside, I simply don't want to build my core workflow around needing very powerful hardware.
      Even CPU optimised LLMs run quite sluggishly on my laptop last I tried.
    - If one day very powerful hardware is extremely prevalent and cheap,
      where computational inefficiency is simply strong-armed into irrelevance,
      then sure, local LLM why not. Or alternatively LLM becomes so efficient
      that we can use it on the most modest of machines while offering good results, that would suffice as well.
    - But I am not confident we are close to that stage yet, so there are still merits to the traditional
      approaches to searching, especially since LLMs still hallucinate wildly, and even if not,
      cannot give guarantee for its exhaustiveness. For instance, if grep does not give any results
      for a search word, then I am confident the word does not exist in the documents, but I cannot say the same
      for LLMs.

### How does Docfd address my complaints?
