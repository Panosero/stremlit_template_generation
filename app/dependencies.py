"""FastAPI dependencies for dependency injection."""

from app.config import Settings, get_settings
from app.database.connection import get_async_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated


def get_current_settings() -> Settings:
    """Get current application settings.

    Returns:
        Settings: Application configuration settings.
    """
    return get_settings()


async def get_db_session() -> AsyncSession:
    """Get database session.

    Yields:
        AsyncSession: Database session for async operations.
    """
    async for session in get_async_session():
        yield session


# Type aliases for common dependencies
SettingsDep = Annotated[Settings, Depends(get_current_settings)]
DBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]
