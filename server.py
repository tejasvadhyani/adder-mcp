import os
from fastmcp import FastMCP

mcp = FastMCP("Adder-MCP")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

if __name__ == "__main__":
    # Streamable HTTP is the modern, production transport
    mcp.run(
        transport="streamable-http",      # or "sse" if you really need SSE
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),  # Render/Heroku inject $PORT
        path="/mcp"                       # default; change only if you want /api etc.
    )
