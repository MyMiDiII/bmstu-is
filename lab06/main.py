import sys
import os
import argparse

from typing import Tuple

import logging
logging.basicConfig(filename="huffman.log", filemode="w", level=logging.DEBUG)

from termcolor import cprint

from fileio.fileio import FileIO
from huffman.coder import HuffmanCoder


def print_error(msg: str):
    cprint("ОШИБКА:", "red", end=" ")
    print(msg)


def parse_args():
    parser = argparse.ArgumentParser(
                 description="Сжатие файлом методом Хаффмана")
    subparsers = parser.add_subparsers(help="режим работы программы")
    subparsers.required = True

    parser_enc = subparsers.add_parser('comp', help='сжатие файла')
    parent_enc = parser_enc.add_argument('filename', type=str, help='путь к файлу')
    parser_enc.set_defaults(mode='comp')

    parser_dec = subparsers.add_parser('decomp', help='распаковка файла')
    parent_dec = parser_dec.add_argument('filename', type=str, help='путь к файлу')
    parser_dec.set_defaults(mode='decomp')

    return parser.parse_args()


#def EncryptFile(file: str, key: Tuple[int, int]) -> None:
#    with open(file, "rb") as fileIn:
#        with open("./encrypted/" + os.path.basename(file), "wb") as fileOut:
#            while (byte := fileIn.read(1)):
#                number = int.from_bytes(byte, "big")
#                encrypted = Encrypt(number, key)
#                fileOut.write(encrypted.to_bytes(8, "big"))
#
#
#def DecryptFile(file: str, key: Tuple[int, int]) -> None:
#    with open(file, "rb") as fileIn:
#        with open("./decrypted/" + os.path.basename(file), "wb") as fileOut:
#            while (byte := fileIn.read(8)):
#                number = int.from_bytes(byte, "big")
#                encrypted = Decrypt(number, key)
#                fileOut.write(encrypted.to_bytes(1, "big"))


if __name__ == "__main__":
    args = parse_args()

    if args.mode == "comp":
        logging.info("COMPRESSING")
        logging.debug(f"args {args}")

        fileWorker = FileIO()
        b = fileWorker.ReadToBytes(args.filename)
        #b = b'\00\01\10'
        #print(b)
        #for bt in b:
        #    print(bt)
        #    d = {bt : 0}
        #    print(d)
        #print("ok")
        coder = HuffmanCoder()
        compressed = coder.Compress(b)

        endPath = os.path.basename(args.filename)
        fileWorker.WriteBitarray(f"./compressed/{endPath}", compressed)

        cprint(f"Файл успешно сжат и сохранен по пути "
               f"./compressed/{endPath}", "green")

    elif args.mode == "decomp":
        logging.info("DECOMPRESSING")
        logging.debug(f"args {args}")

        #Decompress(args.filename)

        endPath = os.path.basename(args.filename)
        cprint(f"Файл успешно распакован и сохранен по пути "
               f"./decompressed/{endPath}", "green")
