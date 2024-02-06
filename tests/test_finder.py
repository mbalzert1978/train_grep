import commands
import events
import handler
from tests.stub import CallableStub
from tests import resources


def test_finder_finds_all_lines(register) -> None:
    # Arrange
    stub: CallableStub[events.LinesFound]
    stub = register(CallableStub(), events.LinesFound)

    # Act
    handler.finder.search_pattern(commands.FindLines(resources.LINES, "sun"))

    # Assert
    assert list(stub.called_with.pop().found) == ["The sun is shining in the sky.\n"]
