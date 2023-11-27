"""Main module."""
import sys

import collector
import error
import finder
import view


def bootstrap() -> None:
    """Set up the handler."""
    collector.setup()
    finder.setup()
    view.setup()
    error.setup()


def main() -> None:
    """Bootstrap."""
    bootstrap()
    collector.parse(sys.argv)


if __name__ == "__main__":
    main()
