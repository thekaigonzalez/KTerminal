import curses
import platform

import terminal.io as io


# s: curses.window, a: list[str], c: int, o: list[bool]
def main(s: curses.window, a: list[str], c: int, o: list[bool]):
    """Lists system specs"""
    s.clear()
    s.refresh()

    io.printw("System Specs:\n " + platform.uname().system + ", {}, {}, {}".format(platform.uname().processor, platform.uname().machine, platform.uname().version) )