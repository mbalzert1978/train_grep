import tempfile

import handler
import commands
import events

from tests.stub import CallableStub
from tests import resources


def test_fetch_lines_invokes_find_lines(register) -> None:
    # Arrange
    stub: CallableStub[commands.FindLines]
    stub = register(CallableStub(), commands.FindLines)
    with tempfile.NamedTemporaryFile(delete=False) as file:
        file.writelines(line.encode() for line in resources.LINES)
    event = events.ArgumentsParsed(path=file.name, pattern=resources.PATTERN)

    # Act
    handler.file.fetch_lines(event)

    # Assert
    assert stub.called_with.pop().lines == resources.LINES


def test_fetch_lines_directory_error_invokes_path_is_directory_error(register) -> None:
    # Arrange
    stub: CallableStub[events.PathIsADirectoryError]
    stub = register(CallableStub(), events.PathIsADirectoryError)
    with tempfile.TemporaryDirectory() as directory:
        event = events.ArgumentsParsed(path=directory, pattern=resources.PATTERN)

        # Act
        handler.file.fetch_lines(event)

    # Assert
    assert isinstance(stub.called_with.pop(), events.PathIsADirectoryError)


def test_fetch_lines_with_file_not_found_invokes_not_found_error(register):
    # Arrange
    stub: CallableStub[events.PathNotFoundError]
    stub = register(CallableStub(), events.PathNotFoundError)
    event = events.ArgumentsParsed(path=resources.NOT_FOUND_PATH, pattern=resources.PATTERN)

    # Act
    handler.file.fetch_lines(event)

    # Assert
    assert isinstance(stub.called_with.pop(), events.PathNotFoundError)
