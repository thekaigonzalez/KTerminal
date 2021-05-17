all:
	gcc usr/wd/_hndmal.c usr/wd/_wdhdlapi.c -lcurses -o usr/clib/hndl
	gcc usr/wd/_hndmal.c usr/wd/_cmalloc.c -lcurses -o usr/clib/memsets.da


run:
	python3 main.py

clean:
	rm usr/local/hndl.mcs