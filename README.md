(REMINDER: ALL COMMANDS WILL NO LONGER BE MADE INSIDE OF MAIN.PY, THE USR.BIN DIRECTORY IS PRIORITY. AS WELL AS THE HOME APPS DIR.)

![img_1.png](img_1.png)

# KTerminal

KTerminal is a light, easy to use Python 3.9 Terminal that 
was perfected and published on May 15th. With over 10 commands (Builtin, and external),
the console has been built to support over 50 different compilers.

KTerminal contains a bunch of symbols, and it's skeleton was built
upon inspiration from the original BASH terminal, in 
combination with the Arch Linux pre-setup terminal.
![img.png](img.png)

The KTerminal features a Unix-Like file structure containing a ./usr directory,
which stores python caches and essential files.

Please enjoy this bash. Star it if you do.

# A Tour Inside KTerminal
## Directories
The directories in KTerminal are based off of the linux
source tree. featuring usr, drivers, and fs. As
well as a system.home directory where apps are stored.
## Apps & Games
The games that come packaged in feature
- vim

It isn't really vim, it's just a console-based text editor.
vim for KTerminal is in early access and is currently just a
writing program with a basic text box.

there's also a application handler built in.

## PKG
Package manager. Uses Https to gather information and
install features.

the package manager searches links (usually github), 
for a repository corresponding with the arguments.
it then checks for the main file and downloads it to your scripts directory.
