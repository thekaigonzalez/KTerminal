import curses

stdscr = curses.initscr()


def grkey():
    curses.cbreak()
    key = stdscr.getkey()
    curses.nocbreak()
    return key
