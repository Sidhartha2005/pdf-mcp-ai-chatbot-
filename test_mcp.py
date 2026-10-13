import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available MCP tools:")

            for tool in tools.tools:
                print("-", tool.name, ":", tool.description)

            result = await session.call_tool(
                "search_pdf",
                {
                    "document_text": (
                        "Greenfield Library opened in 2018. "
                        "It has 12000 books and 24 computers. "
                        "Members can borrow up to 4 books for 14 days."
                    ),
                    "question": "What year did Greenfield Library open?",
                },
            )

            print("\nSearch result:")
            for item in result.content:
                if hasattr(item, "text"):
                    print(item.text)


if __name__ == "__main__":
    asyncio.run(main())