"""Main module."""
import logging
import sys

import collector
import commands
import error
import finder
import view


def setup_logging() -> None:
    """Set up the logging."""
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        level=logging.INFO,
        stream=sys.stdout,
    )

def bootstrap() -> None:
    """Set up the handler."""
    collector.setup()
    finder.setup()
    view.setup()
    error.setup()
    setup_logging()


def main() -> None:
    """Bootstrap."""
    bootstrap()
    commands.post_command(commands.ParseArgs(sys.argv))


if __name__ == "__main__":
    main()
