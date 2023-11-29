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
class StartUp(Event):

    """Programm start Event."""


@dataclasses.dataclass
class ArgumentsParsed(Event):

    """Arguments parsed event."""

    path: Pathlike
    regex: str


@dataclasses.dataclass
class LinesCollected(Event):

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
class NoPathGivenError(Error):

    """No path given event."""


@dataclasses.dataclass
class NoRegexGivenError(Error):

    """Regex error event."""


@dataclasses.dataclass
class PathNotFoundError(Error):

    """No files found event."""

    path: Pathlike


@dataclasses.dataclass
class NoLinesFoundError(Error):

    """No lines found event."""


def register(event_type: type[Event], handler: typing.Callable[..., None]) -> None:
    """Register an event."""
    subscribers[event_type].append(handler)


def emit(event: Event) -> None:
    """Post an event to all subscribers."""
    if type(event) not in subscribers:
        return
    for handler in subscribers[type(event)]:
        handler(event)
