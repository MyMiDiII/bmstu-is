from bitarray import bitarray
from bitarray.util import hex2ba, ba2hex

from tables import IP, IP1
from constants import ROUND_NUMBER

from psblocks import permute, add_zeros
from feistel import feistel
from key_generation import generate_keys

def encipher(msg: bitarray, keys: list[bitarray], deciphiring=False):
    if len(msg) != 64:
        return None

    permutation = permute(msg, IP)
    left, right = permutation[:32], permutation[32:]

    if deciphiring:
        left, right = right, left
        keys = [x for x in reversed(keys)]

    #print(ba2hex(left), ba2hex(right))

    for i in range(ROUND_NUMBER):
        new_right = left ^ feistel(right, keys[i])
        left = right
        right = new_right

        #print(ba2hex(left), end=" ")
        #print(ba2hex(right), end=" ")
        #print(ba2hex(keys[i]))

    if deciphiring:
        left, right = right, left

    return permute(left + right, IP1)


def des(msg: bitarray, key: bitarray, deciphiring=False) -> bitarray:
    if len(msg) != 64 or len(key) != 64:
        return None

    keys = generate_keys(key)

    cipher = encipher(msg, keys, deciphiring)

    return cipher


if __name__ == "__main__":
    msg = add_zeros(hex2ba("123456ABCD132536"), 64)
    key = add_zeros(hex2ba("AABB09182736CCDD"), 64)

    cipher = des(msg, key)
    print(ba2hex(msg))
    print(ba2hex(cipher))
    print(ba2hex(des(cipher, key, True)))