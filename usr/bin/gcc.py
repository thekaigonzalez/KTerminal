import curses
import os
import terminal.io as IO

printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ GCC Utility implemented in KTerminal """
    if c == 0:
        printc("gcc: error: no input files specified")
    elif c == 1:
        os.system("gcc " + a[0])
    elif c >= 2:
        file = a.pop(0)
        os.system('gcc ' + ' '.join(a) + " " + file )
