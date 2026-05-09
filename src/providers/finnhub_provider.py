"""Finnhub provider smoke test."""
from typing import Any

import requests

from src.config import get_settings


def smoke_test_finnhub(symbol: str = "AAPL") -> dict[str, Any]:
    """Test Finnhub API connectivity."""
    settings = get_settings()
    api_key = settings.finnhub_api_key.strip()

    if not api_key:
        return {
            "source": "Finnhub",
            "status": "skipped",
            "message": "FINNHUB_API_KEY not set",
            "sample": {},
        }

    try:
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "source": "Finnhub",
            "status": "ok",
            "message": f"Retrieved quote for {symbol}",
            "sample": {"symbol": symbol, "price": data.get("c")},
        }
    except Exception as e:
        return {
            "source": "Finnhub",
            "status": "error",
            "message": f"Error: {str(e)[:80]}",
            "sample": {},
        }
