import pytest
import commands
import events
import collections
from tests.stub import CallableStub

Message = type[events.Event] | type[commands.Command]


@pytest.fixture()
def cleanup() -> None:
    commands.subscribers = {}
    events.subscribers = collections.defaultdict(list)


@pytest.fixture
def register():
    def _register(stub: CallableStub, message: Message) -> CallableStub:
        match message:
            case _ if issubclass(message, commands.Command):
                commands.register(message, stub)
            case _ if issubclass(message, events.Event):
                events.register(message, stub)
        return stub

    return _register
