"""Application configuration using Pydantic Settings."""

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application Settings
    app_name: str = Field(default="StreamlitFastAPITemplate", description="Application name")
    app_version: str = Field(default="1.0.0", description="Application version")
    debug: bool = Field(default=False, description="Debug mode")
    environment: str = Field(
        default="development", description="Environment (development/staging/production)"
    )

    # API Configuration
    api_host: str = Field(default="localhost", description="API host")
    api_port: int = Field(default=8000, description="API port")
    api_prefix: str = Field(default="/api/v1", description="API prefix")

    # Frontend Configuration
    frontend_host: str = Field(default="localhost", description="Frontend host")
    frontend_port: int = Field(default=8501, description="Frontend port")
    frontend_title: str = Field(default="Streamlit FastAPI App", description="Frontend title")

    # Database Configuration
    database_url: str = Field(default="sqlite+aiosqlite:///./app.db", description="Database URL")
    database_echo: bool = Field(default=False, description="Echo SQL queries")

    # Security Settings
    secret_key: str = Field(
        default="your-super-secret-key-change-in-production-min-32-chars", description="Secret key for JWT"
    )
    algorithm: str = Field(default="HS256", description="JWT algorithm")
    access_token_expire_minutes: int = Field(
        default=30, description="Access token expiration time in minutes"
    )

    # CORS Settings
    allowed_origins: list[str] = Field(
        default=["http://localhost:8501", "http://127.0.0.1:8501"], description="Allowed CORS origins"
    )
    allowed_methods: list[str] = Field(
        default=["GET", "POST", "PUT", "DELETE"], description="Allowed HTTP methods"
    )
    allowed_headers: list[str] = Field(default=["*"], description="Allowed headers")

    # Logging Configuration
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: str = Field(default="json", description="Log format (json/text)")

    # Rate Limiting
    rate_limit_enabled: bool = Field(default=True, description="Enable rate limiting")
    rate_limit_requests: int = Field(default=100, description="Rate limit requests per window")
    rate_limit_window: int = Field(default=60, description="Rate limit window in seconds")

    # Monitoring
    health_check_interval: int = Field(default=30, description="Health check interval in seconds")
    metrics_enabled: bool = Field(default=True, description="Enable metrics collection")

    @property
    def is_development(self) -> bool:
        """Check if the application is running in development mode."""
        return self.environment == "development"

    @property
    def is_production(self) -> bool:
        """Check if the application is running in production mode."""
        return self.environment == "production"

    @property
    def api_url(self) -> str:
        """Get the full API URL."""
        return f"http://{self.api_host}:{self.api_port}"

    @property
    def frontend_url(self) -> str:
        """Get the full frontend URL."""
        return f"http://{self.frontend_host}:{self.frontend_port}"


@lru_cache
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()
