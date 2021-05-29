import curses
from typing import List
from terminal.io import stdscr


class ArgumentPasser:
    def __init__(self, argarray: List[str]):
        self.args = argarray
        self.optlist = []
        self.desc = ""

    def isoption(self, pos):
        if self.args[pos].startswith("-"):
            return True
        else:
            return False

    def echo(self, option: str, var: List[str], output: str, callback, position: int = 0):
        if self.args[position].startswith("-"):
            stdscr.addstr(output)
        else:
            callback()

    def bindonce(self, option: str, func):
        self.optlist.append("[-" + option + " ...] ")
        for i in self.args:
            if i == "-" + option:
                func(self.args, self)

    def setDesc(self, dec):
        self.desc = dec

    def sendhelp(self):

        stdscr.addstr(''.join(self.optlist))
        stdscr.addstr("\n\n" + self.desc + "\n")
