#!/venv/bin python

import os
import sys
import requests
import importlib as ipl

import curses
import platform
from curses import wrapper
false = False
true = True
def cprintf(__scr, Text):
    __scr.addstr(Text + "\n")
def require(module):
    return ipl.import_module(module)
def mainc(scr):
    bios = false
    debug = false
    beta = false
    argc = len(sys.argv)
    if argc >= 2:
        if sys.argv[1] == "--bios":
            bios = true
    stdscr = curses.initscr()
    stdscr.scrollok(True)
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_RED, curses.A_NORMAL)
    curses.init_pair(2, curses.COLOR_CYAN, curses.A_NORMAL)
    stdscr.addstr("[" + platform.python_compiler()  + "] KTerminal Version 1.0\nType 'help' for a list of commands.\n\n", curses.color_pair(1))
    stdscr.refresh()
    history = []
    curses.echo()
    cmp = 0
    while True:
        stdscr.addstr("root", curses.color_pair(2))
        stdscr.addstr(" -# ")
        c = stdscr.getstr ().decode(encoding="utf-8")
        curses.nocbreak()
        kt_argv = str(c).split(" ")

        kt_command = kt_argv.pop(0)
        history.append(kt_command)
        cmp += 1
        kt_argc = len(kt_argv)
        wd = "./"
        if kt_command == "leave":
            curses.endwin()
        elif kt_command == "help":
            stdscr.addstr("Commands:\nls\n")
        elif kt_command == "ls":

            if kt_argv[0] is None:
                stdscr.addstr("Description: Lists Subdirectories in a given directory\nUsage: ls [-opts] [dir] or ls "
                              "[dir]\n")
            else:

                for file in os.listdir(kt_argv[0]):
                        stdscr.addstr("~/" + kt_argv[0] + "/" + file + "\n")
        elif kt_command == "pwd":
            stdscr.addstr("Choose a UserName: ")
            username = stdscr.getstr()
            curses.noecho()
            stdscr.addstr("Choose a Password: ")
            password = stdscr.getstr()
            stdscr.addstr("Verify Password: " )
            vp = stdscr.getstr()
            curses.echo()
            if password == vp:
                stdscr.addstr("User successfully set up.\n")
                a = open('usr/beta/.private-login', 'w')
                a.write("USERNAME=" + username + "\nPASSWORD=" + password)
                a.close()
            else:

                stdscr.addstr("Bash User Failed. Passwords do not match.\n")
        elif kt_command == "diagnostic":
            if bios == true:
                stdscr.addstr("Current System Specs\n\t\tProcessor\n\t\t" + platform.processor().__str__() + "\t\t\tArchitecture\n\t\t\t\t" + platform.architecture().__str__() + "\n\n")
            else:
                stdscr.addstr("BIOS Is not set up correctly.\nRun the Python file with the --bios argument, and try again.\n")
        elif kt_command == "sudo":
            if kt_argv[0] == "get-apt":
                if kt_argv[1] == "-h":
                    stdscr.addstr("Description: Gets a File (or package...file(S)) from a given website.\nspecify directories using the sudo -online <link> Commands.\nUsage: sudo get-apt <module>\n")
            elif kt_argv[0] == "--help":
                stdscr.addstr("Runs given commands into ROOT.\nBase commands:\n\tget-apt\n\tsu_dev\n\tworking_dir\n")
        elif kt_command == "wd":
            stdscr.addstr(wd + "\n")
        elif kt_command == "wd-c":
            wd = kt_argv[0]
            stdscr.addstr("new files and caches will be made in " + wd + " now.\n")
        elif kt_command == "clear":
            stdscr.clear()
        elif kt_command == "curl":
            if kt_argc == 0:
                stdscr.addstr("The CURL Command line tool. Use for KTerminal.\n")
            else:
                if kt_argv[0] == "-h":
                    cprintf(stdscr, "The curl command line tool implemented for KTerminal.")
                elif kt_argv[0] == "-gFu":
                    if kt_argc == 0:
                        cprintf(stdscr, "missing required <url> argument.")
        elif kt_command == "printf":
            for arg in kt_argv:
                stdscr.addstr(arg)
        elif kt_command == "echo":
            for arg in kt_argv:
                stdscr.addstr(arg + " ")
            stdscr.addstr("\n")
        elif kt_command == "dofile":
            if kt_argc == 0:
                stdscr.addstr("Missing required arguments. (FILE) (CONTENT)")
            elif kt_argc == 1:
                stdscr.addstr("Missing CONTENT argument.")
            else:
                a = open(kt_argv[0], 'w')
                a.write(kt_argv[1])
                a.close()
        elif kt_command == "resize":
            if bios == true:
                stdscr.resize(int(kt_argv[0]), int(kt_argv[1]))
                stdscr.addstr("new window proportions are " + kt_argv[0] + "," + kt_argv[1])
            else:
                stdscr.addstr("BIOS Tools are not set up properly.\nThis command is a BIOS only tool. Please run the program with the --bios argument and try again.\n")
        elif kt_command == "last_command":
            stdscr.addstr(history[cmp-2])
        else:

            try:

                module = ipl.import_module('usr.bin.' + kt_command)
                module.main(stdscr, kt_argv, kt_argc, [bios, debug, beta])
            except Exception as e:
                if bios == true:
                    stdscr.addstr(e.__str__()  + "\n")
                else:
                    stdscr.addstr("")








wrapper(mainc)