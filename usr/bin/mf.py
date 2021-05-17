# Creates a new file, the modern way.


def main(s, a, c, o):
    filename = a.pop(0)
    b = ""
    for i in a:
        b += i + " "

    c = open(o[3] + "/" + filename, 'w')
    c.write(b)
    c.close()