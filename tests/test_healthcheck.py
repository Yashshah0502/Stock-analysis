"""Tests for health check functionality."""
from src.healthcheck import run_all_healthchecks


def test_run_all_healthchecks_returns_list() -> None:
    """Verify healthcheck returns a list."""
    results = run_all_healthchecks()
    assert isinstance(results, list)
    assert len(results) > 0


def test_healthcheck_result_structure() -> None:
    """Verify every healthcheck result has required fields."""
    results = run_all_healthchecks()

    required_fields = {"source", "status", "message", "sample"}

    for result in results:
        assert set(result.keys()) == required_fields
        assert isinstance(result["source"], str)
        assert isinstance(result["message"], str)
        assert isinstance(result["sample"], dict)


def test_healthcheck_status_values() -> None:
    """Verify status is only ok, skipped, or error."""
    results = run_all_healthchecks()
    valid_statuses = {"ok", "skipped", "error"}

    for result in results:
        assert result["status"] in valid_statuses
