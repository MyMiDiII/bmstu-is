from bitarray import bitarray

from huffman.table import FrequencyTable
from huffman.tree import HuffmanTree

class HuffmanCoder:

    def __init__(self):
        pass

    def Compress(self, what: bytes) -> bitarray:
        freqTable = FrequencyTable()
        freqTable.Build(what)
        codeTable = HuffmanTree(freqTable).GetHuffmanCodeTable()
        print(codeTable)
        #compressed = comressByTree(what, tree)

        #result = table.ToBitarray() + compressed
        result = 0

        return result


    def Decompress(self, what: bitarray) -> bytes:
        bitTable, data = extract(what)

        table = FrequencyTable()
        table.FromBitarray(bitTable)

        tree = createTree(table)

        decompressed = decompressByTree(what, tree)

        return decompressed


