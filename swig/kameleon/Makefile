# Tested on Ubuntu 18.04

# To compile and run code, you need libcdf.so and libccmc.so.6.1.0.0
# See http://github.com/rweigel/kameleon for instructions on creating these libraries.
 
# Compare speed of interpolation between
# (1) Interpolating N points using a command line program
#     ./kameleon_cl FILENAME N
# (2) Doing the same with a call from Python
#     import _kameleon as kameleon
#     b = kameleon.runner(N)
# As expected, timing is similar.
#
# The next step is to write a program that allows
# (3) V_interpolated = kameleon.runner(X, Y, Z, V)
# instead of only
# (4) for i in range(X)
#       V_interpolated[i] = kameleon.runner(X[i], Y[i], Z[i], V[i])
# Method (3) is expected to be about 3x faster than (4), which is currently used.
# The 3x speed-up was determined by comparing the kameleon_cl code
# here doing the equivalent interpolation with the Kameleon/Python
# code as in
# https://github.com/GaryQ-physics/magnetosphere/blob/master/misc/kameleon_kamodo_compare/kameleon_version_testScript.py

# One way of doing this is with swig, but perhaps an easier way is with ctypes, e.g.,
# https://stackoverflow.com/questions/5862915/passing-numpy-arrays-to-a-c-function-for-input-and-output

# Edit these three paths
CDF_DIR=/home/osboxes/git/kameleon/deps/cdf36_4-dist
KAMELEON_PLUS=/home/osboxes/git/kameleon/ccmc-software/kameleon-plus/trunk/kameleon-plus-working

CDF_LIB=${CDF_DIR}/src/lib
CDF_SO=$(CDF_LIB)/libcdf.so

KAMELEON_INCLUDE=$(KAMELEON_PLUS)/src
KAMELEON_LIB=$(KAMELEON_PLUS)/lib/ccmc
KAMELEON_SO=$(KAMELEON_LIB)/libccmc.so.6.1.0.0

PYTHON=python2
OUT_SO=build/lib.linux-x86_64-2.7/_kameleon.so
PYTHON_INCLUDE=/usr/include/python2.7/

#PYTHON=python3
#OUT_SO=build/lib.linux-x86_64-3.6/_kameleon.cpython-36m-x86_64-linux-gnu.so
#PYTHON_INCLUDE=/usr/include/python3.6m/

TESTFILE=3d__var_3_e20031120-070000-000.out.cdf

SHELL := /bin/bash

K=/home/osboxes/kameleon

elf:
	cp $(CDF_SO) .
	cp $(KAMELEON_SO) .

all:
	make kameleon_so
	make kameleon_cl

test:
	make test_cl
	make test_so

xldd:
	LD_LIBRARY_PATH=${K}/lib/ccmc ldd _k*.so


kameleon_so:
	make _kameleon.so

y_ldd:
	LD_LIBRARY_PATH=${k}/lib/ccmc ldd _k*.so


# Compiles
z_kameleon.so: kameleon_so.cpp kameleon.h kameleon.i $(KAMELEON)
	make clean
	$(PYTHON) setup.py build_ext --swig-opts=-c++ \
		-lccmc -lboost_filesystem -lboost_system -L${K}/lib \
		-L${K}/lib/ccmc -I${K}/include
	cp $(OUT_SO) .
	LD_LIBRARY_PATH=. ldd _k*.so
	make z_test_so

# Fail
z_test_so: _k*.so kameleon_test.py
	make testfile
	cp kameleon.py ${K}/lib/ccmc
	cp _k*.so ${K}/lib/ccmc
	cp kameleon_test.py ${K}/lib/ccmc
	cd ${K}/lib/ccmc; LD_LIBRARY_PATH=. ldd _*.so
	cd ${K}/lib/ccmc; LD_LIBRARY_PATH=. $(PYTHON) kameleon_test.py 
	rm ${K}/lib/ccmc/kameleon.py
	rm ${K}/lib/ccmc/_k*.so
	rm ${K}/lib/ccmc/kameleon_test.py 

# Compiles but y_test_so fails with error:
#Traceback (most recent call last):
#  File "kameleon_test.py", line 1, in <module>
#    import _kameleon as kameleon
#ImportError: /home/osboxes/git/swig-and-ctypes/swig/kameleon/_kameleon.so: undefined symbol: _ZN4ccmc8Kameleon12loadVariableERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
# Adding flag -lboost_filesystem
# gives undefined symbol associated with doesVariablExist
y_kameleon.so: kameleon_so.cpp kameleon.h kameleon.i $(K)
	make clean
	$(PYTHON) setup.py build_ext --swig-opts=-c++ -lccmc --rpath=${K}/lib/ccmc \
		-L${K}/lib/ccmc -I${K}/include
	cp $(OUT_SO) .
	ldd _k*.so
	make y_test_so

y_test_so: _kameleon.so kameleon_test.py
	make testfile
	$(PYTHON) kameleon_test.py 

# Works for python 2 and 3
_kameleon.so: kameleon_so.cpp kameleon.h kameleon.i $(KAMELEON)
	make clean
	$(PYTHON) setup.py build_ext --swig-opts=-c++ -lccmc --rpath=${KAMELEON_LIB} \
		-L${KAMELEON_LIB} -I${KAMELEON_INCLUDE}
	ldd $(OUT_SO)
	cp $(CDF_SO) lib/
	./relativize_libs.sh $(KAMELEON_SO)
	patchelf --set-rpath "\$$ORIGIN/lib" $(OUT_SO)
	cp $(OUT_SO) .
	ldd _*.so
	chmod 644 _*.so
	chmod 644 lib/*.so

# Works for python 2 and 3
test_so: _kameleon.so kameleon_test.py
	make testfile
	$(PYTHON) kameleon_test.py

kameleon_cl: kameleon_cl.cpp $(KAMELEON_INCLUDE)
	g++ kameleon_cl.cpp -Wno-deprecated -o kameleon_cl \
		-I${KAMELEON_INCLUDE} \
		-L$(KAMELEON_LIB) \
		-lccmc \
		-I$(PYTHON_INCLUDE) \
		-lboost_system -lboost_python -lpython2.7
# Last two lines above needed for Boost's wrap_python.hpp (based on error message without it)

test_cl: kameleon_cl
	make testfile
	LD_LIBRARY_PATH=$(KAMELEON_LIB) ./kameleon_cl $(TESTFILE) 1000000

testfile:
	- wget -q -N http://mag.gmu.edu/git-data/sblake/SCARR5_GM_IO2/IO2/$(TESTFILE)

clean:
	- rm -rf build/
	- rm kameleon_wrap.cpp
	- rm kameleon.py
	- rm kameleon_cl
	- rm *.so
	- rm -f *~

distclean:
	make clean
	- rm -f kameleon_cl 3d__var_3_e20031120-070000-000.out.cdf	
