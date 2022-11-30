import sys
import os
import argparse

import logging
logging.basicConfig(filename="rsa.log", filemode="w", level=logging.DEBUG)

from termcolor import cprint

from myrsa.generation import GenerateKeys

def print_error(msg: str):
    cprint("ОШИБКА:", "red", end=" ")
    print(msg)


def parse_args():
    parser = argparse.ArgumentParser(
                 description="RSA шифрование файлов")
    subparsers = parser.add_subparsers(help="режим работы программы")
    subparsers.required = True

    parser_gen = subparsers.add_parser('gen', help='генерация ключей')
    parser_gen.set_defaults(mode='gen')

    parser_enc = subparsers.add_parser('enc', help='шифрование файла')
    parent_enc = parser_enc.add_argument('filename', type=str, help='путь к файлу')
    parser_enc.add_argument('d', help='часть открытого ключа d', type=int)
    parser_enc.add_argument('N', help='часть открытого ключа N', type=int)

    parser_enc.set_defaults(mode='enc')

    parser_dec = subparsers.add_parser('dec', help='шифрование файла')
    parent_dec = parser_dec.add_argument('filename', type=str, help='путь к файлу')
    parser_dec.add_argument('e', help='часть закрытого ключа e', type=int)
    parser_dec.add_argument('N', help='часть закрытого ключа N', type=int)

    parser_dec.set_defaults(mode='dec')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.mode == "gen":
        logging.info("KEYS GENERATION")
        logging.debug(f"args {args}")
        publicKey, privateKey = GenerateKeys(100)

        cprint(f"Открытый ключ: {publicKey[0]} {publicKey[1]}", "cyan")
        cprint(f"Закрытый ключ: {privateKey[0]} {privateKey[1]}", "cyan")
        cprint("Не сообщайте никому закрытый ключ!!!", "red")

    elif args.mode == "enc":
        logging.info("FILE ENCRYPTION")
        logging.debug(f"args {args}")

    elif args.mode == "dec":
        logging.info("FILE DECRYPTION")
        logging.debug(f"args {args}")
