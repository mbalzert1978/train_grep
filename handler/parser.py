"""Parser module."""

import commands
import events
from resources import string


def parse(cmd: commands.ParseArgs) -> None:
    """Parse the arguments."""
    events.emit(events.StartUp())
    match cmd.args:
        case [_, path, regex]:
            events.emit(events.ArgumentsParsed(path, regex))
        case [_, path]:
            events.emit(events.NoRegexGivenError(string.PATTERN_ERROR))
        case [_]:
            events.emit(events.NoPathGivenError(string.PATH_ERROR))
        case _:
            events.emit(events.Error(string.UNREACHABLE_ERROR))


def setup() -> None:
    """Register the parser command."""
    commands.register(commands.ParseArgs, parse)
