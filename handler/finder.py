"""Finder module."""
import re

import commands
import events


def search_pattern(cmd: commands.FindLines) -> None:
    """Find the lines with the given pattern."""
    events.emit(events.LinesFound(line for line in cmd.lines if re.search(cmd.pattern, line)))


def setup() -> None:
    """Register the finder command."""
    commands.register(commands.FindLines, search_pattern)
