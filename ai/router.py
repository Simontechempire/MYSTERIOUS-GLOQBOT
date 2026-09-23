from typing import Optional


class AIModelRouter:

    def __init__(self):
        self.models = {}

    def register_model(
        self,
        name: str,
        provider: str,
        model: str
    ):
        self.models[name] = {
            "provider": provider,
            "model": model,
        }

    def get_model(
        self,
        name: str
    ) -> Optional[dict]:

        return self.models.get(name)

    def list_models(self) -> dict:
        return self.models


router = AIModelRouter()
