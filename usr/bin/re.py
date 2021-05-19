import requests


def main(s, a, c, o):
    s.addstr(str(requests.get(a.pop(0).join(a)).status_code) + "\n")

