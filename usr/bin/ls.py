import os

import terminal.parser


def main(s,a,c,o):

    if c == 0:
        for i in os.listdir(o[3]):
            s.addstr(i + " ")
        s.addstr("\n")
    elif c == 1:

        for file in os.listdir(terminal.parser.checkquotedstring(pos=0, array=a)):
            s.addstr("~/" + terminal.parser.checkquotedstring(0, a) + "/" + file + " ")
            s.addstr("\n")

    elif c == 2:
        for file in os.listdir(a[0]):
            s.addstr("~/" + a[0] + file)
