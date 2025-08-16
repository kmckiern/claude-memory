# claude-memory Repository Memory

## Project Overview

- **Purpose**: Central memory system for Claude Code development patterns and project-specific context
- **Architecture**: Source files + automation to generate combined CLAUDE.md files
- **Key Features**: Global patterns, project templates, automated memory synchronization

## Technical Environment

### Build System

- **Build Tool**: Python 3 scripts (no special requirements)
- **Package Management**: Standard Python
- **Installation**: Direct execution of generation scripts

### Development Environment

- **Dependencies**: Python 3 standard library only
- **Common Issues**: Verify template integrity before bulk regeneration

### Testing Framework

- **Test Runner**: Manual verification of generated files
- **Special Requirements**: Verify CLAUDE.md generation accuracy
- **Coverage Expectations**: All source changes must trigger regeneration

### Code Quality Tools

- **Linting**: Follow existing Python conventions
- **Type Checking**: Not required for this project
- **Formatting**: Standard Python formatting

## Project-Specific Patterns

### Memory Management Philosophy (CRITICAL)

**When processing information for memory incorporation:**

- **Prioritize by significance** - distinguish trivial details from critical insights
- **Weight by importance** - emphasize key patterns, escalate essential learnings
- **Maintain brevity** - avoid bloat, focus on actionable information
- **Integrate holistically** - consider broader context, rework entire files when needed
- **Structure reflects priority** - most important information comes first

### Code Conventions

- Edit source files in `repos/` and `global/` directories only
- Never edit generated CLAUDE.md files directly
- Follow template structures for consistency

### Common Workflows

- **Memory updates**: Edit source files, commit triggers auto-generation
- **Manual generation**: Run `python3 tools/generate-claude-md.py` when hooks fail
- **Template updates**: Modify templates then regenerate all files

## Recent Context

### Active Branches

- `session-insights`: Current working branch
- Focus on memory management improvements

### Recent Issues & Solutions

- Established priority-based memory processing principles
- Restructured memory files to emphasize significance over chronology
- Integrated memory philosophy into development workflow

## Domain Knowledge

### Business Logic

- **Core Concept**: Centralized memory management for development patterns across projects
- **Process**: Source files → automation → combined CLAUDE.md files
- **Key Algorithm**: Template-based generation with priority-weighted information

### Performance Considerations

- **Optimization**: Memory files structured to prioritize most significant information first
- **Efficiency**: Automated generation reduces manual memory maintenance overhead

## External Dependencies

### Key Libraries

- **Python 3 standard library**: File operations, text processing
- **Git hooks**: Automated regeneration on commits

### Services & APIs

- **Local file system**: Source and generated file storage
- **Git integration**: Pre-commit hook triggers

## Troubleshooting Guide

### Common Errors

- **Hook not running**: Check `.git/hooks/pre-commit` is executable
- **Generation fails**: Run `python3 tools/generate-claude-md.py` manually to debug
- **Template inconsistencies**: Verify source files follow template structure

### Debug Strategies

- Manual script execution reveals generation errors
- Check file permissions on hook scripts
- Verify template integrity before bulk regeneration
