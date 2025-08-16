# code-evals Repository Memory

## Project Overview
- **Purpose**: CLI tool that evaluates code changes against specifications using Mandoline AI
- **Architecture**: Simple linear pipeline: config → spec → git analysis → evaluation → output
- **Key Features**: Concurrent evaluation, merge commit handling, spec-based assessment

## Technical Environment

### Build System
- **Build Tool**: setuptools
- **Package Management**: pip
- **Installation**: `pip install -e .[dev]`

### Development Environment
- **Virtual Environment**: Use `.venv` in root directory
- **Common Issues**: AsyncMandoline client instantiation (no context manager support)
- **Dependencies**: mandoline>=0.5.0, asyncio for concurrent evaluation

### Testing Framework
- **Test Runner**: pytest, standard patterns
- **Special Requirements**: Async testing patterns, HTTP-level mocking
- **Coverage Expectations**: Test evaluation logic and git operations

### Code Quality Tools
- **Linting**: `black code_evals/`, `flake8 code_evals/`
- **Type Checking**: `mypy code_evals/`
- **Formatting**: black (standard Python formatting)

## Project-Specific Patterns

### Code Conventions
- Follow async/await patterns for concurrent operations
- Use `asyncio.gather()` for batch processing
- Atomic operations in git analysis

### Testing Patterns
- Mock HTTP requests at API level for Mandoline integration
- Test merge commit scenarios specifically
- Verify concurrent operation behavior

### Common Workflows
- Spec-driven evaluation: spec file → git analysis → concurrent metric evaluation → results
- Debug with verbose mode to verify concurrent operations
- Manual testing: `code-evals --spec [spec-file] --verbose`

## Recent Context

### Active Branches
- Main development on main branch
- Recent focus: merge commit handling, async performance optimization

### Recent Issues & Solutions
- **Merge Commit Bug**: Fixed CI merge commit evaluation causing "No changes detected" errors
- **Performance**: Integrated AsyncMandoline 0.5.0 for concurrent evaluation (dramatic speedup)
- **AsyncMandoline Context**: Fixed context manager protocol issues
- **Code Duplication**: Avoided by reusing `spec_ops.discover_spec_path()` instead of custom helpers

### Version History
- **v0.5.0**: Integrated AsyncMandoline client for concurrent evaluation
- **Key Breaking Change**: Requires mandoline>=0.5.0, async patterns throughout

## Domain Knowledge

### Business Logic
- **Core Concept**: Evaluate code changes against written specifications using AI
- **Evaluation Process**: Extract git changes, exclude specs from diffs, concurrent metric assessment
- **Key Algorithm**: Merge commit detection and proper head/base selection for accurate diffs

### Performance Considerations
- **Bottleneck**: Sequential API calls to Mandoline (solved with async)
- **Optimization**: Concurrent evaluation using `asyncio.gather()` provides dramatic speedup
- **Resource Efficiency**: Better API utilization through simultaneous requests

## External Dependencies

### Key Libraries
- **mandoline>=0.5.0**: Core evaluation engine with async client
- **asyncio**: Concurrent evaluation processing
- **GitPython**: Git repository analysis and diff generation

### Services & APIs
- **Mandoline API**: AI-powered code evaluation service
- **Rate Limits**: Handled through async client connection pooling
- **Error Handling**: Graceful degradation for network/API failures

## Development Challenges

### Self-Referential Evaluation
- **Challenge**: Features that change evaluation behavior create circular evaluation issues
- **Example**: Spec exclusion feature evaluated with spec in diff during development
- **Philosophy**: "Ship of Theseus" problem - modifying evaluation while being evaluated
- **Approach**: Accept inconsistency during transition, enforce consistency post-deployment

### Related Code Discovery Gap
- **Issue**: Evaluation context may miss related code not directly edited
- **Impact**: Can lead to code duplication when existing functionality isn't discovered
- **Example**: `spec_ops` module missed during evaluation despite being related
- **Future Scope**: Static analysis, import graph traversal, semantic similarity needed

## Troubleshooting Guide

### Common Errors
- **"No changes detected"**: Usually merge commit evaluation bug (fixed in git_ops.py:extract_changes)
- **AsyncMandoline context errors**: Don't use `async with` - instantiate directly
- **Empty diffs in CI**: Check merge commit detection logic

### Debug Strategies
- **Verbose mode**: Use `--verbose` to verify concurrent operations and commit selection
- **Merge commit debugging**: Check logs for commit parent detection
- **Performance verification**: Look for concurrent HTTP requests in debug output
- **Git analysis**: Verify base/head commit selection in verbose logs

### CI/GitHub Integration
- **Temporary Merge Commits**: GitHub PR workflow creates commits not visible locally
- **Different Commit History**: CI sees different history than local development environment
- **Infrastructure Dependencies**: Changes require understanding entire CI/eval pipeline