import curses
import os
import pathlib

from typing import List

import terminal.io as IO
import terminal.keyboard

import terminal.parser as ps
import terminal.argsetup as argparse


def printf(vs):
    IO.printw(vs)


def fsck_begin_flag(args: List[str], obj: argparse.ArgumentPasser):
    printf("Are you SURE you want to continue?\nfsck Can cause damage to the system if used incorrectly.")
    IO.stdscr.addstr("Type your answer into the box<n>: ")
    keb = terminal.keyboard.grkey()

    if keb is not None:
        printf('')
    else:
        keb = 'n'
    if keb == 'n':
        printf("open: permission denied")
    elif keb == 'y':
        if pathlib.Path("usr/bin").is_dir():
            printf("exists")
            if pathlib.Path("usr/clib").is_dir():
                printf("integrity true")
                if pathlib.Path('usr/Access.S').exists():
                    printf("able to access inode, checking and reinstalling")

                    for h in os.listdir("."):
                        b = ' '.join(format(ord(x), 'b') for x in h)
                        printf(str(b))
                    printf("byte encoding complete")
                    for i in os.listdir("."):
                        printf("uninstalling " + i)
                        if i != "usr":
                            os.remove(i)

def helpcomd(a, o):
    o.sendhelp()

def main(s: curses.window, a: list, c: int, o: list):
    """ FSCK: Based on the unix version.
    AKA: DELETES EVERYTHING. BE CAREFUL!

    why might i need this?
    reinstall kterminal idk..

    (Remove KTerminal in safe mode, without damaging Kterminal as a whole :>)
    """
    FSCK = argparse.ArgumentPasser(a)
    FSCK.setDesc("""
FSCK is a command line utility for KTerminal systems which checks and
reinstalls KTerminal ENTIRELY. if you're looking for a fresh,
revamped uninstaller, try the dunst utility.
    """)
    FSCK.bindonce("b", fsck_begin_flag)

    FSCK.bindonce("h", helpcomd)
