class CommunitySuite:

    def welcome_message(self, name: str):
        return (
            f"👋 Welcome {name}!\n\n"
            "Welcome to the community."
        )

    def announcement(self, message: str):
        return {
            "type": "announcement",
            "message": message,
        }

    def community_rules(self):
        return [
            "Be respectful.",
            "No spam.",
            "Follow administrator instructions.",
            "Keep the community safe.",
        ]


community_suite = CommunitySuite()
