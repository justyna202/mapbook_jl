from typing import Protocol
# READER
class DataInput(Protocol):
    def read_data(self) -> int:
        ...

class TerminalInput:
    def read_data(self) -> int:
        return int(input())

