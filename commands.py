"""Command module."""
import dataclasses
from collections.abc import Iterable


@dataclasses.dataclass
class Command:

    """Command base class."""


class ParseArguments[T](Command):

    """Parse arguments command."""

    args: Iterable[T]


class CollectLines(Command):

    """Collect lines command."""

    path: str


class FindLines(Command):

    """Find lines command."""

    lines: tuple[str, ...]
    regex: str


class ShowLines(Command):

    """Show lines command."""

    found: Iterable[str]


class Exit(Command):

    """Exit command."""

    msg: str
