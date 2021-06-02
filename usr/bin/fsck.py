import curses
import os
import pathlib
import time
import gitpy
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
                            if i.__contains__("."):
                                if i != ".idea":
                                    os.remove(i)
                    printf("You are now in KTerminal post-boot mode!")
                    printf("DO NOT PANIC! Everything on this end is fine, you've just hit KTerminal's END OF LIFE system. (RECOVERY)")
                    printf("Everything you do from here on out has no effect on the KTerminal filesystems, and can cause errors.")
                    printf("These errors are not fatal, HOWEVER, it's able to be reinstalled with the \"reinstall\" command.")
                    printf("Type exit to confirm your uninstallation and exit forever.")
                    while True:
                        IO.stdscr.addstr("(ramfs) ")
                        command = IO.stdscr.getstr().decode(encoding='utf-8')
                        if command == "exit":
                            printf("Goodbye! Thank you for using KTerminal. It will be shutting off now..")
                            IO.stdscr.refresh()
                            curses.napms(1000)
                            quit()
                        elif command == "reinstall":
                            printf("Reinstalling...")
                            printf("any specific distribution you would like to install? Type it here. (Default: master)")

                            distr = IO.stdscr.getstr().decode(encoding="utf-8")

                            if distr is None:#git clone --single-branch --branch <branchname> <remote-repo>
                                printf("None specified, choosing MASTER as default branch")
                                os.system("git clone --single-branch --branch master https://github.com/Kai-Builder/KTerminal.git/")
                            else:
                                os.system("git clone --single-branch --branch " + distr + " https://github.com/Kai-Builder/KTerminal.git/")






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
