import commands
import events
import handler
from tests.stub import CallableStub
from tests import resources


def test_parser_all_arguments_set_emits_arguments_parsed(register) -> None:
    # Arrange
    stub: CallableStub[events.ArgumentsParsed | events.StartUp]
    stub = register(register(CallableStub(), events.StartUp), events.ArgumentsParsed)
    cmd = commands.ParseArgs(resources.ARGS)

    # Act
    handler.parser.parse(cmd)

    # Assert
    result = stub.called_with.pop()
    assert isinstance(result, events.ArgumentsParsed)
    assert result.path == resources.ARGS[1]
    assert result.pattern == resources.ARGS[2]
    assert isinstance(stub.called_with.pop(), events.StartUp)


def test_parser_no_arguments_set_emits_no_path_given_error(register) -> None:
    # Arrange
    stub: CallableStub[events.NoPathGivenError]
    stub = register(CallableStub(), events.NoPathGivenError)
    cmd = commands.ParseArgs([resources.ARGS[0]])

    # Act
    handler.parser.parse(cmd)

    # Assert
    assert isinstance(stub.called_with.pop(), events.NoPathGivenError)


def test_parser_no_pattern_argument_set_emits_no_pattern_given_error(register) -> None:
    # Arrange
    stub: CallableStub[events.NoPatternGivenError]
    stub = register(CallableStub(), events.NoPatternGivenError)
    cmd = commands.ParseArgs(resources.ARGS[:-1])

    # Act
    handler.parser.parse(cmd)

    # Assert
    assert isinstance(stub.called_with.pop(), events.NoPatternGivenError)


def test_parser_error_on_transfering_args_emits_error(register) -> None:
    # Arrange
    stub: CallableStub[events.Error]
    stub = register(CallableStub(), events.Error)
    cmd = commands.ParseArgs([])

    # Act
    handler.parser.parse(cmd)

    # Assert
    assert isinstance(stub.called_with.pop(), events.Error)
