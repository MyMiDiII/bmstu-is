import sys
import argparse

from enigma.string_enigma import StringEnigma
from enigma.text_enigma import TextEnigma
from enigma.bin_enigma import BinEnigma
from enigma.enigma import Enigma

from config import alphabet, bin_alphabet


def EncipherString():
   enigma = Enigma(alphabet)
   strEnigma = StringEnigma(enigma)

   inString = input("Введите сообщение для шифрования:\n")
   encodedString = strEnigma.Encipher(inString)
   print("Зашифрованное сообщение:", encodedString, sep="\n")

   strEnigma.Reset()
   result = strEnigma.Encipher(encodedString)
   print("Расшифрованное сообщение:", result, sep="\n")

   #print(strEnigma.GetEnigmaConfig())


def EncipherText(filename):
    enigma = Enigma(alphabet)
    textEnigma = TextEnigma(enigma)

    try:
        textEnigma.Encipher(filename)

        textEnigma.Reset()

        textEnigma.Encipher("encodedText.txt", "check.txt")
    except EnvironmentError:
        print("Ошибка при открытии файла!")


def EncipherBinary(filename):
    enigma = Enigma(bin_alphabet)
    binEnigma = BinEnigma(enigma)

    try:
        binEnigma.Encipher(filename)

        binEnigma.Reset()

        binEnigma.Encipher("encoded.bin", "check.bin")

        #print(binEnigma.GetEnigmaConfig())
    except EnvironmentError:
        print("Ошибка при открытии файла!")


def parse_args():
    parser = argparse.ArgumentParser(description="Энигма для шифрования строк,"
                                     + " текстовых и бинарных файлов")
    subparsers = parser.add_subparsers(help="режим работы программы")

    parser_str = subparsers.add_parser('str', help='шифрование строк')
    parser_str.add_argument('--conf', nargs='?',
                        help='указание файла с начальными настройками Энигмы')
    parser_str.set_defaults(mode='str')

    parser_text = subparsers.add_parser('text',
                                        help='шифрование текстового файла')
    parser_text.add_argument('filename', type=str, help='путь к файлу')
    parser_text.add_argument('--conf', nargs='?',
                        help='указание файла с начальными настройками Энигмы')
    parser_text.set_defaults(mode='text')

    parser_bin = subparsers.add_parser('bin', help='шифрование бинарного файла')
    parent_bin = parser_bin.add_argument('filename', type=str,
                             help='путь к файлу')
    parser_bin.add_argument( '--conf', nargs='?',
                    help='указание файла с начальными настройками Энигмы')
    parser_bin.set_defaults(mode='bin')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    print(args)

    if args.mode == "str":
        EncipherString()

    elif args.mode == "text":
        EncipherText(args.filename)

    elif args.mode == "bin":
        EncipherBinary(args.filename)

