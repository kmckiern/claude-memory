# mandoline-integrations Repository Memory

## Project Overview

- **Purpose**: Comprehensive guide to all Mandoline evaluation integration methods and workflows
- **Architecture**: Documentation hub covering SDK, MCP, CI/CD, and web interface integration patterns
- **Key Features**: Real-world evaluation workflows using actual user data and domain-specific metrics

## Critical Insights

### Non-Obvious Patterns

- **Real-world evaluation philosophy**: Focus on actual workflows and user data rather than synthetic benchmarks
- **Integration ecosystem approach**: Multiple complementary evaluation methods rather than single solution
- **Self-evaluation loops**: AI agents can assess and improve their own outputs in real-time through MCP integration
- **Interactive evaluation model**: MCP transforms interaction from generate→review→feedback to generate→self-assess→refine→deliver within single conversation
- **SDK embedded evaluation**: Transforms from separate evaluation processes to evaluation-as-code, making quality assessment part of development workflow
- **CI/CD quality gates**: code-evals transforms code review from manual human process to automated quality gates with custom metrics on every commit
- **Data-driven model selection**: Web interface transforms model choice from trial-and-error to systematic experimentation with actual user prompts and data

### Domain Complexity

- **Custom metrics as first-class citizens**: User-defined evaluation criteria (-1.0 to 1.0) tailored to specific use cases
- **Workflow-specific evaluation**: Different integration methods serve different parts of development lifecycle
- **Context-aware assessment**: Evaluations happen with full conversation/codebase context rather than isolated snippets
- **Continuous evaluation philosophy**: From desktop development → CI/CD → production monitoring

### Agent Behavior Transformation

- **MCP-enabled agents**: Become self-correcting - can evaluate and iterate on code quality before delivering, leading to higher-quality initial outputs
- **SDK-integrated agents**: Shift from "code and hope" to "code with embedded quality checks" - evaluation becomes part of generated code patterns
- **CI/CD monitored agents**: Develop pattern recognition from automated feedback - learn team-specific quality patterns through continuous metric exposure
- **Multi-context agent evolution**: Same agent behaves differently across contexts - more careful in CI, more experimental in desktop, more systematic in model selection

### Development Challenges

- **Moving beyond generic benchmarks**: Creating meaningful evaluation criteria for domain-specific tasks
- **Integration complexity**: Coordinating evaluation across multiple touchpoints in development workflow
- **Data relevance**: Ensuring evaluation uses representative real-world data rather than toy examples

## Performance & Debugging

### Critical Performance Insights

- **Real-time evaluation capability**: MCP integration enables immediate feedback loops in Claude Desktop
- **Batch evaluation efficiency**: CI/CD integration (code-evals) processes multiple metrics per code change
- **Rate limiting considerations**: 3 req/sec limits require batching strategies for large-scale evaluation

### Debugging Complexity

- **Metric definition challenges**: Ensuring custom metrics accurately capture intended quality dimensions
- **Integration testing complexity**: Validating evaluation accuracy across different integration methods
- **Context preservation**: Maintaining evaluation relevance across different integration touchpoints

## Recent Context

### Key Learnings

- **MCP enables desktop evaluation**: Real-time assessment capabilities directly in Claude conversation
- **code-evals prototype**: CI/CD integration for continuous evaluation of agent-generated code
- **Multi-modal evaluation support**: Text and image evaluation capabilities across all integration methods

### Evolution & Trade-offs

- **Trade-off**: Generic vs. specific evaluation - chose domain-specific metrics over universal benchmarks
- **Evolution**: From standalone evaluation platform to integrated development workflow infrastructure
- **Breaking insight**: Evaluation effectiveness depends on using actual user data and workflows rather than synthetic tests
