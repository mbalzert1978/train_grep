"""Log events to stdout."""
import atexit
import dataclasses
import logging
import logging.config
import sys

import events
from resources import default, string

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
    _setup_logging()
    for event in events.Event.__subclasses__():
        events.register(event, handle_info)
    for err_event in events.Error.__subclasses__():
        events.register(err_event, handle_error)


def _setup_logging() -> None:
    logging.config.dictConfig(default.LOGGING_CONFIG)
    match logging.getHandlerByName("queue_handler"):
        case logging.Handler() as queue_handler:
            queue_handler.listener.start()  # type: ignore
            atexit.register(queue_handler.listener.stop)  # type: ignore
        case _:
            logging.basicConfig(format=string.FORMAT, level=LEVEL, stream=STREAM)
