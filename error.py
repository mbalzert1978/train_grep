"""Error handler module."""
import sys

import events

type ErrorEvent = events.NoPathGivenError | events.NoRegexGivenError | events.PathNotFoundError | events.NoLinesFoundError


def handle_error(event: ErrorEvent) -> None:
    """Print the error message to stderr."""
    sys.stderr.write(event.message)


def setup() -> None:
    """Register the error handler event."""
    events.register(events.NoPathGivenError, handle_error)
    events.register(events.NoRegexGivenError, handle_error)
    events.register(events.PathNotFoundError, handle_error)
    events.register(events.NoLinesFoundError, handle_error)
