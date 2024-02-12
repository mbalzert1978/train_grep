"""Mutable Vector."""
from __future__ import annotations

import operator
import reprlib
import sys
from collections.abc import Iterator, MutableSequence, Sequence
from typing import Iterable, Self, SupportsIndex, overload

ERROR_MSG_TYPE = "unsupported operand type(s) for *: %s"
ERROR_MSG_OOB = "Capacity %s is too large."
MIN_CAPACITY = 0
DEFAULT_VALUE = None


class OutofBoundsError(Exception):

    """Exception raised when an index is out of bounds."""


class Vector[T](Sequence):

    """An immutable Vector."""

    __slots__ = ("_components", "_index")
    __match_args__ = ("_components",)

    def __init__(self, __iterable: Iterable[T]) -> None:
        self._components = list(__iterable)
        self._index = 0
        super().__init__()

    @overload
    def __getitem__(self, __index: int, /) -> T:
        ...

    @overload
    def __getitem__(self, __index: slice, /) -> Self:
        ...

    def __getitem__(self, __index):
        """Return the item at the given index."""
        cls = type(self)
        match __index:
            case slice():
                return cls(operator.getitem(self._components, __index))
            case int():
                return operator.getitem(self._components, __index)
            case _:
                raise TypeError(ERROR_MSG_TYPE % (type(self).__getitem__.__name__,))

    def __iter__(self) -> Iterator[T]:
        """Return an iterator over the elements of this vector."""
        return iter(self._components)

    def __eq__(self, __other: object) -> bool:
        """Return True if the given object is equal to this vector."""
        try:
            return all(a == b for a, b in zip(self, __other, strict=True))  # type: ignore[call-overload]
        except ValueError:
            return False

    def __repr__(self) -> str:
        """Return a string representation."""
        return f"{type(self).__name__}{tuple(self)}"

    def __str__(self) -> str:
        """Return a string representation."""
        return str(tuple(self))

    def __hash__(self) -> int:
        """Return the hash value of this vector."""
        return sum(hash(component) for component in self._components)

    def __len__(self) -> int:
        """Return the number of items."""
        return len(self._components)

    def skip(self, n: int) -> Self:
        """
        Create an vector that skips the first n elements.

        skip(n) skips elements until n elements are skipped or
          the end of the iterator is reached (whichever happens first).
        After that, all the remaining elements are returned.
        In particular, if the original iterator is too short,
          then the returned iterator is empty.

        Examples
        --------
        Basic usage:
            foo = MutableVector([1, 2, 3])
            foo.skip(1)

        """
        cls = type(self)
        return cls(self._components[n:])

    def next(self) -> T | None:
        """
        Advances the vector and returns the next value.

        Returns None when iteration is finished.

        Examples
        --------
        Basic usage:
            foo = MutableVector([1, 2, 3])
            foo.next()

        """
        if self._index >= len(self._components):
            return None
        value = operator.getitem(self._components, self._index)
        self._index += 1
        return value


Sequence.register(Vector)


class MutableVector[T](Vector, MutableSequence):

    """A mutable Vector."""

    @classmethod
    def with_capacity(cls, capacity: int = MIN_CAPACITY) -> Self:
        """Create a mutable vector with the given capacity."""
        if capacity > sys.maxsize:
            raise OutofBoundsError(ERROR_MSG_OOB)
        if capacity <= MIN_CAPACITY:
            capacity = MIN_CAPACITY
        return cls([DEFAULT_VALUE] * capacity)

    def __repr__(self) -> str:
        """Return a string representation."""
        components = reprlib.repr(self._components).strip("[]")
        return f"{type(self).__name__}({components})"

    @overload
    def __getitem__(self, __index: int, /) -> T:
        ...

    @overload
    def __getitem__(self, __index: slice, /) -> Self:
        ...

    def __getitem__(self, __index):
        """Return the item at the given index."""
        return super().__getitem__(__index)

    @overload
    def __setitem__(self, index: int, value: T, /) -> None:
        ...

    @overload
    def __setitem__(self, index: slice, value: Iterable[T], /) -> None:
        ...

    def __setitem__(self, index, value):
        """Set the item at the given index."""
        operator.setitem(self._components, index, value)

    @overload
    def __delitem__(self, index: int, /) -> None:
        ...

    @overload
    def __delitem__(self, index: slice, /) -> None:
        ...

    def __delitem__(self, index):
        """Delete the item at the given index."""
        operator.delitem(self._components, index)

    def insert(self, __index: SupportsIndex, __object: T) -> None:
        """Insert a value at the given index."""
        self._components.insert(__index, __object)


MutableSequence.register(MutableVector)
