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
        pass

    @abstractmethod
    def previous(self, amount: int = 1):
        pass

    @abstractmethod
    def current(self) -> IterItem:
        pass

    def __getitem__(self, item_id: Any) -> IterItem:
        if type(item_id) is not str:
            raise TypeError(f"Expected type 'str' for id, got '{type(item_id)}' instead")

        return self.find(item_id)

    @abstractmethod
    def find(self, item_id: str) -> IterItem:
        pass


class StrListIter(DoubleIter):
    def __init__(self, data: list[str]):
        self.data: list[str] = data
        self.idx: int = -1

    def next(self, amount: int = 1) -> IterItem:
        if self.idx + amount >= len(self.data):
            self.idx = len(self.data)
            raise StopIteration

        self.idx += amount

        return str(self.idx), self.data[self.idx]

    def previous(self, amount: int = 1) -> IterItem:
        if self.idx - amount < 0:
            self.idx = -1
            raise StopIteration

        self.idx -= amount
        return str(self.idx), self.data[self.idx]

    def find(self, item_id: str) -> IterItem:
        self.idx = self.data.index(item_id)
        return str(self.idx), self.data[self.idx]

    def current(self) -> IterItem:
        return str(self.idx), self.data[self.idx]
