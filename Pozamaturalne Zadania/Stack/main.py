from typing import Any

class Stack:
    def __init__(self, values: list[Any] = []):
        self.values = values

    def push(self, value):
        self.values.append(value)

    def pop(self) -> Any:
        return self.values.pop()

    def is_empty(self) -> bool:
        return bool(self)