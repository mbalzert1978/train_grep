"""Utility functions."""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from src.adapter.file_repository import FileRepository

Lines = tuple[str, ...]


class Arguments(TypedDict):

    """Arguments Type."""

    path: Path
    value: str


def find(args: Arguments, repository: FileRepository) -> Lines:  # noqa: D417
    """
    Find the lines in the file.

    Args:
    ----
        args: Arguments as a dictionary.
        repository: a FileRepository.

    Returns:
    -------
        a tuple of lines.
    """
    match args:
        case {"path": path, "value": value}:
            return tuple(
                filter(
                    lambda line: value in line,
                    repository.read_lines(path),
                ),
            )
        case _:
            return tuple()


def show(found: Lines) -> None:
    """Show the found lines."""
    for line in found:
        print(line)


def set_arg_parse() -> ArgumentParser:
    """Set up the argument parser."""
    ap = ArgumentParser()
    ap.add_argument("path", help="the path to the file to grep.", type=Path)
    ap.add_argument("value", help="the value to search for.")
    return ap
