#!/usr/bin/env python3
"""
Test client for the FastMCP server
"""
import asyncio
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    """Test the MCP server tools"""
    server_params = StdioServerParameters(
        command="uv", 
        args=["run", "python", "main.py"]
    )
    
    async with stdio_client(server_params) as (read, write):
        # List available tools
        result = await read()
        print(f"Server info: {result}")
        
        # Test the hello tool
        write({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "hello",
                "arguments": {"name": "FastMCP"}
            }
        })
        
        response = await read()
        print(f"Hello response: {response}")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())