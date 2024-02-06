import commands
import events
import handler
from tests.stub import CallableStub


def test_parser_all_arguments_set_emits_arguments_parsed(register) -> None:
    # Arrange
    stub: CallableStub = register(register(CallableStub(), events.StartUp), events.ArgumentsParsed)
    args = ["python_file_name.py", "test file", "pattern"]
    cmd = commands.ParseArgs(args)

    # Act
    handler.parser.parse(cmd)

    # Assert
    result: events.ArgumentsParsed = stub.called_with.pop()
    assert result.path == args[1]
    assert result.pattern == args[2]
    assert isinstance(stub.called_with.pop(), events.StartUp)


def test_parser_no_arguments_set_emits_no_path_given_error(register) -> None:
    # Arrange
    stub: CallableStub = register(CallableStub(), events.NoPathGivenError)
    args = ["python_file_name.py"]
    cmd = commands.ParseArgs(args)

    # Act
    handler.parser.parse(cmd)

    # Assert
    assert isinstance(stub.called_with.pop(), events.NoPathGivenError)


def test_parser_no_pattern_argument_set_emits_no_pattern_given_error(register) -> None:
    # Arrange
    stub: CallableStub = register(CallableStub(), events.NoPatternGivenError)
    args = ["python_file_name.py", "test file"]
    cmd = commands.ParseArgs(args)

    # Act
    handler.parser.parse(cmd)

    # Assert
    assert isinstance(stub.called_with.pop(), events.NoPatternGivenError)


def test_parser_error_on_transfering_args_emits_error(register) -> None:
    # Arrange
    stub: CallableStub = register(CallableStub(), events.Error)
    cmd = commands.ParseArgs([])

    # Act
    handler.parser.parse(cmd)

    # Assert
    assert isinstance(stub.called_with.pop(), events.Error)
