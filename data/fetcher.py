# data/fetcher.py
# Handles all FRED API calls and caching logic
# All other files get their data from here

import os
import pandas as pd
from datetime import datetime, timedelta
from fredapi import Fred
from dotenv import load_dotenv
import ssl
import certifi
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())


# load environment variables from .env
load_dotenv()

# Initalize FRED Client
def get_fred_client():
    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        raise ValueError("FRED_API_KEY not found. Check your .env file.")
    return Fred(api_key=api_key)

# Fetch a single series from FRED
def fetch_series(series_id: str, start_date: str, end_date: str) -> pd.DataFrame:

    """
    Fetch a single FRED series and return as a clean DataFrame.
    
    Args:
        series_id:  FRED series ID (e.g. 'DGS10')
        start_date: 'YYYY-MM-DD'
        end_date:   'YYYY-MM-DD'
    
    Returns:
        DataFrame with columns ['date', 'value']
    """
    try:
        fred = get_fred_client()
        data = fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
        df = data.reset_index()
        df.columns = ["date", "value"]
        df["date"] = pd.to_datetime(df["date"])
        df = df.dropna(subset = ["value"])
        return df
    except Exception as e:
        print(f"Error fetching {series_id}: {e}")
        return pd.DataFrame(columns=["date", "value"])
    

# Fetch all series at once 
def fetch_all_rates(series_dict: dict, lookback_years: int = 5) -> dict:
    
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=365 * lookback_years)).strftime("%Y-%m-%d")

    results = {}
    for label, series_id in series_dict.items():
        df = fetch_series(series_id, start_date, end_date)
        results[label] = df

    return results

# Get the most recent value for a series
def get_latest_value(df: pd.DataFrame) -> tuple:

    if df.empty:
        return None, None
    latest = df.sort_values("date").iloc[-1]
    return latest["date"].strftime("%Y-%m-%d"), round(latest["value"], 2)


# Get Current Rate Summary
def get_current_rates(all_data: dict) -> pd.DataFrame:

    rows = []
    for label, df in all_data.items():
        date, value = get_latest_value(df)
        rows.append({
            "Rate": label,
            "Current Value": f"{value}%" if value is not None else "N/A",
            "As of Date": date if date else "N/A"
        })
    return pd.DataFrame(rows)

# Standalone test 
if __name__ == "__main__":
    from config import FRED_SERIES, DEFAULT_LOOKBACK_YEARS

    print("Fetching all rates from FRED...")
    all_data = fetch_all_rates(FRED_SERIES, DEFAULT_LOOKBACK_YEARS)

    for label, df in all_data.items():
        date, value = get_latest_value(df)
        print(f"  {label:<20} {value}%  (as of {date})")

    print("\nDone.")
