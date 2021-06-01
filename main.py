#!/venv/bin python
import ctypes
import os
import random
import sys

import pathlib
import requests
import importlib as ipl

import curses
import platform
from curses import wrapper

import terminal.eval

false = False
import configparser

true = True


def cprintf(__scr, Text):
    __scr.addstr(Text + "\n")


def require(module):
    return ipl.import_module(module)


def mainc(scr):
    bios = false
    debug = false
    beta = false
    wd = "./"
    argc = len(sys.argv)
    if argc >= 2:
        if sys.argv[1] == "--bios":
            bios = true
        elif sys.argv[1] == "--beta":
            beta = true
        elif sys.argv[1] == '--deb':
            debug = true
    stdscr = curses.initscr()
    stdscr.keypad(True)
    cfg = configparser.ConfigParser()
    configs = cfg.read('./usr/.bashconfig')  # Load bash settings
    wd = cfg["User"]["Working_Directory"]
    stdscr.scrollok(True)
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_RED, curses.A_NORMAL)
    curses.init_pair(2, curses.COLOR_GREEN, curses.A_NORMAL)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.A_NORMAL)
    stdscr.addstr("[" + platform.python_compiler() + "] KTerminal Version 1.3\nType 'help' for a list of commands.\n\n",
                  curses.color_pair(1))
    stdscr.refresh()
    history = []

    curses.echo()
    cmp = 0

    while True:

        stdscr.addstr(open('usr/user.txt', 'r').readlines()[0] + "@" + open('usr/name.txt').readlines()[0] + ":~ ",
                      curses.color_pair(2))
        stdscr.addstr("")
        stdscr.addstr(wd + "", curses.color_pair(3))
        stdscr.addstr("$ ")
        c = stdscr.getstr().decode(encoding=cfg["Buffer"]["Encoding"])
        curses.nocbreak()
        kt_argv = str(c).split(" ")

        kt_command = kt_argv.pop(0).strip()
        history.append(kt_command)
        cmp += 1
        kt_argc = len(kt_argv)

        if kt_command == "leave":
            curses.endwin()
        elif kt_command == "help":
            arr = []
            for fname in os.listdir("usr/bin"):
                if fname.endswith(".py"):
                    if not fname.startswith("__"):
                        arr.append(fname[0:fname.rfind(".")])
            stdscr.addstr("Commands:\n" + ' '.join(arr))
            stdscr.addstr("\n")

        elif kt_command == "pwd":
            stdscr.addstr("Choose a UserName: ")
            username = stdscr.getstr().decode(encoding=cfg["Buffer"]["Encoding"])
            curses.noecho()
            stdscr.addstr("Choose a Password: ")
            password = stdscr.getstr().decode(encoding=cfg["Buffer"]["Encoding"])
            stdscr.addstr("Verify Password: ")
            vp = stdscr.getstr().decode(encoding=cfg["Buffer"]["Encoding"])
            curses.echo()
            if password == vp:
                stdscr.addstr("User successfully set up.\n")
                a = open('usr/beta/.private-login', 'w')
                a.write("[Info]\nUSERNAME=" + username + "\nPASSWORD=" + password)
                a.close()
            else:

                stdscr.addstr("Bash User Failed. Passwords do not match.\n")
        elif kt_command == "diagnostic":
            if bios == true:
                stdscr.addstr(
                    "Current System Specs\n\t\tProcessor\n\t\t" + platform.processor().__str__() + "\t\t\tArchitecture\n\t\t\t\t" + platform.architecture().__str__() + "\n\n")
            else:
                stdscr.addstr(
                    "BIOS Is not set up correctly.\nRun the Python file with the --bios argument, and try again.\n")

        elif kt_command == "wd":
            stdscr.addstr(wd + "\n")


        elif kt_command == "clear":
            stdscr.clear()

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
                stdscr.addstr(
                    "BIOS Tools are not set up properly.\nThis command is a BIOS only tool. Please run the program with the --bios argument and try again.\n")
        elif kt_command == "last_command":
            stdscr.addstr(history[cmp - 2])

        elif kt_command.startswith("#!"):
            if kt_command[3:len(kt_command) - 1] == "wd":
                stdscr.addstr("that is your current working directory. choose a different location.\n")
            try:
                newcommand = kt_command.split()[1]
                module = ipl.import_module('usr.bin.' + newcommand)
                module.main(stdscr, kt_argv, kt_argc, [bios, debug, beta, wd, kt_command])
            except Exception as e:
                if bios == true:
                    stdscr.addstr(e.__str__() + "\n")
                else:
                    stdscr.addstr("")
        else:

            try:

                module = ipl.import_module('usr.bin.' + kt_command)
                ipl.invalidate_caches()
                module.main(stdscr, kt_argv, kt_argc, [bios, debug, beta, wd, kt_command])
            except Exception as e:
                if bios == true:
                    stdscr.addstr(e.__str__() + "\n")
                else:
                    try:
                        if pathlib.Path("./" + kt_command + ".ktsh").exists():
                            file = open('./' + kt_command + ".ktsh")
                            lines = file.readlines()
                            for i in lines:
                                terminal.eval.Evaluatecommand(i, wd, stdscr, kt_argv)
                        elif pathlib.Path("./" + kt_command).exists():
                            file = open('./' + kt_command)
                            lines = file.readlines()
                            for i in lines:
                                terminal.eval.Evaluatecommand(i, wd, stdscr, kt_argv)
                        else:
                            request3 = requests.get(
                                # https://raw.githubusercontent.com/thekaigonzalez/unix-core/master/whoami.py
                                "https://raw.githubusercontent.com/thekaigonzalez/unix-core/master/" + kt_command + ".py")
                            request = requests.get("https://github.com/thekaigonzalez/" + kt_command)
                            if pathlib.Path("usr/clib/" + kt_command + ".so").exists():
                                if cfg["Bash"]["allowCExtensions"] == "yes":
                                    try:

                                        command_fromC = ctypes.CDLL("usr/clib/" + kt_command + ".so")
                                        command_fromC.init()
                                    except Exception as e:
                                        if request.status_code == 200:
                                            request2 = requests.get(
                                                "https://raw.githubusercontent.com/thekaigonzalez/" + kt_command + "/master/" + kt_command + ".py")
                                            if request2.status_code == 200:
                                                stdscr.addstr(
                                                    "command not found. But can be installed with:\nget-apt install {}\n".format(
                                                        kt_command))
                                        else:
                                            stdscr.addstr("(DIAG: " + e.__str__() + ")\n")
                            else:
                                if request.status_code == 200:
                                    request2 = requests.get(
                                        "https://raw.githubusercontent.com/thekaigonzalez/" + kt_command + "/master/" + kt_command + ".py")

                                    if request2.status_code == 200:
                                        stdscr.addstr(
                                            "command not found. But can be installed with:\nsudo apt-get install {}\n".format(
                                                kt_command))
                                    else:
                                        if request3.status_code == 200:
                                            stdscr.addstr(
                                                "Command not found, but can be installed with\nsudo apt-get install {}/{}\n".format(
                                                    "unix-core", kt_command))
                                else:
                                    if request3.status_code == 200:
                                        stdscr.addstr(
                                            "Command not found, but can be installed with\nsudo apt-get install {}/{}\n".format(
                                                "unix-core", kt_command))
                                    else:
                                        stdscr.addstr(kt_command + ": unknown command.\n")
                    except Exception as a:
                        stdscr.addstr("An Unknown error occurred.\na dump file has been created in usr/lib/CRASH.txt\n")
                        deum = open('usr/lib/CRASH' + str(random.randint(0, 900)) + ".txt", 'w')
                        deum.write(
                            "CRASH exception occurred in proccess KTERMINAL_MAIN:\n\nCOMMAND RUN: " + kt_command + "\nSUPPLIED ARGUMENTS: " + str(
                                kt_argv) + "\nCRASH EXCEPTION: " + str(a))
                        deum.close()


wrapper(mainc)
