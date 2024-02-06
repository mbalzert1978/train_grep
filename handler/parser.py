"""Parser module."""

import commands
import events
from resources import string


def parse(cmd: commands.ParseArgs) -> None:
    """Parse the arguments."""
    events.emit(events.StartUp())
    match cmd.args:
        case [_, path, pattern]:
            events.emit(events.ArgumentsParsed(path, pattern))
        case [_, path]:
            events.emit(events.NoPatternGivenError(string.PATTERN_ERROR))
        case [_]:
            events.emit(events.NoPathGivenError(string.PATH_ERROR))
        case _:
            events.emit(events.Error(string.UNREACHABLE_ERROR))


def setup() -> None:
    """Register the parser command."""
    commands.register(commands.ParseArgs, parse)
