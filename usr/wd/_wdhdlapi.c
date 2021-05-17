struct g_wnd;

extern unsigned g_wnd_init();

extern char* str_rep_malloc(char* , char*);

extern void wnd_prn_stdscr(char*);

extern void g_wnd_printf(char*);
extern unsigned endwindow();
extern char get_key();
int main() {
    if (g_wnd_init() == 1)
    {
        get_key();
        endwindow();
    }
}