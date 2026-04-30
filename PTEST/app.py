# zmienna_A=int(input())
# zmienna_B=int(input())
#
# print(zmienna_A+zmienna_B)

from typing import Protocol, List

from PTEST.READER.input_readers import DataInput, TerminalInput
from READER.input_readers import DataInput, TerminalInput
from writer.output_writer import ResultWriter, TerminalWriter, FileReader, FileReader_add
from adder.adders import DataAdder, Adder


# SERVICE
class PTESTService:
    def __init__(self, reader: DataInput, writer: ResultWriter, adder: DataAdder):
        self.reader = reader
        self.writer = writer
        self.adder = adder

    def execute(self):
        digit_A = self.reader.read_data()
        digit_B = self.reader.read_data()
        result = self.adder.add_data(digit_A, digit_B)
        self.writer.write_data(result)


# APP
class PTESTApp:
    @staticmethod
    def run():
        reader = TerminalInput()
        writer = FileReader_add()
        adder = Adder()

        service = PTESTService(reader, writer, adder)
        service.execute()


if __name__ == "__main__":
    PTESTApp.run()
