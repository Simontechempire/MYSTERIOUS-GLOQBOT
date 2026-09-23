import asyncio
from datetime import datetime
from typing import Callable


class TaskScheduler:

    def __init__(self):
        self.tasks = {}

    async def schedule(
        self,
        task_id: str,
        delay: int,
        function: Callable,
        *args,
        **kwargs
    ):

        await asyncio.sleep(delay)

        result = function(
            *args,
            **kwargs
        )

        if hasattr(result, "__await__"):
            result = await result

        self.tasks.pop(task_id, None)

        return result

    def create_task(
        self,
        task_id: str,
        delay: int,
        function: Callable,
        *args,
        **kwargs
    ):

        task = asyncio.create_task(
            self.schedule(
                task_id,
                delay,
                function,
                *args,
                **kwargs
            )
        )

        self.tasks[task_id] = {
            "task": task,
            "created_at": datetime.utcnow().isoformat(),
            "delay": delay,
        }

        return task

    def cancel(self, task_id: str):

        task_info = self.tasks.get(task_id)

        if not task_info:
            return False

        task_info["task"].cancel()

        self.tasks.pop(task_id, None)

        return True


scheduler = TaskScheduler()
