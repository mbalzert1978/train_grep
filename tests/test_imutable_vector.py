import pytest

from model.vector import ImutableVector


def test_vector_init():
    vec_int = ImutableVector(range(1, 4))
    vec_str = ImutableVector(str(x) for x in range(1, 4))

    assert vec_int == [1, 2, 3]
    assert vec_str == ["1", "2", "3"]

    with pytest.raises(TypeError):
        vec_int[0] = 0

    with pytest.raises(AttributeError):
        vec_int.c = 0


def test_skip():
    vec = ImutableVector(range(2))
    assert vec.skip(1) == ImutableVector([1])
    assert vec.skip(2) == ImutableVector([])
    assert vec.skip(3) == ImutableVector([])


def test_next():
    vec = ImutableVector(range(2))
    assert vec.next() == 0
    assert vec.next() == 1
    assert vec.next() is None


def test_repr() -> None:
    vec = ImutableVector([1, 2, 3])

    assert repr(vec) == "ImutableVector(1, 2, 3)"


def test_str() -> None:
    vec = ImutableVector([1, 2, 3])

    assert str(vec) == "(1, 2, 3)"
    assert vec == eval(str(vec))


def test_hash() -> None:
    assert hash(ImutableVector([1, 2, 3])) == 6


def test_unequality() -> None:
    vec1 = ImutableVector([1, 2, 3])
    vec2 = ImutableVector([1, 2])

    assert vec1 != vec2


def test_equality() -> None:
    vec1 = ImutableVector([1, 2, 3])
    vec2 = ImutableVector([1, 2, 3])

    assert vec1 == vec2
