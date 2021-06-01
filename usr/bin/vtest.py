import curses
import os
import terminal.io as IO
import terminal.argsetup as AS
def printf(vs):
    IO.printw(vs)
def HelpCommand(a, o):
    o.sendhelp()

def main(s: curses.window, a: list, c: int, o: list):
    """ Tests variables... Yes... """
    parser = AS.ArgumentPasser(a)
    parser.extract(0)
    printf(parser.parseconfig_getpos("VALUE", 0)) # Should return the first variable...
    parser.bindonce("h", HelpCommand)
