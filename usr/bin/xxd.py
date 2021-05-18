

def main(s, a, c, o):
    b = ' '.join(format(ord(x), 'b') for x in ' '.join(a))
    s.addstr(str(b) + "\n")