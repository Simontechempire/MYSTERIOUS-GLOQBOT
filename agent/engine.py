from agents.planner import planner
from agents.executor import executor


class AgentEngine:

    async def run(
        self,
        goal: str
    ):

        plan = planner.create_plan(goal)

        if not plan:
            return {
                "success": False,
                "message": "No goal provided."
            }

        results = await executor.execute_plan(plan)

        return {
            "success": True,
            "goal": goal,
            "plan": plan,
            "results": results,
        }


agent_engine = AgentEngine()
