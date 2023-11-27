"""View module."""
import sys

import events


def show(event: events.LinesFound) -> None:
    """Show the found lines."""
    found = tuple(event.found)
    if not found:
        events.post_event(events.NoLinesFound(message="No lines found."))
        return
    for line in found:
        sys.stdout.write(line)


def setup() -> None:
    """Register the view event."""
    events.register(events.LinesFound, show)
