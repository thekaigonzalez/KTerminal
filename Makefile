all:
	gcc usr/wd/_hndmal.c usr/wd/_wdhdlapi.c -lcurses -o usr/clib/hndl
	gcc usr/wd/_hndmal.c usr/wd/_cmalloc.c -lcurses -o usr/clib/memsets.da
	gcc -shared -Wall -fPIC usr/shared/_h.c -lcurses -o usr/clib/hello_c.so

	gcc knix/src/util/hello.cpp -fPIC -shared -o knix/usr/bin/hello
	gcc knix/src/util/argdebug.cpp -fPIC -shared -o knix/usr/bin/argdebug
	gcc knix/src/util/printf.cpp -fPIC -shared -o knix/usr/bin/printf
	gcc kefi-runtime/zip.cpp -lstdc++ -shared -o KEFI/zip.kefi
	gcc kefi-runtime/runtime.cpp -lstdc++ -shared -fPIC -o KEFI/runtime.kefi
	gcc kefi-runtime/zunit.cpp -lstdc++ -lzip -lstdc++fs -o ztest.exe

	# this is the next stage, now: binary utilities will be created.
	# (RUST MUST BE INSTALLED.)
	cc knix/knix_terminal.cpp kefi-runtime/runtime.cpp -lstdc++fs -lzip -fPIC -lstdc++ -ldl -o sh
	cc knix/src/util/clear.cpp -shared -lcurses -fPIC -lstdc++ -o knix/usr/bin/ncurses-bin/clear

	gcc usr/wd/primitive.c -S -o usr/Access.S
run:
	python3 main.py

clean:
	rm usr/local/hndl.mcs