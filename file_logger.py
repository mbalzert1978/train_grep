"""Log events to stdout."""
import dataclasses
import logging

import events

logging.basicConfig(filename="stout.log", format="%(asctime)s %(levelname)s %(name)s %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def info(event: events.Event) -> None:
    """Log the event."""
    logger.info(event)


def error(err_event: events.Error) -> None:
    """Log the event."""
    logger.error(dataclasses.asdict(err_event))


def setup() -> None:
    """Register the logger events."""
    for event in events.Event.__subclasses__():
        events.register(event, info)
    for err_event in events.Error.__subclasses__():
        events.register(err_event, error)
