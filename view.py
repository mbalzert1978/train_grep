"""View module."""
import sys

import events


def show(event: events.LinesCollected) -> None:
    """Show the found lines."""
    found = tuple(event.found)
    if not found:
        events.post_event(events.NoLinesFoundError(message="No lines found."))
        return
    for line in found:
        sys.stdout.write(line)
        events.post_event(events.LinesShown(line=line))
    return


def setup() -> None:
    """Register the view event."""
    events.register(events.LinesCollected, show)
