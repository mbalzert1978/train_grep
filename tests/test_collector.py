import pathlib
import tempfile
from unittest.mock import MagicMock

import collector
import commands
import events


def setup_test_file(msg: str) -> tempfile._TemporaryFileWrapper:
    fp = tempfile.NamedTemporaryFile(delete_on_close=False)
    fp.write(msg.encode())
    fp.close()
    return fp


def test_collect_lines_with_str_path():
    # Arrange
    msg = "test line"
    fp = setup_test_file(msg)
    event = events.ArgumentsParsed(path=fp.name, regex="test")
    commands.invoke = MagicMock()

    # Act
    collector.collect_lines(event)

    # Assert
    commands.invoke.assert_called_once_with(commands.FindLines((msg,), "test"))


def test_collect_lines_with_file_not_found():
    # Arrange
    event = events.ArgumentsParsed(path="nonexistent.txt", regex="test")
    events.emit = MagicMock()

    # Act
    collector.collect_lines(event)

    # Assert
    events.emit.assert_called_once_with(
        events.PathNotFoundError(
            message="File not found: nonexistent.txt",
            path=pathlib.PosixPath("nonexistent.txt"),
        )
    )
