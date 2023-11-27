"""Error handler module."""
import sys

import events

type ErrorEvent = events.PathError | events.RegexError | events.NoFilesFound | events.NoLinesFound


def handle_error(event: ErrorEvent) -> None:
    """Print the error message to stderr."""
    sys.stderr.write(event.message)


def setup() -> None:
    """Register the error handler event."""
    events.register_event(events.PathError, handle_error)
    events.register_event(events.RegexError, handle_error)
    events.register_event(events.NoFilesFound, handle_error)
    events.register_event(events.NoLinesFound, handle_error)
