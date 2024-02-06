import pytest

import commands
import events
from boot import bootstrap


@pytest.mark.usefixtures("cleanup")
def test_bootstrap() -> None:
    # Arrange
    assert not events.subscribers
    assert not commands.subscribers

    # Act
    bootstrap()

    # Assert
    assert events.ArgumentsParsed in events.subscribers
    assert events.StartUp in events.subscribers
    assert events.ArgumentsParsed in events.subscribers
    assert events.LinesCollected in events.subscribers
    assert events.LinesShown in events.subscribers
    assert events.Error in events.subscribers
    assert events.NoPathGivenError in events.subscribers
    assert events.NoPatternGivenError in events.subscribers
    assert events.PathNotFoundError in events.subscribers
    assert events.PathPermissionError in events.subscribers
    assert events.PathIsADirectoryError in events.subscribers
    assert events.NoLinesFoundError in events.subscribers
    assert events.ArgumentsParsed in events.subscribers
    assert events.LinesCollected in events.subscribers
    assert events.NoPathGivenError in events.subscribers
    assert events.NoPatternGivenError in events.subscribers
    assert events.PathNotFoundError in events.subscribers
    assert events.PathPermissionError in events.subscribers
    assert events.PathIsADirectoryError in events.subscribers
    assert events.NoLinesFoundError in events.subscribers

    assert commands.ParseArgs in commands.subscribers
    assert commands.FindLines in commands.subscribers
