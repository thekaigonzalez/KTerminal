all:
	gcc usr/wd/_hndmal.c usr/wd/_wdhdlapi.c -lcurses -o usr/clib/hndl
	gcc usr/wd/_hndmal.c usr/wd/_cmalloc.c -lcurses -o usr/clib/memsets.da
	gcc -shared -Wall -fPIC -I/usr/local/include/lua5.4 -lcurses -llua5.4  usr/sbin/luac.c -o lua/curses.so

run:
	python3 main.py

clean:
	rm usr/local/hndl.mcs