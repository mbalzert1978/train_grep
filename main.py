"""Main module."""
from __future__ import annotations

from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable, Sequence


class ArgumentParserLike(Protocol):

    """Protocol for adding arguments to an ArgumentParser."""

    def add_argument(self, *args: Sequence, **kwargs: str | type) -> None:
        """Add an argument to the parser."""
        ...

    def parse_args(
        self,
        args: Sequence | None = None,
        namespace: Namespace | None = None,
    ) -> Namespace:
        """Parse arguments."""
        ...


class FileRepository:

    """File repository."""

    @staticmethod
    def read_lines(path: Path) -> Generator[str, None, None]:
        """Read lines from file."""
        with path.open(encoding="utf8") as f:
            yield from f.readlines()


Lines = tuple[str, ...]


def find(lines: Iterable, value: str) -> Lines:
    """Find the line with the given value."""
    return tuple(filter(lambda line: value in line, lines))


def show(found: Lines) -> None:
    """Show the found lines."""
    for line in found:
        print(line)


def add_arguments(ap: ArgumentParserLike) -> ArgumentParserLike:
    """Set up the argument parser."""
    ap.add_argument("path", help="the path to the file to grep.", type=Path)
    ap.add_argument("value", help="the value to search for.")
    return ap


def main() -> None:  # noqa: D103
    args = add_arguments(ArgumentParser()).parse_args()  # type: ignore [arg-type]
    show(find(FileRepository.read_lines(args.path), args.value))


if __name__ == "__main__":
    main()
