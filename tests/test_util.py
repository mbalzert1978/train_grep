from main import find_lines, show_lines
from model import MutableVector


def test_find():
    result = find_lines(["line1", "line2", "line3"], "2").unwrap()
    expected = MutableVector(("line2",))
    assert result == expected


def test_show(capsys):
    show_lines(["line1", "line2", "line3"])
    result, _ = capsys.readouterr()
    assert result == "line1\nline2\nline3\n"
