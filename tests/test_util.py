from main import find, show


def test_find():
    assert find(["line1", "line2", "line3"], "2") == ("line2",)


def test_show(capsys):
    show(("line1", "line2", "line3"))
    out, _ = capsys.readouterr()
    assert out == "line1\nline2\nline3\n"
