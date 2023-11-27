import pathlib
import re
import sys
from collections.abc import Iterable

import commands
import events


def parse(cmd: commands.ParseArguments, handler: AbstractHandler):
    parse_args(cmd.args)


def collect_lines_from(path: Pathlike) -> tuple[str, ...]:
    """Collect lines from a pathlike."""
    if isinstance(path, str):
        path = pathlib.Path(path)
    with path.open(encoding="utf8") as file:
        return tuple(file)


def find(lines: Iterable, regex: str) -> Iterable[str]:
    """Find the lines with the given regex."""
    for line in lines:
        if re.search(regex, line):
            yield line


def show(found: Iterable) -> None:
    """Show the found lines."""
    for line in found:
        sys.stdout.write(line)


EVENT_HANDLERS = {
    events.Allocated: [publish_allocated_event, add_allocation_to_read_model],
    events.Deallocated: [remove_allocation_from_read_model, reallocate],
    events.OutOfStock: [send_out_of_stock_notification],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.Allocate: allocate,
    commands.CreateBatch: add_batch,
    commands.ChangeBatchQuantity: change_batch_quantity,
}
