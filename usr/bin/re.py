import requests


def main(s, a, c, o):
    """Rejoins a string.

    re * a b c

    a*b*c
    """
    s.addstr(str(a.pop(0).join(a)) + "\n")

