# components/metrics.py
# Renders current rate metric cards and summary table for the dashboard 

import streamlit as st
import pandas as pd
from config import RATE_GROUPS, COLORS

def render_rate_cards(current_rates_df: pd.DataFrame):
    """
    Renders a row of metric cards showing the current value of each rate.
    Organized by group (Benchmark Rates, Treasury Yields, Spreads).

    Args:
        current_rates_df: DataFrame with columns ['Rate', 'Current Value', 'As Of Date']
    """
    for group_name, group_rates in RATE_GROUPS.items():
        st.subheader(group_name)

        cols = st.columns(len(group_rates))

        for col, rate_name in zip(cols, group_rates):
            # Look up this rate in the DataFrame
            row = current_rates_df[current_rates_df["Rate"] == rate_name]

            if not row.empty:
                value   = row["Current Value"].values[0]
                as_of   = row["As of Date"].values[0]
                color   = COLORS.get(rate_name, "#FFFFFF")

                with col:
                    st.markdown(
                        f"""
                        <div style="
                            background-color: #1E1E1E;
                            border-left: 4px solid {color};
                            border-radius: 8px;
                            padding: 16px;
                            margin-bottom: 8px;
                        ">
                            <div style="color: #AAAAAA; font-size: 12px;">{rate_name}</div>
                            <div style="color: #FFFFFF; font-size: 28px; font-weight: bold;">{value}</div>
                            <div style="color: #666666; font-size: 11px;">As of {as_of}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                with col:
                    st.metric(label=rate_name, value="N/A")


def render_summary_table(current_rates_df: pd.DataFrame):
    """
    Renders a clean summary table of all current rates.

    Args:
        current_rates_df: DataFrame with columns ['Rate', 'Current Value', 'As Of Date']
    """
    st.subheader("All Current Rates")
    st.dataframe(
        current_rates_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Rate":          st.column_config.TextColumn("Rate",          width="medium"),
            "Current Value": st.column_config.TextColumn("Current Value", width="small"),
            "As Of Date":    st.column_config.TextColumn("As Of Date",    width="medium"),
        }
    )
