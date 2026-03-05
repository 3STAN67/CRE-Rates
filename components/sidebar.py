# components/sidebar.py
# Renders the sidebar controls for the dashboard
# Returns user selections back to app.py

import streamlit as st
from datetime import datetime, timedelta
from config import FRED_SERIES, RATE_GROUPS, DEFAULT_LOOKBACK_YEARS


def render_sidebar() -> dict:
    """
    Renders the sidebar with all dashboard controls.

    Returns:
        dict with keys:
            - lookback_years:   int
            - start_date:       datetime
            - end_date:         datetime
            - selected_rates:   list of rate label strings
            - show_yield_curve: bool
            - show_spreads:     bool
    """
    st.sidebar.title("⚙️ Dashboard Controls")
    st.sidebar.markdown("---")

    # ── Date Range ─────────────────────────────────────────────────────────────
    st.sidebar.subheader("📅 Date Range")

    lookback_years = st.sidebar.selectbox(
        "Lookback Period",
        options=[1, 2, 3, 5, 10],
        index=[1, 2, 3, 5, 10].index(DEFAULT_LOOKBACK_YEARS),
        format_func=lambda x: f"{x} Year{'s' if x > 1 else ''}"
    )

    end_date   = datetime.today()
    start_date = end_date - timedelta(days=365 * lookback_years)

    st.sidebar.caption(f"From {start_date.strftime('%b %d, %Y')} → {end_date.strftime('%b %d, %Y')}")
    st.sidebar.markdown("---")

    # ── Rate Selection ─────────────────────────────────────────────────────────
    st.sidebar.subheader("📈 Select Rates to Chart")

    selected_rates = []

    for group_name, group_rates in RATE_GROUPS.items():
        st.sidebar.markdown(f"**{group_name}**")
        for rate in group_rates:
            # Default: all rates selected
            checked = st.sidebar.checkbox(rate, value=True, key=f"cb_{rate}")
            if checked:
                selected_rates.append(rate)

    st.sidebar.markdown("---")

    # ── Chart Options ──────────────────────────────────────────────────────────
    st.sidebar.subheader("🔧 Chart Options")

    show_yield_curve = st.sidebar.toggle("Show Yield Curve", value=True)
    show_spreads     = st.sidebar.toggle("Show Spread Chart", value=True)

    st.sidebar.markdown("---")

    # ── Last Updated ───────────────────────────────────────────────────────────
    st.sidebar.caption(f"Data refreshes every 24 hours.")
    st.sidebar.caption(f"Last loaded: {datetime.now().strftime('%b %d, %Y %I:%M %p')}")

    return {
        "lookback_years":   lookback_years,
        "start_date":       start_date,
        "end_date":         end_date,
        "selected_rates":   selected_rates,
        "show_yield_curve": show_yield_curve,
        "show_spreads":     show_spreads,
    }