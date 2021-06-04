all:
	gcc usr/wd/_hndmal.c usr/wd/_wdhdlapi.c -lcurses -o usr/clib/hndl
	gcc usr/wd/_hndmal.c usr/wd/_cmalloc.c -lcurses -o usr/clib/memsets.da
	gcc -shared -Wall -fPIC usr/shared/_h.c -lcurses -o usr/clib/hello_c.so
	gcc knix/knix_terminal.cpp -lstdc++ -ldl -o sh
	gcc knix/src/util/hello.cpp -fPIC -shared -o knix/usr/bin/hello
	gcc knix/src/util/argdebug.cpp -fPIC -shared -o knix/usr/bin/argdebug

	# this is the next stage, now: binary utilities will be created.
	# (RUST MUST BE INSTALLED.)

	gcc usr/wd/primitive.c -S -o usr/Access.S
run:
	python3 main.py

clean:
	rm usr/local/hndl.mcs