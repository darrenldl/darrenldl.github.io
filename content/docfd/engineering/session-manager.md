---
maxwidth: "100ch"
title: Docfd - Session Manager
---

[**Back to Main Page**](index.md)

Session Manager centralizes the management of session history/snapshots and
handles the lifecycle of long-running operations (namely searching and
filtering) to allow for a responsive asynchronous UI.

![Figure: Interaction between UI and Session Manager Module](docfd-session-manager.svg)

## Asynchronous UI

Search is asynchronous, specifically:
- Editing of search field is not blocked by search progress
- Updating/clearing the search field cancels the current search
  and starts a new search immediately

## Problem and Constraints

> **TODO:** Describe why search and filtering cannot run on the UI domain and why Lwd updates must remain on the main domain.

## Session Manager Design

> **TODO:** Describe the UI requester, lock-protected request cells, worker domain, manager fiber, egress acknowledgement, and immutable snapshot publication.

## Cancellation and Debouncing

> **TODO:** Explain stop signals, request overwriting/coalescing, the workload-centric debounce window, and the deliberate distinction between cancellation and interruption.

## Blocking Versus Non-blocking Feedback

> **TODO:** Explain why asynchronous search/filter progress belongs in the status line, while synchronous snapshot reconstruction and document reload use a noninteractive overlay.

## Session History

### Commands and Immutable State

> **TODO:** Describe the command representation, session state, committed versus preview commands, and how snapshots connect commands to states.

### Undo/Redo Semantics

> **TODO:** Cover history truncation after editing an older version, input-field synchronization, worker quiescence, and the blocking reconstruction overlay.

### Checkpointing and Pruning

> **TODO:** Explain why retaining every snapshot state consumed too much memory, which states are retained, and when compaction occurs.

## Reconstruction

> **TODO:** Explain how a missing snapshot is reconstructed from the nearest preceding checkpoint by replaying commands.

