import curses

def printw(s: str):
    wnd = curses.initscr()
    wnd.addstr(s + "\n")
