all:
	gcc usr/wd/_hndmal.c usr/wd/_wdhdlapi.c -lcurses -o usr/local/hndl



run:
	python3 main.py

clean:
	rm usr/local/hndl.mcs