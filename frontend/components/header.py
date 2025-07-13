"""Header component for the Streamlit application."""

import streamlit as st
from frontend.config import get_frontend_settings


def render_header() -> None:
    """Render the application header.

    Displays the application title, navigation, and theme toggle.
    """
    settings = get_frontend_settings()

    # Create header container
    header_container = st.container()

    with header_container:
        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            st.markdown(
                f"""
                # {settings.app_icon} {settings.app_title}
                *Production-ready Streamlit + FastAPI template*
                """,
            )

        with col2:
            # API status indicator
            if st.button("🔗 API Status", help="Check API connectivity"):
                _show_api_status()

        with col3:
            # Theme toggle (if enabled)
            if settings.enable_dark_mode:
                _render_theme_toggle()

    # Add separator
    st.markdown("---")


def _show_api_status() -> None:
    """Show API status in a popup."""
    try:
        from frontend.services.api_client import APIClient

        api_client = APIClient()
        health_data = api_client.get_health()

        st.success("✅ API is online and healthy!")
        with st.expander("API Details"):
            st.json(health_data)

    except Exception as e:
        st.error(f"❌ API is not responding: {e}")


def _render_theme_toggle() -> None:
    """Render theme toggle control."""
    # Note: Streamlit doesn't support dynamic theme switching yet
    # This is a placeholder for future functionality
    theme_mode = st.selectbox(
        "🎨 Theme",
        options=["Light", "Dark", "Auto"],
        index=0,
        help="Theme selection (placeholder for future feature)",
    )

    if theme_mode != "Light":
        st.info("🚧 Theme switching coming soon!")
