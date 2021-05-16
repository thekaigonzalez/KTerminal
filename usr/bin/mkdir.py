import macostools
import os


def main(_s, a, c , o):
    dirname = ""

    for i in a:
        dirname += i

    os.mkdir(dirname)