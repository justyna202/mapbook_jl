from typing import Protocol

# BUSINESS LOGIC
class DataAdder(Protocol):
    def add_data(self, digit_A: int, digit_B: int) -> int:
        ...


class Adder:
    def add_data(self, digit_A: int, digit_B: int) -> int:
        return digit_A + digit_B

