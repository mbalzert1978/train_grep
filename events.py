"""Event classes for the application."""
import dataclasses
import typing
from collections import defaultdict
from collections.abc import Iterable

if typing.TYPE_CHECKING:
    import pathlib

type Pathlike = str | pathlib.Path

subscribers = defaultdict(list)


@dataclasses.dataclass
class Event:

    """Event base class."""


@dataclasses.dataclass
class ArgumentsParsed(Event):

    """Arguments parsed event."""

    path: Pathlike
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
class NoFilesFound(Event):

    """No files found event."""

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

    line: str


def register(event_type: type[Event], handler: typing.Callable) -> None:
    """Register an event."""
    subscribers[event_type].append(handler)


def post_event(event: Event) -> None:
    """Post an event to all subscribers."""
    if type(event) not in subscribers:
        return
    for handler in subscribers[type(event)]:
        handler(event)
