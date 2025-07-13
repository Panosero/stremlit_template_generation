"""Sidebar component for navigation and controls."""

import streamlit as st
from frontend.config import get_frontend_settings


def render_sidebar() -> None:
    """Render the application sidebar with navigation and controls."""
    settings = get_frontend_settings()

    # Logo/branding area
    st.markdown(
        f"""
        <div style='text-align: center; padding: 1rem 0;'>
            <h2>{settings.app_icon} {settings.app_title}</h2>
            <p style='color: #666; font-size: 0.9em;'>v1.0.0</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Navigation menu
    st.subheader("📋 Navigation")

    # Main pages
    page_options = {
        "🏠 Home": "main",
        "📊 Dashboard": "dashboard",
        "👤 Users": "users",
        "📦 Items": "items",
        "⚙️ Settings": "settings",
    }

    selected_page = st.selectbox(
        "Select a page:",
        options=list(page_options.keys()),
        index=0,
        key="page_selector",
    )

    # Store selection in session state
    st.session_state.selected_page = page_options[selected_page]

    st.markdown("---")

    # Quick actions
    st.subheader("🚀 Quick Actions")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Refresh", help="Refresh data"):
            st.rerun()

    with col2:
        if st.button("📥 Export", help="Export data"):
            st.info("Export functionality coming soon!")

    st.markdown("---")

    # System information
    st.subheader("ℹ️ System Info")

    # API connection status
    _show_connection_status()

    # Settings
    if settings.show_debug_info:
        with st.expander("🐛 Debug Info"):
            st.json(
                {
                    "API URL": settings.api_url,
                    "Theme": "Light",  # Placeholder
                    "Session ID": st.session_state.get("session_id", "N/A"),
                    "Cache Status": "Enabled" if settings.enable_caching else "Disabled",
                }
            )

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; font-size: 0.8em; color: #666;'>
            <p>Built with ❤️<br/>Streamlit + FastAPI</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _show_connection_status() -> None:
    """Show API connection status indicator."""
    try:
        from frontend.services.api_client import APIClient

        api_client = APIClient()
        health_data = api_client.get_health()

        st.success("🟢 API Connected")

        if st.button("📋 View Details", key="api_details"):
            st.json(health_data)

    except Exception:
        st.error("🔴 API Disconnected")

        if st.button("🔄 Retry Connection", key="retry_connection"):
            st.rerun()
