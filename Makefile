all:
	gcc usr/wd/_hndmal.c usr/wd/_wdhdlapi.c -lcurses -o usr/clib/hndl
	gcc usr/wd/_hndmal.c usr/wd/_cmalloc.c -lcurses -o usr/clib/memsets.da
	gcc -shared -Wall -fPIC -I/usr/local/include/lua5.4 -lcurses -llua5.4  usr/sbin/luac.c -o lua/curses.so
	gcc -shared -Wall -fPIC usr/shared/_h.c -lcurses -o usr/clib/hello_c.so
	gcc sqifs-util/repl.c sqifs-util/m_replutil.c -o usr/filesystem/sqifs-driver

	# this is the next stage, now: binary utilities will be created.
	# (RUST MUST BE INSTALLED.)

	rustc src/main.rs -o
run:
	python3 main.py

clean:
	rm usr/local/hndl.mcs