# mandoline-python Repository Memory

## Project Overview

- **Purpose**: Python client for Mandoline LLM evaluation platform
- **Architecture**: Dual client system - AsyncMandoline (concurrent), Mandoline (sync)

## Technical Environment

### Build System

- **Build Tool**: hatch
- **Package Management**: pip
- **Installation**: `pip install -e .[dev]`

### Development Environment

- **Dependencies**: Key async libraries for LLM evaluation
- **Common Issues**: Async context manager protocol complexities

### Testing Framework

- **Test Runner**: pytest + `pytest-asyncio`
- **Special Requirements**: Async mocking requires HTTP-level mocking
- **Coverage Expectations**: Complete call chain understanding needed

### Code Quality Tools

- **Linting**: Standard Python linting
- **Type Checking**: Standard type checking
- **Formatting**: Standard Python formatting

## Project-Specific Patterns

### Code Conventions

- Dual client architecture: AsyncMandoline (concurrent) and Mandoline (sync)
- Proper async/await patterns throughout

### Testing Patterns

- HTTP-level mocking for async operations
- Real user experience reflection in tutorials

### Common Workflows

- Client instantiation and context management
- Batch operations with concurrency

## Recent Context

### Active Branches

- Main development on main branch

### Recent Issues & Solutions

- **v0.5.0**: Added AsyncMandoline client with true concurrent batch operations
- **Key Issue**: Async test mocking requires understanding complete call chains

### Version History

- **v0.5.0**: Major async client addition

## Domain Knowledge

### Business Logic

- **Core Concept**: Python client for Mandoline LLM evaluation platform
- **Process**: Sync and async evaluation interfaces
- **Key Algorithm**: Concurrent batch operations for performance

### Performance Considerations

- **Optimization**: AsyncMandoline provides true concurrency
- **Efficiency**: Batch operations reduce API call overhead

## External Dependencies

### Key Libraries

- **asyncio**: Core async functionality
- **httpx/aiohttp**: HTTP client libraries for async operations

### Services & APIs

- **Mandoline API**: LLM evaluation service
- **Rate Limits**: Handled through client connection management

## Troubleshooting Guide

### Common Errors

- **Async context errors**: AsyncMandoline context manager protocol
- **Tutorial testing**: Should reflect real user experience, not dev environment

### Debug Strategies

- Verify proper async context usage
- Test with real-world scenarios
