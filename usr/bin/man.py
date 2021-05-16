import curses
def main(_scr , argv, argc, opts):
    _scr.addstr("opening man-page for " + argv[0] + "\n")
    manPAGE = open('usr/man-pages/' + argv[0] + ".txt", "r+")
    lines = manPAGE.readlines()
    if (len(lines) == 0):
        _scr.addstr("not a valid entry for man-db. cancelling operation.\n")
    else:
        _scr.clear()
        _scr.resize(len(lines)+100, len(lines)+100)
        mypad = curses.newpad(40,60)
        mypad_pos = 0
        mypad.refresh(mypad_pos, 0, 5, 5, 10, 60)
        for line in lines:
            _scr.addstr(line + "\n")
