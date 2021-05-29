import curses
import os
import terminal.io as IO
import terminal.parser


def printf(vs):
    IO.printw(vs)


def main(s: curses.window, a: list, c: int, o: list):
    """ replica of assembly's DB instruction.
     AKA: Cooler printf B)
     """

    printf(terminal.parser.checkquotedstring(pos=0, array=a))
