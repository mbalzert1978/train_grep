from tests.stub import CallableStub
import pytest
import commands


def test_init() -> None:
    pa = commands.ParseArgs(["foo", "bar"])

    assert pa.args == ["foo", "bar"]

    fl = commands.FindLines(("foo", "bar"), "foo")

    assert fl.lines == ("foo", "bar")
    assert fl.regex == "foo"


def test_register() -> None:
    t = CallableStub()
    commands.register(commands.ParseArgs, t)

    assert commands.subscribers[commands.ParseArgs] == t


@pytest.mark.usefixtures("cleanup")
def test_invoke() -> None:
    t = CallableStub()
    commands.register(commands.ParseArgs, t)

    commands.invoke(commands.ParseArgs(["foo", "bar"]))

    assert t.called
    assert t.called_with == [commands.ParseArgs(args=["foo", "bar"])]
