class FileIO:

    def __init__(self):
        pass

    def ReadToBytes(self, filename: str):
        with open(filename, "rb") as file:
            return file.read()
