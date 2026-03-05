# components/charts.py
# Renders all Plotly charts for the dashboard

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from config import RATE_GROUPS, COLORS


def render_history_chart(all_data: dict, selected_rates: list):
    """
    Renders a multi-line historical chart for selected rates.

    Args:
        all_data:       dict of {rate_label: DataFrame with ['date', 'value']}
        selected_rates: list of rate labels to plot
    """
    fig = go.Figure()

    for rate_name in selected_rates:
        df = all_data.get(rate_name)
        if df is None or df.empty:
            continue

        fig.add_trace(go.Scatter(
            x=df["date"],
            y=df["value"],
            name=rate_name,
            mode="lines",
            line=dict(color=COLORS.get(rate_name, "#FFFFFF"), width=2),
            hovertemplate=f"<b>{rate_name}</b><br>Date: %{{x|%Y-%m-%d}}<br>Rate: %{{y:.2f}}%<extra></extra>"
        ))

    fig.update_layout(
        title="Historical Rate Trends",
        xaxis_title="Date",
        yaxis_title="Rate (%)",
        template="plotly_dark",
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        height=500,
        margin=dict(l=40, r=40, t=60, b=40),
    )

    st.plotly_chart(fig, use_container_width=True)


def render_yield_curve(all_data: dict):
    """
    Renders a snapshot yield curve chart using the most recent values
    for the 2yr, 3yr, 5yr, and 10yr Treasuries.

    Args:
        all_data: dict of {rate_label: DataFrame with ['date', 'value']}
    """
    tenors = {
        "2yr Treasury":  2,
        "3yr Treasury":  3,
        "5yr Treasury":  5,
        "10yr Treasury": 10,
    }

    maturities = []
    yields     = []
    labels     = []

    for label, years in tenors.items():
        df = all_data.get(label)
        if df is not None and not df.empty:
            latest_value = df.sort_values("date").iloc[-1]["value"]
            maturities.append(years)
            yields.append(round(latest_value, 2))
            labels.append(label)

    if not maturities:
        st.warning("No Treasury data available for yield curve.")
        return

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=maturities,
        y=yields,
        mode="lines+markers",
        line=dict(color="#2196F3", width=3),
        marker=dict(size=10, color="#2196F3"),
        text=labels,
        hovertemplate="<b>%{text}</b><br>Maturity: %{x}yr<br>Yield: %{y:.2f}%<extra></extra>"
    ))

    fig.update_layout(
        title="Current Yield Curve",
        xaxis=dict(
            title="Maturity (Years)",
            tickvals=maturities,
            ticktext=[f"{m}yr" for m in maturities],
        ),
        yaxis_title="Yield (%)",
        template="plotly_dark",
        height=400,
        margin=dict(l=40, r=40, t=60, b=40),
    )

    st.plotly_chart(fig, use_container_width=True)


def render_spread_chart(all_data: dict):
    """
    Renders a historical chart focused on spreads only.

    Args:
        all_data: dict of {rate_label: DataFrame with ['date', 'value']}
    """
    spread_rates = RATE_GROUPS.get("Spreads", [])

    fig = go.Figure()

    for rate_name in spread_rates:
        df = all_data.get(rate_name)
        if df is None or df.empty:
            continue

        fig.add_trace(go.Scatter(
            x=df["date"],
            y=df["value"],
            name=rate_name,
            mode="lines",
            line=dict(color=COLORS.get(rate_name, "#FFFFFF"), width=2),
            hovertemplate=f"<b>{rate_name}</b><br>Date: %{{x|%Y-%m-%d}}<br>Spread: %{{y:.2f}}%<extra></extra>"
        ))

    # Add a zero line for reference
    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="gray",
        annotation_text="Zero",
        annotation_position="bottom right"
    )

    fig.update_layout(
        title="Spread History",
        xaxis_title="Date",
        yaxis_title="Spread (%)",
        template="plotly_dark",
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        height=400,
        margin=dict(l=40, r=40, t=60, b=40),
    )

    st.plotly_chart(fig, use_container_width=True)