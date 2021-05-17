//
// Created by Kai Gonzalez on 5/17/21.
//

#include <assert.h>
#include "_cmalloc.h"

#define g ' '
int main() {
    initscr();
    noecho();
    cbreak();
    int rows, cols;
    getmaxyx(stdscr, rows, cols);
    scrollok(stdscr, true);
    start_color();

    init_pair(1, COLOR_BLACK, COLOR_WHITE);
    attron(COLOR_PAIR(1));
    move(1, 0);
    printw("KTerminal Interaction Software 1.0 | [q] Exit | [b] Begin | [^D] Exit\n\n");

    attroff(COLOR_PAIR(1));
    char c = getch();
    if (c == 'q') {
        printw("Confirm exit?\n");
        char ex = getch();
        if (ex == 'y')
        {
            echo();
            endwindow();
        }
    }
    else if (c == 'b')
    {
        for (int i = 0; i < 10000; ++i) {
            printw("load\n");
        }
    }
}