"""Tests for health check endpoints."""

from fastapi.testclient import TestClient


def test_health_check(client: TestClient) -> None:
    """Test basic health check endpoint."""
    response = client.get("/api/v1/health/")

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data
    assert "environment" in data


def test_detailed_health_check(client: TestClient) -> None:
    """Test detailed health check endpoint."""
    response = client.get("/api/v1/health/detailed")

    assert response.status_code == 200

    data = response.json()
    assert data["status"] in ["healthy", "unhealthy"]
    assert "timestamp" in data
    assert "version" in data
    assert "environment" in data
    assert "services" in data
    assert isinstance(data["services"], dict)


def test_readiness_check(client: TestClient) -> None:
    """Test Kubernetes readiness probe."""
    response = client.get("/api/v1/health/ready")

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ready"


def test_liveness_check(client: TestClient) -> None:
    """Test Kubernetes liveness probe."""
    response = client.get("/api/v1/health/live")

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "alive"
