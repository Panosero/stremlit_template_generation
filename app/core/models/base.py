"""Base Pydantic models for common functionality."""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any


class BaseAPIModel(BaseModel):
    """Base model for API requests and responses."""

    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
        use_enum_values=True,
    )


class TimestampMixin(BaseModel):
    """Mixin for models with timestamp fields."""

    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")


class PaginationParams(BaseModel):
    """Pagination parameters for list endpoints."""

    page: int = Field(default=1, ge=1, description="Page number (1-based)")
    size: int = Field(default=10, ge=1, le=100, description="Page size (1-100)")

    @property
    def offset(self) -> int:
        """Calculate offset for database queries."""
        return (self.page - 1) * self.size


class PaginatedResponse(BaseAPIModel):
    """Generic paginated response model."""

    items: list[Any] = Field(description="List of items")
    total: int = Field(description="Total number of items")
    page: int = Field(description="Current page number")
    size: int = Field(description="Page size")
    pages: int = Field(description="Total number of pages")

    @classmethod
    def create(
        cls,
        items: list[Any],
        total: int,
        page: int,
        size: int,
    ) -> "PaginatedResponse":
        """Create paginated response.

        Args:
            items: List of items for current page.
            total: Total number of items.
            page: Current page number.
            size: Page size.

        Returns:
            PaginatedResponse: Paginated response instance.
        """
        pages = (total + size - 1) // size if total > 0 else 0
        return cls(
            items=items,
            total=total,
            page=page,
            size=size,
            pages=pages,
        )
