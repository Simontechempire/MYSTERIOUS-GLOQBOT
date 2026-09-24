from aiogram import Router
from .start import router as start_router
from .user import router as user_router
from .admin import router as admin_router


def setup_routers() -> Router:
    root = Router(name="root")
    root.include_router(start_router)
    root.include_router(user_router)
    root.include_router(admin_router)
    return root
