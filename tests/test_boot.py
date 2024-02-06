import handler
from boot import bootstrap
from unittest.mock import MagicMock
import pytest


def test_bootstrap(monkeypatch: pytest.MonkeyPatch) -> None:
    # Arrange
    monkeypatch.setattr(handler.std_out_logger, "setup", MagicMock())
    monkeypatch.setattr(handler.parser, "setup", MagicMock())
    monkeypatch.setattr(handler.file_handler, "setup", MagicMock())
    monkeypatch.setattr(handler.finder, "setup", MagicMock())
    monkeypatch.setattr(handler.std_out_viewer, "setup", MagicMock())
    monkeypatch.setattr(handler.std_out_error_handler, "setup", MagicMock())

    # Act
    bootstrap()

    # Assert
    handler.std_out_logger.setup.assert_called_once()
    handler.parser.setup.assert_called_once()
    handler.file_handler.setup.assert_called_once()
    handler.finder.setup.assert_called_once()
    handler.std_out_viewer.setup.assert_called_once()
    handler.std_out_error_handler.setup.assert_called_once()
