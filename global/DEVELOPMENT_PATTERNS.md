# Global Development Memory

## Core Development Framework

### Spec-First Approach (Critical)
- **Non-negotiable**: All work starts with detailed spec in `specs/` directory
- **CI Integration**: Spec must exist and be clear or code merging will be blocked
- **Transparency**: Write spec first to avoid "cheating" and be transparent about intentions
- **Iterative Process**: Most time spent collaboratively iterating on specs for maximum clarity
- **Branch Naming**: Check out branch with same name as spec file

### Session Documentation Standards
- **Real-time logging**: Document each interactive session in `.claude-code-sessions/[branch-name].md` incrementally
- **Conversation style**: Logs should reflect actual back-and-forth chat, not post-hoc summaries
- **Transparency**: Capture actual conversation flow, including corrections and learning moments

## Communication Patterns

### User Teaching Style
- **Direct corrections**: Immediate, specific guidance on technical issues
- **Process reinforcement**: Consistently emphasizes spec-first approach when jumping to implementation
- **Quality expectations**: High standards with specific style and depth requirements
- **Practical guidance**: Shows specific commands and patterns

### Effective Collaboration Dynamics
- **TodoWrite usage**: Systematic task tracking appreciated for complex work
- **Immediate testing**: Always verify implementations work
- **Following patterns**: Mirror existing code style consistently
- **Building on feedback**: Each suggestion improves the deliverable iteratively

## Git Practices

### Commit Standards
- **User permission required**: Never commit unless explicitly requested
- **Atomic commits**: All changes in single commit with proper branch naming
- **Signature requirement**: Always include Claude Code signature:
  ```
  🤖 Generated with [Claude Code](https://claude.ai/code)
  
  Co-Authored-By: Claude <noreply@anthropic.com>
  ```

### Branch Management
- **Naming convention**: Branch name must match spec file name exactly
- **Work isolation**: Each feature/fix gets its own branch with corresponding spec

## Code Standards

### General Principles
- **No comments**: Unless explicitly requested
- **Pattern following**: Check neighboring files first, follow existing conventions religiously
- **Backward compatibility**: Maintain unless explicitly told to remove constraints
- **Quality focus**: High expectations for production-ready code

### Testing Standards
- **Immediate verification**: Test everything immediately to verify implementations work
- **Comprehensive coverage**: Expect tests that mirror existing style and depth
- **Pattern consistency**: Follow existing test patterns religiously

## Python Environment Patterns

### Virtual Environment Setup
- **Standard location**: Use `.venv` in root directory
- **Common issue**: "pip is disabled in base environment" → deactivate conda first
- **Activation pattern**: `conda deactivate && source .venv/bin/activate`
- **Dependencies**: Install with `pip install -e .[dev]` or specific packages

### Async Testing
- **Requirements**: `pytest-asyncio` and proper mocking at low levels
- **Challenge**: Async test mocking requires understanding call chains
- **Pattern**: Mock at the lowest HTTP/network level for reliable testing

## Process Learnings

### Environment Setup
- Environment setup patterns learned through trial and error
- Tutorial environments should test actual user experience, not dev environment
- Performance improvements must be verified through actual testing

### Collaboration Quality
- User provides direct, practical guidance
- Iterative refinement improves deliverables
- Documentation serves future development needs
- Transparency in process and learning is valued