# t=int(input())
# for i in range(t):
#     n=int(input())
#     lista_liczb=list(map(int, input().split()))
#     print(sum(lista_liczb))

# READER
from typing import Protocol, List

from PTEST.READER.input_readers import DataInput


class DataAdder(Protocol):
    def read_digit(self) -> int: ...

    def read_line_of_digits(self) -> List[str]: ...


class TerminalInput:
    def read_digit(self) -> int:
        return int(input())

    def read_line_of_digits(self) -> List[str]:
        return input().split()


# BUISNESS LOGIC

class DataTransform(Protocol):
    def list_transform(self, list_of_strings: List[str]) -> List[int]: ...


class TerminalTransform:
    def list_transform(self, list_of_strings: List[str]) -> List[int]:
        return list(map(int, list_of_strings))


class DataAdder(Protocol):
    def add_data(self, digits: List[int]) -> int: ...


class TerminalAdder:
    def add_data(self, digits: List[int]) -> int:
        return sum(digits)

# WRITER
class ResultWriter(Protocol):
    def write_data(self, result: int) -> None : ...

class TerminalResultWriter:
    def write_result(self, result: int) -> None:
        print(result)

# SERVICE

class RNO_DODService:
    def __init__(
            self,
            reader: DataInput,
            writer: ResultWriter,
            transformer: DataTransform,
            adder: DataAdder):
        self.reader = reader
        self.writer = writer
        self.transformer = transformer
        self.adder = adder

    def execute(self):
        t = self.reader.read_digit()
        for i in range(t):
            self.reader.read_digit()
            line_of_strings = self.reader.read_line_of_digits()
            list_of_digits = self.transformer.list_transform(line_of_strings)
            result = self.adder.add_data(list_of_digits)
            self.writer.write_result(result)


# APP

class RNO_DODApp:
    @staticmethod
    def run():
        reader = TerminalInput()
        writer = TerminalResultWriter()
        transform = TerminalTransform()
        adder = TerminalAdder()

        service = RNO_DODService(reader, writer, transform, adder)
        service.execute()

if __name__ == "__main__":
    RNO_DODApp().run()