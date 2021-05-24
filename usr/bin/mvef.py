import curses
import pathlib


def main(s: curses.window,a,c,o):
    if pathlib.Path(a[0]).exists():
        s.addstr("yes")
    else:
        s.addstr("no.")