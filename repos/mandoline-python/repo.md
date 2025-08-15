# mandoline-python Repository Memory

## Project Overview
- **Purpose**: Python client for Mandoline LLM evaluation platform
- **Architecture**: Dual client system - AsyncMandoline (concurrent batch operations), Mandoline (simple sync operations)
- **Key Features**: Systematic LLM comparison and evaluation across specific tasks/contexts

## Technical Environment

### Build System
- **Build Tool**: hatch
- **Package Management**: pip
- **Installation**: `pip install -e .[dev]`

### Development Environment
- **Virtual Environment**: `.venv` in root directory
- **Common Issues**: "pip is disabled in base environment" → `conda deactivate && source .venv/bin/activate`
- **Dependencies**: `pytest-asyncio` for async testing

### Testing Framework
- **Test Runner**: pytest
- **Special Requirements**: `pytest-asyncio` for async test support
- **Coverage Expectations**: Comprehensive async and sync test coverage (19 comprehensive async tests)

### Code Quality Tools
- **Linting**: Standard Python linting
- **Type Checking**: Type hints throughout
- **Formatting**: Standard Python formatting

## Project-Specific Patterns

### Code Conventions
- Dual sync/async client pattern
- Context manager protocols for resource management
- Comprehensive type hinting

### Testing Patterns
- **Async Mocking**: Mock at lowest HTTP/network level for reliable testing
- **Call Chain Understanding**: Async test mocking requires understanding complete call chains
- **Comprehensive Coverage**: Both sync and async clients fully tested

### Common Workflows
- Client instantiation → batch operations → result processing
- Context manager pattern for resource cleanup

## Recent Context

### Active Branches
- **async-client-true-batch-operations**: Added AsyncMandoline client with true concurrent batch operations (v0.5.0)
- **fix-tutorial-version-mismatch**: Updated tutorial requirements.txt after async client release

### Recent Issues & Solutions
- **Environment setup confusion**: Learned to distinguish conda vs .venv properly
- **Async test mocking**: Required understanding call chains and mocking at HTTP level
- **Tutorial isolation**: Tutorials should test actual user experience, not dev environment
- **Version mismatch**: Tutorial requirements.txt needed update after v0.5.0 release

### Version History
- **v0.5.0**: Added AsyncMandoline client with concurrent batch operations
- **Breaking changes**: Added new async client alongside existing sync client

## Domain Knowledge

### Business Logic
- LLM evaluation platform for systematic comparison
- Batch operations for efficient evaluation across multiple contexts
- Both synchronous and asynchronous operation modes

### Performance Considerations
- AsyncMandoline enables true concurrent batch operations
- HTTP connection pooling and async context management
- Dramatic performance improvements with concurrent evaluation

## External Dependencies

### Key Libraries
- **aiohttp**: For async HTTP operations
- **pytest-asyncio**: For async testing support
- **Type system**: Comprehensive typing throughout

### Services & APIs
- **Mandoline platform**: Core LLM evaluation service
- **HTTP APIs**: RESTful interface with async support

## Troubleshooting Guide

### Common Errors
- **Environment conflicts**: Conda vs .venv activation issues
- **Async context**: Context manager protocol errors with AsyncMandoline
- **Test mocking**: Async mocking requires low-level HTTP mocking

### Debug Strategies
- **Async debugging**: Understand complete async call chains
- **Performance verification**: Use actual testing to verify concurrent operations
- **Environment isolation**: Ensure tutorial testing reflects real user experience
- **Iterative refinement**: CLAUDE.md created through multiple iterations for clarity