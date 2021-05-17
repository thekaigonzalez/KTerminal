import curses
# family dollar vim.. gets the job done.
try:
    import curses.textpad

    stdscr = curses.initscr()

    curses.noecho()

    curses.cbreak()

    stdscr.keypad(True)
    stdscr.clear()
    stdscr.refresh()
    win = curses.newwin(5, 60, 5, 10)
    tb = curses.textpad.Textbox(win)

    text = tb.edit()
    curses.beep()
    win.addstr(5,2,text.encode('utf_8'))
except KeyboardInterrupt:
    curses.endwin() # end the window and return to root.