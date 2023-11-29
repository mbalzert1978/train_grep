"""Parser module."""

import commands
import events


def parse(args: commands.ParseArgs) -> None:
    """Parse the arguments."""
    iter_args = iter(args.args)
    _ = next(iter_args)
    if (path := next(iter_args, None)) is None:
        msg = "error: The following required arguments were not provided:\n\t <PATH>\n"
        events.post_event(events.NoPathGivenError(msg))
        return
    if (regex := next(iter_args, None)) is None:
        msg = "error: The following required arguments were not provided:\n\t <PATTERN>\n"
        events.post_event(events.NoRegexGivenError(msg))
        return
    events.post_event(events.ArgumentsParsed(path, regex))


def setup() -> None:
    """Register the parser command."""
    commands.register(commands.ParseArgs, parse)
