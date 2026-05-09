"""Source registry with all data providers."""
from typing import Any, TypedDict


class SourceInfo(TypedDict):
    """Type for source information."""

    name: str
    category: str
    purpose: str
    requires_api_key: bool
    env_key: str
    free_or_paid: str
    reliability_note: str


SOURCES: list[SourceInfo] = [
    {
        "name": "Finnhub",
        "category": "Market Data",
        "purpose": "Real-time stock quotes, company news",
        "requires_api_key": True,
        "env_key": "FINNHUB_API_KEY",
        "free_or_paid": "Free tier + paid",
        "reliability_note": "Reliable, requires API key",
    },
    {
        "name": "Financial Modeling Prep",
        "category": "Financial Data",
        "purpose": "Financials, ratios, DCF, historical data",
        "requires_api_key": True,
        "env_key": "FMP_API_KEY",
        "free_or_paid": "Free tier + paid",
        "reliability_note": "Comprehensive, requires API key",
    },
    {
        "name": "SEC EDGAR / EdgarTools",
        "category": "Regulatory Filing",
        "purpose": "10-K, 10-Q, 8-K, proxy filings",
        "requires_api_key": False,
        "env_key": "SEC_USER_AGENT",
        "free_or_paid": "Free (requires User-Agent)",
        "reliability_note": "Official source, needs proper User-Agent header",
    },
    {
        "name": "yfinance",
        "category": "Market Data",
        "purpose": "Historical prices, basic stock info",
        "requires_api_key": False,
        "env_key": "",
        "free_or_paid": "Free",
        "reliability_note": "Fallback/prototype only, not for production",
    },
    {
        "name": "OpenBB",
        "category": "Multi-Source",
        "purpose": "Aggregated stock data, technical analysis",
        "requires_api_key": False,
        "env_key": "",
        "free_or_paid": "Free (optional paid tier)",
        "reliability_note": "Import-based, verify availability",
    },
    {
        "name": "Polygon",
        "category": "Market Data",
        "purpose": "Stock quotes, aggregate bars, news",
        "requires_api_key": True,
        "env_key": "POLYGON_API_KEY",
        "free_or_paid": "Free tier + paid",
        "reliability_note": "Reliable, requires API key",
    },
    {
        "name": "FRED",
        "category": "Economic Data",
        "purpose": "Macro indicators, economic data",
        "requires_api_key": False,
        "env_key": "",
        "free_or_paid": "Free",
        "reliability_note": "US Federal Reserve official data",
    },
]


def get_sources() -> list[SourceInfo]:
    """Return all available sources."""
    return SOURCES


def get_source_names() -> list[str]:
    """Return list of source names."""
    return [source["name"] for source in SOURCES]
