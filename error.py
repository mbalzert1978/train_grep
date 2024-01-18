"""Error handler module."""
import sys

import events


def handle_error(event: events.Error) -> None:
    """Print the error message to stderr."""
    sys.stderr.write(event.message)


def setup() -> None:
    """Register the error handler event."""
    for err_event in events.Error.__subclasses__():
        events.register(err_event, handle_error)
