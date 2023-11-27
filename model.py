"""Model module."""
import re
import typing

import events

if typing.TYPE_CHECKING:
    import pathlib

type Pathlike = str | pathlib.Path


class Product:

    """Product base class."""

    events: list[events.Event]


class Arguments(Product):

    """Arguments product."""

    def __init__(self) -> None:
        self.events = []
        super().__init__()

    @staticmethod
    def _next[T, U](iterator: typing.Iterator[T], default: U) -> T | U:
        """Get the next element from the iterator or return the default."""
        try:
            return next(iterator)
        except StopIteration:
            return default

    def parse_args(self, args: typing.Iterable[typing.Any]) -> None:
        """Parse the arguments."""
        iter_args = iter(args)
        _ = next(iter_args)
        if (path := self._next(iter_args, None)) is None:
            msg = "error: The following required arguments were not provided:\n\t <PATH>\n"
            self.events.append(events.PathError(msg))
        if (regex := self._next(iter_args, None)) is None:
            msg = "error: The following required arguments were not provided:\n\t <PATTERN>\n"
            self.events.append(events.RegexError(msg))
        self.events.append(events.ArgumentsParsed(path, regex))


class Collector(Product):

    """Collector product."""

    def __init__(self, path: Pathlike) -> None:
        self.path = path
        self.events = []
        super().__init__()

    def collect_lines(self) -> None:
        """Collect the lines from the path."""
        try:
            with open(self.path, encoding="utf8") as file:
                self.events.append(events.LinesCollected(tuple(file)))
        except FileNotFoundError as error:
            msg = f"error: {error}\n"
            self.events.append(events.PathError(msg))


class Finder(Product):

    """Finder product."""

    def __init__(self, lines: typing.Iterable[str], regex: str) -> None:
        self.lines = lines
        self.regex = regex
        self.events = []
        super().__init__()

    def find(self) -> None:
        """Find the lines with the given regex."""
        found = [line for line in self.lines if re.search(self.regex, line)]
        if not found:
            msg = f"error: no matches found for {self.regex}\n"
            self.events.append(events.NoLinesFound(msg))
        self.events.append(events.LinesFound(found))


class Shower(Product):

    """Shower product."""

    def __init__(self, found: typing.Iterable[str]) -> None:
        self.found = found
        self.events = []
        super().__init__()

    def show(self) -> None:
        """Show the found lines."""
        for line in self.found:
            print(line, end="")
        self.events.append(events.LinesShown())
