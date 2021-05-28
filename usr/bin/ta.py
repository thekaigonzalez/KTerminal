import curses
import os
import terminal.io as IO
import terminal.dtypes as dt
printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ Testing some of the new primitives in KTerminal 1.10... """
    array = dt.checkarray(a, True)
    printc(str(array)) # Works!
