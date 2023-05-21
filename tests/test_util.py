from src.utiles.util import find, show


def test_find(repo_stub):
    assert find({"path": "", "value": "2"}, repo_stub) == ("line2",)
    assert repo_stub._called


def test_show(capsys):
    show(("line1", "line2", "line3"))
    out, _ = capsys.readouterr()
    assert out == "line1\nline2\nline3\n"
