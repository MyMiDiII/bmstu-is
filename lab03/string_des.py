import string

from textwrap import wrap
from bitarray import bitarray
from bitarray.util import rindex

from des.psblocks import add_zeros
from des.des import des

alphabet = list(string.printable[:62] + " " + "-")

def string_enciphering(str_msg: str, bitkey: bitarray, deciphering: bool):
    #cprint('GET BITARRAY', "blue")
    #print("bef", bitarray(''.join(f"{alphabet.index(i):06b}" for i in string)))
    msg = bitarray(''.join(f"{alphabet.index(i):06b}" for i in str_msg)
                       + ('' if deciphering else '1'))
    #print("msg", msg)

    #cprint('PADDING', "blue")
    if len(msg) % 64:
        if deciphering:
            msg = msg[len(msg)%64:]
        else:
            msg = add_zeros(msg, len(msg) // 64 * 64 + 64, True)

    #print("len msg", len(msg))
    #print("msg", msg)

    #cprint('ENCIPHIREING', "blue")
    result = bitarray()
    for i in range(0, len(msg), 64):
        result += des(msg[i:i + 64], bitkey, deciphering)

    #print('len result', len(result))
    #print('result', result)

    #cprint('TO STRING', "blue")
    if deciphering:
        result = result[:rindex(result, 1)]
    elif len(result) % 6:
        result = add_zeros(result, len(result) // 6 * 6 + 6)

    return "".join([alphabet[int(x, 2)] for x in wrap(result.to01(), 6)])
    #print(wrap(result.to01(), 6))
