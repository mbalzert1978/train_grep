"""Main module."""
import sys

import boot
import commands
import events


def main() -> None:
    """Bootstrap."""
    events.post_event(events.StartUp())
    commands.post_command(commands.ParseArgs(sys.argv))


if __name__ == "__main__":
    boot.bootstrap()
    main()
