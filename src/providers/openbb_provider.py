"""OpenBB provider smoke test."""
from typing import Any


def smoke_test_openbb() -> dict[str, Any]:
    """Test OpenBB import and availability."""
    try:
        import openbb

        version = getattr(openbb, "__version__", "unknown")

        return {
            "source": "OpenBB",
            "status": "ok",
            "message": f"OpenBB available (version: {version})",
            "sample": {"available": True},
        }
    except ImportError:
        return {
            "source": "OpenBB",
            "status": "error",
            "message": "openbb not installed",
            "sample": {},
        }
    except Exception as e:
        return {
            "source": "OpenBB",
            "status": "error",
            "message": f"Error: {str(e)[:80]}",
            "sample": {},
        }
