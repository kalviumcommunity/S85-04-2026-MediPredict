"""Utility functions for MediPredict project."""

from __future__ import annotations

import os
from pathlib import Path


def ensure_directory(path: str | Path) -> None:
    """Create a directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def project_root() -> Path:
    """Return project root path based on this file location."""
    return Path(__file__).resolve().parents[1]


def file_exists(file_path: str | Path) -> bool:
    """Check whether a file exists."""
    return Path(file_path).exists()


def safe_divide(numerator: float, denominator: float) -> float:
    """Safely divide two numbers."""
    if denominator == 0:
        return 0.0
    return numerator / denominator
