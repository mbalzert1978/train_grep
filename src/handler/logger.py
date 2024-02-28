"""Log events to stdout."""
import dataclasses
import logging
import logging.config
import sys

import events

LEVEL = logging.INFO
STREAM = sys.stdout


def handle_info(event: events.Event) -> None:
    """Log the event."""
    logger = logging.getLogger(__name__)
    logger.info(event)


def handle_error(err_event: events.Error) -> None:
    """Log the event."""
    logger = logging.getLogger(__name__)
    logger.error(dataclasses.asdict(err_event))


def setup() -> None:
    """Register the logger events."""
    for event in events.Event.__subclasses__():
        events.register(event, handle_info)
    for err_event in events.Error.__subclasses__():
        events.register(err_event, handle_error)


