"""Main module."""
import sys
from collections.abc import MutableSequence, Sequence
from functools import partial
from pathlib import Path
from typing import NoReturn

from result import as_result

from model import MutableVector


def show_lines(lines: Sequence[str]) -> None:
    """Print the found lines."""
    if not lines:
        msg = "No matches found."
        print(msg)
    for line in lines:
        print(line)


@as_result(Exception)
def find_lines(lines: MutableSequence[str], search_string: str) -> MutableVector[str]:
    """Find the lines that match the given search string."""
    return MutableVector(line for line in lines if search_string in line)


@as_result(Exception)
def read_lines(path: Path) -> MutableVector[str]:
    """Read the lines from a given file."""
    with path.open("r", encoding="utf8") as f:
        return MutableVector(f.readlines())


def leave_on_missing_arg(msg: str) -> NoReturn:
    """Print a message and exit."""
    print(msg)
    sys.exit(1)


def extract_path_and_value(items: MutableSequence[str]) -> tuple[str, str]:
    """Extract the path and search string from the command line arguments."""
    args = MutableVector(items).skip(1)
    if (path := args.next()) is None:
        leave_on_missing_arg("Path argument missing.")
    if (search_string := args.next()) is None:
        leave_on_missing_arg("Search string argument missing.")
    return (path, search_string)


def main() -> None:
    filename, search_string = extract_path_and_value(sys.argv)
    read_lines(Path(filename)).and_then(partial(find_lines, search_string=search_string)).and_then(show_lines)


if __name__ == "__main__":
    main()
