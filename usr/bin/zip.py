import curses
import os
import terminal.io as IO
import zipfile
printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ printc ( items ) """
    fn = zipfile.ZipFile("test.zip", 'w')
    fn.write("./usr/bin/cat.py")
    fn.close()