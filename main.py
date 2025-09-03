from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Brainz Server 🧠")

@mcp.tool
def hello(name: str) -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool
def get_info() -> str:
    """Get information about this MCP server"""
    return "This is the Brainz MCP server built with FastMCP!"

if __name__ == "__main__":
    mcp.run()  # Uses STDIO transport by default
