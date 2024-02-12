"""Main module."""
import sys
from collections.abc import Iterable
from functools import partial
from pathlib import Path
from typing import IO, NoReturn

from result import as_result

from model import MutableVector

type Pathlike = str | Path


def show_lines(lines: Iterable[str]) -> None:
    """Print the found lines."""
    if lines:
        for line in lines:
            print(line)
    else:
        msg = "No matches found."
        print(msg)


@as_result(Exception)
def find_lines(lines: Iterable[str], search_string: str) -> MutableVector[str]:
    """Find the lines that match the given search string."""
    return MutableVector(line for line in lines if search_string in line)


@as_result(Exception)
def read_file(path: Pathlike) -> IO[str]:
    """Read the given file."""
    if isinstance(path, str):
        path = Path(path)
    return path.open("r", encoding="utf8")


@as_result(Exception)
def collect_lines(file: IO[str]) -> MutableVector[str]:
    """Read the lines from a given file."""
    vec = MutableVector(file)
    file.close()
    return vec


def leave_on_missing_arg(msg: str) -> NoReturn:
    """Print a message and exit."""
    print(msg)
    sys.exit(1)


def extract_path_and_value(sys_args: Iterable[str]) -> tuple[str, str]:
    """Extract the path and search string from the command line arguments."""
    args = MutableVector(sys_args).skip(1)
    if (path := args.next()) is None:
        leave_on_missing_arg("Path argument missing.")
    if (search_string := args.next()) is None:
        leave_on_missing_arg("Search string argument missing.")
    return (path, search_string)


def main() -> None:
    filename, search_string = extract_path_and_value(sys.argv)
    (
        read_file(Path(filename))
        .and_then(collect_lines)
        .and_then(partial(find_lines, search_string=search_string))
        .and_then(show_lines)
    )


if __name__ == "__main__":
    main()
