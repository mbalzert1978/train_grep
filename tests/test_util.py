from main import find, show


def test_find():
    assert tuple(find(["line1", "line2", "line3"], "2")) == ("line2",)


def test_show(capsys):
    show(("line1\n", "line2\n", "line3\n"))
    result, _ = capsys.readouterr()
    assert result == "line1\nline2\nline3\n"
