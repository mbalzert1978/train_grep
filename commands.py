"""Command module."""
from __future__ import annotations

import dataclasses
import typing

_TC = typing.TypeVar("_TC", bound="Command")
subscribers: dict[type[Command], typing.Callable[[_TC], None]] = {}


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


def register(command_type: type[_TC], handler: typing.Callable[[_TC], None]) -> None:
    """Register a command."""
    subscribers[command_type] = handler


def invoke(command: Command) -> None:
    """Invoke a command."""
    if type(command) in subscribers:
        subscribers[type(command)](command)
