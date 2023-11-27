"""Error handler module."""
import sys

import events

type ErrorEvent = events.PathError | events.RegexError | events.NoFilesFound | events.NoLinesFound


def handle_error(event: ErrorEvent) -> None:
    """Print the error message to stderr."""
    sys.stderr.write(event.message)


def setup() -> None:
    """Register the error handler event."""
    events.register(events.PathError, handle_error)
    events.register(events.RegexError, handle_error)
    events.register(events.NoFilesFound, handle_error)
    events.register(events.NoLinesFound, handle_error)
