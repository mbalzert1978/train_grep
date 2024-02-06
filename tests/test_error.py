import dataclasses

import pytest
import handler
import events


@dataclasses.dataclass
class ErrorStub:
    message: str


def test_handle(capsys) -> None:
    handler.std_out_error_handler.handle_error(ErrorStub("foo"))

    out, err = capsys.readouterr()

    assert err == "foo"
    assert out == ""


@pytest.mark.usefixtures("cleanup")
def test_setup() -> None:
    assert not events.subscribers

    handler.std_out_error_handler.setup()

    assert events.Error.__subclasses__() == list(events.subscribers)
