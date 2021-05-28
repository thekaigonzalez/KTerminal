import curses
import os
import terminal.io as IO
import terminal.serial

printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ Changes the current distributions display name.
     default distro integrity is not affected, display integrity is.

     (NOTE: If you are making an app that uses KTerminal distribution statistics, PRETTY PLEASE Check distribution information by default integrity, not display integrity.)
     """
    terminal.serial.KTERMINAL_DISPLAYNAME = ' '.join(a)
