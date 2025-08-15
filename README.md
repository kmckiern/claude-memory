# Claude Memory System

Central repository for Claude Code development patterns and project-specific memory.

## Structure

```
claude-memory/
├── global/                     # Universal development patterns
│   └── DEVELOPMENT_PATTERNS.md
├── repos/                      # Project-specific memory
│   ├── code-evals/
│   │   ├── repo.md             # Source content
│   │   └── CLAUDE.md           # Generated: repo.md + global patterns
│   └── mandoline-python/
│       ├── repo.md
│       └── CLAUDE.md
├── templates/                  # Templates for new projects
├── meta/                       # Project documentation
└── tools/                      # Automation scripts
    └── generate-claude-md.py
```

## Usage

### For Other Repositories

Create a symlink to use this memory system in your project:

```bash
ln -s ../claude-memory/repos/[your-repo]/CLAUDE.md ./CLAUDE.md
```

### Adding New Projects

1. Create `repos/[project-name]/repo.md` using the template
2. CLAUDE.md will be auto-generated when you commit

### Updating Memory

1. Edit source files: `global/DEVELOPMENT_PATTERNS.md` or `repos/*/repo.md`
2. Commit changes - pre-commit hook automatically updates CLAUDE.md files

## Automation

Pre-commit hooks ensure CLAUDE.md files stay in sync:
- Detects changes to source memory files
- Regenerates combined CLAUDE.md files
- Adds updated files to commit automatically
