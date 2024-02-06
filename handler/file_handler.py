"""Collector module."""
import pathlib

import commands
import events
from resources import string


def collect_lines(event: events.ArgumentsParsed) -> None:
    """Collect lines from a pathlike."""
    path = pathlib.Path(event.path)
    try:
        with path.open(encoding=string.ENCODING) as file:
            commands.invoke(commands.FindLines(tuple(file), event.regex))
    except FileNotFoundError:
        events.emit(events.PathNotFoundError(message=string.NOT_FOUND_MSG.format(path=path), path=path))
    except PermissionError:
        events.emit(events.PathPermissionError(message=string.PERMISSION_MSG.format(path=path), path=path))
    except IsADirectoryError:
        events.emit(events.PathIsADirectoryError(message=string.IS_DIRECTORY_MSG.format(path=path), path=path))


def setup() -> None:
    """Register the collector event."""
    events.register(events.ArgumentsParsed, collect_lines)
