from bitarray import bitarray
from bitarray.util import ba2int

from huffman.table import FrequencyTable
from huffman.tree import HuffmanTree

class HuffmanCoder:

    def __init__(self):
        pass

    def Compress(self, what: bytes) -> bitarray:
        freqTable = FrequencyTable()
        freqTable.Build(what)
        codesTable = HuffmanTree(freqTable).GetHuffmanCodeTable()
        compressed = self.comressByCodesTable(what, codesTable)

        result = freqTable.ToBitarray() + compressed

        return result


    def comressByCodesTable(self, what: bytes, codesTable: dict):
        result = bitarray()
        for byte in what:
            result += codesTable[byte]

        return result


    def Decompress(self, what: bitarray) -> bytes:
        bitTable, data = self.extract(what)

        freqTable = FrequencyTable()
        freqTable.FromBitarray(bitTable)

        tree = createTree(table)

        decompressed = decompressByTree(what, tree)

        return decompressed


    def extract(self, what: bitarray) -> tuple[bitarray, bitarray]:
        #print(what)
        symbolsNum = ba2int(what[:8])
        tableLen = 32 + 24 * symbolsNum
        # tableLen = 8 * (1 + 3  * (symbolsNum + 1))

        return what[:tableLen], what[tableLen:]

