"""View module."""
import sys

import events
from resources import string


def show(event: events.LinesCollected) -> None:
    """Show the found lines."""
    found = tuple(event.found)
    if not found:
        events.emit(events.NoLinesFoundError(message=string.NO_LINES_MSG))
        return
    for line in found:
        sys.stdout.write(line)
        events.emit(events.LinesShown(line=line))
    return


def setup() -> None:
    """Register the view event."""
    events.register(events.LinesCollected, show)
