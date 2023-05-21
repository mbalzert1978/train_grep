import pytest


class RepoStub:
    def __init__(self):
        self._called = False

    def read_lines(self, _):
        self._called = True
        return ["line1", "line2", "line3"]


@pytest.fixture()
def repo_stub():
    return RepoStub()
