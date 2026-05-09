"""Financial Modeling Prep provider smoke test."""
from typing import Any

import requests

from src.config import get_settings


def smoke_test_fmp(symbol: str = "AAPL") -> dict[str, Any]:
    """Test FMP API connectivity."""
    settings = get_settings()
    api_key = settings.fmp_api_key.strip()

    if not api_key:
        return {
            "source": "Financial Modeling Prep",
            "status": "skipped",
            "message": "FMP_API_KEY not set",
            "sample": {},
        }

    try:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "source": "Financial Modeling Prep",
            "status": "ok",
            "message": f"Retrieved data for {symbol}",
            "sample": {"symbol": symbol, "price": data[0].get("price") if data else None},
        }
    except Exception as e:
        return {
            "source": "Financial Modeling Prep",
            "status": "error",
            "message": f"Error: {str(e)[:80]}",
            "sample": {},
        }
