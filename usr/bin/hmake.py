import curses
import os

import pathlib

import terminal.io as IO
import json
printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ HMAKE: A Make-Like Build system for KTerminal

    Features

    - Continuous integration with the KTerminal interface
    - Dynamic screen adjustments prevent unreadable text
    - Simplistic JSON format allows for use of multiple build commands
    - Modern use of JSON Objects allowing for flexible reading and writing
    - Support for all versions of KTerminal
    """
    if pathlib.Path(o[3] + "HMake.json").exists():
        hmakefile = open(o[3] + "HMake.json")
        js = json.load(hmakefile)
        cmds = js["commands"]
        i= 0

        while i < len(cmds)-1:
            i += 1
            os.system(cmds[i]["program"] + " " + cmds[i]["flags"] + " " + cmds[i]["sourcefile"])


    else:
        printc("hmake: stop. *** no targets for HMake File found. end.")
