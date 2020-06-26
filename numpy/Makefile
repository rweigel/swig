# https://stackoverflow.com/questions/30259591/swig-and-multidimensional-arrays/30335624#30335624
# https://github.com/rsnemmen/swig-numpy-2d
# https://stackoverflow.com/a/30335624
# https://scipy.github.io/old-wiki/pages/Cookbook/SWIG_NumPy_examples.html

# numpy.i from master worked when using Python 2.7 (on 2020-06-13)
# Download numpy.i if not found. (numpy.i does not seem to be distributed with numpy package
# instaled by pip or conda.)
numpy.i:
	[ -f ./numpy.i ] && echo "numpy.i found" || wget https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i

all:
	make distclean
	make ezrange.c
	make inplace.c
	make inplace.cpp

ezrange.c: numpy.i ezrange.i ezrange_setup.c.py ezrange_test.py
	rm -f build/lib.linux-x86_64-2.7/_ezrange.so
	python ezrange_setup.c.py build
	cp build/lib.linux-x86_64-2.7/_ezrange.so .
	python ezrange_test.py 

inplace.c: numpy.i inplace.i inplace_setup.c.py inplace_test.py
	rm -f build/lib.linux-x86_64-2.7/_inplace.so
	python inplace_setup.c.py build
	cp build/lib.linux-x86_64-2.7/_inplace.so .
	python inplace_test.py 

inplace.cpp: numpy.i inplace.i inplace_setup.cpp.py inplace_test.py
	rm -f build/lib.linux-x86_64-2.7/_inplace.so
	python inplace_setup.cpp.py build_ext --swig-cpp
	cp build/lib.linux-x86_64-2.7/_inplace.so .
	python inplace_test.py 

clean:
	- rm -f *_wrap.*
	- rm -f *.so
	- rm -f *.pyc
	- rm ezrange.py
	- rm inplace.py

# TODO: rm statement should only rm created subdirectory
distclean:
	- rm -rf build/
