# 📊 CRE Rates Dashboard

A live interest rate tracking dashboard built with Streamlit, pulling daily data from the Federal Reserve (FRED API). Tracks SOFR, Treasury yields, spreads, and the Fed Funds Rate — all in one place.

---

## 🚀 Live Demo

> Deployed on Streamlit Community Cloud  
> [Add your Streamlit Cloud URL here]

---

## 📈 Rates Tracked

| Category | Rates |
|---|---|
| **Benchmark Rates** | SOFR, Fed Funds Rate, Prime Rate |
| **Treasury Yields** | 2yr, 3yr, 5yr, 10yr |
| **Spreads** | 2s10s Spread, 10Y-3M Spread |

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io)** — dashboard UI
- **[FRED API](https://fred.stlouisfed.org)** — Federal Reserve economic data
- **[Plotly](https://plotly.com)** — interactive charts
- **[Pandas](https://pandas.pydata.org)** — data manipulation
- **[fredapi](https://github.com/mortada/fredapi)** — Python wrapper for FRED

---

## 📁 Project Structure

```
CRE-Rates/
├── app.py                  # Main Streamlit entry point
├── config.py               # FRED series IDs, colors, groupings
├── data/
│   ├── __init__.py
│   └── fetcher.py          # FRED API calls and caching logic
├── components/
│   ├── __init__.py
│   ├── charts.py           # Plotly chart functions
│   ├── metrics.py          # Current rate cards and summary table
│   └── sidebar.py          # Date range and filter controls
├── .env                    # API key (never committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/CRE-Rates.git
cd CRE-Rates
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get a FRED API key
Sign up for a free key at [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html)

### 5. Create your `.env` file
```
FRED_API_KEY=your_key_here
```

### 6. Run the dashboard
```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501`

---

## ☁️ Streamlit Cloud Deployment

1. Push your repo to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Add your FRED API key as a secret:
   - Go to **Settings → Secrets**
   - Add:
     ```toml
     FRED_API_KEY = "your_key_here"
     ```
4. Deploy — data refreshes automatically every 24 hours on page load

---

## 🔧 Configuration

All rates, colors, and settings are managed in `config.py`. To add a new rate:

1. Add the FRED series ID to `FRED_SERIES`
2. Add a color to `COLORS`
3. Add it to the appropriate group in `RATE_GROUPS`

No other files need to change.

---

## 📦 Requirements

```
streamlit
fredapi
pandas
plotly
python-dotenv
certifi
```

---

## 📄 License

MIT License — free to use and modify.