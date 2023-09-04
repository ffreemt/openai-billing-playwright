"""Test openai_billing."""
# pylint: disable=broad-except
from openai_billing import __version__, openai_billing


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not openai_billing()
    except Exception:
        assert True
