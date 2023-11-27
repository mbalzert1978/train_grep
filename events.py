"""Event classes for the application."""
import dataclasses
from collections.abc import Iterable


@dataclasses.dataclass
class Event:

    """Event base class."""


@dataclasses.dataclass
class ArgumentsParsed(Event):

    """Arguments parsed event."""

    path: str
    regex: str


@dataclasses.dataclass
class PathError(Event):

    """Path error event."""

    message: str


@dataclasses.dataclass
class RegexError(Event):

    """Regex error event."""

    message: str


@dataclasses.dataclass
class NoLinesFound(Event):

    """No lines found event."""

    message: str


@dataclasses.dataclass
class LinesCollected(Event):

    """Lines collected event."""

    lines: tuple[str, ...]


@dataclasses.dataclass
class LinesFound(Event):

    """Lines found event."""

    found: Iterable[str]


@dataclasses.dataclass
class LinesShown(Event):

    """Lines shown event."""
