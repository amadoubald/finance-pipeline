import yfinance as yf
import pandas as pd
import duckdb
import os

# ── Paramètres ──────────────────────────────────────────
TICKERS = ["AAPL", "MSFT", "BTC-USD"]
START   = "2022-01-01"
END     = "2024-12-31"
DB_PATH = "database/finance.duckdb"

# ── 1. Téléchargement Yahoo Finance ─────────────────────
print("Téléchargement des données...")
raw = yf.download(TICKERS, start=START, end=END, auto_adjust=True)

# ── 2. Nettoyage ─────────────────────────────────────────
close = raw["Close"].reset_index()
df = close.melt(id_vars="Date", var_name="ticker", value_name="close_price")
df = df.dropna()
df["Date"] = pd.to_datetime(df["Date"])
df.columns = ["date", "ticker", "close_price"]

print(f"{len(df)} lignes chargées")
print(df.head())

# ── 3. Chargement dans DuckDB ────────────────────────────
os.makedirs("database", exist_ok=True)
con = duckdb.connect(DB_PATH)
con.execute("DROP TABLE IF EXISTS prices_raw")
con.execute("CREATE TABLE prices_raw AS SELECT * FROM df")
print(f"Table prices_raw créée dans {DB_PATH}")
con.close()