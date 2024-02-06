from boot import bootstrap
from unittest.mock import MagicMock, call
import pytest
import commands
import events
import handler


def test_bootstrap(monkeypatch: pytest.MonkeyPatch) -> None:
    # Arrange
    monkeypatch.setattr(events, "register", MagicMock())
    monkeypatch.setattr(commands, "register", MagicMock())
    expected_commands = [
        call(commands.ParseArgs, handler.parser.parse),
        call(commands.FindLines, handler.finder.search_pattern),
    ]
    expected_events = [
        call(events.StartUp, handler.std_out_logger.log_info),
        call(events.ArgumentsParsed, handler.std_out_logger.log_info),
        call(events.LinesCollected, handler.std_out_logger.log_info),
        call(events.LinesShown, handler.std_out_logger.log_info),
        call(events.Error, handler.std_out_logger.log_info),
        call(events.NoPathGivenError, handler.std_out_logger.log_error),
        call(events.NoPatternGivenError, handler.std_out_logger.log_error),
        call(events.PathNotFoundError, handler.std_out_logger.log_error),
        call(events.PathPermissionError, handler.std_out_logger.log_error),
        call(events.PathIsADirectoryError, handler.std_out_logger.log_error),
        call(events.NoLinesFoundError, handler.std_out_logger.log_error),
        call(events.ArgumentsParsed, handler.file_handler.fetch_lines),
        call(events.LinesCollected, handler.std_out_viewer.print_lines),
        call(events.NoPathGivenError, handler.std_out_error_handler.handle_error),
        call(events.NoPatternGivenError, handler.std_out_error_handler.handle_error),
        call(events.PathNotFoundError, handler.std_out_error_handler.handle_error),
        call(events.PathPermissionError, handler.std_out_error_handler.handle_error),
        call(events.PathIsADirectoryError, handler.std_out_error_handler.handle_error),
        call(events.NoLinesFoundError, handler.std_out_error_handler.handle_error),
    ]

    # Act
    bootstrap()

    # Assert
    assert list(commands.register.call_args_list) == expected_commands
    assert list(events.register.call_args_list) == expected_events
