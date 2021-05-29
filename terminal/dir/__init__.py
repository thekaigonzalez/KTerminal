import pathlib


class Directory:
    def __init__(self, dirname):
        self.dir = dirname
    def Encrypted(self):
        if pathlib.Path(self.dir + "/IS_ENCRYPTED_SYSTEM").exists():
            return True
        else:
            return False
    def Post(self, file, mode):
        t = open(file, mode)
        return t