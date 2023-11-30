"""Main module."""
import sys

import boot
import commands


def main() -> None:
    """Bootstrap."""
    boot.bootstrap()
    commands.invoke(commands.ParseArgs(sys.argv))


if __name__ == "__main__":
    main()
