"""Finder module."""
import re

import commands
import events


def find(cmd: commands.FindLines) -> None:
    """Find the lines with the given regex."""
    events.post_event(events.LinesCollected(line for line in cmd.lines if re.search(cmd.regex, line)))


def setup() -> None:
    """Register the finder command."""
    commands.register(commands.FindLines, find)
