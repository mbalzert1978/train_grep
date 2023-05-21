"""File repository."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from pathlib import Path


class FileRepository:

    """File repository."""

    @staticmethod
    def read_lines(path: Path) -> Generator[str, None, None]:
        """Read lines from file."""
        with path.open(encoding="utf8") as f:
            yield from f.readlines()
