# Global Development Memory

## Core Workflow

### Spec-First Approach (Critical)

- **Non-negotiable**: All work starts with detailed spec in `specs/` directory
- **Common Violation**: Jumping to implementation without spec review leads to architectural mistakes
- **Consequence**: Process violations compound - missing specs lead to poor branch naming, missing documentation
- **Branch naming**: Branch name must match spec file name exactly
- **Session logging**: Document in `.claude-code-sessions/[branch-name].md` incrementally

## Essential Rules

### Git Practices

- **Atomic commits required**: Each logical step committed separately (spec → investigation → implementation → fixes)
- **Critical for evaluation systems**: Atomic commits enable visibility into decision-making process for agentic evaluation

### Code Standards

- **Good comments only**: Add comments that explain why, not what; avoid restating obvious code behavior
- **Follow existing patterns** religiously - check neighboring files first
- **Anti-duplication**: Always check for existing functionality before implementing new helpers
- **Test immediately** to verify implementations work

### Communication Protocols

- **Reduce cognitive overhead**: Focus user attention on substantive decisions, not low-stakes choices
- **Be decisive**: Make reasoned decisions on small choices rather than offering options
- **Voice transcription awareness**: Since input is often dictated, transcription errors occur; infer from context and ask for clarification when unsure
- **Clarify unclear terms**: Proactively ask for clarification, especially with voice transcription

## Environment Setup

### Python Gotchas

- **Virtual environment**: Use `.venv` in root directory
- **Common issue**: "pip is disabled in base environment" → `conda deactivate && source .venv/bin/activate`
- **Async testing**: Requires `pytest-asyncio` and HTTP-level mocking
