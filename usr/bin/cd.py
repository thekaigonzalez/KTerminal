import curses
import os

import pathlib

import terminal.io as IO
import terminal.parser
import fs

def printf(vs):
    IO.printw(vs)


def main(s: curses.window, a: list, c: int, o: list):
    """ CD's into a new directory. CHANGE DIR "CD" Classic command."""
    directory = terminal.parser.checkquotedstring(pos=0, array=a)
    if pathlib.Path(directory + "/IS_ENCRYPTED_SYSTEM").exists():
        IO.stdscr.addstr("path encrypted: process failed\n")
    else:
        if pathlib.Path(o[3] + "/" + directory).is_dir():

            o[3] = o[3] + "/" + directory
        else:
            IO.stdscr.addstr("path failed: not existent.\n")