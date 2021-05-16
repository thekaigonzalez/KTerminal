#i'd be a fool if i didn't add this here!

def main(scr, args, argc, opts):
    if opts[0] == True:
        # lets give some pre-info
        stdscr = scr

        for i in args:
            exec (i)
    else:
        scr.addstr("BIOS is not set up correctly.\n")