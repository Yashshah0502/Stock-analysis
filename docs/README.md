# Retail Stock Research Agent - Step 1: Foundation & Data Source Health Checks

## Overview

**Step 1** establishes the project foundation with data source health checks only.

### What Step 1 Does

- ✅ Defines all 7 data sources (Finnhub, FMP, SEC EDGAR, yfinance, OpenBB, Polygon, FRED)
- ✅ Loads API keys and configuration from `.env` using pydantic-settings
- ✅ Provides smoke tests for each provider (lightweight connectivity checks)
- ✅ Runs health checks across all sources
- ✅ Displays status in a Rich table format
- ✅ Includes comprehensive test suite
- ✅ Validates that missing API keys are handled gracefully (returns "skipped")
- ✅ Ensures provider failures don't crash the main script (returns "error")

### What Step 1 Does NOT Do

- ❌ Trading logic or buy/sell recommendations
- ❌ Stock price predictions
- ❌ LLM (Large Language Model) calls
- ❌ Broker integration
- ❌ Email or scheduler logic
- ❌ Hardcoded API keys or secrets
- ❌ Print sensitive information

## Step 2: Watchlist / Universe Builder

Step 2 creates a default stock universe / watchlist for monthly investment comparison.
It does not recommend stocks yet.

Command:

```bash
python scripts/build_watchlist.py
```

## Project Structure

```
retail_stock_research_agent/
├── README.md                 # This file
├── .env                      # Local environment variables (DO NOT COMMIT)
├── .env.example             # Template for .env file
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── src/
│   ├── __init__.py
│   ├── config.py            # Pydantic settings loader
│   ├── source_registry.py   # Data source definitions
│   ├── healthcheck.py       # Health check runner
│   └── providers/
│       ├── __init__.py
│       ├── finnhub_provider.py
│       ├── fmp_provider.py
│       ├── edgar_provider.py
│       ├── yfinance_provider.py
│       ├── openbb_provider.py
│       └── polygon_provider.py
├── scripts/
│   └── check_sources.py     # CLI script to run health checks
└── tests/
    ├── test_source_registry.py
    └── test_healthcheck.py
```

## Setup

### 1. Create Virtual Environment

```bash
cd retail_stock_research_agent
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and fill in your API keys:

```
FINNHUB_API_KEY=your_key_here
FMP_API_KEY=your_key_here
POLYGON_API_KEY=your_key_here
SEC_USER_AGENT="Your Name your.email@example.com"
```

**Notes:**
- Finnhub, FMP, and Polygon require API keys (requests will be skipped if missing)
- SEC_USER_AGENT requires a proper email address (SEC requires identification)
- yfinance and OpenBB work without API keys
- Never commit `.env` to version control

## Usage

### Run Health Checks

```bash
python scripts/check_sources.py
```

This displays a table showing:
- Source name
- Status (ok, skipped, or error)
- Message describing the result

Example output:
```
Data Source Health Check

                    Source Status
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Source                    ┃ Status ┃ Message                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Finnhub                   │ ok     │ Retrieved quote for AAPL   │
│ Financial Modeling Prep   │ error  │ Error: 401 Unauthorized   │
│ SEC EDGAR / EdgarTools    │ skipped│ SEC_USER_AGENT not config │
│ yfinance                  │ ok     │ Retrieved data for AAPL    │
│ OpenBB                    │ error  │ openbb not installed       │
│ Polygon                   │ skipped│ POLYGON_API_KEY not set    │
└───────────────────────────┴────────┴────────────────────────────┘

Summary: 2 ok, 2 skipped, 2 error
```

### Run Tests

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run specific test file:

```bash
pytest tests/test_source_registry.py -v
```

## Configuration Details

### `src/config.py`

- Loads settings from `.env` using `pydantic-settings`
- Provides `get_settings()` function
- Never prints secret values
- Gracefully handles missing keys (returns empty string)

### `src/source_registry.py`

Defines all 7 data sources with metadata:
- Name, category, purpose
- Whether API key is required
- Free or paid tier
- Reliability notes

### Provider Files

Each provider module exports a smoke test function:

- `smoke_test_finnhub(symbol="AAPL")` → Fetches real-time quote
- `smoke_test_fmp(symbol="AAPL")` → Fetches financial data
- `smoke_test_polygon(symbol="AAPL")` → Fetches market snapshot
- `smoke_test_edgar(symbol="AAPL")` → Looks up SEC CIK number
- `smoke_test_yfinance(symbol="AAPL")` → Fetches historical data
- `smoke_test_openbb()` → Verifies import works

Each function returns:
```python
{
    "source": "...",
    "status": "ok" | "skipped" | "error",
    "message": "...",
    "sample": {}
}
```

### `src/healthcheck.py`

- Runs all provider smoke tests
- Catches exceptions and returns status="error"
- Returns list of normalized result dictionaries

## Tests

### `test_source_registry.py`

- ✅ Verify all 7 expected sources exist
- ✅ Verify every source has required fields
- ✅ Verify field types and structure

### `test_healthcheck.py`

- ✅ Verify healthcheck returns a list
- ✅ Verify every result has required fields (source, status, message, sample)
- ✅ Verify status is only "ok", "skipped", or "error"

## Troubleshooting

### ImportError: No module named 'edgartools'

```bash
pip install edgartools
```

### ImportError: No module named 'openbb'

```bash
pip install openbb
```

### API Key Errors

Check that your `.env` file is in the project root and formatted correctly:

```bash
cat .env
```

### Connection Timeout

- Check internet connection
- Verify API endpoint URLs
- Check API rate limits

## Code Standards

- ✅ All Python files under 100 lines
- ✅ Functions are small and focused
- ✅ Simple, modular code structure
- ✅ Type hints where useful
- ✅ No hardcoded API keys
- ✅ No printing of secrets
- ✅ Graceful error handling

## Next Steps (Not in Step 1)

Future steps will add:
- Data aggregation and normalization
- Technical analysis calculations
- LLM-powered stock analysis
- Trading signals and recommendations
- Broker integration
- Scheduled data fetching
- Email alerts

---

**Step 1 Complete:** Foundation and data source validation ready for future enhancements.
