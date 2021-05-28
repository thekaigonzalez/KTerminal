def main(s,a,c,o):
    """ SUPER Simplistic echo utility. """
    for arg in a:
        s.addstr(arg + " ")
    s.addstr("\n")
