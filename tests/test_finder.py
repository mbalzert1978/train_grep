import commands
import events
import handler
from tests.stub import CallableStub


def test_finder_finds_all_lines(register) -> None:
    # Arrange
    stub: CallableStub = register(CallableStub(), events.LinesCollected)
    lines = (
        "This is an example of a sentence.",
        "Python is a popular programming language.",
        "The sun is shining in the sky.",
        "This is another sentence.",
        "The world is full of possibilities.",
    )

    # Act
    handler.finder.search_pattern(commands.FindLines(lines, "sun"))

    # Assert
    assert list(stub.called_with.pop().found) == ["The sun is shining in the sky."]
