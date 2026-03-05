# app.py
# CRE Rates Dashboard
# Main entry point — assembles all components and runs the Streamlit app

import ssl
import certifi
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

import streamlit as st
from config import FRED_SERIES, DEFAULT_LOOKBACK_YEARS
from data.fetcher import fetch_all_rates, get_current_rates
from components.sidebar import render_sidebar
from components.metrics import render_rate_cards, render_summary_table
from components.charts import render_history_chart, render_yield_curve, render_spread_chart


# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CRE Rates Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
        .main { background-color: #0E0E0E; }
        .block-container { padding-top: 1.5rem; }
        h1 { color: #FFFFFF; }
        h2, h3 { color: #DDDDDD; }
    </style>
""", unsafe_allow_html=True)


# ── Header ─────────────────────────────────────────────────────────────────────
st.title("📊 CRE Rates Dashboard")
st.caption("Live rate data sourced from the Federal Reserve (FRED). Refreshes every 24 hours.")
st.markdown("---")


# ── Sidebar Controls ───────────────────────────────────────────────────────────
controls = render_sidebar()


# ── Fetch Data ─────────────────────────────────────────────────────────────────
with st.spinner("Loading rate data from FRED..."):
    all_data = fetch_all_rates(FRED_SERIES, controls["lookback_years"])


# ── Current Rate Cards ─────────────────────────────────────────────────────────
current_rates_df = get_current_rates(all_data)
render_rate_cards(current_rates_df)
st.markdown("---")


# ── Historical Chart ───────────────────────────────────────────────────────────
if controls["selected_rates"]:
    render_history_chart(all_data, controls["selected_rates"])
else:
    st.info("Select at least one rate from the sidebar to display the chart.")

st.markdown("---")


# ── Yield Curve ────────────────────────────────────────────────────────────────
if controls["show_yield_curve"]:
    render_yield_curve(all_data)
    st.markdown("---")


# ── Spread Chart ───────────────────────────────────────────────────────────────
if controls["show_spreads"]:
    render_spread_chart(all_data)
    st.markdown("---")


# ── Summary Table ──────────────────────────────────────────────────────────────
render_summary_table(current_rates_df)