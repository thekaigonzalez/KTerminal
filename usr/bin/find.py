import curses
import os
import terminal.io as IO

printc = IO.printw

def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result
def main(s: curses.window, a: list, c: int, o: list):
    """ Checks the given search path for available instances of file. """
    file = a[0]
    path = a[1]
    printc(str(find_files(file, path)))

