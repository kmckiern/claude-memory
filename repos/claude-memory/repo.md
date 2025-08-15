# claude-memory Repository Memory

## Project Overview
- **Purpose**: Central memory system for Claude Code development patterns and project-specific context
- **Architecture**: Source files + automation to generate combined CLAUDE.md files

## Technical Environment
- **Build**: Python 3 scripts for automation
- **Testing**: Manual verification of generated files
- **Pre-commit**: Auto-generates CLAUDE.md files when source content changes

## Key Components
- **Global patterns**: Universal development workflow and rules
- **Project templates**: Reusable formats for new repositories
- **Automation**: Pre-commit hooks ensure files stay in sync

## Recent Changes
- Created structured memory system with global + repo-specific content
- Added pre-commit automation for CLAUDE.md generation
- Trimmed content to focus on essential workflow information

## Troubleshooting
- **Hook not running**: Check `.git/hooks/pre-commit` is executable
- **Generation fails**: Run `python3 tools/generate-claude-md.py` manually to debug