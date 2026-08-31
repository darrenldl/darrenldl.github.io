---
maxwidth: "80ch"
title: Docfd - Responsive Asynchronous UI
---

[**Back to Docfd**](index.md)

## Observable Behaviour

Search is asynchronous, specifically:
- Editing of search field is not blocked by search progress
- Updating/clearing the search field cancels the current search
  and starts a new search immediately

## Problem and Constraints

> **TODO:** Describe why search and filtering cannot run on the UI domain and why Lwd updates must remain on the main domain.

## Worker and Manager Design

> **TODO:** Describe the UI requester, lock-protected request cells, worker domain, manager fiber, egress acknowledgement, and immutable snapshot publication.

## Cancellation and Debouncing

> **TODO:** Explain stop signals, request overwriting/coalescing, the workload-centric debounce window, and the deliberate distinction between cancellation and interruption.

## Blocking Versus Non-blocking Feedback

> **TODO:** Explain why asynchronous search/filter progress belongs in the status line, while synchronous snapshot reconstruction and document reload use a noninteractive overlay.

## Trade-offs and Alternatives

> **TODO:** Discuss the synchronization complexity caused by Lwd not being thread-safe, and compare the current design with a single-domain implementation or a fully message-driven state owner.
