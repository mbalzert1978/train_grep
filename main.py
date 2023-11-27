"""Main module."""
import sys

import message_bus


def main() -> None:
    """Bootstrap."""
    bus = message_bus.MessageBus()
    bus.handle(sys.argv)


if __name__ == "__main__":
    main()
