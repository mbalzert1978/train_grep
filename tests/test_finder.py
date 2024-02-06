import commands
import events
import handler
from tests.stub import CallableStub


def test_finder_finds_all_lines(register) -> None:
    # Arrange
    stub: CallableStub = register(CallableStub(), events.LinesCollected)
    lines = ("Dies ist ein,", "test file", "das bestimmte", "test worte endhaelt")

    # Act
    handler.finder.search_pattern(commands.FindLines(lines, "test"))

    # Assert
    assert list(stub.called_with.pop().found) == ["test file", "test worte endhaelt"]
