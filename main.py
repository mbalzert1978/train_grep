"""Main module."""
import sys

import collector
import commands
import error
import finder
import stout_logger
import view


def bootstrap() -> None:
    """Set up the handler."""
    stout_logger.setup()
    collector.setup()
    finder.setup()
    view.setup()
    error.setup()


def main() -> None:
    """Bootstrap."""
    bootstrap()
    commands.post_command(commands.ParseArgs(sys.argv))


if __name__ == "__main__":
    main()
