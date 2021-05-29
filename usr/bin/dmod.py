import curses

import terminal.argsetup
import terminal.io as IO



def printf(vs):
    IO.printw(vs)


def HelpCommand(argparse, object: terminal.argsetup.ArgumentPasser):
    object.sendhelp()
def CreateCommand(argparse, object: terminal.argsetup.ArgumentPasser):
    printf("e")
def libcmomand(args, object):
    printf("lub")
def dui(a, o):
    printf("abs")

def uin(a,o):
    printf("")
def main(s: curses.window, a: list, c: int, o: list):
    """ dMOD: Distribution MODification services

    dmod -c <distname> <diskfile>
    dmod -u <distname>
    dmod -l<lib> <distname>
    dmod -dUi <distname>
    dmod -h
    """
    parser = terminal.argsetup.ArgumentPasser(a)
    parser.setDesc("DMOD helps you manage your distributions effectively.")
    parser.bindonce("c", CreateCommand)
    parser.bindonce("l", libcmomand)
    parser.bindonce("dUi", dui)
    parser.bindonce("u", uin)
    parser.bindonce("h", HelpCommand)
