# Global Development Memory

## Core Workflow

### Spec-First Approach (Critical)

- **Non-negotiable**: All work starts with detailed spec in `specs/` directory
- **Common Violation**: Jumping to implementation without spec review leads to architectural mistakes
- **Consequence**: Process violations compound - missing specs lead to poor branch naming, missing documentation
- **Branch naming**: Branch name must match spec file name exactly
- **Session logging**: Document in `.claude-code-sessions/[branch-name].md` incrementally

### Session Logging (Critical Understanding)

- **Purpose**: Real-time decision journal capturing reasoning as work progresses, NOT final documentation
- **Common misunderstanding**: Treating as project documentation written at beginning/end vs. live thought process
- **Correct approach**: Update after each significant decision/action, capturing actual reasoning in the moment
- **Critical insight**: Session logs document WHY decisions were made when they were made, not just WHAT was done
- **Anti-pattern**: Batch updating at end of session - this loses the decision-making context that makes logs valuable

## Essential Rules

### Git Practices

- **Atomic commits required**: Each logical step committed separately (spec → investigation → implementation → fixes)
- **Critical for evaluation systems**: Atomic commits enable visibility into decision-making process for agentic evaluation
- **Commit trigger rule**: Any conceptual block or significant decision requires session log update + immediate commit
- **Why this matters**: Decision-making process must be traceable through git history, not just final outcomes

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
