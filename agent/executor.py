from agents.tools import tools


class AgentExecutor:

    async def execute_tool(
        self,
        tool_name: str,
        **kwargs
    ):

        return await tools.execute(
            tool_name,
            **kwargs
        )

    async def execute_plan(
        self,
        plan
    ):

        results = []

        for step in plan:

            if step.action == "execute":
                results.append({
                    "step": step.number,
                    "status": "waiting_for_tool"
                })

            else:
                results.append({
                    "step": step.number,
                    "status": "completed"
                })

        return results


executor = AgentExecutor()
