"""Main module."""
import sys

import boot
import commands
import events


def main() -> None:
    """Bootstrap."""
    events.emit(events.StartUp())
    commands.invoke(commands.ParseArgs(sys.argv))


if __name__ == "__main__":
    boot.bootstrap()
    main()
