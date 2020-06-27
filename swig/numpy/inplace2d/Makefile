# https://stackoverflow.com/questions/30259591/swig-and-multidimensional-arrays/30335624#30335624
# https://github.com/rsnemmen/swig-numpy-2d
# https://stackoverflow.com/a/30335624
# https://scipy.github.io/old-wiki/pages/Cookbook/SWIG_NumPy_examples.html

# numpy.i from master worked when using Python 2.7 (on 2020-06-13)
# Download numpy.i if not found. (numpy.i does not seem to be distributed with numpy package
# instaled by pip or conda.)

all:
	make _inplace2d.so

test:
	python inplace2d_test.py

numpy.i:
	[ -f ./numpy.i ] && echo "numpy.i found" || \
	wget https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i

_inplace2d.so: numpy.i inplace2d.cpp inplace2d.h inplace2d.i inplace2d_setup.cpp.py inplace2d_test.py
	rm -f build/lib.linux-x86_64-2.7/_inplace2d.so
	python inplace2d_setup.cpp.py build_ext --swig-opts=-c++
	cp build/lib.linux-x86_64-2.7/_inplace2d.so .


clean:
	- rm -f *_wrap.*
	- rm -f *.so
	- rm -f *.pyc
	- rm inplace2d.py

# TODO: rm statement should only rm created subdirectory
distclean:
	make clean
	- rm -rf build/
