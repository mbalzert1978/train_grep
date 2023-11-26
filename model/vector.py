"""Mutable Vector."""
from __future__ import annotations

import operator
import reprlib
import sys
from collections.abc import Iterator, MutableSequence, Sequence
from typing import Iterable, Self, SupportsIndex, overload


class OutofBoundsError(Exception):

    """Exception raised when an index is out of bounds."""


class ImutableVector[T](Sequence):

    """An immutable Vector."""

    __slots__ = ("_components", "_index")

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
        if isinstance(__index, slice):
            cls = type(self)
            return cls(self._components[__index])
        index = operator.index(__index)
        return self._components[index]

    def __iter__(self) -> Iterator:
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
        components = reprlib.repr(self._components).replace("[", "]").replace("]", "")
        return f"{type(self).__name__}({components})"

    def __str__(self) -> str:
        """Return a string representation."""
        return str(tuple(self))

    def __hash__(self) -> int:
        """Return the hash value of this vector."""
        return sum(hash(x) for x in self._components)

    def __len__(self) -> int:
        """Return the number of items."""
        return len(self._components)

    def skip(self, n: int) -> Self:
        """
        Create an iterator that skips the first n elements.

        skip(n) skips elements until n elements are skipped or the end of the iterator is reached (whichever happens first).
        After that, all the remaining elements are returned.
        In particular, if the original iterator is too short, then the returned iterator is empty.

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
        Advances the iterator and returns the next value.

        Returns None when iteration is finished.

        Examples
        --------
        Basic usage:
            foo = MutableVector([1, 2, 3])
            foo.next()
        """
        if self._index >= len(self._components):
            return None
        self._index += 1
        return self._components[self._index - 1]


class MutableVector[T](ImutableVector, MutableSequence):

    """A mutable Vector."""

    @classmethod
    def with_capacity(cls, capacity: int = 0) -> Self:
        """Create a mutable vector with the given capacity."""
        if capacity > sys.maxsize:
            msg = f"Capacity {capacity} is too large."
            raise OutofBoundsError(msg)
        return cls([]) if capacity <= 0 else cls(None for _ in range(capacity))

    @overload
    def __getitem__(self, __index: int, /) -> T:
        ...

    @overload
    def __getitem__(self, __index: slice, /) -> Self:
        ...

    def __getitem__(self, __index):
        """Return the item at the given index."""
        if isinstance(__index, slice):
            cls = type(self)
            return cls(self._components[__index])
        index = operator.index(__index)
        return self._components[index]

    @overload
    def __setitem__(self, index: int, value: T, /) -> None:
        ...

    @overload
    def __setitem__(self, index: slice, value: Iterable[T], /) -> None:
        ...

    def __setitem__(self, index, value):
        """Set the item at the given index."""
        self._components.insert(index, value)

    @overload
    def __delitem__(self, index: int, /) -> None:
        ...

    @overload
    def __delitem__(self, index: slice, /) -> None:
        ...

    def __delitem__(self, index):
        """Delete the item at the given index."""
        self._components.pop(index)

    def insert(self, __index: SupportsIndex, __object: T) -> None:
        """Insert a value at the given index."""
        self._components.insert(__index, __object)
