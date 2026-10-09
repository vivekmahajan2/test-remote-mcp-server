from fastmcp import FastMCP
import random
import json

#Create a FastMcp Server instance
mcp = FastMCP('Simple Calculator Server')

@mcp.tool
def add(a:int,b:int) -> int :
    return a+b

@mcp.tool
def random_number(min_val:int = 1, max_val : int = 100) -> int:
    return random.randint(min_val,min_val)

@mcp.resource('info://server')
def server_info() -> str:
    info = {
        'name' : 'Simple Calculator Server',
        'version' : '1.0.0',
        "Description" : "A basic MCP Server with math tools",
        "tools" : ["add","random_number"],
        "author" : "Your Name"
    }
    return json.dumps(info,indent=2)

if __name__ == '__main__':
    mcp.run(transport='http',host = '0.0.0.0',port=8000)