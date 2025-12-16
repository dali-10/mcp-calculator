from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="MyFirstMCP")

@mcp.tool()
def say_hello(name: str):
    """Returns a greeting message."""
    return f"hello ,{name} , welcome to MyFirstMCP!"


if __name__ == "__main__":
    mcp.run(transport="stdio")