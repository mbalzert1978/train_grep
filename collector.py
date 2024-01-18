"""Collector module."""
import pathlib

import commands
import events


def collect_lines(event: events.ArgumentsParsed) -> None:
    """Collect lines from a pathlike."""
    path = event.path
    if isinstance(path, str):
        path = pathlib.Path(path)
    try:
        with path.open(encoding="utf8") as file:
            commands.invoke(commands.FindLines(tuple(file), event.regex))
    except FileNotFoundError:
        events.emit(events.PathNotFoundError(message=f"File not found: {path}", path=path))


def setup() -> None:
    """Register the collector event."""
    events.register(events.ArgumentsParsed, collect_lines)
