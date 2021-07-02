all:
	gcc usr/wd/_hndmal.c usr/wd/_wdhdlapi.c -lcurses -o usr/clib/hndl
	gcc usr/wd/_hndmal.c usr/wd/_cmalloc.c -lcurses -o usr/clib/memsets.da
	gcc -shared -Wall -fPIC usr/shared/_h.c  -lcurses -o usr/clib/hello_c.so

	gcc knix/src/util/hello.cpp -std=c++11 -fPIC -lstdc++  -shared -o knix/usr/bin/hello
	gcc knix/src/util/argdebug.cpp -std=c++11 -fPIC  -lstdc++   -shared -o knix/usr/bin/argdebug
	gcc knix/src/util/printf.cpp -std=c++11 -fPIC  -lstdc++  -shared -o knix/usr/bin/printf
	gcc kefi-runtime/zip.cpp -std=c++11 -lstdc++ -lzip -shared -o KEFI/zip.kefi
	gcc kefi-runtime/runtime.cpp -std=c++11 -lstdc++ -shared -fPIC -o KEFI/runtime.kefi
	gcc kefi-runtime/zunit.cpp -std=c++11 -lstdc++ -lzip -o ztest.exe

	
	cc knix/knix_terminal.cpp kefi-runtime/runtime.cpp -std=c++11  -lzip -fPIC -lstdc++ -ldl -o sh
	cc knix/src/util/clear.cpp -shared -lcurses -fPIC -std=c++11 -lstdc++ -o knix/usr/bin/ncurses-bin/clear

	gcc usr/wd/primitive.c -S -o usr/Access.S

	make ./knix/Makefile.kov
run:
	python3 main.py

clean:
	rm usr/local/hndl.mcs