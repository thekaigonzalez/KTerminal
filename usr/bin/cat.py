
def main(screen, args, argcount, opts):



    if args[0] == "--file":
        if args[1] == "--read":

            name = args[2]
            ufile = open(name, 'r+')
            a= ufile.readlines()
            for line in a:
                screen.addstr(line + "\n")