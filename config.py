# config.py
# Central Configurations for CRE Rates Dashboard
# Add, remove, or rename rates here without touching other files

# --- FRED Series IDs ------------------
FRED_SERIES = {
    "SOFR":             "SOFR",
    "Fed Funds Rate":   "DFF",
    "Prime Rate":       "DPRIME",
    "2yr Treasury":     "DGS2",
    "3yr Treasury":     "DGS3",
    "5yr Treasury":     "DGS5",
    "10yr Treasury":    "DGS10",
    "2s10s Spread":     "T10Y2Y",
    "10Y-3M Spread":    "T10Y3M"
}

# --- Chart Colors ---------------------
COLORS = {
    "SOFR": "#2196F3",
    "Fed Funds Rate":     "#9C27B0",
    "Prime Rate":         "#FF9800",
    "2yr Treasury":       "#09540B",
    "3yr Treasury":       "#8BC34A",
    "5yr Treasury":       "#FFEB3B",
    "10yr Treasury":      "#F44336",
    "2s10s Spread":       "#00BCD4",
    "10Y-3M Spread":      "#E91E63"
}

# --- Grouping (for chart organization)---------
RATE_GROUPS = {
    "Benchmark Rates": ["SOFR", "Fed Funds Rate", "Prime Rate"],
    "Treasury Yields": ["2yr Treasury", "3yr Treasury", "5yr Treasury", "10yr Treasury"],
    "Spreads":         ["2s10s Spread", "10Y-3M Spread"]
}

# --- Default Date Range -----------------------
DEFAULT_LOOKBACK_YEARS = 5

# --- Cache Settings ---------------------------
CACHE_TTL_SECONDS = 86400

# --- Display Settings -------------------------
DECIMAL_PLACES = 2
RATE_SUFFIX = "%"