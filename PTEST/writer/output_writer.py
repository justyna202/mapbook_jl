from typing import Protocol

# WRITER
class ResultWriter(Protocol):
    def write_data(self, value) -> None:
        ...


class TerminalWriter:
    def write_data(self, value) -> None:
        print(value)


class FileReader:
    def write_data(self, value) -> None:
        with open('./output.txt', 'w') as f:
            f.write(f'{value}')

class FileReader_add:
    def write_data(self, value) -> None:
        with open('./output.txt', 'a') as f:
            f.write(f'{value}\n')
