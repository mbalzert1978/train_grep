"""Finder module."""
import functools
import logging
import re

import commands
import events

logger = logging.getLogger(__name__)

def find(cmd: commands.FindLines) -> None:
    """Find the lines with the given regex."""
    events.post_event(events.LinesFound(line for line in cmd.lines if re.search(cmd.regex, line)))


def setup() -> None:
    """Register the finder command."""
    commands.register(commands.FindLines, find)
    events.register(events.LinesFound,functools.partial(logger.info, "Lines found: %s"))
