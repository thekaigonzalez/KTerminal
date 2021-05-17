import os
import sys


def main(s, a, c, o):
    from subprocess import Popen, PIPE

    p = Popen(['python3', 'system/home/apps/' + a[1] + ".py"], stdout=PIPE, stderr=PIPE, stdin=PIPE)

    output = p.stdout.read()
    p.stdin.write(output)