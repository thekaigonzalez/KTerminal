import curses
def printc(__screen, this):
    __screen.addstr(this + "\n")

global defscreen

def default_scr(screen):
    defscreen = screen

def wprint(this):
    defscreen.addstr(this + "\n")