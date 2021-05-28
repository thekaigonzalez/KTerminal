import curses
import os
import terminal.io as IO
import terminal.serial as VINF
printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ Displays System information (SERIAL INFO) """
    printc("Distribution name: " + VINF.KTERMINAL_DISTRIBUTION + "\nDistribution Version: " + VINF.KTERMINAL_DISTRIBUTION_V + "\nOther system informations:\n\nKTerminal Distro w/ Flavor: " + VINF.KTERMINAL_DEFAULT_DISTRIBUTION + " " + VINF.KTERMINAL_FLAVOR + "\nCommand Handling Engine: " + VINF.KTERMINAL_COMMAND_DISTRIBUTIONS + "\nKTerminal Integrity name: " + VINF.KTERMINAL_INTEGRITY_DEFAULTNAME + "\nKTerminal Inspiration/Style: " + VINF.KTERMINAL_STYLE + "\nKTerminal Build: " + VINF.KTERMINAL_BUILD )