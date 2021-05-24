import curses
import pathlib


def main(s: curses.window,a,c,o):
    if len(o) == 6:
        if pathlib.Path(a[0]).exists():
            s.addstr("yes\n")
        else:
            s.addstr("no.\n")
    else:
        s.addstr("Run mvef from Root to prevent problems. `sudo mvef <f>`\n")