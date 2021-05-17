# usage: app-install <app>
# usage: app-install <app> <link_base>

def main(s, a, c, o):
    if c == 1:
        s.addstr("getting information for " + a[0] + "..")
    elif c == 2:
        s.addstr("getting information for " + a[0]  + 'from {} as the base link.'.format(a[1]))
