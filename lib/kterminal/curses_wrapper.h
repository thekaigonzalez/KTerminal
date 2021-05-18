//
// Created by Kai Gonzalez on 5/18/21.
//

#ifndef ALGOS_CURSES_WRAPPER_H
#define ALGOS_CURSES_WRAPPER_H
#include <stdint.h>
#include <curses.h>
#include <stdlib.h>
#include <string.h>

#ifdef __cplusplus

#endif
//wrap around the curses library to create easier to use functionalities.

struct wind_base {
    char name[50];
    uint16_t wind_alloc;
    void (*begin_proc) ();
};

void begin()
{
    initscr();
    echo();//turn on echo
}

void t_command_service()
{
    char* t = malloc(sizeof t);
    getstr(t);
    char *token;
    char* argv_s[40];
    /* get the first token */
    token = strtok(t, " ");
    int mpos = 0;
    /* walk through other tokens */
    while( token != NULL ) {

        mpos++;
        argv_s[mpos] = token;
        token = strtok(NULL, " ");
    }
    if (strcmp(t, "help") != 0)
    {
        printf("yay");
    }
}

struct TERMINAL
{
    void ( *terminal_init_service ) ();
    void ( *terminal_command_service ) ();
    void ( *terminal_wrong_cmd_handle ) ();
    void ( *terminal_clear_service ) ();
    void ( *terminal_removal_service ) ();
};

void terminal_init(struct TERMINAL * terminal)
{
    while ( true ) {
        printw("root -# ");
        terminal->terminal_command_service();
    }
}

void initscreen()
{
    struct wind_base wnb = { "Basic Window" , 1000, begin };

    wnb.begin_proc();
}
#ifndef CONSOLE
void initconsole() {
    struct TERMINAL TERMINAL = { terminal_init , t_command_service};

    terminal_init(&TERMINAL); // fires events accordingly.
}
#endif //CONSOLE
#endif //ALGOS_CURSES_WRAPPER_H
