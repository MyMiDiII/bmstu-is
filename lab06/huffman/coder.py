from bitarray import bitarray

from huffman.table import FrequencyTable
from huffman.tree import HuffmanTree

class HuffmanCoder:

    def __init__(self):
        pass

    def Compress(self, what: bytes) -> bitarray:
        freqTable = FrequencyTable()
        freqTable.Build(what)
        codesTable = HuffmanTree(freqTable).GetHuffmanCodeTable()
        #for item in codesTable.items():
        #    print(item)
        compressed = self.comressByCodesTable(what, codesTable)

        result = freqTable.ToBitarray() + compressed

        return result
        #print(compressed)
        #return compressed


    def comressByCodesTable(self, what: bytes, codesTable: dict):
        result = bitarray()
        for byte in what:
            result += codesTable[byte]

        return result


    def Decompress(self, what: bitarray) -> bytes:
        bitTable, data = extract(what)

        table = FrequencyTable()
        table.FromBitarray(bitTable)

        tree = createTree(table)

        decompressed = decompressByTree(what, tree)

        return decompressed


