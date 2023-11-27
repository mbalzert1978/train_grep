"""Main module."""
from __future__ import annotations

import pathlib
import re
import sys
import typing

if typing.TYPE_CHECKING:
    from collections.abc import Iterable

type Pathlike = str | pathlib.Path


class NoPathError(Exception):

    """No path error."""


class NoRegexError(Exception):

    """No regex error."""


def parse_args[T](args: Iterable[T]) -> tuple[T, T]:
    """Parse the arguments."""
    iter_args = iter(args)
    _ = next(iter_args)
    if (path := _next(iter_args, None)) is None:
        sys.exit("error: The following required arguments were not provided:\n\t <PATH>\n")
    if (regex := _next(iter_args, None)) is None:
        sys.exit("error: The following required arguments were not provided:\n\t <PATTERN>\n")
    return path, regex


def _next[T, U](iterator: typing.Iterator[T], default: U) -> T | U:
    """Get the next element from the iterator or return the default."""
    try:
        return next(iterator)
    except StopIteration:
        return default


def collect_lines_from(path: Pathlike) -> tuple[str, ...]:
    """Collect lines from a pathlike."""
    if isinstance(path, str):
        path = pathlib.Path(path)
    with path.open(encoding="utf8") as file:
        return tuple(file)


def find(lines: Iterable, regex: str) -> Iterable[str]:
    """Find the lines with the given regex."""
    for line in lines:
        if re.search(regex, line):
            yield line


def show(found: Iterable) -> None:
    """Show the found lines."""
    for line in found:
        sys.stdout.write(line)


def main() -> None:
    """Bootstrap."""
    path, regex = parse_args(sys.argv)
    lines = collect_lines_from(path)
    found = find(lines, regex)
    show(found)


if __name__ == "__main__":
    main()
