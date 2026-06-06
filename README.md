Project Setup:
uv init py-mcp-server
cd py-mcp-server
uv add "mcp[cli]"
uv add pytest-asyncio



Project: Python MCP Server: Connect LLMs to Your Data
MCP is an open protocol that allows AI models to interact with external systems in a standardized, extensible way.
will install MCP, explore its client-server architecture, and work with its core concepts: prompts, resources, and tools.
build and test a Python MCP server that queries e-commerce data and integrate it with an AI agent in Cursor to see real tool calls in action.
Ref: https://realpython.com/python-mcp/

this project will include:
What MCP is and why it was created
What MCP prompts, resources, and tools are
How to build an MCP server with customized tools
How to integrate your MCP server with AI agents like Cursor

build a simple MCP server that interacts with a simulated e-commerce database. 
use Cursor’s MCP client, which saves from having to implement dedicated.



MCP server is an API that hosts the prompts, resources, and tools we want to make available to an LLM.
MCP client acts as the bridge between the LLM and the server—exposing the server’s content, 
receiving input from the LLM, executing tools on the server, and returning the results back to the model or end user.

Tool calling processes, like LangChain or Cursor, receive your user prompt before passing it to the underlying LLM via an API call.
In this way, we’re not directly interacting with the LLM API. 
Instead, the Python process, or any other tool we’re using, acts as a mediator between we and the LLM.


MCP servers support three core primitives prompts, resources, and tools, each serving a distinct role in how LLMs interact with external systems.


Resources are read-only and represented via URIs, supporting both text and binary formats. 
Tools are functions hosted by API endpoints that allow LLMs to trigger real-world actions
Tools can encapsulate virtually any logic that you can write in a programming language.
Tools are designed to be model-invoked with client-side approval as needed.
Each tool is defined with a JSON schema for its input, and annotations can hint at safety properties. 
Tools are the most powerful and commonly used primitives, enabling LLMs to interact dynamically with external systems

The power of MCP is that you can seamlessly connect servers to clients hosted in various applications 
like Cursor, Claude Code, Windsurf, LangChain, and any other software that supports MCP clients
Cursor: 
is an AI code editor that makes it straightforward to develop, test, and deploy AI-assisted code.
Cursor is a fork of VS Code, which is arguably the most popular code editor worldwide.
Cursor hosts an MCP client that allows you to connect to multiple servers.