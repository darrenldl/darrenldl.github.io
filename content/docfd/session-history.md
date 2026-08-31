---
maxwidth: "80ch"
title: Docfd - Session History, Snapshots, and Replay
---

[**Back to Docfd**](index.md)

## Editing/viewing command history

> **TODO:** Add an up-to-date walkthrough of undo/redo, editing command history, and saving or replaying the resulting commands as a Docfd script.

## Commands and Immutable State

> **TODO:** Describe the command representation, session state, committed versus preview commands, and how snapshots connect commands to states.

## Checkpointing and Pruning

> **TODO:** Explain why retaining every snapshot state consumed too much memory, which states are retained, and when compaction occurs.

## Reconstruction

> **TODO:** Explain how a missing snapshot is reconstructed from the nearest preceding checkpoint by replaying commands.

## Undo/Redo Semantics

> **TODO:** Cover history truncation after editing an older version, input-field synchronization, worker quiescence, and the blocking reconstruction overlay.

## Trade-offs

> **TODO:** Discuss the memory-versus-reconstruction-time trade-off and whether timing command replay could support better checkpoint heuristics.
