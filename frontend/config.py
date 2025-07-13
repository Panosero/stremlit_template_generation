"""Frontend configuration settings."""

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Any


class FrontendSettings(BaseSettings):
    """Frontend-specific settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application Settings
    app_title: str = Field(default="Streamlit FastAPI App", description="Application title")
    app_icon: str = Field(default="🚀", description="Application icon")

    # API Configuration
    api_base_url: str = Field(default="http://localhost:8000", description="API base URL")
    api_prefix: str = Field(default="/api/v1", description="API prefix")

    # UI Configuration
    layout: str = Field(default="wide", description="Streamlit layout")
    sidebar_state: str = Field(default="expanded", description="Sidebar initial state")

    # Theme Configuration
    primary_color: str = Field(default="#FF6B6B", description="Primary theme color")
    background_color: str = Field(default="#FFFFFF", description="Background color")
    secondary_background_color: str = Field(default="#F0F2F6", description="Secondary background color")
    text_color: str = Field(default="#262730", description="Text color")

    # Feature Flags
    enable_dark_mode: bool = Field(default=True, description="Enable dark mode toggle")
    enable_caching: bool = Field(default=True, description="Enable Streamlit caching")
    show_debug_info: bool = Field(default=False, description="Show debug information")

    @property
    def api_url(self) -> str:
        """Get full API URL with prefix."""
        return f"{self.api_base_url}{self.api_prefix}"

    def get_page_config(self) -> dict[str, Any]:
        """Get Streamlit page configuration.

        Returns:
            dict[str, Any]: Page configuration for st.set_page_config.
        """
        return {
            "page_title": self.app_title,
            "page_icon": self.app_icon,
            "layout": self.layout,
            "initial_sidebar_state": self.sidebar_state,
        }

    def get_theme_config(self) -> dict[str, str]:
        """Get theme configuration.

        Returns:
            dict[str, str]: Theme configuration.
        """
        return {
            "primaryColor": self.primary_color,
            "backgroundColor": self.background_color,
            "secondaryBackgroundColor": self.secondary_background_color,
            "textColor": self.text_color,
        }


@lru_cache
def get_frontend_settings() -> FrontendSettings:
    """Get cached frontend settings."""
    return FrontendSettings()
