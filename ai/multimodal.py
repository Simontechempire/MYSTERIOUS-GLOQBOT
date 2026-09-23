from dataclasses import dataclass
from typing import Optional


@dataclass
class MediaInput:
    media_type: str
    file_id: Optional[str] = None
    text: Optional[str] = None


SUPPORTED_MEDIA = {
    "text",
    "image",
    "voice",
    "document",
    "video",
}


def is_supported(media_type: str) -> bool:
    return media_type in SUPPORTED_MEDIA


def create_media_input(
    media_type: str,
    file_id: Optional[str] = None,
    text: Optional[str] = None
) -> MediaInput:

    if not is_supported(media_type):
        raise ValueError(
            f"Unsupported media type: {media_type}"
        )

    return MediaInput(
        media_type=media_type,
        file_id=file_id,
        text=text,
    )
