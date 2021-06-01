import curses
import os
from typing import List

import terminal.io as IO
import terminal.argsetup as argparse


def printf(vs):
    IO.printw(vs)
def helpc(args: List[str], object: argparse.ArgumentPasser):
    object.sendhelp()

def main(s: curses.window, a: list, c: int, o: list):
    """ A FUCKING COMMENT LOL """