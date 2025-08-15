# code-evals Repository Memory

## Project Overview
- **Purpose**: CLI tool that evaluates code changes against specifications using Mandoline AI
- **Architecture**: Simple linear pipeline: config → spec → git analysis → evaluation → output

## Technical Environment
- **Build**: setuptools, `pip install -e .[dev]`
- **Testing**: pytest, standard patterns
- **Linting**: `black code_evals/`, `mypy code_evals/`, `flake8 code_evals/`

## Recent Changes
- **v0.5.0**: Integrated AsyncMandoline client for concurrent evaluation
- **Key Issue**: AsyncMandoline context manager protocol fix

## Troubleshooting
- Use verbose output to verify concurrent operations