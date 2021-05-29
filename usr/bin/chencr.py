import curses
import os

import pathlib

import terminal.io as IO

def printf(vs):
    IO.printw(vs)


def main(s: curses.window, a: list, c: int, o: list):
    """ Checks the level of encryption for a directory """
    if (pathlib.Path(a[0] + "/IS_ENCRYPTED_SYSTEM").exists()):
        printf("chencr: path exists; is encrypted")
    else:
        printf("path does not exist; not system directory")
