#include <curses.h>
// implements libs and features
#include <mm_malloc.h>
#include <string.h>
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

char* str_rep_malloc(char* __1, char* __2, ...)
{
    char* new = ""; //create a new empty string

    malloc(sizeof &new); // allocate enough bytes to complete this process
    strcat(new, __2);
    __1  = __2;
    free((void *) sizeof(&new));
    return __1;
}
