"""Command module."""
import dataclasses
import typing

subscribers: dict[type["Command"], typing.Callable] = {}


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


def register(command_type: type[Command], handler: typing.Callable[..., None]) -> None:
    """Register a command."""
    subscribers[command_type] = handler


def invoke(command: Command) -> None:
    """Ivoke a command."""
    if type(command) not in subscribers:
        return
    subscribers[type(command)](command)
