import pathlib

ROOT = False


def main(s,a,c,o):

    if len(o) == 6:
        if len(a) == 0:
            s.addstr("CHMOD Utility\n\tCheck system drivers and ensure everything is up to date.\n\nARGUMENTS\n\t[-f "
                     "| -c | -k]\n")
        elif len(a) == 2:
            if a[0] == "-f":
                driver = a[1]
                if pathlib.Path("drivers/" + driver).exists():
                    s.addstr("chmod: driver exists in drivers folder and is not corrupted\n")
                else:
                    s.addstr("chmod: driver does not exist.\n")
    else:
        s.addstr("I do not have full access to your files! please run chmod with the command:\nsudo chmod " + ' '.join(a) + "\n")