# numpy.i from master worked when using Python 2.7 (on 2020-06-13)
# Download numpy.i if not found. (numpy.i does not seem to be distributed with numpy package
# instaled by pip or conda.)
all:
	make distclean
	make _inplace_c.so
	make _inplace_cpp.so

test:
	python inplace_c_test.py
	python inplace_cpp_test.py

numpy.i:
	[ -f ./numpy.i ] && echo "numpy.i found" || \
	wget https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i

_inplace_c.so: numpy.i inplace_c.i inplace_c_setup.py inplace_c_test.py
	rm -f build/lib.linux-x86_64-2.7/_inplace_c.so
	python inplace_c_setup.py build
	cp build/lib.linux-x86_64-2.7/_inplace_c.so .

_inplace_cpp.so: numpy.i inplace_cpp.i inplace.h inplace_cpp_setup.py inplace_cpp_test.py
	rm -f build/lib.linux-x86_64-2.7/_inplace_cpp.so
	python inplace_cpp_setup.py build_ext --swig-cpp
	cp build/lib.linux-x86_64-2.7/_inplace_cpp.so .

clean:
	- rm -f *~
	- rm -f *_wrap.*
	- rm -f *.so
	- rm -f *.pyc
	- rm inplace_cpp.py

# TODO: rm statement should only rm created subdirectory
distclean:
	- make clean
	- rm -f *.so
	- rm -rf build/
