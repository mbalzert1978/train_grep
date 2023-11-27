"""Command module."""
import dataclasses
import typing

subscribers: dict[type["Command"], typing.Callable] = dict()


@dataclasses.dataclass
class Command:

    """Command base class."""


@dataclasses.dataclass
class FindLines(Command):

    """Find lines command."""

    lines: tuple[str, ...]
    regex: str


def register_command(command_type: type[Command], handler: typing.Callable) -> None:
    """Register a command."""
    subscribers[command_type] = handler


def post_command(command: Command) -> None:
    """Ivoke a command."""
    if type(command) not in subscribers:
        return
    subscribers[type(command)](command)