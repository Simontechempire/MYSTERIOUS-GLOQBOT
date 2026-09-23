class ContentStudio:

    def create_post(self, topic: str, platform: str):
        return {
            "platform": platform,
            "topic": topic,
            "status": "draft",
        }

    def create_caption(self, topic: str):
        return (
            f"Create an engaging caption about {topic}."
        )

    def create_script(self, topic: str):
        return {
            "type": "script",
            "topic": topic,
        }


content_studio = ContentStudio()
