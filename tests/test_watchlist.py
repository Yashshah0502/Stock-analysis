from pathlib import Path

from src.watchlist import (
    add_tickers,
    get_default_watchlist,
    load_watchlist,
    normalize_ticker,
)


def test_normalize_ticker_strips_spaces_and_uppercases() -> None:
    assert normalize_ticker(" nvda ") == "NVDA"


def test_get_default_watchlist_contains_expected_tickers() -> None:
    watchlist = get_default_watchlist()
    assert "NVDA" in watchlist
    assert "AAPL" in watchlist
    assert "MSFT" in watchlist
    assert "PLTR" in watchlist
    assert "JPM" in watchlist


def test_get_default_watchlist_has_no_duplicates() -> None:
    watchlist = get_default_watchlist()
    assert len(watchlist) == len(set(watchlist))


def test_add_tickers_removes_duplicates() -> None:
    base = ["AAPL", "msft"]
    new = ["msft", "GOOGL", "AAPL", "TSLA"]
    combined = add_tickers(base, new)
    assert combined == ["AAPL", "MSFT", "GOOGL", "TSLA"]


def test_load_watchlist_returns_default_when_missing(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing_watchlist.json"
    watchlist = load_watchlist(str(missing_file))
    assert watchlist == get_default_watchlist()
