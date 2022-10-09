from bitarray import bitarray
from bitarray.util import hex2ba, ba2hex

from constants import ROUND_NUMBER
from tables import B, SI, CP

from purmutation import purmute


def bitarray_circular_shift(bits: bitarray, step: int):
    return (bitarray([0] * (len(bits) - step)) + bits[:step]) ^ (bits << step)


def generate_keys(key: bitarray):
    if len(key) != 64:
        return []

    result = purmute(key, B)
    #print(result)

    ci, di = result[:28], result[28:]
    #print(ci, di, sep="\n")

    keys = []

    for i in range(ROUND_NUMBER):
        ci = bitarray_circular_shift(ci, SI[i])
        di = bitarray_circular_shift(di, SI[i])
        keys.append(purmute(ci+di, CP))

        #print(ba2hex(ci), ba2hex(di), sep="\n")
        #print(ba2hex(keys[i]))

    return keys


if __name__ == "__main__":
    generate_keys(hex2ba('AABB09182736CCDD'))

