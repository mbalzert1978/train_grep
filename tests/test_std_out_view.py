import events
import handler
from tests.stub import CallableStub


def test_std_out_view_writes_found_lines_to_std_out(register, capsys) -> None:
    # Arrange
    stub: CallableStub = register(CallableStub(), events.LinesShown)
    lines = ("Dies ist ein,", "test file", "das bestimmte", "test worte endhaelt")
    expected = [events.LinesShown(line=line) for line in lines]

    # Act
    handler.std_out_viewer.print_lines(events.LinesCollected(lines))

    # Assert
    captured = capsys.readouterr()
    assert captured.out == "".join(lines)
    assert stub.called_with == expected


def test_std_out_view_emits_no_lines_found_error_if_no_lines_found(register) -> None:
    # Arrange
    stub: CallableStub = register(CallableStub(), events.NoLinesFoundError)

    # Act
    handler.std_out_viewer.print_lines(events.LinesCollected([]))

    # Assert
    assert isinstance(stub.called_with.pop(), events.NoLinesFoundError)
