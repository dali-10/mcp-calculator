from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="MyFirstMCP")

@mcp.tool()
def add_number(a: float,b : float) -> float:
    """Returns the sum of two numbers."""
    return a + b
@mcp.tool()
def substract_number(a: float,b : float) -> float:
    """Returns the substraction of two numbers."""   
    return a - b
@mcp.tool()
def multiply_number(a: float,b : float) -> float:
    """Returns the multiplication of two numbers."""
    return a * b
@mcp.tool()
def divide_number(a: float, b: float) -> float:
    """Divides a by b and returns the result"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


#if __name__ == "__main__":
  #  mcp.run(transport="stdio")
if __name__ == "__main__":
 mcp.run(transport="http") # You can change transport to "sse" if needed