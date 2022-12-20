from bitarray import bitarray

class FileIO:

    def __init__(self):
        pass

    def ReadToBytes(self, filename: str):
        with open(filename, "rb") as file:
            return file.read()

    def WriteBitarray(self, filename:str, bits: bitarray):
        bits += '1'
        addZerosNum = len(bits) % 8
        if addZerosNum:
            bits += '0' * (8 - addZerosNum)

        with open(filename, "wb") as file:
            bits.tofile(file)
