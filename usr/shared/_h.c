#include <stdio.h>
#include <curses.h>


// called when the command is called.
int init() {
    printw("hello!");
    return 1;
}