#include <curses.h>
// implements libs and features
#include <mm_malloc.h>
#include <string.h>
#include <stdio.h>
struct g_wind
{
    int x, y;
};

unsigned int g_wnd_init()
{
    initscr();
    return (1);
}

unsigned int add_str_malloc()
{
    echo();
    char b[100];
    getstr(b);
    if (malloc(sizeof b) != NULL)
    {
        free((void *) sizeof(b));
        return (1);
    }
    else {
        return (2);
    }
}

void g_wnd_printf(char* __T)
{
    printf("%s", __T);
}

char* str_rep_malloc(char* __1, char* __2)
{
    char* new = ""; //create a new empty string

    char* s_t = malloc(sizeof &new); // allocate enough bytes to complete this process
    strcat(s_t, __2);
    __1  = __2;
    return __1;
}
void wnd_prn_stdscr(char* _T)
{
    printw(_T);
}
char get_key()
{
    return getch();
}

unsigned endwindow()
{
    endwin();
    return (1);
}

