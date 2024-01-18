import dataclasses

import pytest
import error
import events


@dataclasses.dataclass
class ErrorStub:
    message: str


def test_handle(capsys) -> None:
    error.handle_error(ErrorStub("foo"))

    out, err = capsys.readouterr()

    assert err == "foo"
    assert out == ""


@pytest.mark.usefixtures("cleanup")
def test_setup() -> None:
    assert not events.subscribers

    error.setup()

    assert events.Error.__subclasses__() == list(events.subscribers)
