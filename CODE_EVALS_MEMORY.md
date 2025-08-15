# code-evals Repository Memory

## Project Overview
- **Purpose**: CLI tool that evaluates code changes against specifications using Mandoline AI
- **Architecture**: Simple linear pipeline: config → spec → git analysis → evaluation → output
- **Key Features**: Auto-discovery of specs/config, git integration, AI-powered evaluation, pass/fail exit codes

## Technical Environment

### Build System
- **Build Tool**: setuptools
- **Package Management**: pip
- **Installation**: `pip install -e .[dev]`

### Development Environment
- **Virtual Environment**: `.venv` in root directory
- **Common Issues**: "pip is disabled in base environment" → `conda deactivate && source .venv/bin/activate`
- **Dependencies**: Uses Mandoline client for AI evaluation

### Testing Framework
- **Test Runner**: pytest
- **Special Requirements**: Standard testing patterns
- **Coverage Expectations**: Mirror existing test style and depth

### Code Quality Tools
- **Linting**: `black code_evals/`
- **Type Checking**: `mypy code_evals/`
- **Formatting**: `flake8 code_evals/`

## Project-Specific Patterns

### Code Conventions
- Simple, linear processing pipeline
- Config-driven behavior with sensible defaults
- Git integration for change detection

### Testing Patterns
- Standard pytest patterns
- Focus on CLI behavior and integration testing

### Common Workflows
- Spec creation → implementation → evaluation
- Git-based change detection and analysis

## Recent Context

### Active Branches
- **mandoline-async-batch-integration**: Integrated Mandoline 0.5.0 async client for performance improvements

### Recent Issues & Solutions
- **AsyncMandoline context manager**: Fixed protocol issue for concurrent evaluation
- **Performance improvements**: Achieved dramatic performance gains with concurrent HTTP connections
- **Verification**: Tested with verbose output to confirm concurrent operations

### Version History
- **Latest**: Integrated Mandoline 0.5.0 with AsyncMandoline client
- **Key Change**: Moved from synchronous to asynchronous batch evaluation

## Domain Knowledge

### Business Logic
- Evaluates code changes against written specifications
- Uses AI to determine if implementation matches spec requirements
- Provides pass/fail exit codes for CI integration

### Performance Considerations
- Concurrent evaluation with AsyncMandoline for batch operations
- HTTP connection pooling for efficient API usage

## External Dependencies

### Key Libraries
- **Mandoline 0.5.0**: AI evaluation platform client
- **AsyncMandoline**: For concurrent batch operations
- **Git integration**: For change detection and analysis

### Services & APIs
- **Mandoline platform**: LLM evaluation service
- **Rate limits**: Handled through async client batching

## Troubleshooting Guide

### Common Errors
- Environment activation issues with conda/pip conflicts
- Context manager protocol errors with async clients

### Debug Strategies
- Use verbose output to verify concurrent operations
- Test actual HTTP connection behavior for performance verification