"""Collector module."""
import pathlib
import typing

import commands
import events


def _next[T, U](iterator: typing.Iterator[T], default: U) -> T | U:
    """Get the next element from the iterator or return the default."""
    try:
        return next(iterator)
    except StopIteration:
        return default


def parse(args: commands.ParseArgs) -> None:
    """Parse the arguments."""
    iter_args = iter(args.args)
    _ = next(iter_args)
    if (path := _next(iter_args, None)) is None:
        msg = "error: The following required arguments were not provided:\n\t <PATH>\n"
        events.post_event(events.NoPathGivenError(msg))
        return
    if (regex := _next(iter_args, None)) is None:
        msg = "error: The following required arguments were not provided:\n\t <PATTERN>\n"
        events.post_event(events.NoRegexGivenError(msg))
        return
    events.post_event(events.ArgumentsParsed(path, regex))


def collect_lines(event: events.ArgumentsParsed) -> None:
    """Collect lines from a pathlike."""
    path = event.path
    if isinstance(path, str):
        path = pathlib.Path(path)
    try:
        with path.open(encoding="utf8") as file:
            commands.post_command(commands.FindLines(tuple(file), event.regex))
    except FileNotFoundError:
        events.post_event(events.PathNotFoundError(message=f"File not found: {path}", path=path))


def setup() -> None:
    """Register the collector event."""
    events.register(events.ArgumentsParsed, collect_lines)
    commands.register(commands.ParseArgs, parse)
