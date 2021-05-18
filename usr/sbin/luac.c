
#include <lua/lua.h>
#include <lua/lauxlib.h>
#include <lua/lualib.h>
#include <curses.h>
int iscr(lua_State *L){

    initscr();
    return (1);
}

int addstr_lua(lua_State *L)
{
    printw(luaL_checkstring(L, 1));
    return 1;
}

int getch_w_c(lua_State*L)
{
    getch();
    return 1;
}
int iendwin(lua_State *L)
{
    endwin();
    return 1;
}



int luaopen_curses(lua_State *L){
    lua_register(
            L,               /* Lua state variable */
            "curses_initscr",        /* func name as known in Lua */
            iscr       /* func name in this file */
    );
    lua_register(
            L,
            "curses_printw",
            addstr_lua
            );
    lua_register(
            L,
            "curses_wgetch",
            getch_w_c
            );
    lua_register(L, "curses_endwin", iendwin);

    return 0;
}