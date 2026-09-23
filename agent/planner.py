from dataclasses import dataclass


@dataclass
class PlanStep:
    number: int
    action: str
    description: str


class AgentPlanner:

    def create_plan(
        self,
        goal: str
    ) -> list[PlanStep]:

        if not goal.strip():
            return []

        return [
            PlanStep(
                number=1,
                action="analyze",
                description=(
                    f"Analyze the user's goal: {goal}"
                )
            ),
            PlanStep(
                number=2,
                action="execute",
                description=(
                    "Execute the required tools."
                )
            ),
            PlanStep(
                number=3,
                action="respond",
                description=(
                    "Return the result to the user."
                )
            ),
        ]


planner = AgentPlanner()
