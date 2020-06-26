
# https://stackoverflow.com/a/16528607

all:
	make _code.so

_code.so: code.i setup.py code_test.py
	rm -f build/lib.linux-x86_64-2.7/_code.so
	python setup.py build_ext --swig-cpp
	cp build/lib.linux-x86_64-2.7/_code.so .
	python code_test.py 

clean:
	- rm -f *~
	- rm -f code_wrap.*
	- rm -f _code.o
	- rm -f _code.so
	- rm -f code.pyc
	- rm code.py

distclean:
	make clean
	- rm -rf build/
