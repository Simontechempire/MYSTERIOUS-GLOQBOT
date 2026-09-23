from dataclasses import dataclass, field


@dataclass
class Agent:
    name: str
    description: str
    system_prompt: str
    tools: list[str] = field(default_factory=list)


class AgentBuilder:

    def __init__(self):
        self.agents = {}

    def create(
        self,
        name: str,
        description: str,
        system_prompt: str,
        tools: list[str] | None = None
    ):

        agent = Agent(
            name=name,
            description=description,
            system_prompt=system_prompt,
            tools=tools or [],
        )

        self.agents[name] = agent

        return agent

    def get(self, name: str):
        return self.agents.get(name)

    def list_agents(self):
        return list(self.agents.keys())


agent_builder = AgentBuilder()
