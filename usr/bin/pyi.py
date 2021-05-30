def main(s, av, ac, op):
    file = open(av[0], 'r+')
    a = file.readlines()
    stras = ""
    for line in a:
        stras += line + "\n"
    exec (stras)