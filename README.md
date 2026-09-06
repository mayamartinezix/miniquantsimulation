# Personal Portfolio Stress-Testing Toolkit

A student-scale version of institutional quant risk methodology, applied to
your own (or paper-traded) holdings. This is a risk-management and
learning project, not a signal generator — see caveats below.

## Scope

- **Historical scenario replay**: replay specific historical windows (2008
  GFC, May 2010 flash crash, March 2020 COVID crash) against current
  position sizes to see hypothetical drawdown.
- **Monte Carlo simulation**: bootstrapped historical returns or correlated
  GBM to estimate 1-day / 10-day VaR and CVaR at 95% / 99% confidence.
- **Factor exposure**: regression against the public Fama-French factor sets
  (market, size, value, momentum) as a stand-in for proprietary Barra
  factors.

## Data sources (all free/cheap, realistic for an individual)

| Need | Source |
|---|---|
| Daily/intraday OHLC | `yfinance`, Alpha Vantage free tier |
| Fundamentals | SEC EDGAR |
| Macro (CPI, employment, yield curves) | FRED (St. Louis Fed) |
| Factor returns | Ken French Data Library |

Full order-book depth (Level 2/3) and options implied-vol surfaces are
institutional-grade licensed data (OPRA, exchange colocation) — out of reach
for an individual project and not attempted here. Alt-data (satellite
imagery, shipping manifests) is likewise skipped as unnecessary for a
learning-grade risk tool.

## Structure

```
src/
  data_loader.py     # pulls & caches price/fundamental/macro data
  scenarios.py        # historical scenario replay
  monte_carlo.py       # simulation + VaR/CVaR
  factors.py           # Fama-French factor regression
data/cache/            # local cache of pulled data (gitignored)
notebooks/             # exploratory analysis
```

Nothing here is implemented yet beyond the skeleton — next step is wiring
`data_loader.py` to `yfinance` for a real portfolio and building
`scenarios.py` against the historical windows above.

## Caveats (worth re-reading before funding this with real trading capital)

- **Pattern Day Trader rule**: US margin accounts need $25k equity to make
  4+ day trades in a 5-business-day window. A short-term rebuy strategy on a
  smaller account will hit this unless you stay in a cash account (which has
  its own settlement-timing limits).
- **Tax**: short-term capital gains are taxed as ordinary income in the US.
- **Backtest overfitting**: a few years of daily bars makes it easy to build
  a model that looks great historically and predicts little. Treat this as
  "how much could I lose in a repeat of 2020," not "what should I buy."
- **Scale mismatch**: institutional quant desks run this math over
  thousands of instruments with dedicated risk teams and licensed data. The
  same math on a personal portfolio still gives genuinely useful numbers —
  just don't expect it to generate an edge the way a real quant fund's
  infrastructure might.
- This is general educational information, not personalized financial
  advice.
