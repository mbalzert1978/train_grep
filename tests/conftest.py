import pytest
import commands
import events
import collections


@pytest.fixture()
def cleanup() -> None:
    commands.subscribers = {}
    events.subscribers = collections.defaultdict(list)
