"""Error handler module."""
import sys

import events

type ErrorEvent = events.PathError | events.RegexError | events.NoFilesFoundError | events.NoLinesFoundError


def handle_error(event: ErrorEvent) -> None:
    """Print the error message to stderr."""
    sys.stderr.write(event.message)


def setup() -> None:
    """Register the error handler event."""
    events.register(events.PathError, handle_error)
    events.register(events.RegexError, handle_error)
    events.register(events.NoFilesFoundError, handle_error)
    events.register(events.NoLinesFoundError, handle_error)
