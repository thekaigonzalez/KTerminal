# RUN KTERMINAL FROM YOUR KTEMRINAL

# this is for embedded runtimes.
# THIS DOES NOT COME WITH THE DEFAULT BRANCH OF KTERMINAL
# install this using pkg install KTerminal

def main(s, a, c, o):
    s.addstr("You are running an embedded system!\n")
    s.addstr("BIOS Mode and others are defaulted to true, as well as all other commands.\nThe default working directory has been changed"
             "to the recommended, ./usr/local\n")
    o[0] = True
    o[1] = True
    o[2] = True
    o[3] = "./usr/local"
