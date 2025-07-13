"""Main Streamlit application entry point."""

import streamlit as st
from frontend.components.header import render_header
from frontend.components.sidebar import render_sidebar
from frontend.config import get_frontend_settings

# Configure page
settings = get_frontend_settings()
st.set_page_config(**settings.get_page_config())

# Apply custom CSS for theme
st.markdown(
    """
    <style>
    .main {
        padding-top: 1rem;
    }
    .stApp > header {
        background-color: transparent;
    }
    .css-1d391kg {
        padding-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main() -> None:
    """Main application function."""
    # Render header
    render_header()

    # Render sidebar
    with st.sidebar:
        render_sidebar()

    # Main content area
    st.title("🏠 Welcome to Your Streamlit App")

    col1, col2 = st.columns(2)

    with col1:
        st.header("🚀 Quick Start")
        st.write(
            """
        This is your production-ready Streamlit + FastAPI template!
        
        **Features:**
        - 🔧 Modern Python tooling with UV
        - 🎨 Clean architecture
        - 📊 Interactive dashboards
        - 🔌 FastAPI backend integration
        - 🧪 Comprehensive testing
        - 🐳 Docker support
        """
        )

        if st.button("🔍 Check API Health", type="primary"):
            from frontend.services.api_client import APIClient

            api_client = APIClient()
            try:
                health_data = api_client.get_health()
                st.success("✅ API is healthy!")
                st.json(health_data)
            except Exception as e:
                st.error(f"❌ API health check failed: {e}")

    with col2:
        st.header("📊 Quick Stats")

        # Example metrics
        col2a, col2b, col2c = st.columns(3)

        with col2a:
            st.metric(
                label="API Status",
                value="🟢 Online",
                delta="Healthy",
            )

        with col2b:
            st.metric(
                label="Users",
                value="1,234",
                delta="↗️ +12%",
            )

        with col2c:
            st.metric(
                label="Requests",
                value="45.6K",
                delta="↗️ +8%",
            )

        # Example chart
        st.subheader("📈 Sample Data")

        import numpy as np
        import pandas as pd

        # Generate sample data
        dates = pd.date_range("2024-01-01", periods=30)
        values = np.cumsum(np.random.randn(30)) + 100

        chart_data = pd.DataFrame(
            {
                "Date": dates,
                "Value": values,
            }
        )

        st.line_chart(chart_data.set_index("Date"))

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Built with ❤️ using Streamlit + FastAPI Template</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
