# code-evals Repository Memory

## Project Overview

- **Purpose**: CLI tool that evaluates code changes against specifications using Mandoline AI
- **Architecture**: Linear pipeline with concurrent evaluation: config → spec → git analysis → parallel evaluation → output
- **Key Features**: Concurrent evaluation, merge commit handling, spec-based assessment

## Critical Insights

### Non-Obvious Patterns

- **Spec exclusion from diffs**: Specifications themselves must be excluded from evaluation diffs to prevent circular evaluation
- **Merge commit detection**: GitHub PR workflow creates temporary merge commits not visible locally, requiring special head/base selection logic
- **Concurrent evaluation architecture**: `asyncio.gather()` provides dramatic speedup through simultaneous API requests vs. sequential evaluation

### Domain Complexity

- **Specification adherence validation**: Evaluates whether code changes match written specifications using AI analysis rather than mechanical rule checking
- **Natural language evaluation**: Uses AI to assess code against human-written requirements instead of relying solely on automated syntax/type checking
- **Self-referential evaluation paradox**: Features that change evaluation behavior create circular evaluation issues during development
- **Git commit history complexity**: CI sees different commit history than local development, requiring robust merge commit detection
- **Evaluation context boundaries**: Related code discovery gap can miss relevant context not directly edited

### Development Challenges

- **Ship of Theseus problem**: Modifying evaluation while being evaluated requires accepting inconsistency during transitions
- **Related code discovery gap**: Static analysis needed to find relevant code not directly modified
- **AsyncMandoline integration**: Context manager protocol differences require direct instantiation patterns

## Performance & Debugging

### Critical Performance Insights

- **Concurrent evaluation bottleneck**: Sequential API calls were primary bottleneck, solved with `asyncio.gather()` providing dramatic speedup
- **Resource efficiency optimization**: Better API utilization through simultaneous requests vs. sequential processing
- **Git analysis optimization**: Atomic operations in git analysis prevent incomplete state issues

### Debugging Complexity

- **Merge commit detection challenges**: GitHub PR workflow creates temporary merge commits invisible locally, requiring verbose mode to debug commit selection
- **Self-referential evaluation debugging**: Features that change evaluation behavior create circular issues during development
- **AsyncMandoline context debugging**: Standard async patterns don't work - requires direct instantiation debugging
- **Empty diffs in CI**: Merge commit detection logic often fails, requiring git analysis verification

## Recent Context

### Key Learnings

- **Merge commit bug discovery**: CI merge commit evaluation causing "No changes detected" revealed fundamental git analysis complexity
- **Performance breakthrough**: AsyncMandoline 0.5.0 integration provided dramatic concurrent evaluation speedup
- **Code duplication prevention**: Reusing `spec_ops.discover_spec_path()` avoided custom helper duplication
- **Related code discovery gap**: Evaluation context misses related code not directly edited

### Evolution & Trade-offs

- **Trade-off**: Self-referential evaluation consistency vs. development velocity - accepted inconsistency during transitions
- **Evolution**: From sequential to concurrent evaluation architecture for performance
- **Breaking change**: v0.5.0 requires mandoline>=0.5.0, async patterns throughout
- **Philosophy**: "Ship of Theseus" approach to modifying evaluation while being evaluated
