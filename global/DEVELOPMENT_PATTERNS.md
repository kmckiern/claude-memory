# Global Development Memory

## Core Workflow

### Spec-First Approach (Critical)
- **Non-negotiable**: All work starts with detailed spec in `specs/` directory
- **Branch naming**: Branch name must match spec file name exactly
- **Session logging**: Document in `.claude-code-sessions/[branch-name].md` incrementally

## Essential Rules

### Git Practices
- **Never commit** unless explicitly requested
- **Always include** Claude Code signature:
  ```
  🤖 Generated with [Claude Code](https://claude.ai/code)
  
  Co-Authored-By: Claude <noreply@anthropic.com>
  ```

### Code Standards
- **No comments** unless explicitly requested
- **Follow existing patterns** religiously - check neighboring files first
- **Test immediately** to verify implementations work

## Environment Setup

### Python Gotchas
- **Virtual environment**: Use `.venv` in root directory
- **Common issue**: "pip is disabled in base environment" → `conda deactivate && source .venv/bin/activate`
- **Async testing**: Requires `pytest-asyncio` and HTTP-level mocking