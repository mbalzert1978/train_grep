import pytest

import commands
from tests.stub import CallableStub


@pytest.mark.usefixtures("cleanup")
def test_invoke(register) -> None:
    # Arrange
    assert not commands.subscribers
    stub = register(CallableStub(), commands.Command)

    # Act
    commands.invoke(commands.Command())

    # Assert
    assert stub.called_with == [commands.Command()]
