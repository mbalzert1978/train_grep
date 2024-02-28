"""Main module."""
import sys
import typing

from src import boot
from src import commands


def main(args: typing.Sequence[str]) -> None:
    """Bootstrap."""
    boot.bootstrap()
    commands.invoke(commands.ParseArgs(args))


if __name__ == "__main__":
    main(sys.argv)
