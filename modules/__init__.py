class PersonalOS:

    def create_task(self, title: str):
        return {
            "type": "task",
            "title": title,
            "status": "pending",
        }

    def create_note(self, content: str):
        return {
            "type": "note",
            "content": content,
        }

    def create_knowledge(self, title: str, content: str):
        return {
            "type": "knowledge",
            "title": title,
            "content": content,
        }


personal_os = PersonalOS()
