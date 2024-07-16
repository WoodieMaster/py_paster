from typing import Any, Self
from abc import ABC, abstractmethod

type IterItem = tuple[str, str]


class DoubleIter(ABC):
    def __iter__(self) -> Self:
        return self

    def __next__(self) -> IterItem:
        return self.next()

    @abstractmethod
    def next(self, amount: int = 1) -> IterItem:
        """
        moves forwards `amount` items and returns that item

        Raises StopIteration if it would skip past the start

        Raises ValueError if the amount is negative
        :param amount: how many items to go backwards
        :return: the item `amount` items before the current one
        """
        pass

    @abstractmethod
    def previous(self, amount: int = 1) -> IterItem:
        """
        moves backwards `amount` items and returns that item

        Raises StopIteration if it would skip past the start

        Raises ValueError if the amount is negative
        :param amount: how many items to go backwards
        :return: the item `amount` items before the current one
        """
        pass

    @abstractmethod
    def current(self) -> IterItem:
        """
        :return: the current item of the iterator
        """
        pass

    def __getitem__(self, item_id: Any) -> IterItem:
        if type(item_id) is not str:
            raise TypeError(f"Expected type 'str' for id, got '{type(item_id)}' instead")

        return self.find(item_id)

    @abstractmethod
    def find(self, item_id: str) -> IterItem:
        """
        Search for the id inside the iterator

        Raises ValueError, if the id is not found
        :param item_id: the id associated with an item
        :return: the item tuple if found
        """
        pass


class StrListIter(DoubleIter):
    def __init__(self, data: list[str]):
        self.data: list[str] = data
        self.idx: int = -1

    def next(self, amount: int = 1) -> IterItem:
        if amount < 0:
            raise ValueError("Amount must be greater than or equal to zero")

        if self.idx + amount >= len(self.data):
            raise StopIteration

        self.idx += amount

        return str(self.idx), self.data[self.idx]

    def previous(self, amount: int = 1) -> IterItem:
        if amount < 0:
            raise ValueError("Amount must be greater than or equal to zero")

        if self.idx - amount < 0:
            raise StopIteration

        self.idx -= amount
        return str(self.idx), self.data[self.idx]

    def find(self, item_id: str) -> IterItem:
        self.idx = self.data.index(item_id)
        return str(self.idx), self.data[self.idx]

    def current(self) -> IterItem:
        return str(self.idx), self.data[self.idx]
