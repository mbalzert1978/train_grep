import sys

import pytest

from model.vector import MutableVector, OutofBoundsError


def test_vector_init():
    vec_int = MutableVector(range(1, 4))
    vec_str = MutableVector(str(x) for x in range(1, 4))

    assert vec_int._items == [1, 2, 3]
    assert vec_str._items == ["1", "2", "3"]

    vec_int.insert(0, 0)
    assert vec_int == MutableVector(range(4))

    vec_str[5] = "4"
    assert vec_str == MutableVector(str(x) for x in range(1, 5))

    assert len(vec_int) == 4

    assert vec_str.pop() == "4"

    assert vec_str[0] == "1"

    assert vec_int != [0, 1, 2, 3]


def test_vector_with_capacity():
    vec = MutableVector.with_capacity(10)
    assert vec._items == [None] * 10


def test_vector_with_capacity_out_bounds():
    with pytest.raises(OutofBoundsError):
        MutableVector.with_capacity(sys.maxsize + 1)


def test_skip():
    vec = MutableVector(range(2))
    assert vec.skip(1) == MutableVector([1])
    assert vec.skip(2) == MutableVector([])
    assert vec.skip(3) == MutableVector([])


def test_next():
    vec = MutableVector(range(2))
    assert vec.next() == 0
    assert vec.next() == 1
    assert vec.next() is None


def test_repr() -> None:
    vec = MutableVector([1, 2, 3])

    assert repr(vec) == "MutableVector([1, 2, 3])"
    assert vec == eval(repr(vec))


def test_str() -> None:
    vec = MutableVector([1, 2, 3])

    assert str(vec) == "MutableVector([1, 2, 3])"
    assert vec == eval(str(vec))
