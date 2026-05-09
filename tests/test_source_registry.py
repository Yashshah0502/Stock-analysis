"""Tests for source registry."""
from src.source_registry import SOURCES, get_source_names, get_sources


def test_sources_exist() -> None:
    """Verify expected sources exist."""
    sources = get_sources()
    assert len(sources) > 0
    source_names = get_source_names()
    assert "Finnhub" in source_names
    assert "Financial Modeling Prep" in source_names
    assert "SEC EDGAR / EdgarTools" in source_names
    assert "yfinance" in source_names
    assert "OpenBB" in source_names
    assert "Polygon" in source_names


def test_sources_have_required_fields() -> None:
    """Verify every source has required fields."""
    required_fields = {
        "name",
        "category",
        "purpose",
        "requires_api_key",
        "env_key",
        "free_or_paid",
        "reliability_note",
    }

    for source in SOURCES:
        assert set(source.keys()) == required_fields, f"Source {source.get('name')} missing fields"
        assert isinstance(source["name"], str)
        assert isinstance(source["requires_api_key"], bool)


def test_get_source_names_returns_list() -> None:
    """Verify get_source_names returns correct list."""
    names = get_source_names()
    assert isinstance(names, list)
    assert len(names) == len(SOURCES)
    assert all(isinstance(name, str) for name in names)
