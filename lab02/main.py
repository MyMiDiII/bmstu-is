import sys

from enigma.string_enigma import StringEnigma
from enigma.text_enigma import TextEnigma
from enigma.bin_enigma import BinEnigma
from enigma.enigma import Enigma

from config import alphabet, bin_alphabet

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) >= 1 and args[0] == "str":
        enigma = Enigma(alphabet)
        strEnigma = StringEnigma(enigma)

        inString = input("Введите сообщение для шифрования:\n")
        encodedString = strEnigma.Encode(inString)
        print("Зашифрованное сообщение:", encodedString, sep="\n")

        print("Обратно:")
        strEnigma.Reset()
        result = strEnigma.Encode(encodedString)
        print("Расшифрованное сообщение:", result, sep="\n")

    elif len(args) >= 2 and args[0] == "text":
        enigma = Enigma(alphabet)
        textEnigma = TextEnigma(enigma)
        filename = args[1]

        try:
            textEnigma.Encode(filename)

            textEnigma.Reset()

            textEnigma.Encode("encodedText.txt", "check.txt")
        except EnvironmentError:
            print("Ошибка при открытии файла!")

    elif len(args) >= 2 and args[0] == "bin":
        enigma = Enigma(bin_alphabet)
        binEnigma = BinEnigma(enigma)
        filename = args[1]

        try:
            binEnigma.Encode(filename)

            binEnigma.Reset()

            binEnigma.Encode("encoded.bin", "check.bin")
        except EnvironmentError:
            print("Ошибка при открытии файла!")

    else:
        print("Usage:")
        print("main.py str -- encode string;")
        print("main.py text filename -- encode text file;")
        print("main.py bin  filename -- encode binary file.")

