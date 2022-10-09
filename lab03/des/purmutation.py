from bitarray import bitarray

def purmute(in_array: bitarray, table: list[int]) -> bitarray:
    return bitarray([in_array[i - 1] for i in table])

