---
maxwidth: "80ch"
title: Docfd - Design Context
---

[**Back to Docfd**](index.md)

## Initial Motivation

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
        - But then the number of regexes grows quickly with the number of words, especially if we allow reordering of words and desire typo tolerance.
- **[fzf](https://github.com/junegunn/fzf), [skim](https://github.com/skim-rs/skim), [television](https://github.com/alexpasmantier/television)**
    - Great for fuzzy finding within a single line
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
- **[Elasticsearch](https://www.elastic.co/elasticsearch/), [Lucene](https://lucene.apache.org/), [meilisearch](https://github.com/meilisearch/meilisearch), etc**
    - Nothing beats the search performance of actual search engines.
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
    - I personally believe these could be the gold standard for information retrieval, but they are still very computationally heavy,
      and there are a lot of fine-tuning needed in terms of chunking, etc, to yield optimal results. And even after
      all that, we still face the issue of hallucinations.
    - Arguments of the energy efficiency aside, I simply don't want to build my core workflow around needing very powerful hardware.
      Even CPU optimised LLMs run quite sluggishly on my laptop last I tried.
    - If one day very powerful hardware is extremely prevalent and cheap,
      where computational inefficiency is simply strong-armed into irrelevance,
      then sure, local LLM why not. Or alternatively LLM becomes so efficient
      that we can use it on the most modest of machines while offering good results, that would suffice as well.
    - But I am not confident we are close to that stage yet, so there are still very real needs for the traditional
      approaches to searching, especially since LLMs still hallucinate wildly, and even if not,
      cannot give guarantee for its exhaustiveness. For instance, if grep does not give any results
      for a search word, then I am confident the word does not exist in the documents, but I cannot say the same
      for LLMs.

## Design Decisions

### Primary Use Case and Main Technical Requirements

The main use case Docfd targets is a user navigating through an unstructured
folder of human text documents with a mix of text files and PDFs at
a scale more commonly seen at personal storage or small office level, e.g. a few hundred files to scan through at a time.

To make the requirements concrete, CC-MAIN-2021-31-PDF-UNTRUNCATED 0000.zip
from [PDF Corpora](https://github.com/pdf-association/pdf-corpora) was used as
benchmark on a mid-tier level laptop with the following specification:

| Component | Details |
| --- | --- |
| CPU | 13th Gen Intel(R) Core(TM) i5-1334U (4+8) @ 4.60 GHz |
| RAM | 16GB |
| Disk | SAMSUNG MZVL8512HELU-00BTW |

0000.zip consists of 1k PDF documents with an average file size of 1.3 MiB average.

After extensive "dogfooding", I arrived at the following final set of technical requirements:

| Description | Constraint |
| --- | --- |
| Docfd needs to index fresh files relatively quickly | <5 minutes |
| Docfd needs to finish processing files already indexed significantly faster than unindexed files, as otherwise what's the point | <10 seconds |
| Docfd needs to not compete for RAM too heavily as it's mainly run on desktop environment rather than dedicated server | <200MB upon start, before any user action |

### Why a Custom Search Engine

I opted to implement a custom search engine instead of using an off-the-shelf
engine for a mix of reasons:

- I wanted to stay in OCaml, and there wasn't an off-the-shelf engine
  available in OCaml.
- The core search functionality I wanted (proximity search + DFS) is fairly
  straightforward to implement correctly, and I only need the
  implementation to be "good enough" for the type of workload I'm expecting
  myself (<1k files to search through at a time).
- I want to have precise control over fundamental components, including the
  search behaviour, result ranking heuristics, and the design of the query
  language. A custom search engine is a simplest way to ensure
  this.
- And lastly, I want side projects to give a good learning or
  exploratory experience, and I thought it would be nice to get a concrete
  feel of the core search and ranking problem.

Suffice to say my choices would be different had this been an actual product
that targets more general and larger use cases,
as it is very difficult to beat the optimisation of existing search engines.
And even if a custom query language is needed, a translation layer on top of
the search engine's native query language would likely
cover all the practical cases.

### Supporting Ad Hoc Workflow

Docfd only processes the current directory or the specified directories and
files upon startup. Hashing is used to check if file has been previously
indexed. This means there is no central storage requirement, and no background
indexing.

In principle, this causes slower start-up time in the general case
compared to programs with background indexing. But since the set
of documents of interest is usually small (<100 documents), the
start-up is often instantaneous.

### Resource Constraints

There were some concessions made to avoid disrupting other desktop
applications. One particularly noticeable choice is giving up storage of
heavy indices in memory and instead rely on disk I/O via SQLite.

The tradeoff is that at larger scale (say a few thousand documents, depending
on the sizes), Docfd will noticeably struggle where results will take seconds
instead of less than a second to show up.

There are naturally middleground tactics that can be adopted, e.g. holding
indices into a caching memory layer, and optionally pre-warming the layer with
heuristics, but this was not further explored as basic design already suffices
for the scale targetted.

> **TODO:** Distil the constraints established above into a short list and link each constraint to the corresponding engineering decision.
