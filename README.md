# finance-pipeline
# Finance Data Pipeline

Pipeline de données end-to-end sur des actifs financiers réels (actions, ETF, crypto).

## Stack technique
- **Ingestion** : Python, yfinance, Pandas
- **Stockage** : DuckDB
- **Transformation** : dbt (staging → intermediate → marts)
- **Dashboard** : Streamlit

## Architecture
Yahoo Finance API → DuckDB → dbt → Streamlit

## Indicateurs calculés
- Rendement journalier
- Volatilité glissante (30 jours)
- Moyennes mobiles (SMA 20 / SMA 50)
- Sharpe Ratio
- Max Drawdown

## Lancer le projet
```bash
pip install -r requirements.txt
python ingestion/fetch_data.py
```

## Auteur
Amadou BALDE — www.linkedin.com/in/amadou-balde-b85834280
