import curses
stdscr = curses.initscr()
def printw(s):
    """
    Creates a screen and prints to the screen, simulating a stdscr print.
    You can also use the global variable "stdscr".
    :param s:
    :return:
    """
    wnd = curses.initscr()
    wnd.addstr(str(s) + "\n")
