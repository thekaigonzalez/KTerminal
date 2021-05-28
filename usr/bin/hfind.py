import curses
import os
import terminal.io as IO

printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ Finding system written with slashes and stuff """

    findflags = "/.!@#$%^&*(][)"
    sttext = ' '.join(a)
    firstquoteendquote = sttext[sttext.find("\"")+1:sttext.rfind("\"")]
    firstfindflags = sttext[sttext.find("[")+1:sttext.rfind("]")]
    c = 0
    while c < len(firstfindflags):
        if firstquoteendquote[c] == firstfindflags[c]:
            printc("true")
        else:
            printc("")
