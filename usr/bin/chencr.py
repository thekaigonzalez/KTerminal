import curses
import os

import pathlib

import terminal.dir
import terminal.io as IO
import terminal.parser
def printf(vs):
    IO.printw(vs)


def main(s: curses.window, a: list, c: int, o: list):
    """ Checks the level of encryption for a directory using the Terminal Encryption API
    (USE QUOTATION MARKS FOR DIRECTORIES WITH SPACES!)
    """
    userdir = terminal.dir.Directory(terminal.parser.checkquotedstring(0, a))
    if userdir.Encrypted():
        printf("Directory encrypted: true")
    else:
        printf("directory encrypted: false")
