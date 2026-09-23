from collections import defaultdict


class ConversationMemory:

    def __init__(self, max_messages: int = 20):
        self.max_messages = max_messages
        self._memory = defaultdict(list)

    def add_message(
        self,
        user_id: int,
        role: str,
        content: str
    ):
        messages = self._memory[user_id]

        messages.append({
            "role": role,
            "content": content,
        })

        if len(messages) > self.max_messages:
            self._memory[user_id] = messages[
                -self.max_messages:
            ]

    def get_messages(
        self,
        user_id: int
    ) -> list:
        return self._memory.get(user_id, [])

    def clear(
        self,
        user_id: int
    ):
        self._memory.pop(user_id, None)


memory = ConversationMemory()
