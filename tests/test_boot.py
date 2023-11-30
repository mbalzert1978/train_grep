import stout_logger
import parsing
import collector
import finder
import view
import error
from boot import bootstrap
from unittest.mock import MagicMock
import pytest


def test_bootstrap(monkeypatch: pytest.MonkeyPatch) -> None:
    # Arrange
    monkeypatch.setattr(stout_logger, "setup", MagicMock())
    monkeypatch.setattr(parsing, "setup", MagicMock())
    monkeypatch.setattr(collector, "setup", MagicMock())
    monkeypatch.setattr(finder, "setup", MagicMock())
    monkeypatch.setattr(view, "setup", MagicMock())
    monkeypatch.setattr(error, "setup", MagicMock())

    # Act
    bootstrap()

    # Assert
    stout_logger.setup.assert_called_once()
    parsing.setup.assert_called_once()
    collector.setup.assert_called_once()
    finder.setup.assert_called_once()
    view.setup.assert_called_once()
    error.setup.assert_called_once()
