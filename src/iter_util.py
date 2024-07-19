from typing import Any, Self
from abc import ABC, abstractmethod
from arg_handler import value_args, normal_args
import csv

type IterItem = tuple[str, str]
from util import error


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


class CSVIter(DoubleIter):
    def __init__(self, filepath: str):
        try:
            self._id_idx: int = int(value_args.get("--id-idx", 0))
        except ValueError:
            error("Invalid index for --id-idx")

        try:
            self._value_idx: int = int(value_args.get("--value-idx", 0))
        except ValueError:
            error("Invalid index for --value-idx")

        self._header: bool = "--header" in normal_args

        self._seperator: str | None = value_args.get("--sep", value_args.get("--seperator", ";"))
        if self._seperator is None:
            self._seperator = ";"

        self._current: tuple[str, str] | None = None

        self._file = open(filepath)
        self._idx = -1
        self._new_reader()

    def next(self, amount: int = 1) -> IterItem:
        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        current_idx = self._idx

        col: list[str]
        try:
            for i in range(amount - 1):
                next(self._reader)

            col = next(self._reader)
        except StopIteration:
            self._idx = current_idx
            self._new_reader()
            raise StopIteration

        return col[self._id_idx], col[self._value_idx]

    def _new_reader(self) -> None:
        self._reader = csv.reader(self._file, delimiter=self._seperator)

        if self._header:
            next(self._reader)

        for i in range(self._idx):
            next(self._reader)

        col = next(self._reader)
        self._current = col[self._id_idx], col[self._value_idx]

    def previous(self, amount: int = 1) -> IterItem:
        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        new_idx = self._idx - amount

        if new_idx < 0:
            raise StopIteration

        self._idx = self
        self._new_reader()
        return self._current

    def current(self) -> IterItem:
        if self._current is None:
            raise StopIteration

        return self._current

    def find(self, item_id: str) -> IterItem:
        current_idx = self._idx
        self._idx = -1
        self._new_reader()

        for col in self._reader:
            self._idx += 1
            if col[self._id_idx] == item_id:
                self._current = col[self._id_idx], col[self._value_idx]
                return self._current

        self._idx = current_idx
        self._new_reader()
        raise StopIteration


class JSONIter(DoubleIter):
    def __init__(self, filepath: str):
        pass

    def next(self, amount: int = 1) -> IterItem:
        pass

    def previous(self, amount: int = 1) -> IterItem:
        pass

    def current(self) -> IterItem:
        pass

    def find(self, item_id: str) -> IterItem:
        pass


class TextIter(DoubleIter):
    def __init__(self, filepath: str):
        pass

    def next(self, amount: int = 1) -> IterItem:
        pass

    def previous(self, amount: int = 1) -> IterItem:
        pass

    def current(self) -> IterItem:
        pass

    def find(self, item_id: str) -> IterItem:
        pass
