"""Studi Kasus 2 - Library models"""
from __future__ import annotations
from typing import List


class LibraryItem:
    """Generic library item."""

    def __init__(self, item_id: int, title: str):
        self.item_id = item_id
        self.title = title

    def display_info(self) -> None:
        print(f"Item {self.item_id}: {self.title}")

    def calculate_late_fee(self, days_late: int) -> float:
        if days_late <= 0:
            return 0.0
        return 0.5 * days_late


class Author:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def get_age(self, current_year: int) -> int:
        return current_year - self.birth_year


class Book(LibraryItem):
    def __init__(self, item_id: int, title: str, isbn: str, author: Author):
        super().__init__(item_id, title)
        self.isbn = isbn
        self.author = author

    def display_info(self) -> None:
        print(f"Book {self.item_id}: {self.title} (ISBN: {self.isbn}) by {self.author.name}")

    def calculate_late_fee(self, days_late: int) -> float:
        if days_late <= 0:
            return 0.0
        return 1.0 * days_late


class LibraryMember:
    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_items: List[LibraryItem] = []

    def borrow_item(self, item: LibraryItem) -> None:
        self.borrowed_items.append(item)
        print(f"{self.name} borrowed '{item.title}' (id={item.item_id})")

    def return_item(self, item: LibraryItem) -> None:
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"{self.name} returned '{item.title}' (id={item.item_id})")
        else:
            print(f"{self.name} does not have '{item.title}' borrowed")