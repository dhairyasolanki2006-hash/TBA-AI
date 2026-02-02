Built an AI-powered tooling engine that turns natural-language questions into structured backend tool calls using LangChain and a locally hosted Ollama (LLaMA 3.2) model. The system routes user queries to the correct function using semantic tool definitions and a strict JSON-only schema, then executes approved tools through a controlled executor layer to return reliable results.

Key components

LLaMA 3.2 via Ollama for local inference
LLM router for intent + argument extraction
Semantic tool definitions to describe capabilities and inputs
JSON-based decision output to enforce predictable tool calling
Executor layer for safe tool execution and structured responses

Highlights
Modular design: add new tools/APIs without changing core routing logic
Safety-first: the AI doesn’t invent data—only calls approved tools
Clear separation of routing, execution, and data handling

Use cases
API-driven assistants
Any system that needs safe mapping from natural language → tool/function calls
