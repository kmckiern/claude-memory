# mandoline-python Repository Memory

## Project Overview

- **Purpose**: Python client for Mandoline LLM evaluation platform
- **Architecture**: Dual client system - AsyncMandoline (true concurrency), Mandoline (sync simplicity)
- **Key Features**: Concurrent batch operations, context-aware client management

## Critical Insights

### Non-Obvious Patterns

- **Dual client architecture**: AsyncMandoline and Mandoline serve different use cases - not just async/sync variants but fundamentally different operation models
- **Context manager complexity**: AsyncMandoline context protocol requires careful instantiation patterns that differ from typical async context managers
- **HTTP-level mocking necessity**: Async testing requires understanding complete call chains, not just method-level mocking

### Domain Complexity

- **Concurrent batch operations**: True concurrency for performance vs. sequential operations for simplicity
- **LLM evaluation platform integration**: Client must handle rate limits, connection pooling, and evaluation-specific response patterns
- **Tutorial vs. dev environment gap**: Real user experience requires different testing approaches than development environment

### Development Challenges

- **Async test mocking complexity**: Complete call chain understanding needed for effective testing
- **Context manager protocol**: AsyncMandoline requires non-standard instantiation patterns
- **Performance vs. simplicity trade-off**: Dual clients address different user needs and technical constraints

## Performance & Debugging

### Critical Performance Insights

- **True concurrency benefit**: AsyncMandoline provides dramatic speedup through simultaneous API requests vs. sequential calls
- **Connection pooling efficiency**: Rate limits handled through client connection management rather than request-level throttling
- **Batch operation optimization**: Reduces API call overhead through intelligent request grouping

### Debugging Complexity

- **Async context manager pitfalls**: AsyncMandoline requires direct instantiation, not standard `async with` patterns
- **HTTP-level mocking requirements**: Testing must mock at API level, not method level, due to complex async call chains
- **Tutorial vs. development environment gaps**: Real user scenarios require different testing approaches than dev environment assumptions

## Recent Context

### Key Learnings

- **v0.5.0 insight**: Async test mocking complexity revealed need for complete call chain understanding
- **Context manager protocol discovery**: Standard async patterns don't apply to AsyncMandoline instantiation
- **Performance validation**: Concurrent batch operations provide measurable performance improvements

### Evolution & Trade-offs

- **Trade-off**: Complexity vs. performance - AsyncMandoline adds complexity for significant speed gains
- **Evolution**: From single sync client to dual architecture addressing different user needs
- **Breaking change**: v0.5.0 introduced async patterns requiring new testing approaches
