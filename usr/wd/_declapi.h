

#ifndef ALGOS__DECLAPI_H
#define ALGOS__DECLAPI_H
struct g_wnd;
// contains official lists of definitions from the
// library.

extern unsigned g_wnd_init();

extern char* str_rep_malloc(char* , char*);

extern void wnd_prn_stdscr(char*);

extern void g_wnd_printf(char*);
extern unsigned endwindow();
extern char get_key();
#endif //ALGOS__DECLAPI_H
