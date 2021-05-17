def main(s, a, c, o):
    ctx=""
    name=a.pop(0)
    for i in a:
        ctx += i
    w = open(name, 'wb')
    w.write(b"{}".format(ctx))
    w.close()
