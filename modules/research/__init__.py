class ResearchLab:

    def create_research_plan(self, topic: str):
        return {
            "topic": topic,
            "steps": [
                "Define the research question",
                "Collect relevant sources",
                "Analyze information",
                "Compare findings",
                "Create a summary",
            ],
        }

    def create_question(self, topic: str):
        return (
            f"Research question: "
            f"What are the important facts about {topic}?"
        )


research_lab = ResearchLab()
