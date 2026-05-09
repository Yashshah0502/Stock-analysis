import json
from pathlib import Path

DEFAULT_WATCHLIST = [
    "NVDA",
    "AAPL",
    "GOOGL",
    "MSFT",
    "AMZN",
    "JPM",
    "JNJ",
    "GS",
    "PLTR",
    "WMT",
    "WFC",
    "META",
    "TSLA",
    "AVGO",
    "AMD",
    "COST",
    "V",
    "MA",
    "UNH",
    "LLY",
]


def normalize_ticker(ticker: str) -> str:
    """Normalize a ticker by stripping whitespace and uppercasing."""
    return ticker.strip().upper()


def get_default_watchlist() -> list[str]:
    """Return the default watchlist with normalized tickers and no duplicates."""
    normalized = [normalize_ticker(t) for t in DEFAULT_WATCHLIST]
    seen = set()
    unique = []
    for ticker in normalized:
        if ticker not in seen:
            seen.add(ticker)
            unique.append(ticker)
    return unique


def add_tickers(base: list[str], new_tickers: list[str]) -> list[str]:
    """Add new tickers to a base watchlist, preserving order and removing duplicates."""
    normalized_base = [normalize_ticker(t) for t in base]
    seen = set(normalized_base)
    combined = normalized_base.copy()
    for ticker in new_tickers:
        normalized = normalize_ticker(ticker)
        if normalized and normalized not in seen:
            seen.add(normalized)
            combined.append(normalized)
    return combined


def save_watchlist(tickers: list[str], path: str = "data/watchlist.json") -> None:
    """Save the watchlist tickers to a JSON file, creating directories as needed."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as handle:
        json.dump(tickers, handle, indent=2)


def load_watchlist(path: str = "data/watchlist.json") -> list[str]:
    """Load a watchlist from a JSON file or return the default watchlist if missing."""
    file_path = Path(path)
    if not file_path.exists():
        return get_default_watchlist()
    with file_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        return get_default_watchlist()
    return [normalize_ticker(ticker) for ticker in data if isinstance(ticker, str)]
