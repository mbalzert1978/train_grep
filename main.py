from __future__ import annotations

from src.utiles.util import find, set_arg_parse, show


def main() -> None:
    show(find(vars(set_arg_parse().parse_args())))


if __name__ == "__main__":
    main()
