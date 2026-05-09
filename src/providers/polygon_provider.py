"""Polygon provider smoke test."""
from typing import Any

import requests

from src.config import get_settings


def smoke_test_polygon(symbol: str = "AAPL") -> dict[str, Any]:
    """Test Polygon API connectivity."""
    settings = get_settings()
    api_key = settings.polygon_api_key.strip()

    if not api_key:
        return {
            "source": "Polygon",
            "status": "skipped",
            "message": "POLYGON_API_KEY not set",
            "sample": {},
        }

    try:
        url = f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{symbol}?apiKey={api_key}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "source": "Polygon",
            "status": "ok",
            "message": f"Retrieved snapshot for {symbol}",
            "sample": {
                "symbol": symbol,
                "price": data.get("results", [{}])[0].get("lastPrice"),
            },
        }
    except Exception as e:
        return {
            "source": "Polygon",
            "status": "error",
            "message": f"Error: {str(e)[:80]}",
            "sample": {},
        }
