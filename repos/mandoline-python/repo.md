# mandoline-python Repository Memory

## Project Overview
- **Purpose**: Python client for Mandoline LLM evaluation platform
- **Architecture**: Dual client system - AsyncMandoline (concurrent), Mandoline (sync)

## Technical Environment
- **Build**: hatch, `pip install -e .[dev]`
- **Testing**: pytest + `pytest-asyncio`
- **Key pattern**: Async mocking requires HTTP-level mocking

## Recent Changes
- **v0.5.0**: Added AsyncMandoline client with true concurrent batch operations
- **Key Issue**: Async test mocking requires understanding complete call chains

## Troubleshooting
- **Async context errors**: AsyncMandoline context manager protocol
- **Tutorial testing**: Should reflect real user experience, not dev environment