from bitarray import bitarray
from collections import Counter


class FrequencyTable:

    def __init__(self):
        self.table = None

    def __iter__(self):
        return iter(self.table.items())

    def Build(self, what: bytes):
        # self.table = Counter(what)
        self.table = Counter()
        for byte in what:
            #print(type(byte))
            self.table[byte] += 1

    def FromBitarray(self, what: bitarray):
        pass

    def ToBitarray(self):
        pass

