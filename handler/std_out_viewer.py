"""View module."""
import sys

import events
from resources import string


def print_lines(event: events.LinesFound) -> None:
    """Show the found lines."""
    match list(event.found):
        case []:
            events.emit(events.NoLinesFoundError(message=string.NO_LINES_MSG))
        case [*found]:
            for line in found:
                sys.stdout.write(line)
                events.emit(events.LinesShown(line=line))
        case _:
            events.emit(events.UnreachableError(message=string.UNREACHABLE_ERROR))


def setup() -> None:
    """Register the view event."""
    events.register(events.LinesFound, print_lines)
