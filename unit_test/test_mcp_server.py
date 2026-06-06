import asyncio
import pytest
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


"""
Testing Your MCP Server
Before connecting MCP server to an MCP client, 
it’s important to verify that mcp server is running and that the tools we’ve created are available to the client. 
To do this, write a unit test that connects to MCP server in the same way an MCP client would. 
This will give a deeper understanding of how MCP clients interact with MCP server and expose tools to LLMs. 
"""

SERVER_PATH = "./main.py"


# EXPECTED_TOOLS are the function names from mcp server.
EXPECTED_TOOLS = [
    "get_customer_info",
    "get_order_details",
    "check_inventory",
    "get_customer_ids_by_name",
    "get_orders_by_customer_id",
]


"""
define a test for mcp server
which connects to your server, displays the server’s tool names and descriptions, and asserts that all of the expected tools are there.
run test from a terminal using the 'pytest -s' command
"""
@pytest.mark.asyncio
async def test_mcp_server_connection():
    """Connect to an MCP server and verify the tools"""

    # instantiate an AsyncExitStack object that manages multiple async with contexts for proper cleanup, especially for open connections to your server.
    exit_stack = AsyncExitStack()

    # connect to server and initialize a client session
    server_params = StdioServerParameters(command="python", args=[SERVER_PATH], env=None)

    stdio_transport = await exit_stack.enter_async_context(
        stdio_client(server_params)
    )
    stdio, write = stdio_transport
    session = await exit_stack.enter_async_context(
        ClientSession(stdio, write)
    )

    await session.initialize()

    response = await session.list_tools() # makes a request to server to extract the names and descriptions of all the available tools.
    tools = response.tools
    tool_names = [tool.name for tool in tools]
    tool_descriptions = [tool.description for tool in tools]

    print("\nYour server has the following tools:")
    for tool_name, tool_description in zip(tool_names, tool_descriptions):
        print(f"{tool_name}: {tool_description}")

    assert sorted(EXPECTED_TOOLS) == sorted(tool_names)

    await exit_stack.aclose()