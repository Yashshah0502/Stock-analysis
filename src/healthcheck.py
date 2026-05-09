"""Health check runner for all data sources."""
from typing import Any

from src.providers.edgar_provider import smoke_test_edgar
from src.providers.finnhub_provider import smoke_test_finnhub
from src.providers.fmp_provider import smoke_test_fmp
from src.providers.openbb_provider import smoke_test_openbb
from src.providers.polygon_provider import smoke_test_polygon
from src.providers.yfinance_provider import smoke_test_yfinance


def run_all_healthchecks(symbol: str = "AAPL") -> list[dict[str, Any]]:
    """Run health checks for all providers."""
    results = []

    # Test API-based providers
    for test_func in [
        smoke_test_finnhub,
        smoke_test_fmp,
        smoke_test_polygon,
        smoke_test_edgar,
        smoke_test_yfinance,
    ]:
        try:
            result = test_func(symbol)
            results.append(result)
        except Exception as e:
            results.append(
                {
                    "source": getattr(test_func, "__doc__", "Unknown").split(".")[-1],
                    "status": "error",
                    "message": f"Exception: {str(e)[:80]}",
                    "sample": {},
                }
            )

    # Test OpenBB (no symbol needed)
    try:
        result = smoke_test_openbb()
        results.append(result)
    except Exception as e:
        results.append(
            {
                "source": "OpenBB",
                "status": "error",
                "message": f"Exception: {str(e)[:80]}",
                "sample": {},
            }
        )

    return results
