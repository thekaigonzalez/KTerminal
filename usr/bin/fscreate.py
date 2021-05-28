import curses
import os
import terminal.io as IO

printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    if c == 0:
        printc("needs ONE argument. optionally two. Type fscreate -h for help. ")
    elif c == 1:
        printc("fscreate: creating user directory for " + a[0])
        os.mkdir('./system/home/' + a[0])
        os.mkdir('./system/home/' + a[0] + "/scripts")
        os.mkdir('./system/home/' + a[0] + "/SYSTEM")
        os.mkdir('./var/tmp/' + a[0])
        printc("fscreate: finished creating user directories.")