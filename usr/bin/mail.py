# View mail, Send Mail, and receive mail.
import curses
import os


# s: curses.window, a: list[str], c: int, o: list[bool]
def main(s: curses.window, a: list[str], c: int, o: list[bool]):
    if c == 1:
        if a[0] == "-c":
            if len(os.listdir("usr/mail")) == 0:
                s.addstr("you have no new mail")
            elif len(os.listdir("usr/mail")) > 0:
                s.addstr("you have new mail in /usr/mail")
    elif c == 3:
        if a[0] == "-u":
            if a[1] == "read":
                umailist = open('usr/mail/' + a[2] + ".ml")
                ab = umailist.readlines()
                strs = ' '.join(ab)
                s.addstr(strs)
