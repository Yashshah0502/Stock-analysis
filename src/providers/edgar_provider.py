"""EDGAR provider smoke test."""
from typing import Any

from src.config import get_settings


def smoke_test_edgar(symbol: str = "AAPL") -> dict[str, Any]:
    """Test EDGAR connectivity with edgartools."""
    settings = get_settings()
    user_agent = settings.sec_user_agent.strip()

    placeholder = "Your Name your.email@example.com"
    if not user_agent or user_agent == placeholder:
        return {
            "source": "SEC EDGAR / EdgarTools",
            "status": "skipped",
            "message": "SEC_USER_AGENT not configured",
            "sample": {},
        }

    try:
        from edgartools import get_company

        company = get_company(symbol)
        cik = company.cik_str

        return {
            "source": "SEC EDGAR / EdgarTools",
            "status": "ok",
            "message": f"Retrieved CIK for {symbol}",
            "sample": {"symbol": symbol, "cik": cik},
        }
    except ImportError:
        return {
            "source": "SEC EDGAR / EdgarTools",
            "status": "error",
            "message": "edgartools not installed",
            "sample": {},
        }
    except Exception as e:
        return {
            "source": "SEC EDGAR / EdgarTools",
            "status": "error",
            "message": f"Error: {str(e)[:80]}",
            "sample": {},
        }
