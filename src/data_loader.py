"""
Pulls and caches price/fundamental/macro data for the portfolio.

TODO: wire up yfinance for OHLC, pandas-datareader (FRED) for macro series.
Cache to data/cache/ so repeated runs don't re-hit the API unnecessarily.
"""
