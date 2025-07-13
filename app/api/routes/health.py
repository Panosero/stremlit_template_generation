"""Health check endpoints for monitoring application status."""

from app.dependencies import SettingsDep
from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    timestamp: datetime
    version: str
    environment: str
    uptime: str | None = None


class DetailedHealthResponse(BaseModel):
    """Detailed health check response model."""

    status: str
    timestamp: datetime
    version: str
    environment: str
    uptime: str | None = None
    services: dict[str, Any]


@router.get("/", response_model=HealthResponse)
async def health_check(settings: SettingsDep) -> HealthResponse:
    """Basic health check endpoint.

    Returns:
        HealthResponse: Basic health status information.
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version=settings.app_version,
        environment=settings.environment,
    )


@router.get("/detailed", response_model=DetailedHealthResponse)
async def detailed_health_check(settings: SettingsDep) -> DetailedHealthResponse:
    """Detailed health check endpoint with service status.

    Returns:
        DetailedHealthResponse: Detailed health status with service information.
    """
    # Check database connectivity
    database_status = await _check_database_health()

    services = {
        "database": database_status,
        "api": {"status": "healthy", "details": "API is responding"},
    }

    # Determine overall status
    overall_status = (
        "healthy" if all(service.get("status") == "healthy" for service in services.values()) else "unhealthy"
    )

    return DetailedHealthResponse(
        status=overall_status,
        timestamp=datetime.utcnow(),
        version=settings.app_version,
        environment=settings.environment,
        services=services,
    )


@router.get("/ready")
async def readiness_check() -> dict[str, str]:
    """Kubernetes readiness probe endpoint.

    Returns:
        dict[str, str]: Readiness status.
    """
    return {"status": "ready"}


@router.get("/live")
async def liveness_check() -> dict[str, str]:
    """Kubernetes liveness probe endpoint.

    Returns:
        dict[str, str]: Liveness status.
    """
    return {"status": "alive"}


async def _check_database_health() -> dict[str, Any]:
    """Check database connectivity.

    Returns:
        dict[str, Any]: Database health status.
    """
    try:
        # Import here to avoid circular imports
        from app.database.connection import async_engine

        async with async_engine.connect() as conn:
            await conn.execute("SELECT 1")

        return {
            "status": "healthy",
            "details": "Database connection successful",
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "details": f"Database connection failed: {str(e)}",
        }
