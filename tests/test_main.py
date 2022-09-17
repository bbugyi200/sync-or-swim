"""Tests the sync_or_swim project's CLI."""

from __future__ import annotations

from sync_or_swim.__main__ import main


def test_main() -> None:
    """Tests main() function."""
    assert main([""]) == 0
