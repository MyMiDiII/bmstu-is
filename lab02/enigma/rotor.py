import random
import sys

import logging
logging.basicConfig(level=logging.DEBUG)

class Rotor:

    def __init__(self, alphabetLen,
                 orderSeed=None, positionSeed=None):
        self._alphabet = [x for x in range(alphabetLen)]

        self._orderSeed = (orderSeed if orderSeed is not None
                               else random.randrange(sys.maxsize))
        self._setOrder(self._orderSeed)

        self._positionSeed = (positionSeed if positionSeed is not None
                                  else random.randrange(sys.maxsize))
        self._setPosition(self._positionSeed)

        logging.debug("\nAlphabet:\n{0}".format(self._alphabet))
        logging.debug("\nOrder:\n{0}".format(self._order))
        logging.debug("\nPosition:\n{0}".format(self._position))


    def _setOrder(self, orderSeed):
        random.seed(orderSeed)
        self._order = self._alphabet.copy()
        random.shuffle(self._order)


    def _setPosition(self, positionSeed):
        random.seed(positionSeed)
        self._position = random.randint(0, len(self._order))


    def SetConfig(self, orderSeed, positionSeed):
        self._setOrder(orderSeed)
        self._setPosition(positionSeed)

        logging.debug("\nOrder:\n{0}".format(self._order))
        logging.debug("\nPosition:\n{0}".format(self._position))


    def GetConfig(self):
        return self._orderSeed, self._positionSeed


    def GetForward(self, index):
        return self._order[(index + self._position) % len(self._alphabet)]


    def GetInverse(self, value):
        return (self._order.index(value)
                    - self._position) % len(self._alphabet)


    def Rotate(self):
        self._position += 1
        return self._position


if __name__ == "__main__":
    rotor = Rotor(26)

    rotor1 = Rotor(26)

    rotorCopy1 = Rotor(26, orderSeed=rotor._orderSeed,
                       positionSeed=rotor._positionSeed)

    rotor1.SetConfig(*rotor.GetConfig())

    alphabet = list("abcde")

    test = Rotor(len(alphabet))

    for i in range(len(alphabet)):
        print("forward", alphabet[test.GetForward(i)])
        print("inverse", alphabet[test.GetInverse(i)])

