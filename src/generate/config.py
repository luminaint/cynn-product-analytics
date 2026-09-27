"""Settings for the synthetic data generator.

Every generator file reads its numbers from here, so there is exactly
one place to change the seed, the date window, or the size of the data.
"""
from datetime import date
from pathlib import Path

# --- Reproducibility ---
SEED = 42  # fixed random seed: same seed -> identical data on every run

# --- Date window (decision 2) ---
START_DATE = date(2025, 9, 1)  # first day of data
END_DATE = date(2026, 8, 31)   # last day of data
AS_OF_DATE = END_DATE          # "today" for the analysis; used for right-censoring

# --- Size ---
N_USERS = 20_000  # real signups, before duplicates, test accounts and bots are added

# --- Where generated files go ---
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # config.py -> generate -> src -> project
RAW_DIR = PROJECT_ROOT / "data" / "raw"             # gitignored; rebuilt by the generator 


