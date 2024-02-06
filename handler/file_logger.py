"""Log events to stdout."""
import dataclasses
import logging

import events
from resources import string

LEVEL = logging.INFO

logging.basicConfig(filename=string.FILE_NAME, format=string.FORMAT, level=LEVEL)
logger = logging.getLogger(__name__)


def log_info(event: events.Event) -> None:
    """Log the event."""
    logger.info(event)


def log_error(err_event: events.Error) -> None:
    """Log the event."""
    logger.error(dataclasses.asdict(err_event))


def setup() -> None:
    """Register the logger events."""
    for event in events.Event.__subclasses__():
        events.register(event, log_info)
    for err_event in events.Error.__subclasses__():
        events.register(err_event, log_error)
