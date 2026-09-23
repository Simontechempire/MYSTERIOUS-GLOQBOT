class CreativeStudio:

    def generate_text_prompt(self, topic: str):
        return (
            f"Create high-quality creative content about: {topic}"
        )

    def generate_image_prompt(self, description: str):
        return (
            f"Create an image based on this description: "
            f"{description}"
        )

    def generate_video_prompt(self, description: str):
        return (
            f"Create a video concept based on: {description}"
        )

    def generate_audio_prompt(self, description: str):
        return (
            f"Create an audio concept based on: {description}"
        )


creative_studio = CreativeStudio()
