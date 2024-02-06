"""View module."""
import sys

import events
from resources import string


def print_lines(event: events.LinesFound) -> None:
    """Print the found lines."""
    match list(event.found):
        case [*found]:
            for line in found:
                sys.stdout.write(line)
                events.emit(events.LinesShown(line=line))
        case []:
            events.emit(events.NoLinesFoundError(message=string.NO_LINES_MSG))
        case _:
            events.emit(events.UnreachableError(message=string.UNREACHABLE_ERROR))


def setup() -> None:
    """Register the view event."""
    events.register(events.LinesFound, print_lines)
