"""View module."""
import functools
import logging
import sys

import events

logger = logging.getLogger(__name__)

def show(event: events.LinesFound) -> None:
    """Show the found lines."""
    found = tuple(event.found)
    if not found:
        events.post_event(events.NoLinesFound(message="No lines found."))
        return
    for line in found:
        sys.stdout.write(line)
        events.post_event(events.LinesShown(line=line))
    return



def setup() -> None:
    """Register the view event."""
    events.register(events.LinesShown, functools.partial(logger.info, "Lines shown: %s"))
    events.register(events.NoLinesFound, functools.partial(logger.error, "No lines found: %s"))
    events.register(events.LinesFound, show)
