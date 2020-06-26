# https://stackoverflow.com/questions/30259591/swig-and-multidimensional-arrays/30335624#30335624
# https://github.com/rsnemmen/swig-numpy-2d
# https://stackoverflow.com/a/30335624
# https://scipy.github.io/old-wiki/pages/Cookbook/SWIG_NumPy_examples.html
# https://github.com/dblalock/swig-numpy-example

# numpy.i from master worked when using Python 2.7 (on 2020-06-13)
# Download numpy.i if not found. (numpy.i does not seem to be distributed with numpy package
# instaled by pip or conda.)
all:
	make distclean
#	make _inplace_c.so
	make _inplace_cpp.so

test:
#	python inplace_c_test.py
	python inplace_cpp_test.py

numpy.i:
	[ -f ./numpy.i ] && echo "numpy.i found" || \
	wget https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i

_inplace_c.so: numpy.i inplace.i inplace_setup.c.py inplace_c_test.py
	rm -f build/lib.linux-x86_64-2.7/_inplace.so
	python inplace_setup.c.py build
	cp build/lib.linux-x86_64-2.7/_inplace.so .

_inplace_cpp.so: numpy.i inplace_cpp.i inplace_cpp.h inplace_cpp_setup.py inplace_cpp_test.py
	rm -f build/lib.linux-x86_64-2.7/_inplace_cpp.so
	python inplace_cpp_setup.py build_ext --swig-cpp
	cp build/lib.linux-x86_64-2.7/_inplace_cpp.so .

clean:
	- rm -f *_wrap.*
	- rm -f *.so
	- rm -f *.pyc
	- rm inplace_cpp.py

# TODO: rm statement should only rm created subdirectory
distclean:
	- make clean
	- rm -f _inplace_cpp.so
	- rm -rf build/
