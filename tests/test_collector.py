import pathlib
import tempfile
from unittest.mock import MagicMock

import handler
import commands
import events
import pytest


def setup_test_file(msg: str) -> tempfile._TemporaryFileWrapper:
    fp = tempfile.NamedTemporaryFile(delete_on_close=False)
    fp.write(msg.encode())
    fp.close()
    return fp


def test_collect_lines(monkeypatch: pytest.MonkeyPatch) -> None:
    # Arrange
    msg = "test line"
    fp = setup_test_file(msg)
    event = events.ArgumentsParsed(path=fp.name, regex="test")
    monkeypatch.setattr(commands, "invoke", MagicMock())
    # Act
    handler.file_handler.collect_lines(event)

    # Assert
    commands.invoke.assert_called_once_with(commands.FindLines((msg,), "test"))


def test_collect_lines_with_file_not_found(monkeypatch: pytest.MonkeyPatch):
    # Arrange
    event = events.ArgumentsParsed(path="nonexistent.txt", regex="test")
    monkeypatch.setattr(events, "emit", MagicMock())
    # Act
    handler.file_handler.collect_lines(event)

    # Assert
    events.emit.assert_called_once_with(
        events.PathNotFoundError(
            message="File not found: nonexistent.txt",
            path=pathlib.PosixPath("nonexistent.txt"),
        )
    )


@pytest.mark.usefixtures("cleanup")
def test_setup() -> None:
    assert not events.subscribers

    handler.file_handler.setup()

    assert events.ArgumentsParsed in events.subscribers
