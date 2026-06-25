import duckdb

con = duckdb.connect("database/finance.duckdb")

# 1. Combien de lignes par actif ?
print("=== Lignes par actif ===")
print(con.execute("""
    SELECT ticker, COUNT(*) as nb_jours
    FROM prices_raw
    GROUP BY ticker
    ORDER BY ticker
""").df())

# 2. Prix min / max / moyen par actif
print("\n=== Stats par actif ===")
print(con.execute("""
    SELECT
        ticker,
        ROUND(MIN(close_price), 2)  AS prix_min,
        ROUND(MAX(close_price), 2)  AS prix_max,
        ROUND(AVG(close_price), 2)  AS prix_moyen
    FROM prices_raw
    GROUP BY ticker
    ORDER BY ticker
""").df())

# 3. Les 5 dernières dates disponibles
print("\n=== Dernières dates ===")
print(con.execute("""
    SELECT DISTINCT date
    FROM prices_raw
    ORDER BY date DESC
    LIMIT 5
""").df())

con.close()