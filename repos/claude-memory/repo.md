# claude-memory Repository Memory

## Project Overview
- **Purpose**: Central memory system for Claude Code development patterns and project-specific context
- **Architecture**: Source files + automation to generate combined CLAUDE.md files
- **Key Features**: Global patterns, project templates, automated memory synchronization

## Technical Environment
- **Build Tool**: Python 3 scripts (no special requirements)
- **Dependencies**: Python 3 standard library only
- **Testing**: Manual verification of generated files
- **Code Quality**: Follow existing Python conventions

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

## Troubleshooting Guide

### Common Errors
- **Hook not running**: Check `.git/hooks/pre-commit` is executable
- **Generation fails**: Run `python3 tools/generate-claude-md.py` manually to debug
- **Template inconsistencies**: Verify source files follow template structure

### Debug Strategies
- Manual script execution reveals generation errors
- Check file permissions on hook scripts
- Verify template integrity before bulk regeneration