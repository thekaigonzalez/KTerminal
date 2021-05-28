import curses
import os
import terminal.io as IO

printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """
    renames the system user name.txt

    by default it's KTerminalLiteVanilla, but can be changed to whatever you want by either editing usr/name.txt,
    or running (rn <new name>)
    """
    b = open('usr/name.txt', 'w')
    b.write(' '.join(a))
    b.close()
