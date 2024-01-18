import typing


class CallableStub:
    def __init__(self, to_raise: type[Exception] | None = None) -> None:
        self.called = False
        self.called_with: list[typing.Any] = []
        self.to_raise = to_raise

    def __call__[T](self, cmd: T) -> None:
        self.called = True
        self.called_with.append(cmd)
        if self.to_raise is None:
            return
        raise self.to_raise()
