import asyncio
from typing import AsyncGenerator


async def stream_text(
    text: str,
    delay: float = 0.02
) -> AsyncGenerator[str, None]:

    words = text.split()

    for word in words:
        yield word + " "
        await asyncio.sleep(delay)
