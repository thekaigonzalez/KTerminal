
import os

TYPE="system-root"

def main(_s, a, c , o):
    dirname = ""
    for i in a:
        dirname += i

    if o[2] == True:
        _s.addstr("ENOENT: dir " + dirname + "\n")
    os.mkdir(o[3] + "/" + dirname)