from typing import List


class Stack:
    def __init__(self) -> None:
        self.items: List[int] = []

    def push(self, value: int):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
