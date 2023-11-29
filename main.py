"""Main module."""
import sys

import arg_parser
import collector
import commands
import error
import events
import finder
import stout_logger
import view


def bootstrap() -> None:
    """Set up the handler."""
    stout_logger.setup()
    arg_parser.setup()
    collector.setup()
    finder.setup()
    view.setup()
    error.setup()


def main() -> None:
    """Bootstrap."""
    bootstrap()
    events.post_event(events.StartUp())
    commands.post_command(commands.ParseArgs(sys.argv))


if __name__ == "__main__":
    main()
