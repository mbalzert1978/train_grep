"""Mutable Vector."""
import sys
from collections.abc import MutableSequence
from typing import Self, Sequence, SupportsIndex


class OutofBoundsError(Exception):

    """Exception raised when an index is out of bounds."""


class MutableVector[T](MutableSequence):

    """A mutable sequence."""

    def __init__(self, items: Sequence[T], n: int = 0) -> None:
        self._items = list(items)
        self._n = n
        super().__init__()

    @classmethod
    def with_capacity(cls, capacity: int = 0) -> Self:
        """Create a mutable vector with the given capacity."""
        if capacity > sys.maxsize:
            msg = f"Capacity {capacity} is too large."
            raise OutofBoundsError(msg)
        return cls([]) if capacity <= 0 else cls(None for _ in range(capacity))

    def __eq__(self, __value: object) -> bool:
        """Return True if the given object is equal to this vector."""
        if not isinstance(__value, type(self)):
            return False
        return self._items == __value._items

    def __repr__(self) -> str:
        """Return a string representation."""
        return f"{type(self).__name__}({self._items!r})"

    def __str__(self) -> str:
        """Return a string representation."""
        return f"{type(self).__name__}({self._items!s})"

    def __getitem__(self, index: int) -> T:
        """Return the item at the given index."""
        self._n = index
        return self._items[index]

    def __setitem__(self, index: int, value: T) -> None:
        """Set the item at the given index."""
        self._items.insert(index, value)

    def __delitem__(self, index: int) -> None:
        """Delete the item at the given index."""
        self._items.pop(index)

    def __len__(self) -> int:
        """Return the number of items."""
        return len(self._items)

    def insert(self, __index: SupportsIndex, __object: T) -> None:
        """Insert a value at the given index."""
        self._items.insert(__index, __object)

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
        return type(self)(self._items[n:])

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
        if self._n >= len(self._items):
            return None
        self._n += 1
        return self._items[self._n - 1]


MutableSequence.register(MutableVector)
