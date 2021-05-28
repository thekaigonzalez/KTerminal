import curses
import os
import terminal.io as IO

printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ Creates a file.. That's it """
    y = open(' '.join(a), 'w')
    y.write("")
    y.close()
