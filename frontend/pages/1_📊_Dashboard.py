"""Dashboard page for data visualization and metrics."""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime, timedelta
from frontend.services.api_client import APIClient


def main() -> None:
    """Main dashboard page function."""
    st.set_page_config(page_title="Dashboard - Streamlit FastAPI", page_icon="📊" layout="wide")

    st.title("📊 Analytics Dashboard")
    st.markdown("Real-time data visualization and key performance indicators")

    # API Status Check
    api_client = APIClient()

    with st.sidebar:
        st.header("🔧 Controls")

        # Refresh button
        if st.button("🔄 Refresh Data", type="primary"):
            st.cache_data.clear()
            st.rerun()

        # Date range selector
        date_range = st.date_input(
            "📅 Date Range",
            value=(datetime.now() - timedelta(days=30), datetime.now()),
            max_value=datetime.now(),
        )

        # Metrics selector
        selected_metrics = st.multiselect(
            "📈 Metrics to Display",
            options=["Revenue", "Users", "Sessions", "Conversion Rate"],
            default=["Revenue", "Users"],
        )

    # Main dashboard content
    col1, col2, col3, col4 = st.columns(4)

    # KPI Cards
    with col1:
        st.metric(
            label="💰 Revenue" value="$45,231", delta="↗️ +12.5%", help="Total revenue for selected period"
        )

    with col2:
        st.metric(label="👥 Active Users" value="1,234", delta="↗️ +8.2%", help="Number of active users")

    with col3:
        st.metric(
            label="📊 Sessions",
            value="8,456",
            delta="↘️ -2.1%",
            help="Total sessions count",
            delta_color="inverse",
        )

    with col4:
        st.metric(label="🎯 Conversion" value="3.42%", delta="↗️ +0.8%", help="Conversion rate percentage")

    st.markdown("---")

    # Charts Section
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Revenue Trend")

        # Generate sample revenue data
        dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq="D")
        revenue_data = pd.DataFrame(
            {
                "Date": dates,
                "Revenue": np.cumsum(np.random.normal(1500, 300, len(dates))) + 10000,
                "Target": np.linspace(25000, 35000, len(dates)),
            }
        )

        fig_revenue = px.line(
            revenue_data,
            x="Date",
            y=["Revenue", "Target"],
            title="Daily Revenue vs Target",
            color_discrete_map={"Revenue": "#1f77b4", "Target": "#ff7f0e"},
        )
        fig_revenue.update_layout(height=400)
        st.plotly_chart(fig_revenue, use_container_width=True)

    with col2:
        st.subheader("👥 User Acquisition")

        # Generate sample user data
        channels = ["Organic", "Paid Search", "Social Media", "Email", "Direct"]
        users = np.random.randint(100, 1000, len(channels))

        fig_users = px.pie(values=users, names=channels, title="Users by Acquisition Channel")
        fig_users.update_layout(height=400)
        st.plotly_chart(fig_users, use_container_width=True)

    # Detailed Analytics Section
    st.subheader("📋 Detailed Analytics")

    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["📊 Performance", "🌍 Geography", "🕒 Real-time"])

    with tab1:
        # Performance metrics table
        performance_data = pd.DataFrame(
            {
                "Metric": ["Page Views", "Unique Visitors", "Bounce Rate", "Avg. Session Duration"],
                "Current": ["125,456", "45,123", "32.5%", "4m 32s"],
                "Previous": ["118,234", "42,567", "35.1%", "4m 12s"],
                "Change": ["+6.1%", "+6.0%", "-7.4%", "+4.8%"],
            }
        )
        st.dataframe(performance_data, use_container_width=True)

        # Performance trend chart
        perf_dates = pd.date_range(start=datetime.now() - timedelta(days=7), periods=7)
        perf_data = pd.DataFrame(
            {
                "Date": perf_dates,
                "Page Views": np.random.randint(15000, 25000, 7),
                "Sessions": np.random.randint(8000, 15000, 7),
                "Users": np.random.randint(5000, 12000, 7),
            }
        )

        fig_perf = px.line(
            perf_data, x="Date", y=["Page Views", "Sessions", "Users"], title="7-Day Performance Trend"
        )
        st.plotly_chart(fig_perf, use_container_width=True)

    with tab2:
        st.info("🚧 Geographic analytics coming soon!")

        # Placeholder for geographic data
        countries = ["United States", "Canada", "United Kingdom", "Germany", "France"]
        visits = np.random.randint(1000, 10000, len(countries))

        geo_data = pd.DataFrame(
            {
                "Country": countries,
                "Visits": visits,
                "Revenue": visits * np.random.uniform(2, 8, len(countries)),
            }
        )

        st.dataframe(geo_data, use_container_width=True)

    with tab3:
        # Real-time metrics
        st.subheader("⚡ Real-time Activity")

        # Simulated real-time data
        realtime_col1, realtime_col2, realtime_col3 = st.columns(3)

        with realtime_col1:
            st.metric("🔴 Active Users", "127", "↗️ +5")

        with realtime_col2:
            st.metric("📄 Page Views/min", "2,345", "↗️ +12")

        with realtime_col3:
            st.metric("💸 Revenue/hour", "$1,245", "↗️ +$67")

        # Activity feed
        st.subheader("📱 Recent Activity")
        activity_data = [
            {"time": "2 min ago", "event": "New user registration", "details": "user@example.com"},
            {"time": "3 min ago", "event": "Purchase completed", "details": "$129.99"},
            {"time": "5 min ago", "event": "Page view", "details": "/products/premium"},
            {"time": "7 min ago", "event": "User login", "details": "john.doe@email.com"},
        ]

        for activity in activity_data:
            with st.container():
                st.write(f"**{activity['time']}** - {activity['event']}")
                st.caption(activity["details"])
                st.markdown("---")

    # API Health Status
    with st.expander("🔗 API Status"):
        try:
            health_data = api_client.get_detailed_health()
            if health_data["status"] == "healthy":
                st.success("✅ API is healthy and responding")
            else:
                st.warning("⚠️ API health check shows issues")

            st.json(health_data)
        except Exception as e:
            st.error(f"❌ Cannot connect to API: {e}")


if __name__ == "__main__":
    main()
