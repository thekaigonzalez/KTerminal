import curses
import os
import terminal.io as IO
import terminal.serial as get_dist
printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    if get_dist.KTERMINAL_DISTRIBUTION == "KTerminal Vanilla 1.10":
        printc("You are running KTerminal Vanilla (Base) Version " + get_dist.KTERMINAL_DISTRIBUTION_V)
    else:
        printc("You are running " + get_dist.KTERMINAL_DISTRIBUTION + " version " + get_dist.KTERMINAL_DISTRIBUTION_V )