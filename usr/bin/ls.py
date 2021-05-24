import os


def main(s,a,c,o):

    if c == 0:
        s.addstr("Description: Lists Subdirectories in a given directory\nUsage: ls [-opts] [dir] or ls "
                      "[dir]\n")
    elif c == 1:

        for file in os.listdir(o[4]):
            s.addstr("~/" + o[4] + "/" + file + " ")
            s.addstr("\n")

    elif c == 2:
        for file in os.listdir(a[0]):
            s.addstr("~/" + a[0] + file)