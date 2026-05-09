"""yfinance provider smoke test."""
from typing import Any


def smoke_test_yfinance(symbol: str = "AAPL") -> dict[str, Any]:
    """Test yfinance connectivity (prototype/fallback only)."""
    try:
        import yfinance

        ticker = yfinance.Ticker(symbol)
        info = ticker.info
        price = info.get("currentPrice")

        return {
            "source": "yfinance",
            "status": "ok",
            "message": f"Retrieved data for {symbol} (fallback/prototype only)",
            "sample": {"symbol": symbol, "price": price},
        }
    except ImportError:
        return {
            "source": "yfinance",
            "status": "error",
            "message": "yfinance not installed",
            "sample": {},
        }
    except Exception as e:
        return {
            "source": "yfinance",
            "status": "error",
            "message": f"Error: {str(e)[:80]}",
            "sample": {},
        }
