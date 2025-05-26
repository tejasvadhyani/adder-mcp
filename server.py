from fastmcp import FastMCP
import os

# ➊  Create the MCP server
mcp = FastMCP(
    "Adder-MCP",
    description="Returns the sum of two numbers"
)

# ➋  Declare an MCP tool
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Return the arithmetic sum of a and b.
    """
    return a + b

# ➌  Entrypoint for local/dev use
if __name__ == "__main__":
    # Runs under uvicorn/FastAPI inside FastMCP
    mcp.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
