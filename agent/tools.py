from typing import Callable, Any


class ToolRegistry:

    def __init__(self):
        self.tools: dict[str, Callable] = {}

    def register(
        self,
        name: str,
        description: str,
        function: Callable
    ):
        self.tools[name] = {
            "description": description,
            "function": function,
        }

    def get(self, name: str):
        return self.tools.get(name)

    def list_tools(self):
        return {
            name: {
                "description": tool["description"]
            }
            for name, tool in self.tools.items()
        }

    async def execute(
        self,
        name: str,
        **kwargs
    ) -> Any:

        tool = self.get(name)

        if not tool:
            raise ValueError(
                f"Tool '{name}' does not exist."
            )

        function = tool["function"]

        result = function(**kwargs)

        if hasattr(result, "__await__"):
            result = await result

        return result


tools = ToolRegistry()
