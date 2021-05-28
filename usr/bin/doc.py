import curses
import os
import terminal.io as IO
import terminal.modular as mods
import inspect
printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ Document summaries of functions from KTerminal Command Builds > 1.10
    Throws an error if the documentation is not found

    Part of KTerminal Silicon Beta 1.10-2
    """
    fobj = mods.require("usr.bin." + a[0])
    docs = inspect.getdoc(fobj.main)
    printc(docs)