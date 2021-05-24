# Runs a command from ROOT.
import curses
import importlib

import requests

import terminal.eval

import configparser


def main(s: curses.window, a, c, o):
    try:
        curses.noecho()
        s.addstr("enter password: ")

        par = configparser.ConfigParser()
        par.read("usr/beta/.private-login")
        ifdef = s.getstr().decode(encoding='utf-8')
        curses.echo()
        if ifdef == par["Info"]["PASSWORD"]:

            o.append(True)
            terminal.eval.Evaluatecommand(a.pop(0) + " " + ' '.join(a), "./usr/sbin", s, o)
        else:
            s.addstr("invalid password.\n")
            curses.echo()
    except Exception as we:

        s.addstr("Login file not found. Please login by using the PWD utility.\n" + we.__str__() + "\n")

