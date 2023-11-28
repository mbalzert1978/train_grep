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
class LinesFound(Event):

    """Lines found event."""

    found: Iterable[str]


@dataclasses.dataclass
class LinesShown(Event):

    """Lines shown event."""

    line: str


@dataclasses.dataclass
class Error(Event):

    """Error event."""

    message: str


@dataclasses.dataclass
class PathError(Error):

    """Path error event."""

    message: str


@dataclasses.dataclass
class RegexError(Error):

    """Regex error event."""

    message: str


@dataclasses.dataclass
class NoFilesFoundError(Error):

    """No files found event."""

    message: str


@dataclasses.dataclass
class NoLinesFoundError(Error):

    """No lines found event."""

    message: str


def register(event_type: type[Event], handler: typing.Callable) -> None:
    """Register an event."""
    subscribers[event_type].append(handler)


def post_event(event: Event) -> None:
    """Post an event to all subscribers."""
    if type(event) not in subscribers:
        return
    for handler in subscribers[type(event)]:
        handler(event)
