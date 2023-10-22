from model.vector import MutableVector


def test_vector_init():
    vec = MutableVector([1, 2, 3])
    assert vec._items == [1, 2, 3]


def test_vector_with_capacity():
    vec = MutableVector.with_capacity(10)
    assert vec._items == [None] * 10
