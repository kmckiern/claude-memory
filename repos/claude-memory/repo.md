# claude-memory Repository Memory

## Project Overview

- **Purpose**: Central memory system for Claude Code development patterns and project-specific context
- **Architecture**: Source files + automation to generate combined CLAUDE.md files with priority-weighted information
- **Key Features**: Global patterns, project templates, automated memory synchronization

## Critical Insights

### Non-Obvious Patterns

- **Source-only editing**: Never edit generated CLAUDE.md files directly - they're completely regenerated from source files
- **Priority-weighted architecture**: Information structure reflects significance, not chronology
- **Holistic integration**: Changes consider broader context, often requiring entire file rework rather than incremental updates

### Domain Complexity

- **Memory Management Philosophy**: Distinguish trivial details from critical insights, weight by importance, maintain brevity while integrating holistically
- **Template-driven generation**: Consistent structure across projects through template inheritance
- **Automated synchronization**: Git hooks trigger regeneration to keep memory files current

### Development Challenges

- **Information overload prevention**: Constant tension between completeness and brevity
- **Significance assessment**: Determining what deserves memory vs. what can be discovered
- **Context integration**: Balancing project-specific details with global patterns

## Performance & Debugging

### Critical Performance Insights

- **Memory structure optimization**: Most significant information prioritized first to reduce cognitive load
- **Automated generation efficiency**: Reduces manual memory maintenance overhead through template-driven approach
- **Information density**: Balancing completeness with brevity to prevent cognitive overload

### Debugging Complexity

- **Template inconsistencies**: Source files must follow template structure exactly or generation fails
- **Hook dependencies**: Pre-commit hook failures require manual generation debugging
- **Context integration challenges**: Changes often require holistic file rework rather than simple additions

## Recent Context

### Key Learnings

- Established priority-based memory processing principles as core philosophy
- Discovered that chronological organization creates cognitive overhead vs. significance-based structure
- Template adherence critical for consistent cross-project memory management

### Evolution & Trade-offs

- **Trade-off**: Automated generation vs. manual control - chose automation for consistency
- **Evolution**: From chronological to significance-based information architecture
- **Breaking change**: Template structure now enforced, requiring all repos to conform
