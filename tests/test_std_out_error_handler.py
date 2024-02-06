import events
import handler


def test_std_out_error_handler_writes_error_to_std_err(capsys) -> None:
    # Arrange
    expected = "Error Message"

    # Act
    handler.std_out_error_handler.handle_error(events.Error(expected))

    # Assert
    captured = capsys.readouterr()
    assert captured.err == expected
