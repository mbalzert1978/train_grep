"""Event classes for the application."""
from __future__ import annotations

import collections
import dataclasses
import typing

if typing.TYPE_CHECKING:
    import pathlib
    from collections.abc import Iterable


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


subscribers = collections.defaultdict(list)
type Pathlike = str | pathlib.Path


def register[T: Event](event_type: type[T], handler: typing.Callable[[T], None]) -> None:
    """Register an event."""
    subscribers[event_type].append(handler)


def emit[T: Event](event: T) -> None:
    """Emit an event to all subscribers."""
    if type(event) in subscribers:
        for handler in subscribers[type(event)]:
            handler(event)
