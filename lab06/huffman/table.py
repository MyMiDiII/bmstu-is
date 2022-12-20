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
            self.table[byte] += 1

    def FromBitarray(self, what: bitarray):
        pass

    def ToBitarray(self) -> bitarray:
        result = bitarray("{0:08b}".format(len(self.table) - 1))
        for item in self.table.items():
            itemCode = f"{'{0:08b}'.format(item[0])}{'{0:016b}'.format(item[1])}"
            result += itemCode

        #print(result)
        return result

