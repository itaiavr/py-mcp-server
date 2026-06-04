Project Setup:
uv init py-mcp-server
cd py-mcp-server
uv add "mcp[cli]"
uv add pytest-asyncio

Project: Python MCP Server: Connect LLMs to Your Data
MCP is an open protocol that allows AI models to interact with external systems in a standardized, extensible way.
will install MCP, explore its client-server architecture, and work with its core concepts: prompts, resources, and tools.
build and test a Python MCP server that queries e-commerce data and integrate it with an AI agent in Cursor to see real tool calls in action.

this project will include:
What MCP is and why it was created
What MCP prompts, resources, and tools are
How to build an MCP server with customized tools
How to integrate your MCP server with AI agents like Cursor
