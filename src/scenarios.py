"""
Historical scenario replay.

TODO: define named windows (2008 GFC, May 2010 flash crash, March 2020
crash) as (start_date, end_date) pairs, pull the return series for each
holding over that window from data_loader, and apply proportionally to
current position sizes to estimate hypothetical drawdown.
"""

SCENARIOS = {
    "2008_gfc": ("2008-09-01", "2009-03-01"),
    "2010_flash_crash": ("2010-05-06", "2010-05-06"),
    "2020_covid_crash": ("2020-02-19", "2020-03-23"),
}
