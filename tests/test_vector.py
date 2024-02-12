import pytest

from model.vector import Vector


def test_vector_init():
    vec_int = Vector(range(1, 4))
    vec_str = Vector(str(x) for x in range(1, 4))

    assert vec_int == [1, 2, 3]
    assert vec_str == ["1", "2", "3"]

    with pytest.raises(TypeError):
        vec_int[0] = 0

    with pytest.raises(AttributeError):
        vec_int.c = 0

    with pytest.raises(TypeError):
        vec_int["a"]


def test_skip():
    vec = Vector(range(2))
    assert vec.skip(1) == Vector([1])
    assert vec.skip(2) == Vector([])
    assert vec.skip(3) == Vector([])


def test_next():
    vec = Vector(range(2))
    assert vec.next() == 0
    assert vec.next() == 1
    assert vec.next() is None


def test_repr() -> None:
    vec = Vector([1, 2, 3])

    assert repr(vec) == "Vector(1, 2, 3)"


def test_str() -> None:
    vec = Vector([1, 2, 3])

    assert str(vec) == "(1, 2, 3)"
    assert vec == eval(str(vec))


def test_hash() -> None:
    assert hash(Vector([1, 2, 3])) == 6


def test_unequality() -> None:
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([1, 2])

    assert vec1 != vec2


def test_equality() -> None:
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([1, 2, 3])

    assert vec1 == vec2
