import logging
import typing

import commands
import events

logger = logging.getLogger(__name__)

type Message = commands.Command | events.Event


class MessageBus:
    def __init__(
        self,
        event_handlers: dict[type[events.Event], list[typing.Callable]],
        command_handlers: dict[type[commands.Command], typing.Callable],
    ):
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers

    def handle(self, message: Message):
        self.queue = [message]
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, events.Event):
                self.handle_event(message)
            elif isinstance(message, commands.Command):
                self.handle_command(message)
            else:
                msg = f"{message} was not an Event or Command"
                raise TypeError(msg)

    def handle_event(self, event: events.Event):
        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug("handling event %s with handler %s", event, handler)
                handler(event)
            except Exception:
                logger.exception("Exception handling event %s", event)
                continue

    def handle_command(self, command: commands.Command):
        logger.debug("handling command %s", command)
        try:
            handler = self.command_handlers[type(command)]
            handler(command)
        except Exception:
            logger.exception("Exception handling command %s", command)
            raise
