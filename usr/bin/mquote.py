import curses
import os
import terminal.io as IO
import terminal.parser


def printf(vs):
    IO.printw(vs)


def main(s: curses.window, a: list, c: int, o: list):
    """ Gets the first argument quote """
    quotedstr = terminal.parser.checkquotedstring(pos=0, array=a)
    printf(quotedstr)