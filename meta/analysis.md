# Analysis of CLAUDE.md Files and Session Logs

## Overview
Analysis of development practices and project context from two repositories: `code-evals` and `mandoline-python`, based on their CLAUDE.md files and `.claude-code-sessions/` logs.

## Development Framework

### Spec-First Approach (Critical)
- **Non-negotiable**: All work starts with detailed spec in `specs/` directory
- **CI Integration**: Spec must exist and be clear or code merging will be blocked
- **Transparency**: Write spec first to avoid "cheating" and be transparent about intentions
- **Iterative Process**: Most time spent collaboratively iterating on specs for maximum clarity
- **Branch Naming**: Check out branch with same name as spec file

### Session Documentation
- **Real-time logging**: Document each interactive session in `.claude-code-sessions/[branch-name].md` incrementally
- **Conversation style**: Logs should reflect actual back-and-forth chat, not post-hoc summaries
- **Transparency**: Capture actual conversation flow, including corrections and learning moments

## Communication & Workflow Patterns

### User Teaching Style
- **Direct corrections**: "use the .venv in the root of the repo"
- **Process reinforcement**: Consistently emphasizes spec-first approach when jumping to implementation
- **Quality expectations**: "make sure to mirror the other tests in style and depth"
- **Practical guidance**: Shows specific commands and patterns

### Effective Collaboration Dynamics
- **TodoWrite usage**: Systematic task tracking appreciated for complex work
- **Immediate testing**: Always verify implementations work
- **Following patterns**: Mirror existing code style consistently
- **Building on feedback**: Each suggestion improves the deliverable iteratively

## Technical Environment

### Python Setup
- **Virtual environment**: Use `.venv` in root directory
- **Common issue**: "pip is disabled in base environment" → deactivate conda first
- **Activation pattern**: `conda deactivate && source .venv/bin/activate`
- **Dependencies**: Install with `pip install -e .[dev]` or specific packages like `pytest-asyncio`

### Testing Standards
- **Immediate verification**: Test everything immediately to verify implementations work
- **Comprehensive coverage**: Expect tests that mirror existing style and depth
- **Async testing**: Requires `pytest-asyncio` and proper mocking at low levels
- **Pattern consistency**: Follow existing test patterns religiously

### Code Standards
- **No comments**: Unless explicitly requested
- **Pattern following**: Check neighboring files first, follow existing conventions religiously
- **Backward compatibility**: Maintain unless explicitly told to remove constraints
- **Quality focus**: High expectations for production-ready code

## Project Context

### code-evals Repository
- **Purpose**: CLI tool that evaluates code changes against specifications using Mandoline AI
- **Architecture**: Simple linear pipeline: config → spec → git analysis → evaluation → output
- **Key features**: Auto-discovery of specs/config, git integration, AI-powered evaluation, pass/fail exit codes
- **Recent work**: Integrated Mandoline 0.5.0 async client for performance improvements
- **Build tool**: Uses setuptools for packaging
- **Linting**: `black code_evals/` and `flake8 code_evals/`, `mypy code_evals/`

### mandoline-python Repository
- **Purpose**: Python client for Mandoline LLM evaluation platform
- **Platform**: Systematic LLM comparison and evaluation across specific tasks/contexts
- **Clients**: AsyncMandoline (concurrent batch operations), Mandoline (simple sync operations)
- **Recent work**: Added AsyncMandoline client with true concurrent batch operations (v0.5.0)
- **Build tool**: Uses hatch for building/packaging
- **Testing**: Comprehensive async and sync test coverage

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

## Recent Session Insights

### async-client-true-batch-operations (mandoline-python)
- **Challenge**: Environment setup confusion (conda vs .venv)
- **Learning**: Proper async test mocking requires understanding call chains
- **Outcome**: 19 comprehensive async tests, async tutorial, version bump to 0.5.0
- **Documentation**: Created comprehensive CLAUDE.md through iterative refinement

### fix-tutorial-version-mismatch (mandoline-python)
- **Issue**: Tutorial requirements.txt had wrong version after async client release
- **Process correction**: Reminded about spec-first approach when trying to jump to implementation
- **Solution**: Updated tutorial environment with proper isolation
- **Learning**: Tutorials should test actual user experience, not dev environment

### mandoline-async-batch-integration (code-evals)
- **Goal**: Integrate Mandoline 0.5.0 async client for performance improvements
- **Challenge**: AsyncMandoline context manager protocol issue
- **Success**: Achieved concurrent evaluation with dramatic performance improvements
- **Verification**: Tested with verbose output, verified concurrent HTTP connections

## Key Learnings

### Process Adherence
- Spec-first approach is consistently enforced and non-negotiable
- Session logging captures real learning and collaboration dynamics
- Testing and verification are immediate, not deferred

### Technical Growth
- Environment setup patterns learned through trial and error
- Async mocking requires low-level understanding of call chains
- Performance improvements verified through actual testing

### Collaboration Quality
- User provides direct, practical guidance
- Iterative refinement improves deliverables
- Documentation serves future development needs
- Transparency in process and learning is valued