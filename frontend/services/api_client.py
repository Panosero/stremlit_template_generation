"""API client for communicating with the FastAPI backend."""

import httpx
import streamlit as st
from frontend.config import get_frontend_settings
from typing import Any


class APIClient:
    """HTTP client for API communication."""

    def __init__(self) -> None:
        """Initialize the API client."""
        self.settings = get_frontend_settings()
        self.base_url = self.settings.api_url
        self.timeout = 30.0

    @st.cache_data(ttl=30)
    def get_health(self) -> dict[str, Any]:
        """Get API health status.

        Returns:
            dict[str, Any]: Health status data.

        Raises:
            Exception: If API request fails.
        """
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.get(f"{self.base_url}/health/")
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            raise Exception(f"Connection error: {e}") from e
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error {e.response.status_code}: {e.response.text}") from e

    @st.cache_data(ttl=30)
    def get_detailed_health(self) -> dict[str, Any]:
        """Get detailed API health status.

        Returns:
            dict[str, Any]: Detailed health status data.

        Raises:
            Exception: If API request fails.
        """
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.get(f"{self.base_url}/health/detailed")
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            raise Exception(f"Connection error: {e}") from e
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error {e.response.status_code}: {e.response.text}") from e

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """Make a GET request to the API.

        Args:
            endpoint: API endpoint (without base URL).
            params: Query parameters.

        Returns:
            dict[str, Any]: Response data.

        Raises:
            Exception: If API request fails.
        """
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.get(
                    f"{self.base_url}/{endpoint.lstrip('/')}",
                    params=params or {},
                )
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            raise Exception(f"Connection error: {e}") from e
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error {e.response.status_code}: {e.response.text}") from e

    def post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        json_data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make a POST request to the API.

        Args:
            endpoint: API endpoint (without base URL).
            data: Form data.
            json_data: JSON data.

        Returns:
            dict[str, Any]: Response data.

        Raises:
            Exception: If API request fails.
        """
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(
                    f"{self.base_url}/{endpoint.lstrip('/')}",
                    data=data,
                    json=json_data,
                )
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            raise Exception(f"Connection error: {e}") from e
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error {e.response.status_code}: {e.response.text}") from e

    def put(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        json_data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make a PUT request to the API.

        Args:
            endpoint: API endpoint (without base URL).
            data: Form data.
            json_data: JSON data.

        Returns:
            dict[str, Any]: Response data.

        Raises:
            Exception: If API request fails.
        """
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.put(
                    f"{self.base_url}/{endpoint.lstrip('/')}",
                    data=data,
                    json=json_data,
                )
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            raise Exception(f"Connection error: {e}") from e
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error {e.response.status_code}: {e.response.text}") from e

    def delete(self, endpoint: str) -> dict[str, Any]:
        """Make a DELETE request to the API.

        Args:
            endpoint: API endpoint (without base URL).

        Returns:
            dict[str, Any]: Response data.

        Raises:
            Exception: If API request fails.
        """
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.delete(f"{self.base_url}/{endpoint.lstrip('/')}")
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            raise Exception(f"Connection error: {e}") from e
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error {e.response.status_code}: {e.response.text}") from e


# Global API client instance
api_client = APIClient()
