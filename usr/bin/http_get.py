# usage: http_get <url>
# usage: http_get <url> <flags>

# flags:
import requests
# --rco : response code
# --astr : as a string
# NONE : as a string

def main(s, a, c, o):
    if c == 0:
        s.addstr("Missing 'link' argument.\n")
    elif c == 1:
        s.addstr(requests.get(a[0]).text + "\n")
    elif c == 2:
        if a[1] == '--rco':
            s.addstr(str(requests.get(a[0]).status_code) + "\n")
        elif a[2] == '--astr':
            s.addstr(requests.get(a[0]).text + "\n")