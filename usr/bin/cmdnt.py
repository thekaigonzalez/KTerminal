import curses
import os
import terminal.io as IO
import terminal.serial


def printf(vs):
    IO.printw(vs)


def main(s: curses.window, a: list, c: int, o: list):
    """ Check the amount of commands for the current distribution.

    (NOTE TO DISTRO MAKERS: EDIT THIS FILE IF YOU PLAN TO EDIT THE USR/BIN DIRECTORY PLEASE. OTHERWISE IT WILL BREAK.)
    """
    arr = []
    for fname in os.listdir("usr/bin"):
        if fname.endswith(".py"):
            if not fname.startswith("__"):
                arr.append(fname[0:fname.rfind(".")])

    printf("you have {} commands installed on distribution {}".format(str(len(arr)), terminal.serial.KTERMINAL_DISTRIBUTION))
