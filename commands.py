"""Command module."""
from __future__ import annotations

import dataclasses
import typing


@dataclasses.dataclass
class Command:

    """Command base class."""


@dataclasses.dataclass
class ParseArgs(Command):

    """Parse arguments command."""

    args: list[str]


@dataclasses.dataclass
class FindLines(Command):

    """Find lines command."""

    lines: tuple[str, ...]
    regex: str


T = typing.TypeVar("T", bound=Command)
subscribers: dict[type[Command], typing.Callable[[T], None]] = {}


def register(command_type: type[T], handler: typing.Callable[[T], None]) -> None:
    """Register a command."""
    subscribers[command_type] = handler


def invoke(command: Command) -> None:
    """Invoke a command."""
    if type(command) in subscribers:
        subscribers[type(command)](command)
