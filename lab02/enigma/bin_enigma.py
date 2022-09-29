class BinEnigma:

    def __init__(self, enigma):
        self._enigma = enigma


    def SetEnigma(self, enigma):
        self._enigma = enigma


    def GetEnigmaConfig(self):
        return self._enigma.GetConfig()


    def Reset(self):
        self._enigma.Reset()


    def Encode(self, inFilename, outFilename="encoded.bin"):

        with (open(inFilename, "rb") as inFile,
              open(outFilename, "wb") as outFile):

            i = 0
            while (byte := inFile.read(1)):
                print(byte)
                i += 1
                print("num = ", i)
                x = bytes([self._enigma.Encode(byte)])
                print(x)
                print("len = ", len(x))
                outFile.write(x)

