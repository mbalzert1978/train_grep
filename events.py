"""Event classes for the application."""
from __future__ import annotations

import collections
import dataclasses
import pathlib
import typing

if typing.TYPE_CHECKING:
    from collections.abc import Iterable

_TE = typing.TypeVar("_TE", bound="Event")
subscribers: dict[type[Event], list[typing.Callable[[_TE], None]]] = collections.defaultdict(list)
Pathlike = str | pathlib.Path


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
    pattern: str


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
class NoPatternGivenError(Error):

    """Regex error event."""


@dataclasses.dataclass
class PathNotFoundError(Error):

    """No files found event."""

    path: Pathlike


@dataclasses.dataclass
class PathPermissionError(Error):

    """Permission denied event."""

    path: Pathlike


@dataclasses.dataclass
class PathIsADirectoryError(Error):

    """Path is a directory event."""

    path: Pathlike


@dataclasses.dataclass
class NoLinesFoundError(Error):

    """No lines found event."""


def register(event_type: type[_TE], handler: typing.Callable[[_TE], None]) -> None:
    """Register an event."""
    subscribers[event_type].append(handler)


def emit(event: _TE) -> None:
    """Emit an event to all subscribers."""
    if type(event) in subscribers:
        for handler in subscribers[type(event)]:
            handler(event)
