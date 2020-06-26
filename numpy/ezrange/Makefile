# numpy.i from master worked when using Python 2.7 (on 2020-06-13)
# Download numpy.i if not found. (numpy.i does not seem to be distributed with numpy package
# instaled by pip or conda.)
all:
	make distclean
	make _ezrange.so

test:
	python ezrange_test.py

numpy.i:
	[ -f ./numpy.i ] && echo "numpy.i found" || \
	wget -q https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i

_ezrange.so: numpy.i ezrange.i ezrange.h ezrange_setup.py ezrange_test.py
	rm -f build/lib.linux-x86_64-2.7/_ezrange.so
	python ezrange_setup.py build
	cp build/lib.linux-x86_64-2.7/_ezrange.so .

clean:
	- rm -f *_wrap.*
	- rm -f *.so
	- rm -f *.pyc
	- rm ezrange.py

distclean:
	make clean
	- rm -rf build/
